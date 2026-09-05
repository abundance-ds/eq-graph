import { researchWorkingGroups } from '../../shared/utils/workingGroups'

const escapeText = value => String(value ?? '')
  .replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;')
const escapeAttr = value => escapeText(value).replaceAll('"', '&quot;').replaceAll("'", '&#39;')
const CHART_FRAME = Object.freeze({ legendY:20, valueInset:2 })

const truncateText = (value, maxLength) => {
  const text = String(value || '')
  if (text.length <= maxLength) return text
  return `${text.slice(0, Math.max(1, maxLength - 1)).trimEnd()}…`
}

const wrapWords = (value, maxLength, maxLines = 2) => {
  const words = String(value || '').trim().split(/\s+/).filter(Boolean)
  const lines = []
  for (const word of words){
    const last = lines.at(-1)
    if (!last || (last.length + word.length + 1 > maxLength && lines.length < maxLines)) {
      lines.push(word)
    } else {
      lines[lines.length - 1] = `${last} ${word}`
    }
  }
  if (lines.length > maxLines) {
    lines[maxLines - 1] = lines.slice(maxLines - 1).join(' ')
    lines.length = maxLines
  }
  if (lines[maxLines - 1]?.length > maxLength) {
    lines[maxLines - 1] = truncateText(lines[maxLines - 1], maxLength)
  }
  return lines
}

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
  // The graph supplies canonical instrument labels. The patterns keep family views stable.
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
  <svg viewBox="0 0 ${width} ${height}" focusable="false">
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

/* The EQ measures a study can use, matched on a pattern rather than an exact string.  */
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
const COVERAGE_ROW_SHORT = ['Value sets', 'Measurement', 'Instrument dev.', 'Applied use', 'Preferences', 'Health outcomes']
const COVERAGE_COLUMNS = INSTRUMENTS

function coverageMatrix(studies, width, height){
      /* Rows are research types, columns are instruments, cells are the studies that are both.  */
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
      `<text class="viz-label" x="${left - 10}" y="${y(index) + cellH * .62}" text-anchor="end">${escapeText(compact ? COVERAGE_ROW_SHORT[index] : titleCase(row))}</text>`).join('')
    + COVERAGE_COLUMNS.map(([, short], index) =>
      `<text class="viz-axis is-strong" x="${x(index) + cellW / 2}" y="${top - 24}" text-anchor="middle">${escapeText(short)}</text>`).join('')
        /* The margin's label is rotated beside its own column.  */
    + `<text class="viz-axis-title" x="${left + (COVERAGE_COLUMNS.length * cellW) / 2}" y="${top - 44}" text-anchor="middle">EQ measures</text>`
    + `<text class="viz-axis is-strong" x="${totalX + totalW / 2}" y="${top - 24}" text-anchor="middle">Total</text>`
    + `<text class="viz-label" x="${left - 10}" y="${totalY + cellH * .62}" text-anchor="end">Total</text>`

  const marks = cells.map(item => {
    const opacity = item.value ? .12 + .84 * Math.sqrt(item.share) : .03
    const row = COVERAGE_ROW_SHORT[item.rowIndex]
    const instrument = COVERAGE_COLUMNS[item.columnIndex][0]
    const aria = `${row} and ${instrument}: ${item.value} ${item.value === 1 ? 'study' : 'studies'}.`
    return `<g class="viz-matrix-hit" tabindex="0" role="group" aria-label="${escapeAttr(aria)}">
      <title>${escapeText(aria)}</title>
      <rect class="viz-matrix-cell is-teal" style="opacity:${opacity.toFixed(3)}" x="${x(item.columnIndex) + 2}" y="${y(item.rowIndex) + 2}" width="${Math.max(4, cellW - 4)}" height="${Math.max(4, cellH - 4)}" rx="3" />
      <text class="viz-cell-value ${opacity > .55 ? 'is-reverse' : ''}" x="${x(item.columnIndex) + cellW / 2}" y="${y(item.rowIndex) + cellH * .62}" text-anchor="middle">${item.value || '—'}</text>`
      + `</g>`
  }).join('')

  /* The margins are set as figures on the page rather than shaded cells.  */
  const margins = rowTotals.map((total, index) =>
      `<text class="viz-cell-total" x="${totalX + totalW / 2}" y="${y(index) + cellH * .62}" text-anchor="middle">${total}</text>`).join('')
    + columnTotals.map((total, index) =>
      `<text class="viz-cell-total" x="${x(index) + cellW / 2}" y="${totalY + cellH * .62}" text-anchor="middle">${total}</text>`).join('')
    + `<line class="viz-rule" x1="${left - 4}" y1="${totalY - 2}" x2="${totalX + totalW}" y2="${totalY - 2}" />`
    + `<line class="viz-rule" x1="${totalX - 4}" y1="${top - 14}" x2="${totalX - 4}" y2="${totalY + cellH * .8}" />`
    // Centred under the bottom row; rotated up the side of the totals column.
    + `<text class="viz-margin-note" x="${left + (COVERAGE_COLUMNS.length * cellW) / 2}" y="${totalY + cellH + 18}" text-anchor="middle">studies using each instrument</text>`
    + `<text class="viz-margin-note" text-anchor="middle" transform="translate(${totalX + totalW + 16} ${top + (totalY - top) / 2}) rotate(-90)">studies of each research type</text>`

  return chartFrame(width, height, labels + marks + margins)
}

    /* Two bars on one row, sharing a baseline and scale.  */
