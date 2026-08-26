const escapeText = value => String(value ?? '')
  .replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;')

const titleCase = value => {
  const source = String(value || '').replaceAll('_', ' ').trim()
  const text = /^[A-Z0-9 -]+$/.test(source) ? source.toLowerCase() : source
  return text.replace(/\bstudy$/i, '').trim()
    .replace(/(^|[-\s])\w/g, match => match.toUpperCase())
}

const valuesFor = (studies, field) => {
  const counts = new Map()
  for (const study of studies){
    for (const raw of new Set(study[field] || [])){
      const value = String(raw).trim()
      if (value) counts.set(value, (counts.get(value) || 0) + 1)
    }
  }
  return [...counts].map(([label, value]) => ({ label, value }))
    .sort((a, b) => b.value - a.value || a.label.localeCompare(b.label))
}

const hasValue = (study, field, value) => {
  // Instruments are free text from the papers, so they match on a pattern.
  // Every other field is a controlled value and still compares exactly.
  const re = field === 'instruments' ? INSTRUMENT_RE.get(value) : null
  return (study[field] || []).some(item => re
    ? re.test(String(item))
    : String(item).toLowerCase() === value.toLowerCase())
}

const countWhere = (studies, test) => studies.reduce((sum, study) => sum + Number(test(study)), 0)

const matrixCount = (studies, rowField, rowValue, columnField, columnValue) => countWhere(
  studies,
  study => hasValue(study, rowField, rowValue) && hasValue(study, columnField, columnValue),
)

const tickValues = max => {
  const rough = max / 3
  const power = 10 ** Math.floor(Math.log10(Math.max(1, rough)))
  const step = [1, 2, 5, 10].map(n => n * power).find(n => n >= rough) || power * 10
  const output = []
  for (let value = 0; value <= max + step * .25; value += step) output.push(value)
  return output
}

function rankedBars(rows, width, height, note = ''){
  const visible = rows.slice(0, width < 560 ? 7 : 9)
  const margin = { top:28, right:58, bottom:34, left:Math.min(232, width * .4) }
  const innerW = width - margin.left - margin.right
  const innerH = height - margin.top - margin.bottom
  const rowH = innerH / Math.max(1, visible.length)
  const max = Math.max(...visible.map(row => row.value), 1)
  const bars = visible.map((row, index) => {
    const y = margin.top + index * rowH + rowH * .18
    const barH = Math.max(10, rowH * .54)
    const barW = row.value / max * innerW
    return `<text class="viz-label" x="${margin.left - 12}" y="${y + barH * .72}" text-anchor="end">${escapeText(titleCase(row.label))}</text>
      <rect class="viz-bar ${index === 0 ? 'is-amber' : 'is-teal'}" x="${margin.left}" y="${y}" width="${Math.max(1, barW)}" height="${barH}" rx="2" />
      <text class="viz-value" x="${Math.min(width - 2, margin.left + barW + 8)}" y="${y + barH * .72}">${escapeText(row.display ?? row.value)}</text>`
  }).join('')
  return chartFrame(width, height, bars, note)
}

const chartFrame = (width, height, content, note = '') => `
  <svg viewBox="0 0 ${width} ${height}" focusable="false" aria-hidden="true">
    ${content}
    ${note ? `<text class="viz-note" x="0" y="${height - 5}">${escapeText(note)}</text>` : ''}
  </svg>`

function fieldShape(studies, width, height){
  const rows = valuesFor(studies, 'studyTypes').slice(0, width < 560 ? 7 : 9)
  const margin = { top:28, right:44, bottom:34, left:Math.min(178, width * .32) }
  const innerW = width - margin.left - margin.right
  const innerH = height - margin.top - margin.bottom
  const rowH = innerH / rows.length
  const max = Math.max(...rows.map(row => row.value), 1)
  const x = value => margin.left + value / max * innerW
  const ticks = tickValues(max)
  const grid = ticks.map(value => `
    <line class="viz-gridline" x1="${x(value)}" x2="${x(value)}" y1="${margin.top - 8}" y2="${height - margin.bottom}" />
    <text class="viz-axis" x="${x(value)}" y="${margin.top - 14}" text-anchor="middle">${value}</text>`).join('')
  const bars = rows.map((row, index) => {
    const y = margin.top + index * rowH + rowH * .18
    const barH = Math.max(10, rowH * .54)
    const emphasis = index === 0 ? 'is-amber' : index === 1 ? 'is-teal' : ''
    return `
      <text class="viz-label" x="${margin.left - 12}" y="${y + barH * .72}" text-anchor="end">${escapeText(titleCase(row.label))}</text>
      <rect class="viz-bar ${emphasis}" x="${margin.left}" y="${y}" width="${Math.max(1, x(row.value) - margin.left)}" height="${barH}" rx="2" />
      <text class="viz-value" x="${Math.min(width - 2, x(row.value) + 8)}" y="${y + barH * .72}">${row.value}</text>`
  }).join('')
  return chartFrame(width, height, grid + bars, 'Each study has one primary research family.')
}

/* The EQ measures a study can use, matched on a pattern rather than an exact
   string.

   Five of these are instruments; the EQ VAS is not. It is the rating scale that
   ships inside the EQ-5D questionnaire, and EuroQol does not list it among its
   instruments. It has a column because studies use it and report it on its own,
   but the axis is titled measures for that reason.

   The pipeline records the instrument as the paper wrote it, so one instrument
   arrives under many names: "EQ VAS", "EQ-VAS (Visual Analogue Scale)",
   "EQ VAS (EuroQol visual analog scale)" and nine more. Comparing strings
   exactly dropped every one of those, which put badly wrong numbers on the
   fold — EQ-HWB was showing 9 studies against a real 36.

   Separators are optional everywhere because the same instrument appears as
   EQ-5D-5L, EQ 5D 5L and EQ-5D-5 L. The youth patterns carry their Y, and the
   adult ones cannot match across one, so Y-5L is never counted as 5L.

   A label that names no level — plain "EQ-5D" or "EQ-5D-Y" — is deliberately
   matched by nothing. Assigning it to a level would be a guess, and a guess
   here is indistinguishable from data. */
const INSTRUMENTS = [
  ['EQ-5D-5L',   '5L',   /\bEQ[\s-]*5[\s-]*D[\s-]*5[\s-]*L\b/i],
  ['EQ VAS',     'VAS',  /\bEQ[\s-]*VAS\b|\bEQ[\s-]*visual[\s-]*analog|\bEuroQ[Oo]?[Ll]?[\s-]*visual[\s-]*analog/i],
  ['EQ-5D-3L',   '3L',   /\bEQ[\s-]*5[\s-]*D[\s-]*3[\s-]*L\b/i],
  ['EQ-5D-Y-3L', 'Y-3L', /\bEQ[\s-]*5[\s-]*D[\s-]*Y[\s-]*3[\s-]*L\b/i],
  ['EQ-5D-Y-5L', 'Y-5L', /\bEQ[\s-]*5[\s-]*D[\s-]*Y[\s-]*5[\s-]*L\b/i],
  // The column is the family, so the short form counts under it.
  ['EQ-HWB',     'HWB',  /\bEQ[\s-]*HWB\b/i],
]
const INSTRUMENT_RE = new Map(INSTRUMENTS.map(([label, , re]) => [label, re]))

// Values that appear in a project's working-group field but are not groups.
const NOT_A_GROUP = new Set(['others', 'oa fee', 'unassigned'])

function instrumentMatrix(studies, width, height){
  return rankedBars(
    valuesFor(studies, 'instruments'), width, height,
    'Studies in which the instrument is used directly or is the object of evaluation.',
  )
}

