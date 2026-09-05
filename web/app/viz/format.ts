const integer = new Intl.NumberFormat("en", { maximumFractionDigits: 0 });
const decimal = new Intl.NumberFormat("en", { maximumFractionDigits: 2 });
const compact = new Intl.NumberFormat("en", {
  notation: "compact",
  maximumFractionDigits: 1,
});

export function numeric(value: unknown): number | null {
  if (typeof value === "number") return Number.isFinite(value) ? value : null;
  if (typeof value !== "string" || value.trim() === "") return null;
  const parsed = Number(value);
  return Number.isFinite(parsed) ? parsed : null;
}

export function formatNumber(value: unknown, unit = ""): string {
  const parsed = numeric(value);
  if (parsed === null) return value == null ? "" : String(value);
  const shown = Math.abs(parsed) >= 10_000
    ? compact.format(parsed)
    : Number.isInteger(parsed)
      ? integer.format(parsed)
      : decimal.format(parsed);
  if (["€", "$", "£"].includes(unit)) return `${unit}${shown}`;
  if (!unit) return shown;
  return /^\p{L}/u.test(unit) ? `${shown} ${unit}` : `${shown}${unit}`;
}

export function fieldLabel(field: string): string {
  const label = field.replaceAll("_", " ").trim();
  return label ? label.charAt(0).toUpperCase() + label.slice(1) : "Value";
}