function groupPapers(studies, width, height, data){
  /* Projects per working group, one dot each.  */
  const projects = (data?.nodes || []).filter(node => node.type === 'project')
  const totals = new Map()
  for (const project of projects){
    for (const name of researchWorkingGroups(project.wg)){
      totals.set(name, (totals.get(name) || 0) + 1)
    }
  }
  const rows = [...totals.entries()]
    .map(([label, funded]) => ({ label, funded }))
    .sort((a, b) => b.funded - a.funded)

  const compact = width < 560
  const left = compact ? 108 : 190
  const top = 48, bottom = 40
  const peak = Math.max(1, ...rows.map(r => r.funded))
  const bandH = (height - top - bottom) / Math.max(1, rows.length)
  const plotW = width - left - 90           // fixed value column at the right edge

  /* Square packing, same rule as the year fold: the pitch follows from how many dots have to fit the longest row in the width available, so the dots very nearly touch instead of floating in a grid of air. */
  const bandUse = bandH * 0.72
  const perCol = Math.max(1, Math.round(Math.sqrt(peak * bandUse / plotW)))
  const pitch = Math.min(bandUse / perCol, plotW / Math.ceil(peak / perCol))
  const r = Math.max(0.8, pitch * 0.42)

  const marks = rows.map((row, index) => {
    const mid = top + index * bandH + bandH / 2
    const y0 = mid - (perCol - 1) * pitch / 2
    const labelLines = compact ? wrapWords(row.label, 17) : [row.label]
    const labelY = mid - (labelLines.length - 1) * 5.5
    const label = labelLines.map((line, lineIndex) =>
      `<tspan x="${left - 12}" y="${(labelY + lineIndex * 11).toFixed(1)}">${escapeText(line)}</tspan>`).join('')
    let dots = ''
    for (let i = 0; i < row.funded; i++){
      const cx = left + Math.floor(i / perCol) * pitch + pitch / 2
      const cy = y0 + (i % perCol) * pitch
      dots += `<circle class="viz-dot" cx="${cx.toFixed(1)}" cy="${cy.toFixed(1)}" r="${r.toFixed(2)}" />`
    }
    const aria = `${row.label}: ${row.funded.toLocaleString('en')} funded projects.`
    return `<g class="viz-project-row" tabindex="0" role="group" aria-label="${escapeAttr(aria)}"><title>${escapeText(aria)}</title><text class="viz-label" text-anchor="end">${label}</text>
      ${dots}
      <text class="viz-cell-total" x="${width - CHART_FRAME.valueInset}" y="${mid + 1}" text-anchor="end">${row.funded}</text></g>`
  }).join('')

  const keyX = compact ? 0 : left
  const key = `<circle class="viz-dot" cx="${keyX + 5}" cy="${CHART_FRAME.legendY}" r="${Math.min(4, r * 1.25).toFixed(2)}" />
    <text class="viz-legend" x="${keyX + 18}" y="${CHART_FRAME.legendY + 5}">One dot = one funded project</text>`

  return chartFrame(width, height, key + marks)
}

    /* Phosphor regular, inlined rather than loaded so the page stays self-contained. */
const ICON = {
  paper: 'M216,40H40A16,16,0,0,0,24,56V200a16,16,0,0,0,16,16H216a16,16,0,0,0,16-16V56A16,16,0,0,0,216,40Zm0,160H40V56H216V200ZM184,96a8,8,0,0,1-8,8H80a8,8,0,0,1,0-16h96A8,8,0,0,1,184,96Zm0,32a8,8,0,0,1-8,8H80a8,8,0,0,1,0-16h96A8,8,0,0,1,184,128Zm0,32a8,8,0,0,1-8,8H80a8,8,0,0,1,0-16h96A8,8,0,0,1,184,160Z',
  people: 'M117.25,157.92a60,60,0,1,0-66.5,0A95.83,95.83,0,0,0,3.53,195.63a8,8,0,1,0,13.4,8.74,80,80,0,0,1,134.14,0,8,8,0,0,0,13.4-8.74A95.83,95.83,0,0,0,117.25,157.92ZM40,108a44,44,0,1,1,44,44A44.05,44.05,0,0,1,40,108Zm210.14,98.7a8,8,0,0,1-11.07-2.33A79.83,79.83,0,0,0,172,168a8,8,0,0,1,0-16,44,44,0,1,0-16.34-84.87,8,8,0,1,1-5.94-14.85,60,60,0,0,1,55.53,105.64,95.83,95.83,0,0,1,47.22,37.71A8,8,0,0,1,250.14,206.7Z',
}
const icon = name =>
  `<svg class="viz-ico" viewBox="0 0 256 256" fill="currentColor" aria-hidden="true"><path d="${ICON[name]}"/></svg>`

    /* Structurally Paul's, including his force parameters.  */
/* The most cited work. A dotted field keeps the texture of the wider story without assigning a false unit to one dot. */
const GROUP_INK = [
  ['Instrument development', '#00705f'],
  ['Value-set development', '#b88016'],
  ['Measurement properties', '#7a736a'],
  ['Evidence synthesis', '#4f8f83'],
  ['Methods research', '#a7a096'],
]
const groupInk = name => (GROUP_INK.find(g => g[0] === name) || [, '#b9beba'])[1]