function methodBundles(studies, width, height){
  return rankedBars(
    valuesFor(studies, 'methods'), width, height,
    'Direct current-study methods only; planned, cited, and source-study methods are excluded.',
  )
}

function methodProfiles(studies, width, height){
  const families = new Map()
  for (const study of studies){
    const family = study.studyTypes?.[0]
    if (!family) continue
    const row = families.get(family) || { label:family, count:0, methods:0 }
    row.count += 1
    row.methods += new Set(study.methods || []).size
    families.set(family, row)
  }
  const rows = [...families.values()].map(row => ({
    label:row.label,
    value:row.methods / row.count,
    display:`${(row.methods / row.count).toFixed(1)} · n=${row.count}`,
  })).sort((a, b) => b.value - a.value || a.label.localeCompare(b.label))
  return rankedBars(rows, width, height, 'Mean distinct direct methods per study · n = studies in the family.')
}

function categoricalMatrix(studies, width, height, rows, columns, columnField, note){
  const compact = width < 560
  const left = compact ? 100 : 150
  const top = 54
  const bottom = 36
  const cellW = (width - left - 8) / columns.length
  const cellH = (height - top - bottom) / rows.length
  const values = rows.flatMap((row, rowIndex) => columns.map(([value], columnIndex) => ({
    rowIndex, columnIndex, value:matrixCount(studies, 'studyTypes', row, columnField, value),
  })))
  const max = Math.max(...values.map(item => item.value), 1)
  const labels = rows.map((row, index) => `<text class="viz-label" x="${left - 10}" y="${top + index * cellH + cellH * .62}" text-anchor="end">${escapeText(titleCase(row))}</text>`).join('')
    + columns.map(([, label], index) => `<text class="viz-axis is-strong" x="${left + index * cellW + cellW / 2}" y="${top - 18}" text-anchor="middle">${escapeText(compact && label.length > 8 ? label.slice(0, 7) + '…' : label)}</text>`).join('')
  const cells = values.map(item => {
    const opacity = item.value ? .12 + .82 * Math.sqrt(item.value / max) : .03
    return `
      <rect class="viz-matrix-cell is-teal" style="opacity:${opacity.toFixed(3)}" x="${left + item.columnIndex * cellW + 2}" y="${top + item.rowIndex * cellH + 2}" width="${Math.max(4, cellW - 4)}" height="${Math.max(4, cellH - 4)}" rx="3" />
      <text class="viz-cell-value ${opacity > .55 ? 'is-reverse' : ''}" x="${left + item.columnIndex * cellW + cellW / 2}" y="${top + item.rowIndex * cellH + cellH * .62}" text-anchor="middle">${item.value || '—'}</text>`
  }).join('')
  return chartFrame(width, height, labels + cells, note)
}

function conceptAtlas(studies, width, height){
  return rankedBars(
    valuesFor(studies, 'concepts'), width, height,
    'Number of studies tagged with each recurring scientific concept.',
  )
}

function productLandscape(studies, width, height){
  return rankedBars(
    valuesFor(studies, 'productTypes'), width, height,
    'Number of studies that produced each reusable product type.',
  )
}

const COVERAGE_ROWS = [
  'VALUE_SET_DEVELOPMENT', 'MEASUREMENT_PROPERTY_EVALUATION',
  'INSTRUMENT_VERSION_DEVELOPMENT', 'APPLIED_USE_RESEARCH',
  'HEALTH_PREFERENCE_RESEARCH', 'HEALTH_OUTCOME_RESEARCH',
]
const COVERAGE_COLUMNS = INSTRUMENTS

function coverageMatrix(studies, width, height){
      /* Rows are research types, columns are instruments, cells are the studies
         that are both. Keep the two totals lines: without them a reader has to
         add six numbers to answer "which instrument is used most". */
  const compact = width < 560
  const left = compact ? 100 : 172
  const top = compact ? 74 : 92   // room for the axis title above the names
  const bottom = 70   // room for the margin captions
  const totalW = compact ? 40 : 50
  const cellW = (width - left - totalW - 34) / COVERAGE_COLUMNS.length   // 34 leaves the rotated label its lane
  const cellH = (height - top - bottom) / (COVERAGE_ROWS.length + 1)

  const columnTotals = COVERAGE_COLUMNS.map(([instrument]) => countWhere(
    studies, study => hasValue(study, 'instruments', instrument),
  ))
  const rowTotals = COVERAGE_ROWS.map(row => countWhere(
    studies, study => hasValue(study, 'studyTypes', row),
  ))

  const cells = COVERAGE_ROWS.flatMap((row, rowIndex) => COVERAGE_COLUMNS.map(([instrument], columnIndex) => {
    const value = matrixCount(studies, 'studyTypes', row, 'instruments', instrument)
    return { rowIndex, columnIndex, value, share:value / Math.max(1, columnTotals[columnIndex]) }
  }))

  const x = i => left + i * cellW
  const y = r => top + r * cellH
  const totalX = left + COVERAGE_COLUMNS.length * cellW + 8
  const totalY = y(COVERAGE_ROWS.length) + 6

  const labels = COVERAGE_ROWS.map((row, index) =>
      `<text class="viz-label" x="${left - 10}" y="${y(index) + cellH * .62}" text-anchor="end">${escapeText(titleCase(row))}</text>`).join('')
    + COVERAGE_COLUMNS.map(([, short], index) =>
      `<text class="viz-axis is-strong" x="${x(index) + cellW / 2}" y="${top - 24}" text-anchor="middle">${escapeText(short)}</text>`).join('')
        /* The margin's label is rotated beside its own column. Set flat on top of
           the totals it read as a seventh instrument. */
    + `<text class="viz-axis-title" x="${left + (COVERAGE_COLUMNS.length * cellW) / 2}" y="${top - 44}" text-anchor="middle">EQ measures</text>`
    + `<text class="viz-axis is-strong" x="${totalX + totalW / 2}" y="${top - 24}" text-anchor="middle">Total</text>`
    + `<text class="viz-label" x="${left - 10}" y="${totalY + cellH * .62}" text-anchor="end">Total</text>`

  const marks = cells.map(item => {
    const opacity = item.value ? .12 + .84 * Math.sqrt(item.share) : .03
    return `<rect class="viz-matrix-cell is-teal" style="opacity:${opacity.toFixed(3)}" x="${x(item.columnIndex) + 2}" y="${y(item.rowIndex) + 2}" width="${Math.max(4, cellW - 4)}" height="${Math.max(4, cellH - 4)}" rx="3" />
      <text class="viz-cell-value ${opacity > .55 ? 'is-reverse' : ''}" x="${x(item.columnIndex) + cellW / 2}" y="${y(item.rowIndex) + cellH * .62}" text-anchor="middle">${item.value || '—'}</text>`
  }).join('')

  /* The margins are set as figures on the page rather than shaded cells. They
     are a different kind of number — a sum, not a crossing — and shading them
     on the same ramp would invite the eye to compare them with the cells. */
  const margins = rowTotals.map((total, index) =>
      `<text class="viz-cell-total" x="${totalX + totalW / 2}" y="${y(index) + cellH * .62}" text-anchor="middle">${total}</text>`).join('')
    + columnTotals.map((total, index) =>
      `<text class="viz-cell-total" x="${x(index) + cellW / 2}" y="${totalY + cellH * .62}" text-anchor="middle">${total}</text>`).join('')
    + `<line class="viz-rule" x1="${left - 4}" y1="${totalY - 2}" x2="${totalX + totalW}" y2="${totalY - 2}" />`
    + `<line class="viz-rule" x1="${totalX - 4}" y1="${top - 14}" x2="${totalX - 4}" y2="${totalY + cellH * .8}" />`
    // Centred under the bottom row; rotated up the side of the totals column.
    + `<text class="viz-margin-note" x="${left + (COVERAGE_COLUMNS.length * cellW) / 2}" y="${totalY + cellH + 18}" text-anchor="middle">studies using each instrument</text>`
    + `<text class="viz-margin-note" text-anchor="middle" transform="translate(${totalX + totalW + 16} ${top + (totalY - top) / 2}) rotate(-90)">studies of each research type</text>`

  return chartFrame(width, height, labels + marks + margins,
    'Number: study count. Colour: share of that instrument\'s studies. Totals count each study once; a study may use several instruments.')
}



    /* Two bars on one row, sharing a baseline and scale. The question is what
       share of a group's funding has reached the literature, which is a
       comparison. EQ-HWB is large in projects and near absent in papers; plot
       one bar and that disappears. */
