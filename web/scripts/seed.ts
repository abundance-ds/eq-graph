/**
 * Writes false data into the graph, in the correct ontology.
 *
 * The rows are invented. The vocabularies are real: the working groups, the
 * grant type codes, the EQ instrument family, the elicitation techniques and
 * the evidence kinds all come from Kazik's pipeline. The agent therefore learns
 * the true value sets, and only the numbers change when the real loader runs.
 *
 * The generator is deterministic, so two runs give the same graph.
 *
 * Run: pnpm db:local:seed   add the data
 *      pnpm db:local:reset  delete local data, then add the fixture
 */
import neo4j from "neo4j-driver";
import { localDatabaseConnection } from "./local-database";

const { uri, user, password } = localDatabaseConnection("The demo-data script");
const wipe = process.argv.includes("--wipe");

// --- A deterministic random generator ---------------------------------------

let state = 0x9e3779b9;
function rnd(): number {
  state |= 0;
  state = (state + 0x6d2b79f5) | 0;
  let t = Math.imul(state ^ (state >>> 15), 1 | state);
  t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t;
  return ((t ^ (t >>> 14)) >>> 0) / 4294967296;
}
const pick = <T>(list: readonly T[]): T => list[Math.floor(rnd() * list.length)]!;
const between = (low: number, high: number) => low + Math.floor(rnd() * (high - low + 1));

// --- The real vocabularies ---------------------------------------------------

const WORKING_GROUPS = [
  "Valuation",
  "Descriptive Systems",
  "Populations and Health Systems",
  "Education and Outreach",
  "Youth",
  "EQ-HWB",
  "Others",
  "Dissemination, OA fee",
] as const;

const GRANT_TYPES = [
  { code: "RA", label: "Regular research project", category: "Research grants" },
  { code: "VS", label: "Valuation study", category: "Research grants" },
  { code: "SG", label: "Seed grants", category: "Research grants" },
  { code: "BT", label: "Bolt-on Toolbox validation", category: "Research grants" },
  { code: "PHD", label: "PhD grant", category: "Individual grants" },
  { code: "PD", label: "Postdoctoral grant", category: "Individual grants" },
  { code: "TVG", label: "Travel grant", category: "Individual grants" },
  { code: "EO", label: "Education and outreach project", category: "Dissemination and knowledge transfer" },
  { code: "EOI", label: "EOI for regional events", category: "Dissemination and knowledge transfer" },
  { code: "TR", label: "Tools and resources", category: "Implementation grants" },
  { code: "PCG", label: "Program coordination grants", category: "Implementation grants" },
] as const;

const INSTRUMENTS = [
  { instrumentId: "EQ-5D-3L", name: "EQ-5D-3L", family: "EQ-5D", version: "3L", isEuroQol: true },
  { instrumentId: "EQ-5D-5L", name: "EQ-5D-5L", family: "EQ-5D", version: "5L", isEuroQol: true },
  { instrumentId: "EQ-5D-Y-3L", name: "EQ-5D-Y-3L", family: "EQ-5D-Y", version: "3L", isEuroQol: true },
  { instrumentId: "EQ-5D-Y-5L", name: "EQ-5D-Y-5L", family: "EQ-5D-Y", version: "5L", isEuroQol: true },
  { instrumentId: "EQ-HWB", name: "EQ-HWB", family: "EQ-HWB", version: "full", isEuroQol: true },
  { instrumentId: "EQ-HWB-S", name: "EQ-HWB-S", family: "EQ-HWB", version: "short", isEuroQol: true },
  { instrumentId: "EQ-VAS", name: "EQ-VAS", family: "EQ-VAS", version: "", isEuroQol: true },
  { instrumentId: "SF-36", name: "SF-36", family: "SF", version: "v2", isEuroQol: false },
  { instrumentId: "HUI3", name: "HUI3", family: "HUI", version: "3", isEuroQol: false },
  { instrumentId: "AQoL-8D", name: "AQoL-8D", family: "AQoL", version: "8D", isEuroQol: false },
] as const;

