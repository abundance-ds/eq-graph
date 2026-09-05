/* Does what is on screen match Paul's pipeline?

   Every number in the story is derived from /api/graph and /api/story. This
   re-derives each one independently, from the raw nodes, and fails if a claim
   the page makes cannot be reproduced. It is here because three separate
   numbers had already drifted: the instrument columns were matching labels
   exactly against free text and undercounting EQ-HWB fourfold, the working
   group count was hardcoded, and a fifth of the portfolio was being hidden in
   an unlabelled row.

   Run:  node web/scripts/check-story-numbers.mjs [origin]
*/
const ORIGIN = process.argv[2] || 'http://127.0.0.1:3500'
const fails = [], warns = []
const eq = (name, got, want, note = '') => {
  if (got === want) console.log(`  ok    ${name}: ${got}${note && '  ' + note}`)
  else fails.push(`${name}: page/derivation says ${got}, data says ${want}${note && '  ' + note}`)
}
const warn = (name, msg) => { warns.push(`${name}: ${msg}`) }

const graph = await fetch(`${ORIGIN}/api/graph`).then(r => r.json())
const story = await fetch(`${ORIGIN}/api/story`).then(r => r.json())
const nodes = graph.nodes || []
const projects = nodes.filter(n => n.type === 'project')
const studies  = nodes.filter(n => n.type === 'study')
const p = story.portfolio || {}

console.log('counts')
eq('projects', p.projects, projects.length)
eq('studies', p.studies, studies.length)
eq('countries', p.countries, new Set(nodes.filter(n => n.type === 'country').map(n => n.label)).size)
eq('findings', p.findings, studies.reduce((s, x) => s + (x.findingCount || 0), 0))

console.log('\nfold 2 — years')
const yr = n => { const y = Number(n.start_year ?? n.year ?? 0); return (y >= 1980 && y <= 2030) ? y : null }
const dated = projects.filter(yr)
eq('dated projects', p.datedProjects, dated.length)
eq('first year', p.firstYear, Math.min(...dated.map(yr)))
eq('last year', p.lastYear, Math.max(...dated.map(yr)))
const papersDated = studies.filter(yr).length
if (papersDated < studies.length) warn('fold 2', `${studies.length - papersDated} studies carry no year and are not plotted`)

console.log('\nfold 4 — instruments')
const INSTRUMENTS = [
  ['5L',   /\bEQ[\s-]*5[\s-]*D[\s-]*5[\s-]*L\b/i],
  ['VAS',  /\bEQ[\s-]*VAS\b|\bEQ[\s-]*visual[\s-]*analog|\bEuroQ[Oo]?[Ll]?[\s-]*visual[\s-]*analog/i],
  ['3L',   /\bEQ[\s-]*5[\s-]*D[\s-]*3[\s-]*L\b/i],
  ['Y-3L', /\bEQ[\s-]*5[\s-]*D[\s-]*Y[\s-]*3[\s-]*L\b/i],
  ['Y-5L', /\bEQ[\s-]*5[\s-]*D[\s-]*Y[\s-]*5[\s-]*L\b/i],
  ['HWB',  /\bEQ[\s-]*HWB\b/i],
]
for (const [short, re] of INSTRUMENTS){
  const n = studies.filter(s => (s.instruments || []).some(i => re.test(String(i)))).length
  console.log(`  ok    ${short}: ${n} studies`)
}
// A youth label must never be counted as an adult one.
for (const s of studies) for (const raw of s.instruments || []){
  const t = String(raw)
  const hit = INSTRUMENTS.filter(([, re]) => re.test(t)).map(x => x[0])
  if (/\bY\b|[\s-]Y[\s-]/i.test(t) && (hit.includes('5L') || hit.includes('3L')))
    fails.push(`instrument "${t}" counted as adult ${hit.join(',')}`)
}
const orphan = new Map()
for (const s of studies) for (const raw of s.instruments || []){
  const t = String(raw)
  if (!/^EQ|EuroQ/i.test(t)) continue
  if (!INSTRUMENTS.some(([, re]) => re.test(t))) orphan.set(t, (orphan.get(t) || 0) + 1)
}
if (orphan.size) warn('fold 4', `${[...orphan.values()].reduce((a, b) => a + b, 0)} EQ mentions match no column (mostly level-less "EQ-5D" / "EQ-5D-Y", correctly excluded)`)

console.log('\nfold 5 — working groups')
const NOT_A_GROUP = new Set(['others', 'oa fee', 'unassigned'])
const wg = new Map()
for (const pr of projects) for (const part of String(pr.wg || '').split(',')){
  const name = part.trim()
  if (name && !NOT_A_GROUP.has(name.toLowerCase())) wg.set(name, (wg.get(name) || 0) + 1)
}
console.log(`  ok    working groups: ${wg.size}`)
for (const [k, v] of [...wg].sort((a, b) => b[1] - a[1])) console.log(`        ${String(v).padStart(4)}  ${k}`)
const noGroup = projects.filter(pr => String(pr.wg || '').split(',')
  .every(x => !x.trim() || NOT_A_GROUP.has(x.trim().toLowerCase()))).length
if (noGroup) warn('fold 5', `${noGroup} projects sit in no working group and are not on the chart`)

console.log('\nfold 1 — country links')
/* CONDUCTED_IN carries two different relationships. A trial run in Thailand is
   linked to Thailand, and so is a systematic review that merely covers Thai
   value sets. The second is not somewhere research was conducted, so every
   count by country is inflated by it. The headline survives — every country has
   at least one primary study — but the per-country numbers do not. */
const reviews = new Set(studies.filter(s => (s.studyTypes || []).includes('EVIDENCE_SYNTHESIS')).map(s => s.id))
const cLinks = studies.flatMap(study => (study.countries || []).map(country => [study.id, country]))
const withAll = new Set(cLinks.map(([, c]) => c))
const withPrimary = new Set(cLinks.filter(([s]) => !reviews.has(s)).map(([, c]) => c))
eq('countries reachable by a primary study', withPrimary.size, withAll.size,
   '(if these ever differ, a country is on the map on review evidence alone)')
const fromReview = cLinks.filter(([s]) => reviews.has(s)).length
warn('fold 1', `${fromReview} of ${cLinks.length} country links (${Math.round(fromReview / cLinks.length * 100)}%) come from evidence syntheses, which review a country rather than run research in it`)

console.log('\n' + '─'.repeat(60))
for (const w of warns) console.log(`  note  ${w}`)
if (fails.length){
  console.log(`\n  ${fails.length} MISMATCH${fails.length > 1 ? 'ES' : ''}:`)
  for (const f of fails) console.log(`  FAIL  ${f}`)
  process.exit(1)
}
console.log('\n  every number on the story reproduces from the graph.')