function citedWork(studies, width, height, data, coauthors, cites){
  const papers = (cites && cites.papers) || []
  if (!papers.length) return chartFrame(width, height, '', 'Citation data not loaded.')

  const compact = width < 620
  const narrow = width < 320
  const rows = papers.slice(0, compact ? (narrow ? 6 : 8) : 12)
  const left = compact ? 8 : 14
  const shown = [...new Set(rows.map(x => x.group).filter(Boolean))]
  const legendColumns = compact ? (narrow ? 1 : 2) : Math.max(1, shown.length)
  const legendRows = Math.ceil(shown.length / legendColumns)
  const top = compact ? 28 + legendRows * 20 : 58, bottom = 42
  const bandH = (height - top - bottom) / rows.length
  const peak = Math.max(...rows.map(r => r.citations))
  const plotW = width - left - (compact ? 66 : 88)
  const stack = 5
  const pitch = compact ? 3.25 : 3.55
  const columns = Math.max(28, Math.floor(plotW / pitch))
  const capacity = columns * stack
  const dotR = pitch * .37
  const titleLength = compact
    ? Math.max(24, Math.floor((width - left - 68) / 5.3))
    : 76

  const marks = rows.map((row, index) => {
    const y = top + index * bandH
    const ink = groupInk(row.group)
    const count = Math.max(1, Math.round(row.citations / Math.max(1, peak) * capacity))
    const title = truncateText(row.title, titleLength)
    const aria = `${row.title}. ${row.citations.toLocaleString('en')} citations. ${row.group || 'Other research'}.`
    const dots = Array.from({ length:count }, (_, i) => {
      const column = Math.floor(i / stack)
      const line = i % stack
      const cx = left + column * pitch
      const cy = y + bandH * .44 + line * pitch
      return `<circle class="viz-citation-dot" cx="${cx.toFixed(1)}" cy="${cy.toFixed(1)}" r="${dotR.toFixed(2)}" fill="${ink}" />`
    }).join('')
    return `<g class="viz-hover-row" tabindex="0" role="link" aria-label="${escapeAttr(`${aria} Open publication.`)}" data-paper-index="${index}" data-url="${escapeAttr(row.url || '')}">
      <title>${escapeText(aria)}</title>
      <rect class="viz-row-hit" x="0" y="${y.toFixed(1)}" width="${width}" height="${bandH.toFixed(1)}" />
      <text class="viz-label" x="${left}" y="${(y + bandH * .25).toFixed(1)}" text-anchor="start">${escapeText(title)}</text>
      ${dots}
      <text class="viz-cell-total" x="${width - CHART_FRAME.valueInset}" y="${(y + bandH * .64).toFixed(1)}" text-anchor="end">${row.citations.toLocaleString('en')}</text>
    </g>`
  }).join('')

  // The key names only the groups on the chart. On a phone it becomes a grid,
  // so no item has to leave the figure to make room for the next one.
  let key = ''
  if (compact){
    const cellW = (width - left * 2) / legendColumns
    key = shown.map((name, index) => {
      const column = index % legendColumns
      const row = Math.floor(index / legendColumns)
      const x = left + column * cellW
      const y = 17 + row * 20
      return `<rect class="viz-legend-swatch" x="${x}" y="${y - 7}" width="10" height="10" fill="${groupInk(name)}" />
        <text class="viz-legend" style="font-size:12px" x="${x + 16}" y="${y + 2}">${escapeText(name)}</text>`
    }).join('')
  } else {
    let kx = left
    key = shown.map(name => {
      const bit = `<rect class="viz-legend-swatch" x="${kx}" y="${CHART_FRAME.legendY - 8}" width="12" height="12" fill="${groupInk(name)}" />
        <text class="viz-legend" x="${kx + 20}" y="${CHART_FRAME.legendY + 3}">${escapeText(name)}</text>`
      kx += name.length * 7.5 + 46
      return bit
    }).join('')
  }

  return chartFrame(width, height, key + marks,
    'Citation count')
}