const TECHNIQUES = ["cTTO", "TTO", "DCE", "DCE-TTO", "VAS", "BWS", "PTO"] as const;

const EVIDENCE_KINDS = [
  { kind: "grant_id_acknowledged", weight: 1.0 },
  { kind: "grant_id_structured", weight: 1.0 },
  { kind: "title_exact", weight: 0.95 },
  { kind: "grant_id_fulltext", weight: 0.9 },
  { kind: "title_strong", weight: 0.8 },
  { kind: "title_fuzzy", weight: 0.65 },
  { kind: "ack_pi_year", weight: 0.45 },
] as const;

const COUNTRIES = [
  ["NL", "Netherlands"], ["GB", "United Kingdom"], ["SE", "Sweden"], ["DE", "Germany"],
  ["ES", "Spain"], ["FR", "France"], ["IT", "Italy"], ["PL", "Poland"], ["DK", "Denmark"],
  ["NO", "Norway"], ["BE", "Belgium"], ["PT", "Portugal"], ["CN", "China"], ["JP", "Japan"],
  ["KR", "South Korea"], ["AU", "Australia"], ["CA", "Canada"], ["US", "United States"],
  ["BR", "Brazil"], ["ZA", "South Africa"], ["IN", "India"], ["SG", "Singapore"],
  ["ET", "Ethiopia"], ["UG", "Uganda"], ["CL", "Chile"],
] as const;

const JOURNALS = [
  "Quality of Life Research", "Value in Health", "Health and Quality of Life Outcomes",
  "The European Journal of Health Economics", "PharmacoEconomics", "Social Science and Medicine",
  "Medical Decision Making", "BMC Health Services Research", "Health Economics",
] as const;

const FIRST = ["Anna", "Bas", "Chen", "Diana", "Elena", "Farid", "Greta", "Hugo", "Ingrid",
  "Jonas", "Karin", "Luis", "Maria", "Nils", "Olga", "Pieter", "Qian", "Rosa", "Sofia",
  "Tomas", "Ulrike", "Vera", "Wei", "Xavier", "Yara", "Zoltan"] as const;
const LAST = ["Andersson", "Bakker", "Chen", "Dimitrova", "Esposito", "Fernandez", "Garcia",
  "Hansen", "Ibrahim", "Jansen", "Kowalski", "Lindqvist", "Muller", "Nguyen", "Olsen",
  "Petersen", "Quinn", "Rossi", "Silva", "Tanaka", "Ustun", "Vermeulen", "Wang", "Yilmaz"] as const;

const TOPIC = ["EQ-5D-5L valuation", "the descriptive system", "a bolt-on dimension",
  "proxy reporting", "population norms", "measurement invariance", "a value set",
  "the ceiling effect", "self-reported health", "a discrete choice experiment"] as const;
const POPULATION = ["older adults", "children", "cancer patients", "a general population sample",
  "people with diabetes", "carers", "adolescents", "stroke survivors", "the working age population"] as const;
const CONDITION = ["dementia", "type 2 diabetes", "breast cancer", "chronic pain", "asthma",
  "depression", "stroke", "COPD", "rheumatoid arthritis", "no specific condition"] as const;

// --- The generated rows ------------------------------------------------------

const N_PROJECTS = 140;
const N_PEOPLE = 70;
const N_WORKS = 260;
const N_ORGS = 34;

const people = Array.from({ length: N_PEOPLE }, (_, i) => {
  const first = pick(FIRST);
  const last = pick(LAST);
  return {
    personId: `P${String(i + 1).padStart(4, "0")}`,
    fullName: `${first} ${last}`,
    lastName: last,
    orcid: `0000-0002-${String(between(1000, 9999))}-${String(between(1000, 9999))}`,
    resolved: rnd() > 0.15,
  };
});