function groupPapers(studies, width, height, data){
  /* Projects per working group, one dot each.

     Papers used to sit beside them as a second bar. Two quantities on one row
     invites a ratio across rows, and that ratio is not readable: the groups are
     different ages, so EQ-HWB looks like it is failing when it is simply new.
     One quantity cannot be misread that way.

     Dots rather than a bar, matching the year fold. A length asks to be
     trusted; a dot can be counted.

     A project shared between groups is counted in each of them, so the rows sum
     to more than the portfolio. The alternative, bucketing every shared project
     into one "Several groups" row, made the second largest row on the chart a
     row that is not a group at all and hid a fifth of the portfolio inside it.
     Rows are no longer capped either: the cap silently dropped the smallest
     group off the bottom. */
  const projects = (data?.nodes || []).filter(node => node.type === 'project')
  const totals = new Map()
  for (const project of projects){
    for (const part of String(project.wg || '').split(',')){
      const name = part.trim()
      if (!name || NOT_A_GROUP.has(name.toLowerCase())) continue
      totals.set(name, (totals.get(name) || 0) + 1)
    }
  }
  const rows = [...totals.entries()]
    .map(([label, funded]) => ({ label, funded }))
    .sort((a, b) => b.funded - a.funded)

  const compact = width < 560
  const left = compact ? 108 : 190
  const top = 40, bottom = 40
  const peak = Math.max(1, ...rows.map(r => r.funded))
  const bandH = (height - top - bottom) / Math.max(1, rows.length)
  const plotW = width - left - 74           // room for the count after the row

  /* Square packing, same rule as the year fold: the pitch follows from how many
     dots have to fit the longest row in the width available, so the dots very
     nearly touch instead of floating in a grid of air. */
  const bandUse = bandH * 0.72
  const perCol = Math.max(1, Math.round(Math.sqrt(peak * bandUse / plotW)))
  const pitch = Math.min(bandUse / perCol, plotW / Math.ceil(peak / perCol))
  const r = Math.max(0.8, pitch * 0.42)

  const marks = rows.map((row, index) => {
    const mid = top + index * bandH + bandH / 2
    const y0 = mid - (perCol - 1) * pitch / 2
    let dots = ''
    for (let i = 0; i < row.funded; i++){
      const cx = left + Math.floor(i / perCol) * pitch + pitch / 2
      const cy = y0 + (i % perCol) * pitch
      dots += `<circle class="viz-dot" cx="${cx.toFixed(1)}" cy="${cy.toFixed(1)}" r="${r.toFixed(2)}" />`
    }
    const cols = Math.ceil(row.funded / perCol)
    const endX = left + cols * pitch + 10
    return `<text class="viz-label" x="${left - 12}" y="${mid + 1}" text-anchor="end">${escapeText(row.label)}</text>
      ${dots}
      <text class="viz-cell-total" x="${endX.toFixed(1)}" y="${mid + 1}" text-anchor="start">${row.funded}</text>`
  }).join('')

  const key = `<circle class="viz-dot" cx="${left + 4}" cy="${top - 24}" r="${Math.min(3, r).toFixed(2)}" />
    <text class="viz-axis" x="${left + 14}" y="${top - 20}">one dot is one funded project</text>`

  return chartFrame(width, height, key + marks,
    'A shared project counts in each of its groups, so the rows total more than the portfolio.')
}


    /* Phosphor regular, inlined rather than loaded so the page stays
       self-contained. */
const ICON = {
  paper: 'M216,40H40A16,16,0,0,0,24,56V200a16,16,0,0,0,16,16H216a16,16,0,0,0,16-16V56A16,16,0,0,0,216,40Zm0,160H40V56H216V200ZM184,96a8,8,0,0,1-8,8H80a8,8,0,0,1,0-16h96A8,8,0,0,1,184,96Zm0,32a8,8,0,0,1-8,8H80a8,8,0,0,1,0-16h96A8,8,0,0,1,184,128Zm0,32a8,8,0,0,1-8,8H80a8,8,0,0,1,0-16h96A8,8,0,0,1,184,160Z',
  people: 'M117.25,157.92a60,60,0,1,0-66.5,0A95.83,95.83,0,0,0,3.53,195.63a8,8,0,1,0,13.4,8.74,80,80,0,0,1,134.14,0,8,8,0,0,0,13.4-8.74A95.83,95.83,0,0,0,117.25,157.92ZM40,108a44,44,0,1,1,44,44A44.05,44.05,0,0,1,40,108Zm210.14,98.7a8,8,0,0,1-11.07-2.33A79.83,79.83,0,0,0,172,168a8,8,0,0,1,0-16,44,44,0,1,0-16.34-84.87,8,8,0,1,1-5.94-14.85,60,60,0,0,1,55.53,105.64,95.83,95.83,0,0,1,47.22,37.71A8,8,0,0,1,250.14,206.7Z',
}
const icon = name =>
  `<svg class="viz-ico" viewBox="0 0 256 256" fill="currentColor" aria-hidden="true"><path d="${ICON[name]}"/></svg>`


    /* Structurally Paul's, including his force parameters. Do not clamp nodes
       inside a box: they pin to the edge and the links cross the middle. The
       centring force does that job. Only the largest are named — labelling
       every node turns a network into a diagram of labels. */
/* The most cited work, one dot per citation.

   Every other fold counts what EuroQol did. This counts what the rest of the
   field did with it: a citation is somebody else, unprompted, building on the
   work. One dot is one citation, the same rule as everywhere else, so the top
   paper's block is visibly larger than the bottom several put together — which
   is the honest shape of citation, not a flaw in the chart.

   Colour is the working group that funded it. Only three or four appear at this
   depth, few enough to tell apart without inventing a palette: the two brand
   colours carry the largest and the rest take neutral steps. */
const GROUP_INK = [
  ['Valuation',                      'var(--teal)'],
  ['Descriptive Systems',            'var(--yellow)'],
  ['Youth',                          '#5b8f86'],
  ['Populations and Health Systems', '#9aa3a1'],
  ['EQ-HWB',                         '#c2b48a'],
]
const groupInk = name => (GROUP_INK.find(g => g[0] === name) || [, '#b9beba'])[1]