function coauthorCommunities(people, links, maxGroups){
  const ids = people.map(person => person.person_id)
  const neighbours = new Map(ids.map(id => [id, new Map()]))
  const degree = new Map(ids.map(id => [id, 0]))
  let totalWeight = 0
  for (const link of links){
    const weight = Number(link.coauthored_paper_count || 0)
    if (!neighbours.has(link.source) || !neighbours.has(link.target) || !weight) continue
    neighbours.get(link.source).set(link.target, (neighbours.get(link.source).get(link.target) || 0) + weight)
    neighbours.get(link.target).set(link.source, (neighbours.get(link.target).get(link.source) || 0) + weight)
    degree.set(link.source, degree.get(link.source) + weight)
    degree.set(link.target, degree.get(link.target) + weight)
    totalWeight += weight * 2
  }
  if (!totalWeight) return new Map(ids.map(id => [id, 0]))

  const community = new Map(ids.map((id, index) => [id, index]))
  const totals = new Map(ids.map((id, index) => [index, degree.get(id)]))
  const order = [...ids].sort((a, b) => degree.get(b) - degree.get(a) || a.localeCompare(b))
  const resolution = .7
  for (let pass = 0; pass < 24; pass++){
    let moved = 0
    for (const id of order){
      const own = community.get(id)
      const weightByCommunity = new Map()
      for (const [other, weight] of neighbours.get(id)){
        const group = community.get(other)
        weightByCommunity.set(group, (weightByCommunity.get(group) || 0) + weight)
      }
      const nodeWeight = degree.get(id)
      totals.set(own, totals.get(own) - nodeWeight)
      let best = own
      let bestGain = (weightByCommunity.get(own) || 0) - resolution * totals.get(own) * nodeWeight / totalWeight
      for (const [group, inwardWeight] of weightByCommunity){
        const gain = inwardWeight - resolution * totals.get(group) * nodeWeight / totalWeight
        if (gain > bestGain + 1e-9 || (Math.abs(gain - bestGain) < 1e-9 && group < best)){
          best = group
          bestGain = gain
        }
      }
      community.set(id, best)
      totals.set(best, (totals.get(best) || 0) + nodeWeight)
      if (best !== own) moved += 1
    }
    if (!moved) break
  }

  const sizes = new Map()
  for (const group of community.values()) sizes.set(group, (sizes.get(group) || 0) + 1)
  const major = [...sizes].sort((a, b) => b[1] - a[1] || a[0] - b[0]).slice(0, maxGroups).map(([group]) => group)
  const assigned = new Map(major.map(group => [group, group]))
  const between = new Map([...sizes.keys()].map(group => [group, new Map()]))
  for (const link of links){
    const a = community.get(link.source), b = community.get(link.target)
    if (a === b) continue
    const weight = Number(link.coauthored_paper_count || 0)
    between.get(a).set(b, (between.get(a).get(b) || 0) + weight)
    between.get(b).set(a, (between.get(b).get(a) || 0) + weight)
  }
  let unresolved = [...sizes.keys()].filter(group => !assigned.has(group))
  while (unresolved.length){
    let progress = 0
    for (const group of unresolved){
      const scores = new Map()
      for (const [other, weight] of between.get(group)){
        const target = assigned.get(other)
        if (target != null) scores.set(target, (scores.get(target) || 0) + weight)
      }
      if (!scores.size) continue
      const target = [...scores].sort((a, b) => b[1] - a[1] || major.indexOf(a[0]) - major.indexOf(b[0]))[0][0]
      assigned.set(group, target)
      progress += 1
    }
    unresolved = unresolved.filter(group => !assigned.has(group))
    if (!progress){
      unresolved.forEach((group, index) => assigned.set(group, major[index % major.length]))
      break
    }
  }

  const finalSizes = new Map(major.map(group => [group, 0]))
  for (const group of community.values()){
    const target = assigned.get(group)
    finalSizes.set(target, finalSizes.get(target) + 1)
  }
  const ranked = [...finalSizes].sort((a, b) => b[1] - a[1] || major.indexOf(a[0]) - major.indexOf(b[0])).map(([group]) => group)
  const rank = new Map(ranked.map((group, index) => [group, index]))
  return new Map(ids.map(id => [id, rank.get(assigned.get(community.get(id)))]))
}