const organizations = Array.from({ length: N_ORGS }, (_, i) => ({
  rorId: `0${between(10000, 99999)}${i}`,
  name: `${pick(["University of", "Institute of", "Centre for"])} ${pick(["Rotterdam", "Sheffield", "Stockholm", "Munich", "Barcelona", "Lyon", "Milan", "Krakow", "Copenhagen", "Oslo", "Leuven", "Lisbon", "Beijing", "Tokyo", "Seoul", "Sydney", "Toronto", "Boston", "Sao Paulo", "Cape Town"])} Health Economics`,
  country: pick(COUNTRIES)[0],
}));

const projects = Array.from({ length: N_PROJECTS }, (_, i) => {
  const grantType = pick(GRANT_TYPES);
  const startYear = between(2008, 2024);
  const hasEnd = rnd() > 0.18;
  return {
    projectId: rnd() > 0.5 ? `${startYear}${String(between(1, 99)).padStart(3, "0")}` : `${between(10, 2599)}-${grantType.code}`,
    title: `${pick(["A study of", "Validation of", "Estimating", "Comparing", "Developing"])} ${pick(TOPIC)} in ${pick(POPULATION)}`,
    abstract: `This project examines ${pick(TOPIC)} among ${pick(POPULATION)} with ${pick(CONDITION)}. The work supports the EuroQol research programme.`,
    status: rnd() > 0.3 ? "Completed" : rnd() > 0.05 ? "Ongoing" : "Closed",
    startYear,
    endYear: hasEnd ? startYear + between(1, 4) : null,
    approvedBudgetEur: between(8, 260) * 1000,
    grantTypeCode: grantType.code,
    workingGroup: pick(WORKING_GROUPS),
    leader: pick(people).personId,
  };
});

const works = Array.from({ length: N_WORKS }, (_, i) => {
  const year = between(2010, 2026);
  return {
    workId: `doi:10.1007/s11136-${year}-${String(i + 1).padStart(5, "0")}`,
    doi: `10.1007/s11136-${year}-${String(i + 1).padStart(5, "0")}`,
    title: `${pick(["Measuring", "Valuing", "Comparing", "Assessing", "Mapping"])} ${pick(TOPIC)} in ${pick(POPULATION)} with ${pick(CONDITION)}`,
    abstract: `We report ${pick(TOPIC)} in a sample of ${pick(POPULATION)}. The analysis uses ${pick(INSTRUMENTS).name}.`,
    year,
    journalName: pick(JOURNALS),
    isOa: rnd() > 0.4,
  };
});

// Each project claims between zero and three works, through an Attribution.
let attributionCounter = 0;
let evidenceCounter = 0;
const attributions: any[] = [];
const evidences: any[] = [];
for (const project of projects) {
  const count = rnd() > 0.25 ? between(1, 3) : 0;
  for (let i = 0; i < count; i++) {
    const score = Number(rnd().toFixed(2));
    const confidence = score >= 0.85 ? "accepted" : score >= 0.6 ? "review" : "weak";
    attributionCounter += 1;
    const attributionId = `A${String(attributionCounter).padStart(5, "0")}`;
    attributions.push({
      attributionId,
      confidence,
      score,
      sources: ["europepmc", "crossref"].slice(0, between(1, 2)),
      projectId: project.projectId,
      workId: pick(works).workId,
    });
    for (let e = 0; e < between(1, 2); e++) {
      const kind = pick(EVIDENCE_KINDS);
      evidenceCounter += 1;
      evidences.push({
        evidenceId: `E${String(evidenceCounter).padStart(6, "0")}`,
        kind: kind.kind,
        weight: kind.weight,
        detail: `Matched on ${kind.kind.replace(/_/g, " ")}.`,
        attributionId,
      });
    }
  }
}

// Authorships connect a person to a work.
let authorshipCounter = 0;
const authorships: any[] = [];
for (const work of works) {
  const authorCount = between(2, 6);
  const used = new Set<string>();
  for (let position = 1; position <= authorCount; position++) {
    const person = pick(people);
    if (used.has(person.personId)) continue;
    used.add(person.personId);
    authorshipCounter += 1;
    authorships.push({
      authorshipId: `AU${String(authorshipCounter).padStart(6, "0")}`,
      position,
      isFirst: position === 1,
      isLast: position === authorCount,
      personId: person.personId,
      workId: work.workId,
      rorId: pick(organizations).rorId,
    });
  }
}