function citedWork(studies, width, height, data, coauthors, cites){
  const papers = (cites && cites.papers) || []
  if (!papers.length) return chartFrame(width, height, '', 'Citation data not loaded.')

  const compact = width < 620
  const rows = papers.slice(0, compact ? 8 : 12)
  const left = compact ? 8 : 14
  const top = 58, bottom = 34
  const bandH = (height - top - bottom) / rows.length
  const peak = Math.max(...rows.map(r => r.citations))
  const plotW = width - left - 64

  /* One pitch for the whole chart, set by the longest row, so a dot means the
     same thing on every line. */
  const bandUse = bandH * 0.52
  const perCol = Math.max(2, Math.round(Math.sqrt(peak * bandUse / plotW)))
  const pitch = Math.min(bandUse / perCol, plotW / Math.ceil(peak / perCol))
  const r = Math.max(0.7, pitch * 0.42)

  const marks = rows.map((row, index) => {
    const mid = top + index * bandH + bandH * 0.62
    const y0 = mid - (perCol - 1) * pitch / 2
    const ink = groupInk(row.group)
    let dots = ''
    for (let i = 0; i < row.citations; i++){
      const cx = left + Math.floor(i / perCol) * pitch + pitch / 2
      const cy = y0 + (i % perCol) * pitch
      dots += `<circle cx="${cx.toFixed(1)}" cy="${cy.toFixed(1)}" r="${r.toFixed(2)}" fill="${ink}" />`
    }
    const endX = left + Math.ceil(row.citations / perCol) * pitch + 9
    const title = row.title.length > 76 ? row.title.slice(0, 75) + '…' : row.title
    return `${dots}
      <text class="viz-cell-total" x="${endX.toFixed(1)}" y="${(mid + 1).toFixed(1)}" text-anchor="start">${row.citations}</text>
      <text class="viz-label" x="${left}" y="${(top + index * bandH + bandH * 0.22).toFixed(1)}" text-anchor="start">${escapeText(title)}</text>`
  }).join('')

  // The key names only the groups actually on the chart.
  const shown = [...new Set(rows.map(x => x.group).filter(Boolean))]
  let kx = left
  const key = shown.map(name => {
    const bit = `<circle cx="${kx + 4}" cy="${top - 34}" r="3.4" fill="${groupInk(name)}" />
      <text class="viz-axis" x="${kx + 13}" y="${top - 30}">${escapeText(name)}</text>`
    kx += name.length * 6.4 + 30
    return bit
  }).join('')

  return chartFrame(width, height, key + marks,
    `One dot is one citation. OpenAlex, ${cites.retrieved}. ${cites.totalPublications} papers have earned ${cites.totalCitations.toLocaleString('en')} between them.`)
}

