/**
 * The chat endpoint.
 *
 * The AI SDK owns the agent loop and the wire format. useChat on the browser
 * reads the same format, so there is no protocol to write by hand.
 *
 * The widgets travel as an ordinary tool result. The browser reads the part
 * `tool-render` when its state is `output-available`, and it draws
 * `part.output.widget`. No custom data part is needed for that.
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
import { SYSTEM_PROMPT } from "../utils/schema";
import { agentTools } from "../utils/tools";

export default defineLazyEventHandler(() => {
  const config = useRuntimeConfig();
  if (!config.anthropicApiKey) {
    throw new Error("NUXT_ANTHROPIC_API_KEY is not set. Copy .env.example to .env.");
  }

  // The only line that names a provider. To use another model, change this
  // line and the package. The tools and the prompt do not change.
  const anthropic = createAnthropic({ apiKey: config.anthropicApiKey });

  return defineEventHandler(async (event) => {
    const { messages } = await readBody<{ messages: UIMessage[] }>(event);

    const stream = createUIMessageStream({
      execute: ({ writer }) => {
        const result = streamText({
          model: anthropic(config.agentModel),
          system: SYSTEM_PROMPT,
          messages: convertToModelMessages(messages),
          tools: agentTools,
          // The loop runs until the model stops calling tools, or until it
          // reaches this many steps.
          stopWhen: stepCountIs(12),
          providerOptions: {
            anthropic: {
              // The schema block is large and it never changes, so cache it.
              cacheControl: { type: "ephemeral" },
            },
          },
        });
        writer.merge(result.toUIMessageStream());
      },
      onError: (error) => {
        console.error("[chat]", error);
        return error instanceof Error ? error.message : "The request failed.";
      },
    });

    return createUIMessageStreamResponse({ stream });
  });
});
