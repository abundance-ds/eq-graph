export type ChatWidgetSpec = {
  mark: "stat" | "bar" | "line" | "donut" | "table";
  title: string;
  caption?: string;
  encoding: {
    x?: string;
    y?: string;
    series?: string;
    value?: string;
    columns?: string[];
  };
  options?: {
    orientation?: "vertical" | "horizontal";
    sort?: "asc" | "desc" | "none";
    limit?: number;
    unit?: string;
    color?: string;
    hint?: string;
  };
  rows: Record<string, unknown>[];
  rowCount: number;
};

export type ChatToolPart = Record<string, any>;

export type ChatSegment =
  | { kind: "text"; key: string; text: string }
  | { kind: "widget"; key: string; widget: ChatWidgetSpec }
  | { kind: "tools"; key: string; parts: ChatToolPart[] };

export type ChatTurn = {
  id: string;
  role: "user" | "assistant";
  list: ChatSegment[];
};

export type ChatDataCounts = {
  projects: number;
  works: number;
  findings: number;
};

export type ChatDataState = "ready" | "loading" | "error";