function coauthorNetwork(studies, width, height, data, coauthors){
  if (!coauthors || !coauthors.nodes) return chartFrame(width, height, '', 'Co-authorship data not loaded.')

  const TOP = width < 720 ? 40 : 72
  const people = [...coauthors.nodes].sort((a, b) => b.paper_count - a.paper_count).slice(0, TOP)
  const keep = new Set(people.map(p => p.person_id))
  const links = coauthors.edges.filter(e => keep.has(e.source) && keep.has(e.target))

  const top = 44, bottom = 34
  const w = width, h = height - top - bottom
  const cx = w / 2, cy = top + h / 2
  const maxPapers = Math.max(1, ...people.map(p => p.paper_count))
  const rOf = n => 7 + Math.sqrt(n / maxPapers) * 20

  const at = new Map()
  people.forEach((p, i) => {
    // a phyllotaxis spiral, so the start is spread rather than a ring, and
    // deterministic so the same data always settles the same way
    const a = i * 2.399963, rr = Math.sqrt(i) * 13
    at.set(p.person_id, { id:p.person_id, p, x: cx + Math.cos(a) * rr, y: cy + Math.sin(a) * rr, vx:0, vy:0, r: rOf(p.paper_count) })
  })
  const nodes = [...at.values()]

  for (let step = 0; step < 320; step++){
    const cool = 1 - step / 360
    for (let i = 0; i < nodes.length; i++){
      const A = nodes[i]
      for (let j = i + 1; j < nodes.length; j++){
        const B = nodes[j]
        let dx = B.x - A.x, dy = B.y - A.y
        let d = Math.hypot(dx, dy) || 0.01
        // charge: bigger authors push harder, as in his setup
        // stronger than Paul's, because his canvas is a full dark screen and
        // this one is half a fold: the same charge packs into a ball here
        const q = (34 + A.p.paper_count * 1.7) * 2.4 / (d * d)
        const ux = dx / d, uy = dy / d
        A.vx -= ux * q * cool; A.vy -= uy * q * cool
        B.vx += ux * q * cool; B.vy += uy * q * cool
        // collide: circles must not sit on top of each other
        const min = A.r + B.r + 7
        if (d < min){
          const push = (min - d) * 0.5
          A.x -= ux * push; A.y -= uy * push
          B.x += ux * push; B.y += uy * push
        }
      }
      A.vx += (cx - A.x) * 0.035 * cool
      A.vy += (cy - A.y) * 0.035 * cool
    }
    for (const e of links){
      const A = at.get(e.source), B = at.get(e.target)
      const dx = B.x - A.x, dy = B.y - A.y
      const d = Math.max(0.01, Math.hypot(dx, dy))
          /* The more two people publish together, the shorter the spring. The range
             matters as much as the rule: at a narrow spread every pair sits at
             the same distance and the encoding is invisible. */
      const rest = 260 / Math.pow(e.coauthored_paper_count, 0.85)
      const k = Math.min(0.95, 0.18 + e.coauthored_paper_count * 0.10)
      const f = (d - rest) * k * 0.045 * cool
      const ux = dx / d, uy = dy / d
      A.vx += ux * f; A.vy += uy * f
      B.vx -= ux * f; B.vy -= uy * f
    }
    for (const A of nodes){ A.x += A.vx; A.y += A.vy; A.vx *= 0.62; A.vy *= 0.62 }
  }

  /* Fit by scaling what settled, not by clamping.

     The budget is the room a MARK needs, not the room a centre needs. Fitting
     the centres alone let the largest circles and their name plates hang past
     the frame, so the network ran off the right of the screen. Every inset
     below therefore carries the biggest radius: the legend along the top and
     the names hanging under their circles get their own allowance on top. */
  const xs = nodes.map(n => n.x), ys = nodes.map(n => n.y)
  const sx = Math.max(...xs) - Math.min(...xs), sy = Math.max(...ys) - Math.min(...ys)
  const maxR = Math.max(...nodes.map(n => n.r))
  const padX = maxR + 12
  const padTop = maxR + 38                    // the key sits along the top
  const padBottom = maxR + 24                 // names hang below their circle
  const availW = Math.max(40, w - padX * 2)
  const availH = Math.max(40, h - padTop - padBottom)
  const k = Math.min(availW / (sx || 1), availH / (sy || 1), 2.4)
  /* The blob settles roughly square, so height binds first and the field left a
     third of its width empty. Stretched across a little, capped at a third more
     than the uniform fit: the layout is a force result rather than a metric
     space, so widening it costs nothing real, but past this the clusters start
     to read as ellipses. */
  const kWide = Math.min(availW / (sx || 1), k * 1.34)
  const ox = (padX + availW / 2) - ((Math.min(...xs) + Math.max(...xs)) / 2) * kWide
  const oy = (padTop + availH / 2) - ((Math.min(...ys) + Math.max(...ys)) / 2) * k
  for (const n of nodes){ n.x = n.x * kWide + ox; n.y = n.y * k + oy }
  const fitBox = { padX, padTop, padBottom }

  const heaviest = Math.max(1, ...links.map(l => l.coauthored_paper_count))
  const wire = links.map((e, i) => {
    const A = at.get(e.source), B = at.get(e.target)
    return `<line class="viz-net-link" data-a="${e.source}" data-b="${e.target}" x1="${A.x.toFixed(1)}" y1="${A.y.toFixed(1)}" x2="${B.x.toFixed(1)}" y2="${B.y.toFixed(1)}" style="stroke-width:${(0.4 + (e.coauthored_paper_count / heaviest) * 2.6).toFixed(2)}" />`
  }).join('')

  const named = new Set([...nodes].sort((a, b) => b.p.paper_count - a.p.paper_count).slice(0, 12).map(n => n.id))
      /* Shade carries paper count, and so does size. Doubling up is deliberate:
         a size difference alone is hard to judge at these radii. Non-members
         stay grey on the same ramp — a second hue would make membership look
         like a third quantity. */
  const shade = n => {
    const t = Math.sqrt(n.paper_count / maxPapers)
    return n.euroqol_member
      ? `rgb(${Math.round(196 - t * 176)},${Math.round(226 - t * 108)},${Math.round(218 - t * 110)})`
      : `rgb(${Math.round(226 - t * 46)},${Math.round(226 - t * 46)},${Math.round(219 - t * 44)})`
  }

  /* One soft field behind the whole cluster, lighting it from underneath.

     A halo on each node was the wrong reading of this: seventy small rings ate
     the space between the marks and said nothing. A single wide haze says the
     same thing the reference does, that these dots are one specimen under a
     light, and it leaves the space between them alone. The core is near-white
     so the middle stays clean and the dots keep their contrast; the warmth only
     appears at the edge, where there is nothing to read. */
  const hz = {
    x:(Math.min(...nodes.map(n => n.x)) + Math.max(...nodes.map(n => n.x))) / 2,
    y:(Math.min(...nodes.map(n => n.y)) + Math.max(...nodes.map(n => n.y))) / 2,
  }
  hz.r = Math.max(...nodes.map(n => Math.hypot(n.x - hz.x, n.y - hz.y))) * 1.18 + 40
  const haze = `<defs>
      <linearGradient id="viz-net-sheen" x1="0" y1="0" x2="1" y2="0">
        <stop offset="0%"   stop-color="rgb(255,238,170)" stop-opacity="0" />
        <stop offset="38%"  stop-color="rgb(255,245,205)" stop-opacity=".30" />
        <stop offset="50%"  stop-color="rgb(255,250,225)" stop-opacity=".72" />
        <stop offset="62%"  stop-color="rgb(255,245,205)" stop-opacity=".30" />
        <stop offset="100%" stop-color="rgb(255,238,170)" stop-opacity="0" />
        <animateTransform attributeName="gradientTransform" type="translate"
          from="-1 0" to="1 0" dur="1.6s" repeatCount="indefinite" />
      </linearGradient>
      <radialGradient id="viz-net-haze">
        <stop offset="0%"   stop-color="#ffffff" stop-opacity=".72" />
        <stop offset="42%"  stop-color="#ffffff" stop-opacity=".58" />
        <stop offset="63%"  stop-color="rgb(214,163,60)" stop-opacity=".22" />
        <stop offset="82%"  stop-color="rgb(0,125,108)" stop-opacity=".10" />
        <stop offset="100%" stop-color="rgb(0,125,108)" stop-opacity="0" />
      </radialGradient>
    </defs>
    <circle class="viz-net-haze" cx="${hz.x.toFixed(1)}" cy="${hz.y.toFixed(1)}" r="${hz.r.toFixed(1)}" />`

  const marks = nodes.map((n, i) => {
    const cls = n.p.euroqol_member ? 'is-member' : 'is-other'
    const ring = n.p.project_leader
      ? `<circle class="viz-net-ring" data-id="${n.id}" cx="${n.x.toFixed(1)}" cy="${n.y.toFixed(1)}" r="${(n.r + 2.6).toFixed(1)}" />` : ''
    // The count goes inside wherever the circle can hold it legibly. Below
    // about eleven pixels the digits would be smaller than the label beneath,
    // and a number too small to read is just texture.
    const count = n.r >= 11
      ? `<text class="viz-net-count" data-id="${n.id}" x="${n.x.toFixed(1)}" y="${(n.y + n.r * 0.32).toFixed(1)}" text-anchor="middle" style="font-size:${Math.max(10, n.r * 0.82).toFixed(1)}px">${n.p.paper_count}</text>`
      : ''
    // Biggest arrive first, so the shape of the field is established before the
    // detail fills in. Capped, or the tail of the network is still landing long
    // after the reader has moved on.
    const delay = Math.min(0.44, i * 0.006).toFixed(3)
    return `${ring}<circle class="viz-net-node ${cls}" data-id="${n.id}" data-name="${escapeText(n.p.name)}" data-papers="${n.p.paper_count}" cx="${n.x.toFixed(1)}" cy="${n.y.toFixed(1)}" r="${n.r.toFixed(1)}" style="fill:${shade(n.p)};animation-delay:${delay}s" />${count}`
  }).join('')

      /* Show the encoding, do not describe it. A small circle beside a large
         one states the mapping in the form the reader is about to meet. */
      /* Names go in a pass of their own, after every circle and line, or a name
         ends up under a later circle. Each carries a plate of the page colour. */
      /* A name is drawn only if it lands clear of every name already placed,
         biggest first. That is why some circles have no label. */
  /* Names are placed once, here, after every circle and line so a label is
     never buried. Four positions are tried per name and the first clear one
     wins; if none is clear the name is dropped, because the circle is still
     shaded and sized, so the quantity is on the page either way. Biggest first,
     so when two compete the more significant author keeps their label. */
  const taken = []
  const plates = nodes.filter(n => named.has(n.id))
    .sort((a, b) => b.p.paper_count - a.p.paper_count)
    .map(n => {
      const t = n.p.name, w = t.length * 6.6
      const spots = [
        { x:n.x, y:n.y + n.r + 13 },            // below
        { x:n.x, y:n.y - n.r - 7 },             // above
        { x:n.x + n.r + 6 + w / 2, y:n.y + 4 }, // right
        { x:n.x - n.r - 6 - w / 2, y:n.y + 4 }, // left
      ]
      const spot = spots.find(c =>
        !taken.some(q => Math.abs(q.x - c.x) < (q.w + w) / 2 + 8 && Math.abs(q.y - c.y) < 15) &&
        !nodes.some(m => m !== n && Math.abs(m.x - c.x) < w / 2 + m.r - 2 && Math.abs(m.y - c.y) < m.r + 4))
      if (!spot) return ''
      taken.push({ x:spot.x, y:spot.y, w })
      return `<rect class="viz-net-plate" data-id="${n.id}" x="${(spot.x - w / 2 - 4).toFixed(1)}" y="${(spot.y - 10).toFixed(1)}" width="${(w + 8).toFixed(1)}" height="14" rx="4" />
        <text class="viz-net-name" data-id="${n.id}" x="${spot.x.toFixed(1)}" y="${spot.y.toFixed(1)}" text-anchor="middle">${escapeText(t)}</text>`
    }).join('')

  const members = people.filter(p => p.euroqol_member).length
  const smallest = Math.min(...people.map(p => p.paper_count))
      /* Each item declares its width and the row advances by it. Literal x
         offsets collide the moment a label changes length. */
  const ky = 20
  const CHAR = 6.6
  let kx = 6
  const bits = []
  const put = (mark, text, extra = 0) => {
    const w = text.length * CHAR + 22 + extra
    if (kx + w > width - 8) return          // no room: leave it out rather than overlap
    bits.push(mark(kx))
    bits.push(`<text class="viz-net-key" x="${kx + 16 + extra}" y="${ky + 4}">${text}</text>`)
    kx += w + 14
  }
  const deep = shade({ paper_count: maxPapers, euroqol_member: true })
  const pale = shade({ paper_count: smallest, euroqol_member: true })
  put(x => `<circle class="viz-net-node" cx="${x + 6}" cy="${ky}" r="6" style="fill:${deep}" />`, 'EuroQol member')
  put(x => `<circle class="viz-net-node" cx="${x + 6}" cy="${ky}" r="6" style="fill:${shade({ paper_count: maxPapers, euroqol_member: false })}" />`, 'other author')
  put(x => `<circle class="viz-net-ring" cx="${x + 7}" cy="${ky}" r="7.5" />`, 'project leader')
  put(x => `<circle class="viz-net-node" cx="${x + 4}" cy="${ky}" r="3.5" style="fill:${pale}" />
            <circle class="viz-net-node" cx="${x + 20}" cy="${ky}" r="9" style="fill:${deep}" />`,
      `${smallest}-${maxPapers} papers`, 16)
  put(x => `<line class="viz-net-link" x1="${x}" y1="${ky - 3}" x2="${x + 22}" y2="${ky - 3}" style="stroke-width:.6" />
            <line class="viz-net-link" x1="${x}" y1="${ky + 4}" x2="${x + 22}" y2="${ky + 4}" style="stroke-width:3" />`,
      'more shared papers', 10)
  const key = bits.join('')


  return chartFrame(width, height, haze + key + wire + marks + plates, 'Hover to follow one person. Click to keep them.')
}

