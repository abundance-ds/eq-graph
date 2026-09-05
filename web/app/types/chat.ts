export type ChatWidgetMark =
  | "stat"
  | "bar"
  | "line"
  | "area"
  | "scatter"
  | "histogram"
  | "heatmap"
  | "donut"
  | "network"
  | "table";

export type ChatWidgetSpec = {
  mark: ChatWidgetMark;
  title: string;
  caption?: string;
  encoding: {
    x?: string;
    y?: string;
    series?: string;
    value?: string;
    source?: string;
    target?: string;
    weight?: string;
    columns?: string[];
  };
  options?: {
    orientation?: "vertical" | "horizontal";
    layout?: "grouped" | "stacked";
    unit?: string;
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