function coauthorNetwork(studies, width, height, data, coauthors){
  if (!coauthors || !coauthors.nodes) return chartFrame(width, height, '', 'Co-authorship data not loaded.')

  const TOP = width < 720 ? 72 : width < 820 ? 140 : 220
  const people = [...coauthors.nodes].sort((a, b) => b.paper_count - a.paper_count).slice(0, TOP)
  const keep = new Set(people.map(p => p.person_id))
  const maxLinks = width < 720 ? 320 : width < 820 ? 620 : 1000
  const layoutLinks = coauthors.edges.filter(e => keep.has(e.source) && keep.has(e.target))
  const links = [...layoutLinks]
    .sort((a, b) => b.coauthored_paper_count - a.coauthored_paper_count)
    .slice(0, maxLinks)

  const communityOf = coauthorCommunities(people, layoutLinks, width < 720 ? 5 : 8)
  const communitySizes = new Map()
  for (const group of communityOf.values()) communitySizes.set(group, (communitySizes.get(group) || 0) + 1)
  const groupIds = [...communitySizes.keys()].sort((a, b) => a - b)

  const top = 18, bottom = 24
  const w = width, h = height - top - bottom
  const cx = w / 2, cy = top + h / 2
  const maxPapers = Math.max(1, ...people.map(p => p.paper_count))
  const rOf = n => 4.5 + Math.sqrt(n / maxPapers) * 13

  const clusterTarget = new Map([[groupIds[0], { x:cx, y:cy }]])
  const satellites = Math.max(1, groupIds.length - 1)
  groupIds.slice(1).forEach((group, index) => {
    const angle = -Math.PI / 2 + index / satellites * Math.PI * 2
    clusterTarget.set(group, {
      x:cx + Math.cos(angle) * w * .33,
      y:cy + Math.sin(angle) * h * .31,
    })
  })

  const at = new Map()
  const placedByGroup = new Map()
  people.forEach(p => {
    const group = communityOf.get(p.person_id)
    const index = placedByGroup.get(group) || 0
    placedByGroup.set(group, index + 1)
    const target = clusterTarget.get(group)
    const angle = index * 2.399963
    const radius = Math.sqrt(index) * 11
    at.set(p.person_id, {
      id:p.person_id, p, community:group,
      x:target.x + Math.cos(angle) * radius,
      y:target.y + Math.sin(angle) * radius * .78,
      vx:0, vy:0, r:rOf(p.paper_count),
    })
  })
  const nodes = [...at.values()]

  for (let step = 0; step < 280; step++){
    const cool = 1 - step / 320
    for (let i = 0; i < nodes.length; i++){
      const A = nodes[i]
      for (let j = i + 1; j < nodes.length; j++){
        const B = nodes[j]
        let dx = B.x - A.x, dy = B.y - A.y
        let d = Math.hypot(dx, dy) || 0.01
        // charge: bigger authors push harder, as in his setup stronger than Paul's, because his canvas is a full dark screen and this one is half a fold: the same charge packs into a ball here
        const q = (30 + A.p.paper_count * 1.5) * 2.5 / (d * d)
        const ux = dx / d, uy = dy / d
        A.vx -= ux * q * cool; A.vy -= uy * q * cool
        B.vx += ux * q * cool; B.vy += uy * q * cool
        // collide: circles must not sit on top of each other
        const min = A.r + B.r + 5
        if (d < min){
          const push = (min - d) * 0.5
          A.x -= ux * push; A.y -= uy * push
          B.x += ux * push; B.y += uy * push
        }
      }
      const target = clusterTarget.get(A.community)
      A.vx += (target.x - A.x) * 0.024 * cool
      A.vy += (target.y - A.y) * 0.024 * cool
    }
    for (const e of layoutLinks){
      const A = at.get(e.source), B = at.get(e.target)
      const dx = B.x - A.x, dy = B.y - A.y
      const d = Math.max(0.01, Math.hypot(dx, dy))
          /* The more two people publish together, the shorter the spring.  */
      const sameCommunity = A.community === B.community
      const rest = (sameCommunity ? 230 : 420) / Math.pow(e.coauthored_paper_count, 0.85)
      const k = Math.min(0.95, 0.18 + e.coauthored_paper_count * 0.10)
      const f = (d - rest) * k * (sameCommunity ? 0.045 : 0.008) * cool
      const ux = dx / d, uy = dy / d
      A.vx += ux * f; A.vy += uy * f
      B.vx -= ux * f; B.vy -= uy * f
    }
    for (const A of nodes){ A.x += A.vx; A.y += A.vy; A.vx *= 0.62; A.vy *= 0.62 }
  }

  /* Fit by scaling what settled, not by clamping.  */
  const xs = nodes.map(n => n.x), ys = nodes.map(n => n.y)
  const sx = Math.max(...xs) - Math.min(...xs), sy = Math.max(...ys) - Math.min(...ys)
  const maxR = Math.max(...nodes.map(n => n.r))
  const padX = maxR + 12
  const padTop = maxR + top
  const padBottom = maxR + 24                 // names hang below their circle
  const availW = Math.max(40, w - padX * 2)
  const availH = Math.max(40, h - padTop - padBottom)
  const k = Math.min(availW / (sx || 1), availH / (sy || 1), 2.4)
  /* The blob settles roughly square, so height binds first and the field left a third of its width empty.  */
  const kWide = Math.min(availW / (sx || 1), k * 1.62)
  const ox = (padX + availW / 2) - ((Math.min(...xs) + Math.max(...xs)) / 2) * kWide
  const oy = (padTop + availH / 2) - ((Math.min(...ys) + Math.max(...ys)) / 2) * k
  for (const n of nodes){ n.x = n.x * kWide + ox; n.y = n.y * k + oy }
  const fitBox = { padX, padTop, padBottom }

  const heaviest = Math.max(1, ...links.map(l => l.coauthored_paper_count))
  const wire = links.map(e => {
    const A = at.get(e.source), B = at.get(e.target)
    return `<line class="viz-net-link" data-a="${e.source}" data-b="${e.target}" data-w="${e.coauthored_paper_count}" x1="${A.x.toFixed(1)}" y1="${A.y.toFixed(1)}" x2="${B.x.toFixed(1)}" y2="${B.y.toFixed(1)}" style="stroke-width:${(0.25 + (e.coauthored_paper_count / heaviest) * 1.35).toFixed(2)}" />`
  }).join('')

  const rankedNodes = [...nodes].sort((a, b) => b.p.paper_count - a.p.paper_count)
  const named = new Set(rankedNodes.slice(0, 16).map(n => n.id))
  const counted = new Set(rankedNodes.slice(0, 8).map(n => n.id))
      /* Shade carries paper count, and so does size.  */
  const shade = n => {
    const t = Math.sqrt(n.paper_count / maxPapers)
    return `rgba(${Math.round(196 - t * 176)},${Math.round(226 - t * 108)},${Math.round(218 - t * 110)},.82)`
  }

  const marks = nodes.map(n => {
    const count = counted.has(n.id) && n.r >= 9
      ? `<text class="viz-net-count" data-id="${n.id}" x="${n.x.toFixed(1)}" y="${(n.y + n.r * 0.32).toFixed(1)}" text-anchor="middle" style="font-size:${Math.max(10, n.r * 0.82).toFixed(1)}px">${n.p.paper_count}</text>`
      : ''
    const aria = `${n.p.name}. ${n.p.paper_count} papers, ${n.p.coauthor_count || 0} collaborators.`
    return `<circle class="viz-net-node" tabindex="0" role="button" aria-label="${escapeAttr(aria)}" data-id="${n.id}" data-name="${escapeAttr(n.p.name)}" data-community="${n.community}" data-papers="${n.p.paper_count}" data-coauthors="${n.p.coauthor_count || 0}" data-projects="${n.p.project_count || 0}" data-led-projects="${n.p.led_project_count || 0}" data-member="${String(Boolean(n.p.euroqol_member))}" data-leader="${String(Boolean(n.p.project_leader))}" cx="${n.x.toFixed(1)}" cy="${n.y.toFixed(1)}" r="${n.r.toFixed(1)}" style="fill:${shade(n.p)}" />${count}`
  }).join('')

      /* Show the encoding, do not describe it.  */
      /* Names go in a pass of their own, after every circle and line, or a name ends up under a later circle.  */
      /* A name is drawn only if it lands clear of every name already placed, biggest first.  */
  /* Names are placed once, here, after every circle and line so a label is never buried.  */
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
      return `<rect class="viz-net-plate" data-id="${n.id}" x="${(spot.x - w / 2 - 4).toFixed(1)}" y="${(spot.y - 10).toFixed(1)}" width="${(w + 8).toFixed(1)}" height="14" rx="1" />
        <text class="viz-net-name" data-id="${n.id}" x="${spot.x.toFixed(1)}" y="${spot.y.toFixed(1)}" text-anchor="middle">${escapeText(t)}</text>`
    }).join('')

  return chartFrame(width, height, wire + marks + plates)
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
const STORY_RENDERERS = ['coauthorNetwork', 'groupPapers', 'citedWork', 'coverageMatrix']

