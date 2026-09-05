/**
 * The chat endpoint.
 *
 * The AI SDK owns the agent loop and the wire format. useChat on the browser
 * reads the same format, so there is no protocol to write by hand.
 *
 * query_sql returns request-scoped rows. show_visualization turns one result
 * into a widget after the model sees the data. The browser draws
 * `part.output.widget`; no custom stream part is needed.
 *
 * The writer exists for the transient status line, which comes later.
 */
import {
  streamText,
  convertToModelMessages,
  createUIMessageStream,
  createUIMessageStreamResponse,
  stepCountIs,
  type UIMessage,
} from "ai";
import { createAnthropic } from "@ai-sdk/anthropic";
import { buildSystemPrompt } from "../utils/prompt";
import { createAgentTools } from "../utils/tools";
import { chatUsage } from "../utils/chatUsage";
import {
  recordAnalyticsSafely,
  type ChatFinishInput,
  type ChatSource,
} from "../utils/analyticsStore";

const FINAL_RESPONSE_STEP = 10;
const MAX_STEPS = 12;
const CHAT_SOURCES = new Set<ChatSource>(["typed", "sample", "followup", "story", "retry"]);

function messageText(message: UIMessage | undefined): string {
  return message?.parts
    .filter((part): part is Extract<typeof part, { type: "text" }> => part.type === "text")
    .map((part) => part.text)
    .join("\n")
    .trim() ?? "";
}

function lastQuestion(messages: UIMessage[]): string {
  return messageText([...messages].reverse().find((message) => message.role === "user"));
}

function visibleAnswer(value: string): string {
  const followups = value.indexOf("<followups>");
  return (followups === -1 ? value : value.slice(0, followups)).trim();
}

function chartType(steps: any[]): string | undefined {
  return steps.flatMap((step) => step.toolResults ?? [])
    .map((result) => result.output?.widget?.mark)
    .find((mark) => typeof mark === "string");
}

export default defineLazyEventHandler(() => {
  const config = useRuntimeConfig();
  if (!config.anthropicApiKey) {
    throw new Error("NUXT_ANTHROPIC_API_KEY is not set. Copy .env.example to .env.");
  }

  // This is the only line that names the provider.
  const anthropic = createAnthropic({ apiKey: config.anthropicApiKey });

  return defineEventHandler(async (event) => {
    const permit = chatUsage.acquire();
    if (!permit.allowed) {
      setResponseStatus(event, permit.statusCode);
      setResponseHeader(event, "Retry-After", permit.retryAfterSeconds);
      return permit.message;
    }

    const analyticsStarted = performance.now();
    let analyticsTurnId: string | undefined;
    let analyticsFinished = false;
    const finishAnalytics = (result: ChatFinishInput) => {
      if (!analyticsTurnId || analyticsFinished) return;
      analyticsFinished = true;
      recordAnalyticsSafely((store) => store.finishChat(analyticsTurnId!, result));
    };

    try {
      const body = await readBody<{
        messages: UIMessage[];
        analytics?: { viewId?: string; source?: string };
      }>(event);
      const messages = body.messages;
      const source = CHAT_SOURCES.has(body.analytics?.source as ChatSource)
        ? body.analytics!.source as ChatSource
        : "typed";
      const viewId = typeof body.analytics?.viewId === "string" && /^[0-9a-f-]{36}$/i.test(body.analytics.viewId)
        ? body.analytics.viewId
        : undefined;
      recordAnalyticsSafely((store) => {
        analyticsTurnId = store.startChat({
          viewId,
          source,
          question: lastQuestion(messages),
          model: config.agentModel,
        });
      });
      const stream = createUIMessageStream({
        execute: ({ writer }) => {
          const result = streamText({
            model: anthropic(config.agentModel),
            system: buildSystemPrompt(),
            messages: convertToModelMessages(messages),
            tools: createAgentTools(),
            // Reserve the last calls for a direct answer. Without this guard, a
            // long tool sequence can reach the limit and leave only query steps.
            prepareStep: ({ stepNumber }) => (
              stepNumber >= FINAL_RESPONSE_STEP ? { toolChoice: "none" } : undefined
            ),
            stopWhen: stepCountIs(MAX_STEPS),
            onFinish: ({ text, finishReason, steps }) => {
              finishAnalytics({
                status: "success",
                answer: visibleAnswer(text),
                durationMs: performance.now() - analyticsStarted,
                modelSteps: steps.length,
                toolCalls: steps.reduce((total, step) => total + step.toolCalls.length, 0),
                chartType: chartType(steps),
              });
              if (!text.trim()) {
                console.warn("[chat] The agent finished without an answer.", {
                  finishReason,
                  steps: steps.length,
                });
              }
            },
            onAbort: ({ steps }) => {
              finishAnalytics({
                status: "aborted",
                durationMs: performance.now() - analyticsStarted,
                modelSteps: steps.length,
                toolCalls: steps.reduce((total, step) => total + step.toolCalls.length, 0),
              });
            },
            onError: ({ error }) => {
              finishAnalytics({
                status: "error",
                durationMs: performance.now() - analyticsStarted,
                errorType: error instanceof Error ? error.name : "UnknownError",
              });
            },
            providerOptions: {
              anthropic: {
                // The prompt is stable within a day, so cache its shared prefix.
                cacheControl: { type: "ephemeral" },
              },
            },
          });
          writer.merge(result.toUIMessageStream());
        },
        onFinish: ({ isAborted }) => {
          if (isAborted) {
            finishAnalytics({ status: "aborted", durationMs: performance.now() - analyticsStarted });
          }
          permit.release();
        },
        onError: (error) => {
          finishAnalytics({
            status: "error",
            durationMs: performance.now() - analyticsStarted,
            errorType: error instanceof Error ? error.name : "UnknownError",
          });
          console.error("[chat]", error);
          return error instanceof Error ? error.message : "The request failed.";
        },
      });

      return createUIMessageStreamResponse({ stream });
    } catch (error) {
      finishAnalytics({
        status: "error",
        durationMs: performance.now() - analyticsStarted,
        errorType: error instanceof Error ? error.name : "UnknownError",
      });
      permit.release();
      throw error;
    }
  });
});
