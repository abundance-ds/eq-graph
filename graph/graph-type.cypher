// eq-graph schema as a declarative GRAPH TYPE.
//
// PREVIEW feature — Neo4j 2026.02+, Enterprise/Aura only, syntax may change before GA.
// graph/schema.cypher is the GA-safe equivalent and remains the one to run today.
// This file exists because GRAPH TYPE expresses two things schema.cypher cannot:
//   - which node types a relationship may connect (the closed relationship model)
//   - label implications, i.e. that every :Condition is also a :Concept
// Both are load-bearing here: layer C grows its vocabulary in data, so the label
// set has to be enforced rather than merely documented.
//
// Vector, full-text and range indexes are NOT covered by GRAPH TYPE — sections 5-7
// of graph/schema.cypher are still required alongside this.
//
// The `_`-prefixed catalog labels are deliberately left undeclared: GRAPH TYPE is an
// open model, so undeclared elements are still permitted, and the catalog is generated
// from the live database rather than authored.
//
// Untested against a live instance. Two declarations reuse a relationship type with
// different endpoints (:SAME_AS on both :Person and :Concept); confirm the preview
// accepts that union before relying on this file.

CYPHER 25
ALTER CURRENT GRAPH TYPE SET {

  // ---- Layer A: bibliographic spine ---------------------------------------

  (project:Project {
    projectId         :: STRING NOT NULL,
    title             :: STRING NOT NULL,
    abstract          :: STRING,
    status            :: STRING NOT NULL,
    startYear         :: INTEGER,
    endYear           :: INTEGER,
    approvedBudgetEur :: INTEGER,
    idScheme          :: STRING,
    sequenceNumber    :: INTEGER,
    callYear          :: INTEGER,
    revision          :: STRING
  }) REQUIRE project.projectId IS KEY,

  (wg:WorkingGroup { name :: STRING NOT NULL }) REQUIRE wg.name IS KEY,

  (gt:GrantType {
    code  :: STRING NOT NULL,
    label :: STRING NOT NULL
  }) REQUIRE gt.code IS KEY,

  (gc:GrantCategory { name :: STRING NOT NULL }) REQUIRE gc.name IS KEY,

  (work:Work {
    workId       :: STRING NOT NULL,
    title        :: STRING NOT NULL,
    abstract     :: STRING,
    doi          :: STRING,
    pmid         :: STRING,
    pmcid        :: STRING,
    year         :: INTEGER,
    journalName  :: STRING,
    isOa         :: BOOLEAN,
    licence      :: STRING,
    oaUrl        :: STRING,
    landingPage  :: STRING,
    retrieval    :: STRING
  }) REQUIRE work.workId IS KEY,

  (journal:Journal { name :: STRING NOT NULL }) REQUIRE journal.name IS KEY,

  (person:Person {
    personId :: STRING NOT NULL,
    fullName :: STRING NOT NULL,
    lastName :: STRING,
    orcid    :: STRING,
    resolved :: BOOLEAN NOT NULL
  }) REQUIRE person.personId IS KEY,

  (authorship:Authorship {
    authorshipId    :: STRING NOT NULL,
    position        :: INTEGER,
    isFirst         :: BOOLEAN,
    isLast          :: BOOLEAN,
    isCorresponding :: BOOLEAN
  }) REQUIRE authorship.authorshipId IS KEY,

  (org:Organization {
    rorId :: STRING NOT NULL,
    name  :: STRING NOT NULL,
    kind  :: STRING
  }) REQUIRE org.rorId IS KEY,

  (country:Country {
    iso2      :: STRING NOT NULL,
    name      :: STRING NOT NULL,
    m49Region :: STRING
  }) REQUIRE country.iso2 IS KEY,

  (attribution:Attribution {
    attributionId :: STRING NOT NULL,
    confidence    :: STRING NOT NULL,   // accepted | review | weak
    score         :: FLOAT NOT NULL,
    curated       :: BOOLEAN,
    sources       :: LIST<STRING>
  }) REQUIRE attribution.attributionId IS KEY,

  (evidence:Evidence {
    evidenceId :: STRING NOT NULL,
    kind       :: STRING NOT NULL,      // 7 closed values, see docs/graph-model.md
    detail     :: STRING,
    weight     :: FLOAT NOT NULL
  }) REQUIRE evidence.evidenceId IS KEY,

  (ft:FullText {
    sha256    :: STRING NOT NULL,
    path      :: STRING NOT NULL,
    format    :: STRING NOT NULL,       // xml | pdf
    bytes     :: INTEGER,
    licence   :: STRING,
    method    :: STRING,
    sourceUrl :: STRING,
    status    :: STRING
  }) REQUIRE ft.sha256 IS KEY,

  (chunk:Chunk {
    chunkId     :: STRING NOT NULL,
    text        :: STRING NOT NULL,
    source      :: STRING NOT NULL,     // fulltext | workAbstract | projectAbstract
    sectionType :: STRING,
    sectionPath :: STRING,
    chunkIndex  :: INTEGER,
    charStart   :: INTEGER,
    charEnd     :: INTEGER
  }) REQUIRE chunk.chunkId IS KEY,

  // ---- Layer B: extracted study content ------------------------------------

  (study:Study {
    studyId    :: STRING NOT NULL,
    designCode :: STRING,
    aimText    :: STRING
  }) REQUIRE study.studyId IS KEY,

  (sample:Sample {
    sampleId           :: STRING NOT NULL,
    n                  :: INTEGER,
    ageMin             :: FLOAT,
    ageMax             :: FLOAT,
    ageMean            :: FLOAT,
    femalePct          :: FLOAT,
    recruitmentSetting :: STRING
  }) REQUIRE sample.sampleId IS KEY,

  (instrument:Instrument {
    instrumentId :: STRING NOT NULL,
    name         :: STRING NOT NULL,
    family       :: STRING,
    version      :: STRING,
    isEuroQol    :: BOOLEAN NOT NULL
  }) REQUIRE instrument.instrumentId IS KEY,

  (use:InstrumentUse {
    instrumentUseId :: STRING NOT NULL,
    role            :: STRING,          // index | comparator
    mode            :: STRING,          // self | interviewer | proxy | web | paper | phone
    language        :: STRING
  }) REQUIRE use.instrumentUseId IS KEY,

  (valueSet:ValueSet {
    valueSetId   :: STRING NOT NULL,
    year         :: INTEGER,
    technique    :: STRING,             // cTTO | TTO | DCE | DCE-TTO | VAS | BWS | PTO
    nRespondents :: INTEGER
  }) REQUIRE valueSet.valueSetId IS KEY,

  (coefficient:Coefficient {
    coefficientId :: STRING NOT NULL,
    dimension     :: STRING NOT NULL,
    level         :: INTEGER NOT NULL,
    value         :: FLOAT NOT NULL,
    se            :: FLOAT
  }) REQUIRE coefficient.coefficientId IS KEY,

  (finding:Finding {
    findingId :: STRING NOT NULL,
    metric    :: STRING NOT NULL,
    statement :: STRING NOT NULL,
    value     :: FLOAT,
    ciLow     :: FLOAT,
    ciHigh    :: FLOAT,
    pValue    :: FLOAT,
    n         :: INTEGER,
    direction :: STRING
  }) REQUIRE finding.findingId IS KEY,

  // ---- Layer C: emergent vocabulary ----------------------------------------

  (concept:Concept {
    conceptId  :: STRING NOT NULL,
    prefLabel  :: STRING NOT NULL,
    definition :: STRING,
    scheme     :: STRING NOT NULL,      // mesh | cosmin | local
    kind       :: STRING,
    status     :: STRING NOT NULL,      // candidate | promoted | merged
    support    :: INTEGER NOT NULL
  }) REQUIRE concept.conceptId IS KEY,

  (term:Term {
    normalized :: STRING NOT NULL,
    text       :: STRING NOT NULL
  }) REQUIRE term.normalized IS KEY,

  // Promotion attaches a curated label; the implication keeps the two in step,
  // so a promoted concept can never lose its :Concept identity.
  (condition:Condition => :Concept),
  (method:Method       => :Concept),
  (property:Property   => :Concept),

  // ---- Relationships: the closed model -------------------------------------

  (:Project)-[:REVIEWED_BY]->(:WorkingGroup),
  (:Project)-[:OF_GRANT_TYPE]->(:GrantType),
  (:GrantType)-[:IN_CATEGORY]->(:GrantCategory),
  (:Project)-[:LED_BY]->(:Person),

  (:Project)-[:CLAIMS]->(:Attribution),
  (:Attribution)-[:TO_WORK]->(:Work),
  (:Attribution)-[:SUPPORTED_BY]->(:Evidence),

  (:Person)-[:AUTHORED]->(:Authorship),
  (:Authorship)-[:OF_WORK]->(:Work),
  (:Authorship)-[:AT_ORGANIZATION]->(:Organization),
  (:Person)-[:SAME_AS]->(:Person),
  (:Organization)-[:LOCATED_IN]->(:Country),
  (:Work)-[:PUBLISHED_IN]->(:Journal),

  (:Work)-[:HAS_FULLTEXT]->(:FullText),
  (:FullText)-[:HAS_CHUNK]->(:Chunk),
  (:Work)-[:HAS_CHUNK]->(:Chunk),
  (:Project)-[:HAS_CHUNK]->(:Chunk),

  (:Work)-[:REPORTS]->(:Study),
  (:Study)-[:ENROLLED]->(:Sample),
  (:Sample)-[:RECRUITED_IN]->(:Country),
  (:Sample)-[:HAS_CONDITION]->(:Condition),
  (:Study)-[:USED]->(:InstrumentUse),
  (:InstrumentUse)-[:OF_INSTRUMENT]->(:Instrument),
  (:Study)-[:APPLIED]->(:Method),
  (:Study)-[:PRODUCED_VALUE_SET]->(:ValueSet),
  (:ValueSet)-[:FOR_INSTRUMENT]->(:Instrument),
  (:ValueSet)-[:VALUES_FOR]->(:Country),
  (:ValueSet)-[:HAS_COEFFICIENT]->(:Coefficient),

  (:Finding)-[:ABOUT_INSTRUMENT]->(:Instrument),
  (:Finding)-[:IN_SAMPLE]->(:Sample),
  (:Finding)-[:MEASURES_PROPERTY]->(:Property),
  (:Finding)-[:USED_METHOD]->(:Method),
  (:Finding)-[:REPORTED_IN]->(:Work),
  (:Finding)-[:EXTRACTED_FROM { quote :: STRING }]->(:Chunk),

  (:Term)-[:DENOTES]->(:Concept),
  (:Concept)-[:BROADER]->(:Concept),
  (:Concept)-[:SAME_AS]->(:Concept),
  (:Chunk)-[:MENTIONS { count :: INTEGER }]->(:Concept)
};