export function createStoryCharts(data, root, coauthors = null, cites = null){
  const host = root.querySelector('[data-charts]')
  const studies = data.nodes.filter(node => node.type === 'study')
  if (!host) return { resize(){}, show(){}, destroy(){} }

  host.innerHTML = STORY_RENDERERS.map(id => `
    <div class="sh-chart-scene" data-chart="${id}"><svg /></div>`).join('')
    + '<div class="viz-chart-tip" role="tooltip" hidden></div>'
  const scenes = new Map([...host.querySelectorAll('[data-chart]')].map(scene => [scene.dataset.chart, scene]))
  const tip = host.querySelector('.viz-chart-tip')
  let tipTarget = null

  const positionTip = (clientX, clientY) => {
    if (!tip || tip.hidden) return
    const box = host.getBoundingClientRect()
    const gap = 14
    let left = clientX - box.left + gap
    let top = clientY - box.top + gap
    if (left + tip.offsetWidth > box.width - 8) left = clientX - box.left - tip.offsetWidth - gap
    if (top + tip.offsetHeight > box.height - 8) top = clientY - box.top - tip.offsetHeight - gap
    tip.style.left = `${Math.max(8, left)}px`
    tip.style.top = `${Math.max(8, top)}px`
  }
  const hideTip = () => {
    tipTarget = null
    if (tip) tip.hidden = true
  }
  const authorTip = node => {
    if (!tip) return
    const roles = [node.dataset.member === 'true' ? 'EuroQol member' : '', node.dataset.leader === 'true' ? 'project leader' : ''].filter(Boolean).join(' · ')
    tip.innerHTML = `<strong>${escapeText(node.dataset.name)}</strong>
      <span>${node.dataset.papers || 0} papers · ${node.dataset.coauthors || 0} collaborators · ${node.dataset.projects || 0} funded projects</span>
      ${roles ? `<span>${escapeText(roles)}</span>` : ''}
      <em>Select to isolate this collaboration network</em>`
    tip.hidden = false
  }
  const paperTip = mark => {
    if (!tip) return
    const paper = cites?.papers?.[Number(mark.dataset.paperIndex)]
    if (!paper) return hideTip()
    const names = paper.authors || []
    const authors = names.length > 8 ? `${names.slice(0, 8).join(', ')} and ${names.length - 8} more` : names.join(', ')
    const record = [paper.journal, paper.year || null, `${Number(paper.citations).toLocaleString('en')} citations`].filter(Boolean).join(' · ')
    tip.innerHTML = `<strong>${escapeText(paper.title)}</strong>
      ${authors ? `<span>${escapeText(authors)}</span>` : ''}
      <span>${escapeText(record)}</span>
      <em>Open publication ↗</em>`
    tip.hidden = false
  }

  host.addEventListener('pointermove', ev => {
    const author = ev.target.closest?.('circle.viz-net-node[data-id]')
    const paper = ev.target.closest?.('.viz-hover-row[data-paper-index]')
    const target = author || paper
    if (!target) return hideTip()
    if (target !== tipTarget){
      if (author) authorTip(author)
      else paperTip(paper)
    }
    tipTarget = target
    positionTip(ev.clientX, ev.clientY)
  })
  host.addEventListener('pointerleave', hideTip)
  host.addEventListener('focusin', ev => {
    const author = ev.target.closest?.('circle.viz-net-node[data-id]')
    const paper = ev.target.closest?.('.viz-hover-row[data-paper-index]')
    if (!author && !paper) return
    if (author) authorTip(author)
    else paperTip(paper)
    tipTarget = author || paper
    const box = ev.target.getBoundingClientRect()
    positionTip(box.right, box.top + box.height / 2)
  })
  host.addEventListener('focusout', hideTip)

      /* One click lights that person and everyone they have written with.  */
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

  /* Clicking someone reforms the network around them.  */
  const REFORM_MS = 900
  const reformState = new WeakMap()

  function indexScene(scene){
    let idx = reformState.get(scene)
    if (idx) return idx
    const svg = scene.querySelector('svg')
    if (!svg) return null
    const byId = new Map()
    // Every mark that belongs to a node, with its offset from that node's home, so the group keeps its shape as it moves.
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
    // Leaning up and right of centre keeps the orbit clear of the panel, which sits bottom left and would otherwise cover the closest collaborators.
    const cx = box.width * 0.54, cy = box.height * 0.44

    const targets = new Map()
    if (id){
      const partners = (adjacency.get(id) || []).filter(x => idx.byId.has(x.id))
        .sort((a, b) => b.w - a.w)
      targets.set(id, { x:cx, y:cy })
      /* Rings widen as they go out, and each holds more than the last, because a ring's circumference grows with its radius.  */
      const SEATS = [7, 12, 17, 22]
      const rings = []
      for (let i = 0, k = 0; i < partners.length; k++){
        const take = SEATS[Math.min(k, SEATS.length - 1)]
        rings.push(partners.slice(i, i + take)); i += take
      }
      /* Bounded by the room that actually exists on each side, not by the box.  */
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
      // Everyone else is pushed straight out from where they already are, so the field opens rather than shuffling.
      for (const row of idx.byId.values()){
        if (targets.has(row.id)) continue
        const vx = row.home.x - cx, vy = row.home.y - cy
        const d = Math.hypot(vx, vy) || 1
        targets.set(row.id, { x:cx + (vx / d) * (d + 190), y:cy + (vy / d) * (d + 190) })
      }
    } else {
      for (const row of idx.byId.values()) targets.set(row.id, { ...row.home })
    }

    // The light follows the specimen. 
    const glow = idx.svg.querySelector('.viz-net-haze')
    const glowFrom = glow
      ? { x:+glow.getAttribute('cx'), y:+glow.getAttribute('cy'), r:+glow.getAttribute('r') } : null
    const glowTo = glow
      ? (id ? { x:cx, y:cy, r:idx.homeGlow.r * 0.92 } : { ...idx.homeGlow }) : null

    const from = new Map([...idx.byId.values()].map(r => [r.id, { ...r.at }]))

    /* Each mark that has far to go comes apart into motes for the journey and puts itself back together on arrival, which is the move the opening fold makes with the headline.  */
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
        // Each mote takes its own arc and its own pace, so the group scatters and gathers instead of sliding across as one rigid shape.
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
    scene.classList.remove('is-focused')
    scene.querySelectorAll('.is-picked, .is-faded, .is-lit').forEach(el => el.classList.remove('is-picked', 'is-faded', 'is-lit'))
    if (panel) { panel.remove(); panel = null }
  }

  function shownNear(scene, id){
    const near = new Set([id])
    scene.querySelectorAll('.viz-net-link').forEach(line => {
      if (line.dataset.a === id) near.add(line.dataset.b)
      else if (line.dataset.b === id) near.add(line.dataset.a)
    })
    return near
  }

  function placePanel(scene, node, point){
    if (!panel || !node) return
    const box = scene.getBoundingClientRect()
    const mark = node.getBoundingClientRect()
    const x = point?.clientX ? point.clientX - box.left : mark.right - box.left
    const y = point?.clientY ? point.clientY - box.top : mark.top - box.top + mark.height / 2
    const gap = 14
    let left = x + gap
    let top = y + gap
    if (left + panel.offsetWidth > box.width - 8) left = x - panel.offsetWidth - gap
    if (top + panel.offsetHeight > box.height - 8) top = y - panel.offsetHeight - gap
    panel.style.left = `${Math.max(8, left)}px`
    panel.style.top = `${Math.max(8, top)}px`
  }

  function pick(scene, id, point = null){
    scene.classList.add('is-focused')
    const near = shownNear(scene, id)
    scene.querySelectorAll('[data-id]').forEach(el => {
      const mine = el.dataset.id
      el.classList.toggle('is-faded', !near.has(mine))
      el.classList.toggle('is-picked', mine === id)
    })
    scene.querySelectorAll('.viz-net-link').forEach(el => {
      el.classList.toggle('is-faded', el.dataset.a !== id && el.dataset.b !== id)
    })
    const partners = [...scene.querySelectorAll('.viz-net-link')]
      .filter(line => line.dataset.a === id || line.dataset.b === id)
      .map(line => ({ id:line.dataset.a === id ? line.dataset.b : line.dataset.a, w:Number(line.dataset.w || 0) }))
      .sort((a, b) => b.w - a.w)
    const strongest = partners.slice(0, 4).map(x => `${escapeText(nameOf.get(x.id) || 'unknown')} · ${x.w} papers`).join(', ')
    // The leader ring carries the same data-id and sits before the node in the markup, so a bare circle[data-id] lookup found the ring, which has no paper count on it. 
    const node = scene.querySelector(`circle.viz-net-node[data-id="${id}"]`)
    const roles = [node?.dataset.member === 'true' ? 'EuroQol member' : '', node?.dataset.leader === 'true' ? 'project leader' : ''].filter(Boolean).join(' · ')
    if (panel) panel.remove()
    panel = document.createElement('div')
    panel.className = 'viz-net-panel'
    panel.innerHTML = `<strong>${escapeText(nameOf.get(id) || '')}</strong>
      <span class="viz-net-figs">
        <span class="viz-fig">${icon('paper')}<b>${node?.dataset.papers || 0}</b> papers</span>
        <span class="viz-fig">${icon('people')}<b>${node?.dataset.coauthors || 0}</b> collaborators</span>
        <span class="viz-fig"><b>${node?.dataset.ledProjects || 0}</b> projects led</span>
      </span>
      ${roles ? `<span>${escapeText(roles)}</span>` : ''}
      ${strongest ? `<span>Strongest shown links: ${strongest}</span>` : ''}
      <button type="button" aria-label="Close">×</button>`
    panel.querySelector('button').onclick = () => clearPick(scene)
    scene.appendChild(panel)
    placePanel(scene, node, point)
    hideTip()
  }

  let held = null

  function lightsUp(scene){
    scene.classList.remove('is-focused')
    scene.querySelectorAll('.is-faded, .is-lit').forEach(el => el.classList.remove('is-faded', 'is-lit'))
  }

  /* A kept selection survives small scroll movements. It clears only when the network leaves the stage. */
  function dropSelection(){
    if (!held) return
    held = null
    for (const scene of scenes.values()){
      if (!scene.querySelector('.viz-net-panel') && !scene.classList.contains('is-focused')) continue
      lightsUp(scene); clearPick(scene)
    }
  }
  host.addEventListener('click', ev => {
    const scene = ev.target.closest('.sh-chart-scene')
    if (!scene) return
    const hit = ev.target.closest('circle.viz-net-node[data-id]')
    if (hit){ held = hit.dataset.id; pick(scene, held, ev); return }
    const paper = ev.target.closest('.viz-hover-row[data-url]')
    if (paper?.dataset.url){ window.open(paper.dataset.url, '_blank', 'noopener,noreferrer'); return }
    if (scene.dataset.chart === 'coauthorNetwork'){
      held = null; lightsUp(scene); clearPick(scene)
    }
  })

  host.addEventListener('keydown', ev => {
    const scene = ev.target.closest?.('.sh-chart-scene')
    const hit = ev.target.closest?.('circle.viz-net-node[data-id]')
    if (!scene) return
    if (ev.key === 'Escape'){
      ev.preventDefault()
      if (scene.dataset.chart !== 'coauthorNetwork') return
      held = null
      lightsUp(scene)
      clearPick(scene)
      return
    }
    if (ev.key === 'Enter'){
      const paper = ev.target.closest?.('.viz-hover-row[data-url]')
      if (paper?.dataset.url){ ev.preventDefault(); window.open(paper.dataset.url, '_blank', 'noopener,noreferrer'); return }
    }
    if (ev.key !== 'Enter' && ev.key !== ' ') return
    if (!hit) return
    ev.preventDefault()
    held = hit.dataset.id
    pick(scene, held)
  })

  function resize(){
    const width = Math.round(host.clientWidth)
    const height = Math.round(host.clientHeight)
    if (!width || !height) return
    for (const id of STORY_RENDERERS){
      const render = RENDERERS[id]
      // `data` is passed too: most charts only need the studies, but the working-group one counts projects, which are nodes rather than studies.
      scenes.get(id).innerHTML = render(studies, width, height, data, coauthors, cites)
    }
    /* Bind the primary network action on the live scene itself. This keeps it reachable even when the story layers change their hit-testing rules. */
    const network = scenes.get('coauthorNetwork')
    if (network){
      network.onclick = ev => {
        ev.stopPropagation()
        const hit = ev.target.closest?.('circle.viz-net-node[data-id]')
        if (hit){ held = hit.dataset.id; pick(network, held, ev) }
        else { held = null; lightsUp(network); clearPick(network) }
      }
      network.onkeydown = ev => {
        const hit = ev.target.closest?.('circle.viz-net-node[data-id]')
        if (ev.key === 'Escape'){
          ev.preventDefault(); held = null; lightsUp(network); clearPick(network); return
        }
        if (!hit || (ev.key !== 'Enter' && ev.key !== ' ')) return
        ev.preventDefault(); held = hit.dataset.id; pick(network, held)
      }
    }
  }

  /* One scene owns the stage. The parent controls its scroll-linked fade. */
  function show(activeId = null, visibility = 1){
    const liveEnough = visibility >= .72
    let networkLive = false
    for (const [id, scene] of scenes){
      const active = id === activeId
      const live = active && liveEnough
      scene.style.opacity = active ? '1' : '0'
      scene.classList.toggle('is-live', live)
      scene.toggleAttribute('inert', !live)
      scene.setAttribute('aria-hidden', String(!live))
      if (id === 'coauthorNetwork') networkLive = live
    }
    if (!liveEnough) hideTip()
    if (!networkLive) dropSelection()
  }

  /* Turn a rendered chart into particles.  */
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

    /* Only data marks.  */
    const box = svg.viewBox.baseVal
    const AREA_CAP = (box.width * box.height) * 0.06
    const R_CAP = Math.min(box.width, box.height) * 0.09

    for (const el of svg.querySelectorAll('circle, rect, line')){
      const css = getComputedStyle(el)
      if (css.display === 'none' || css.visibility === 'hidden') continue
      const alpha = parseFloat(el.style.opacity || css.opacity || '1')
      if (alpha < 0.08) continue
      if (el.classList.contains('viz-net-haze') || el.classList.contains('viz-net-plate')) continue
      // Only whether it is drawn at all. 
      if (!rgb(css.fill) && !rgb(css.stroke)) continue

      if (el.tagName === 'circle'){
        const cx = num(el, 'cx'), cy = num(el, 'cy'), r = num(el, 'r')
        if (r < 0.4 || r > R_CAP) continue
        // A small mark still owes at least one particle, or the fine detail of a chart vanishes and only its big shapes travel.
        if (r <= pitch * 0.6){ pts.push([cx, cy]); continue }
        for (let y = cy - r; y <= cy + r; y += pitch)
          for (let x = cx - r; x <= cx + r; x += pitch)
            if ((x - cx) ** 2 + (y - cy) ** 2 <= r * r) pts.push([x, y])
      }
      else if (el.tagName === 'rect'){
        const x0 = num(el, 'x'), y0 = num(el, 'y')
        const w = num(el, 'width'), h = num(el, 'height')
        if (w < 0.4 || h < 0.4 || w * h > AREA_CAP) continue
        /* A matrix cell is large.  */
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
    host.innerHTML = ''
  } }
}