// Value sets. These make the country chart and the technique chart interesting.
const studies: any[] = [];
const valueSets: any[] = [];
const valuationWorks = works.filter(() => rnd() > 0.72);
valuationWorks.forEach((work, i) => {
  const studyId = `S${String(i + 1).padStart(4, "0")}`;
  studies.push({
    studyId,
    designCode: pick(["valuation", "cross-sectional", "psychometric", "longitudinal"]),
    aimText: `To estimate a value set using ${pick(TECHNIQUES)}.`,
    workId: work.workId,
  });
  valueSets.push({
    valueSetId: `VS${String(i + 1).padStart(4, "0")}`,
    year: work.year,
    technique: pick(TECHNIQUES),
    nRespondents: between(300, 4200),
    studyId,
    instrumentId: pick(INSTRUMENTS.filter((x) => x.isEuroQol)).instrumentId,
    countryIso2: pick(COUNTRIES)[0],
  });
});

// --- Write to the database ---------------------------------------------------

async function main() {
  const driver = neo4j.driver(uri, neo4j.auth.basic(user, password));
  await driver.verifyConnectivity();
  const session = driver.session();

  const run = (cypher: string, params: Record<string, unknown> = {}) =>
    session.run(cypher, params);

  try {
    if (wipe) {
      console.log("wiping the graph…");
      await run("MATCH (n) WHERE NOT n:_Migration DETACH DELETE n");
    }

    await run(
      `UNWIND $rows AS row MERGE (c:GrantCategory {name: row})`,
      { rows: [...new Set(GRANT_TYPES.map((g) => g.category))] },
    );
    await run(
      `UNWIND $rows AS row
       MERGE (g:GrantType {code: row.code}) SET g.label = row.label
       WITH g, row MATCH (c:GrantCategory {name: row.category})
       MERGE (g)-[:IN_CATEGORY]->(c)`,
      { rows: GRANT_TYPES as unknown as any[] },
    );
    await run(`UNWIND $rows AS row MERGE (:WorkingGroup {name: row})`, {
      rows: WORKING_GROUPS as unknown as string[],
    });
    await run(
      `UNWIND $rows AS row MERGE (c:Country {iso2: row[0]}) SET c.name = row[1]`,
      { rows: COUNTRIES as unknown as any[] },
    );
    await run(`UNWIND $rows AS row MERGE (:Journal {name: row})`, {
      rows: JOURNALS as unknown as string[],
    });
    await run(
      `UNWIND $rows AS row MERGE (i:Instrument {instrumentId: row.instrumentId})
       SET i.name = row.name, i.family = row.family, i.version = row.version,
           i.isEuroQol = row.isEuroQol`,
      { rows: INSTRUMENTS as unknown as any[] },
    );
    await run(
      `UNWIND $rows AS row MERGE (p:Person {personId: row.personId})
       SET p.fullName = row.fullName, p.lastName = row.lastName,
           p.orcid = row.orcid, p.resolved = row.resolved`,
      { rows: people },
    );
    await run(
      `UNWIND $rows AS row MERGE (o:Organization {rorId: row.rorId}) SET o.name = row.name
       WITH o, row MATCH (c:Country {iso2: row.country}) MERGE (o)-[:LOCATED_IN]->(c)`,
      { rows: organizations },
    );
    await run(
      `UNWIND $rows AS row
       MERGE (p:Project {projectId: row.projectId})
       SET p.title = row.title, p.abstract = row.abstract, p.status = row.status,
           p.startYear = row.startYear, p.endYear = row.endYear,
           p.approvedBudgetEur = row.approvedBudgetEur, p.grantTypeCode = row.grantTypeCode
       WITH p, row
       MATCH (g:GrantType {code: row.grantTypeCode}) MERGE (p)-[:OF_GRANT_TYPE]->(g)
       WITH p, row
       MATCH (w:WorkingGroup {name: row.workingGroup}) MERGE (p)-[:REVIEWED_BY]->(w)
       WITH p, row
       MATCH (leader:Person {personId: row.leader}) MERGE (p)-[:LED_BY]->(leader)`,
      { rows: projects },
    );
    await run(
      `UNWIND $rows AS row
       MERGE (w:Work {workId: row.workId})
       SET w.doi = row.doi, w.title = row.title, w.abstract = row.abstract,
           w.year = row.year, w.journalName = row.journalName, w.isOa = row.isOa
       WITH w, row MATCH (j:Journal {name: row.journalName}) MERGE (w)-[:PUBLISHED_IN]->(j)`,
      { rows: works },
    );
    await run(
      `UNWIND $rows AS row
       MERGE (a:Attribution {attributionId: row.attributionId})
       SET a.confidence = row.confidence, a.score = row.score, a.sources = row.sources
       WITH a, row MATCH (p:Project {projectId: row.projectId}) MERGE (p)-[:CLAIMS]->(a)
       WITH a, row MATCH (w:Work {workId: row.workId}) MERGE (a)-[:OF_WORK]->(w)`,
      { rows: attributions },
    );
    await run(
      `UNWIND $rows AS row
       MERGE (e:Evidence {evidenceId: row.evidenceId})
       SET e.kind = row.kind, e.weight = row.weight, e.detail = row.detail
       WITH e, row MATCH (a:Attribution {attributionId: row.attributionId})
       MERGE (a)-[:SUPPORTED_BY]->(e)`,
      { rows: evidences },
    );
    await run(
      `UNWIND $rows AS row
       MERGE (au:Authorship {authorshipId: row.authorshipId})
       SET au.position = row.position, au.isFirst = row.isFirst, au.isLast = row.isLast
       WITH au, row MATCH (p:Person {personId: row.personId}) MERGE (p)-[:AUTHORED]->(au)
       WITH au, row MATCH (w:Work {workId: row.workId}) MERGE (au)-[:OF_WORK]->(w)
       WITH au, row MATCH (o:Organization {rorId: row.rorId}) MERGE (au)-[:AT_ORGANIZATION]->(o)`,
      { rows: authorships },
    );
    await run(
      `UNWIND $rows AS row
       MERGE (s:Study {studyId: row.studyId})
       SET s.designCode = row.designCode, s.aimText = row.aimText
       WITH s, row MATCH (w:Work {workId: row.workId}) MERGE (w)-[:REPORTS]->(s)`,
      { rows: studies },
    );
    await run(
      `UNWIND $rows AS row
       MERGE (v:ValueSet {valueSetId: row.valueSetId})
       SET v.year = row.year, v.technique = row.technique, v.nRespondents = row.nRespondents
       WITH v, row MATCH (s:Study {studyId: row.studyId}) MERGE (s)-[:PRODUCED_VALUE_SET]->(v)
       WITH v, row MATCH (i:Instrument {instrumentId: row.instrumentId}) MERGE (v)-[:FOR_INSTRUMENT]->(i)
       WITH v, row MATCH (c:Country {iso2: row.countryIso2}) MERGE (v)-[:VALUES_FOR]->(c)`,
      { rows: valueSets },
    );

    const counts = await run(
      `MATCH (n) WHERE NOT n:_Migration
       RETURN labels(n)[0] AS label, count(*) AS n ORDER BY n DESC`,
    );
    console.log("\nnodes written:");
    for (const record of counts.records) {
      console.log(`  ${String(record.get("label")).padEnd(16)} ${record.get("n")}`);
    }
    const edges = await run("MATCH ()-[r]->() RETURN count(r) AS n");
    console.log(`\nrelationships: ${edges.records[0]?.get("n")}`);
  } finally {
    await session.close();
    await driver.close();
  }
}

main().catch((error) => {
  console.error(error);
  process.exit(1);
});