const RENDERERS = {
  fieldShape,
  instrumentMatrix,
  methodBundles,
  methodProfiles,
  conceptAtlas,
  productLandscape,
  coverageMatrix,
  citedWork,
  groupPapers,
  coauthorNetwork,
}

export function createStoryCharts(data, root, coauthors = null, cites = null){
  const host = root.querySelector('[data-charts]')
  const studies = data.nodes.filter(node => node.type === 'study')
  if (!host) return { resize(){}, show(){}, destroy(){} }

  host.innerHTML = Object.keys(RENDERERS).map(id => `
    <div class="sh-chart-scene" data-chart="${id}"><svg /></div>`).join('')
  const scenes = new Map([...host.querySelectorAll('[data-chart]')].map(scene => [scene.dataset.chart, scene]))

      /* One click lights that person and everyone they have written with. The
         panel names the strongest links, because a thick line says a bond is
         strong without saying whose. Background click lets go. */
  const adjacency = new Map()
  if (coauthors && coauthors.edges){
    for (const e of coauthors.edges){
      if (!adjacency.has(e.source)) adjacency.set(e.source, [])
      if (!adjacency.has(e.target)) adjacency.set(e.target, [])
      adjacency.get(e.source).push({ id:e.target, w:e.coauthored_paper_count })
      adjacency.get(e.target).push({ id:e.source, w:e.coauthored_paper_count })
    }
  }
  const nameOf = new Map((coauthors?.nodes || []).map(n => [n.person_id, n.name]))
  let panel = null

  /* Clicking someone reforms the network around them.

     The whole story moves by flying its marks from one arrangement to the next,
     and this is that same move. The chosen author settles in the middle, the
     people they have written with pull into an orbit ordered by how often, and
     everyone else drifts outward and thins away. Reading the answer means
     watching the field become the answer, which is the thing a static highlight
     cannot do.

     Positions are tweened and written as attributes each frame, links included,
     rather than handed to CSS. The endpoints have to stay attached to the
     circles while they travel, and a transform on the marks alone would leave
     every line behind. */
  const REFORM_MS = 900
  const reformState = new WeakMap()

  function indexScene(scene){
    let idx = reformState.get(scene)
    if (idx) return idx
    const svg = scene.querySelector('svg')
    if (!svg) return null
    const byId = new Map()
    // Every mark that belongs to a node, with its offset from that node's home,
    // so the group keeps its shape as it moves.
    for (const el of svg.querySelectorAll('[data-id]')){
      const id = el.dataset.id
      const isCircle = el.tagName === 'circle'
      const ax = isCircle ? 'cx' : 'x', ay = isCircle ? 'cy' : 'y'
      const x = parseFloat(el.getAttribute(ax)), y = parseFloat(el.getAttribute(ay))
      if (!Number.isFinite(x) || !Number.isFinite(y)) continue
      const row = byId.get(id) || { id, home:null, els:[] }
      if (el.classList.contains('viz-net-node')) row.home = { x, y }
      row.els.push({ el, ax, ay, x, y })
      byId.set(id, row)
    }
    // Offsets are only meaningful once the node's own centre is known.
    for (const row of byId.values()){
      if (!row.home){ byId.delete(row.id); continue }
      for (const m of row.els){ m.dx = m.x - row.home.x; m.dy = m.y - row.home.y }
      row.at = { ...row.home }
    }
    const links = [...svg.querySelectorAll('.viz-net-link')].filter(l => l.dataset.a && l.dataset.b)
    const g = svg.querySelector('.viz-net-haze')
    const homeGlow = g
      ? { x:+g.getAttribute('cx'), y:+g.getAttribute('cy'), r:+g.getAttribute('r') }
      : { x:0, y:0, r:0 }
    idx = { svg, byId, links, frame:0, homeGlow }
    reformState.set(scene, idx)
    return idx
  }

  function paint(idx){
    for (const row of idx.byId.values())
      for (const m of row.els){
        m.el.setAttribute(m.ax, (row.at.x + m.dx).toFixed(1))
        m.el.setAttribute(m.ay, (row.at.y + m.dy).toFixed(1))
      }
    for (const line of idx.links){
      const A = idx.byId.get(line.dataset.a), B = idx.byId.get(line.dataset.b)
      if (!A || !B) continue
      line.setAttribute('x1', A.at.x.toFixed(1)); line.setAttribute('y1', A.at.y.toFixed(1))
      line.setAttribute('x2', B.at.x.toFixed(1)); line.setAttribute('y2', B.at.y.toFixed(1))
    }
  }

  function reform(scene, id){
    const idx = indexScene(scene)
    if (!idx) return
    const box = idx.svg.viewBox.baseVal
    // Leaning up and right of centre keeps the orbit clear of the panel, which
    // sits bottom left and would otherwise cover the closest collaborators.
    const cx = box.width * 0.54, cy = box.height * 0.44

    const targets = new Map()
    if (id){
      const partners = (adjacency.get(id) || []).filter(x => idx.byId.has(x.id))
        .sort((a, b) => b.w - a.w)
      targets.set(id, { x:cx, y:cy })
      /* Rings widen as they go out, and each holds more than the last, because
         a ring's circumference grows with its radius. Fixed seats per ring
         packed the inner one until the circles overlapped. Closest ring is the
         strongest collaborators, so distance reads as how often. */
      const SEATS = [7, 12, 17, 22]
      const rings = []
      for (let i = 0, k = 0; i < partners.length; k++){
        const take = SEATS[Math.min(k, SEATS.length - 1)]
        rings.push(partners.slice(i, i + take)); i += take
      }
      /* Bounded by the room that actually exists on each side, not by the box.
         Taken from the box alone the widest ring ran up into the legend. The
         top allowance is larger because that is where the key sits. */
      const span = Math.max(70, Math.min(
        (cy - 46) / 0.82,                       // clear of the legend
        (box.height - cy - 20) / 0.82,
        cx - 18, box.width - cx - 18))
      rings.forEach((ring, k) => {
        const rad = span * ((k + 1) / rings.length) * 0.92
        ring.forEach((x, seat) => {
          const a = (seat / ring.length) * Math.PI * 2 - Math.PI / 2 + k * 0.42
          targets.set(x.id, { x:cx + Math.cos(a) * rad, y:cy + Math.sin(a) * rad * 0.82 })
        })
      })
      // Everyone else is pushed straight out from where they already are, so
      // the field opens rather than shuffling.
      for (const row of idx.byId.values()){
        if (targets.has(row.id)) continue
        const vx = row.home.x - cx, vy = row.home.y - cy
        const d = Math.hypot(vx, vy) || 1
        targets.set(row.id, { x:cx + (vx / d) * (d + 190), y:cy + (vy / d) * (d + 190) })
      }
    } else {
      for (const row of idx.byId.values()) targets.set(row.id, { ...row.home })
    }

    // The light follows the specimen. Left where it was, the haze would sit off
    // to one side of a reformed cluster and read as a stain on the page.
    const glow = idx.svg.querySelector('.viz-net-haze')
    const glowFrom = glow
      ? { x:+glow.getAttribute('cx'), y:+glow.getAttribute('cy'), r:+glow.getAttribute('r') } : null
    const glowTo = glow
      ? (id ? { x:cx, y:cy, r:idx.homeGlow.r * 0.92 } : { ...idx.homeGlow }) : null

    const from = new Map([...idx.byId.values()].map(r => [r.id, { ...r.at }]))

    /* Each mark that has far to go comes apart into motes for the journey and
       puts itself back together on arrival, which is the move the opening fold
       makes with the headline. Grey on purpose: the motes are the same mark in
       transit, not a new quantity, and giving them the node's own colour would
       read as more circles appearing. */
    const NS = 'http://www.w3.org/2000/svg'
    idx.svg.querySelectorAll('.viz-net-mote').forEach(el => el.remove())
    const motes = []
    for (const row of idx.byId.values()){
      const a = from.get(row.id), b = targets.get(row.id)
      const trip = Math.hypot(b.x - a.x, b.y - a.y)
      if (trip < 34) continue
      const count = Math.min(7, 2 + Math.round(trip / 90))
      for (let j = 0; j < count; j++){
        const el = document.createElementNS(NS, 'circle')
        el.setAttribute('class', 'viz-net-mote')
        el.setAttribute('r', (0.9 + (j % 3) * 0.35).toFixed(2))
        idx.svg.appendChild(el)
        // Each mote takes its own arc and its own pace, so the group scatters
        // and gathers instead of sliding across as one rigid shape.
        motes.push({ el, a, b,
          off:(j / count) * 0.34,
          arc:((j % 2 ? 1 : -1) * (10 + (j * 7) % 26)),
          spread:(j % 4) * 5 })
      }
    }

    const t0 = performance.now()
    cancelAnimationFrame(idx.frame)
    const step = now => {
      const t = Math.min(1, (now - t0) / REFORM_MS)
      const e = 1 - Math.pow(1 - t, 3)          // out-cubic, so it settles
      for (const row of idx.byId.values()){
        const a = from.get(row.id), b = targets.get(row.id)
        row.at.x = a.x + (b.x - a.x) * e
        row.at.y = a.y + (b.y - a.y) * e
      }
      if (glow && glowFrom && glowTo){
        glow.setAttribute('cx', (glowFrom.x + (glowTo.x - glowFrom.x) * e).toFixed(1))
        glow.setAttribute('cy', (glowFrom.y + (glowTo.y - glowFrom.y) * e).toFixed(1))
        glow.setAttribute('r',  (glowFrom.r + (glowTo.r - glowFrom.r) * e).toFixed(1))
      }
      // While its motes are out, the mark itself is thin. It is in pieces.
      if (motes.length){
        const apart = Math.sin(Math.min(1, t) * Math.PI)
        for (const row of idx.byId.values()){
          const node = row.els.find(m => m.el.classList.contains('viz-net-node'))
          if (node) node.el.style.opacity = (1 - apart * 0.55).toFixed(3)
        }
      }
      for (const m of motes){
        const mt = Math.max(0, Math.min(1, (t - m.off) / (1 - m.off)))
        const me = 1 - Math.pow(1 - mt, 3)
        const nx = m.a.x + (m.b.x - m.a.x) * me
        const ny = m.a.y + (m.b.y - m.a.y) * me
        const bow = Math.sin(mt * Math.PI)          // widest at half way
        m.el.setAttribute('cx', (nx + m.arc * bow).toFixed(1))
        m.el.setAttribute('cy', (ny + m.spread * bow).toFixed(1))
        m.el.setAttribute('opacity', (bow * 0.5).toFixed(3))
      }
      paint(idx)
      if (t < 1) idx.frame = requestAnimationFrame(step)
      else {
        motes.forEach(m => m.el.remove())
        for (const row of idx.byId.values())
          for (const m of row.els) m.el.style.opacity = ''
      }
    }
    idx.frame = requestAnimationFrame(step)
  }

  function clearPick(scene){
    sheenOff(scene)
    reform(scene, null)
    scene.classList.remove('is-focused')
    scene.querySelectorAll('.is-picked, .is-faded, .is-lit').forEach(el => el.classList.remove('is-picked', 'is-faded', 'is-lit'))
    if (panel) { panel.remove(); panel = null }
  }

  function pick(scene, id){
    const near = new Set((adjacency.get(id) || []).map(x => x.id))
    near.add(id)
    scene.querySelectorAll('[data-id]').forEach(el => {
      const mine = el.dataset.id
      el.classList.toggle('is-faded', !near.has(mine))
      el.classList.toggle('is-picked', mine === id)
    })
    scene.querySelectorAll('.viz-net-link').forEach(el => {
      el.classList.toggle('is-faded', el.dataset.a !== id && el.dataset.b !== id)
    })
    const partners = (adjacency.get(id) || []).slice().sort((a, b) => b.w - a.w)
    const strongest = partners.slice(0, 4).map(x => `${nameOf.get(x.id) || 'unknown'} (${x.w})`).join(', ')
    // The leader ring carries the same data-id and sits before the node in the
    // markup, so a bare circle[data-id] lookup found the ring, which has no
    // paper count on it. Hence every panel said "0 papers".
    const node = scene.querySelector(`circle.viz-net-node[data-id="${id}"]`)
    if (panel) panel.remove()
    panel = document.createElement('div')
    panel.className = 'viz-net-panel'
    panel.innerHTML = `<strong>${nameOf.get(id) || ''}</strong>
      <span class="viz-net-figs">
        <span class="viz-fig">${icon('paper')}<b>${node?.dataset.papers || 0}</b> papers</span>
        <span class="viz-fig">${icon('people')}<b>${partners.length}</b> co-authors</span>
      </span>
      ${strongest ? `<span>Most often with ${strongest}</span>` : ''}
      <button type="button" aria-label="Close">×</button>`
    panel.querySelector('button').onclick = () => clearPick(scene)
    scene.appendChild(panel)
    sheenOff(scene)
    reform(scene, id)
  }

      /* Hover is temporary and leaves nothing behind. A kept selection is not
         disturbed by the pointer wandering over other nodes. */
  let held = null

  /* The sheen is one element moved onto whichever circle is under the pointer,
     rather than one per node. Only ever one is lit, and the gradient inside it
     sweeps on its own clock, so it costs a single element for the whole chart. */
  function sheenOn(scene, node){
    const svg = scene.querySelector('svg')
    if (!svg) return
    let sheen = svg.querySelector('.viz-net-sheen')
    if (!sheen){
      sheen = document.createElementNS('http://www.w3.org/2000/svg', 'circle')
      sheen.setAttribute('class', 'viz-net-sheen')
      svg.appendChild(sheen)
    }
    // Above the circle it lights but below that circle's number.
    const count = svg.querySelector(`text.viz-net-count[data-id="${node.dataset.id}"]`)
    if (count) svg.insertBefore(sheen, count)
    else svg.appendChild(sheen)
    sheen.setAttribute('cx', node.getAttribute('cx'))
    sheen.setAttribute('cy', node.getAttribute('cy'))
    sheen.setAttribute('r', node.getAttribute('r'))
  }
  function sheenOff(scene){
    scene.querySelector('.viz-net-sheen')?.remove()
  }

  function lightUp(scene, id){
    scene.classList.add('is-focused')
    const near = new Set((adjacency.get(id) || []).map(x => x.id))
    near.add(id)
    scene.querySelectorAll('[data-id]').forEach(el => {
      el.classList.toggle('is-faded', !near.has(el.dataset.id))
      el.classList.toggle('is-lit', el.dataset.id === id)
    })
    scene.querySelectorAll('.viz-net-link').forEach(el => {
      el.classList.toggle('is-faded', el.dataset.a !== id && el.dataset.b !== id)
    })
  }
  function lightsUp(scene){
    sheenOff(scene)
    scene.classList.remove('is-focused')
    scene.querySelectorAll('.is-faded, .is-lit').forEach(el => el.classList.remove('is-faded', 'is-lit'))
  }

  host.addEventListener('pointerover', ev => {
    const scene = ev.target.closest('.sh-chart-scene')
    if (!scene || held) return
    const hit = ev.target.closest('circle.viz-net-node[data-id]')
    if (hit){ lightUp(scene, hit.dataset.id); sheenOn(scene, hit) }
  })
  host.addEventListener('pointerout', ev => {
    const scene = ev.target.closest('.sh-chart-scene')
    if (!scene || held) return
    if (!ev.relatedTarget || !ev.relatedTarget.closest?.('circle.viz-net-node')){ lightsUp(scene); sheenOff(scene) }
  })

  /* Same rule as the country card: a kept selection is a temporary state, and
     the chart it belongs to slides away as soon as the reader scrolls. */
  function dropSelection(){
    if (!held) return
    held = null
    for (const scene of scenes.values()){
      if (!scene.querySelector('.viz-net-panel') && !scene.classList.contains('is-focused')) continue
      lightsUp(scene); clearPick(scene)
    }
  }
  window.addEventListener('scroll', dropSelection, { passive:true })

  host.addEventListener('click', ev => {
    const scene = ev.target.closest('.sh-chart-scene')
    if (!scene) return
    const hit = ev.target.closest('circle.viz-net-node[data-id]')
    if (hit){ held = hit.dataset.id; lightUp(scene, held); pick(scene, held) }
    else { held = null; lightsUp(scene); clearPick(scene) }
  })

  function resize(){
    const width = Math.round(host.clientWidth)
    const height = Math.round(host.clientHeight)
    if (!width || !height) return
    for (const [id, render] of Object.entries(RENDERERS)){
      // `data` is passed too: most charts only need the studies, but the
      // working-group one counts projects, which are nodes rather than studies.
      scenes.get(id).innerHTML = render(studies, width, height, data, coauthors, cites)
    }
  }


  /* `to` defaults to null, not to `from`.

     Two of the five folds draw on the canvas and have no chart at all, so
     crossing into one passed `to` as undefined. Defaulting that to `from` made
     the outgoing chart think it was also the incoming one, so it sat at full
     strength through the whole crossing and then snapped to nothing at the end.
     That snap was the thing that read as broken. */
  function show(from = null, to = null, progress = 0, cross = 0){
    for (const [id, scene] of scenes){
      /* The chart is on screen only when its particles are not.

         `cross` is handed in from the field and rises to 1 within the first few
         per cent of a crossing. A chart's opacity is 1 minus that, so the
         instant the particles reach full strength the chart is gone — and they
         are sampled from it, so they are standing exactly where it was. The
         swap is meant to be invisible; only the travelling should be seen. */
      let opacity = 0
      if (from === to && id === from) opacity = 1
      else if (id === from || id === to) opacity = Math.max(0, 1 - cross)
      scene.style.opacity = opacity.toFixed(3)
      // Hit-testing follows what you can see. Without this a faded scene still
      // catches clicks aimed at whatever is behind it.
      scene.classList.toggle('is-live', opacity > 0.5)
    }
  }

  /* Turn a rendered chart into particles.

     Every mark in the scene is walked and filled with points on ONE grid, the
     same pitch for every chart, so a matrix cell and a network node and a bar
     all come apart into the same size of dot at the same spacing. That is the
     whole point: the reader should not be able to tell which fold they are
     leaving from the way it dissolves.

     Geometry, not pixels. Rasterising the SVG would have meant inlining every
     computed style first, because the classes live in a stylesheet the image
     would not carry, and the result would still be at the mercy of the filters.
     Reading the shapes is exact and costs nothing.

     Coordinates come back in the scene's own space; the caller places them. */
  function sample(id, pitch = 5.4){
    const scene = scenes.get(id)
    const svg = scene && scene.querySelector('svg')
    if (!svg) return []
    const pts = []
    const rgb = value => {
      const m = /rgba?\(([^)]+)\)/.exec(value || '')
      if (!m) return null
      const n = m[1].split(',').map(parseFloat)
      return (n[3] !== undefined && n[3] < 0.06) ? null : [n[0], n[1], n[2]]
    }
    const num = (el, a) => parseFloat(el.getAttribute(a) || '0')

    /* Only data marks. A chart also contains scenery — the network's haze is a
       single circle 379px across, the name plates are rectangles the colour of
       the page, the legend has swatches. Filling those gave a solid disc or a
       block that had nothing to do with the chart, which is the shape that kept
       appearing before the next fold arrived. Anything bigger than a mark is
       scenery by definition. */
    const box = svg.viewBox.baseVal
    const AREA_CAP = (box.width * box.height) * 0.06
    const R_CAP = Math.min(box.width, box.height) * 0.09

    for (const el of svg.querySelectorAll('circle, rect, line')){
      const css = getComputedStyle(el)
      if (css.display === 'none' || css.visibility === 'hidden') continue
      const alpha = parseFloat(el.style.opacity || css.opacity || '1')
      if (alpha < 0.08) continue
      if (el.classList.contains('viz-net-haze') || el.classList.contains('viz-net-plate')) continue
      // Only whether it is drawn at all. The colour is the field's, not the
      // chart's, so it is never read.
      if (!rgb(css.fill) && !rgb(css.stroke)) continue

      if (el.tagName === 'circle'){
        const cx = num(el, 'cx'), cy = num(el, 'cy'), r = num(el, 'r')
        if (r < 0.4 || r > R_CAP) continue
        // A small mark still owes at least one particle, or the fine detail of
        // a chart vanishes and only its big shapes travel.
        if (r <= pitch * 0.6){ pts.push([cx, cy]); continue }
        for (let y = cy - r; y <= cy + r; y += pitch)
          for (let x = cx - r; x <= cx + r; x += pitch)
            if ((x - cx) ** 2 + (y - cy) ** 2 <= r * r) pts.push([x, y])
      }
      else if (el.tagName === 'rect'){
        const x0 = num(el, 'x'), y0 = num(el, 'y')
        const w = num(el, 'width'), h = num(el, 'height')
        if (w < 0.4 || h < 0.4 || w * h > AREA_CAP) continue
        /* A matrix cell is large. Filled solid, thirty-six of them make one
           block and the grid that carries the meaning disappears. The edges are
           drawn and the inside is left sparse, so what travels still reads as a
           table. */
        const big = w > pitch * 4 && h > pitch * 4
        const inner = big ? pitch * 3 : pitch
        for (let x = x0; x <= x0 + w; x += pitch){ pts.push([x, y0]); pts.push([x, y0 + h]) }
        for (let y = y0 + pitch; y < y0 + h; y += pitch){ pts.push([x0, y]); pts.push([x0 + w, y]) }
        if (inner > 0)
          for (let y = y0 + inner; y < y0 + h; y += inner)
            for (let x = x0 + inner; x < x0 + w; x += inner) pts.push([x, y])
      }
      else {
        const x1 = num(el, 'x1'), y1 = num(el, 'y1')
        const x2 = num(el, 'x2'), y2 = num(el, 'y2')
        const len = Math.hypot(x2 - x1, y2 - y1)
        const steps = Math.max(1, Math.round(len / pitch))
        for (let k = 0; k <= steps; k++)
          pts.push([x1 + (x2 - x1) * k / steps, y1 + (y2 - y1) * k / steps])
      }
    }
    return pts
  }

  return { resize, show, sample, destroy(){
    window.removeEventListener('scroll', dropSelection)
    host.innerHTML = ''
  } }
}
