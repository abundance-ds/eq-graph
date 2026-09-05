const WORKING_GROUPS = [
  "Populations and Health Systems",
  "Dissemination, OA fee",
  "Education and Outreach",
  "Descriptive Systems",
  "Valuation",
  "EQ-HWB",
  "Youth",
  "Others",
] as const;

const NON_RESEARCH_GROUPS = new Set(["Dissemination, OA fee", "Others"]);

export function parseWorkingGroups(value: unknown): string[] {
  const raw = String(value ?? "").trim();
  let rest = raw;
  const groups: string[] = [];

  while (rest) {
    const group = WORKING_GROUPS.find((candidate) => (
      rest === candidate || rest.startsWith(`${candidate}, `)
    ));
    if (!group) throw new Error(`Unrecognized working-group value: ${raw}`);
    groups.push(group);
    rest = rest.slice(group.length).replace(/^, /, "");
  }

  return groups;
}

export function researchWorkingGroups(value: unknown): string[] {
  return parseWorkingGroups(value).filter((group) => !NON_RESEARCH_GROUPS.has(group));
}
