const escapeText = value => String(value ?? '')
  .replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;')

const titleCase = value => String(value || '')
  .replace(/\bstudy$/i, '').trim()
  .replace(/(^|[-\s])\w/g, match => match.toUpperCase())

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

const hasValue = (study, field, value) => (study[field] || [])
  .some(item => String(item).toLowerCase() === value.toLowerCase())

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
  return chartFrame(width, height, grid + bars, 'Study families are non-exclusive; one study can have more than one label.')
}

const INSTRUMENTS = [
  ['EQ-5D-5L', '5L'], ['EQ VAS', 'VAS'], ['EQ-5D-3L', '3L'],
  ['EQ-5D-Y-3L', 'Y-3L'], ['EQ-5D-Y-5L', 'Y-5L'], ['EQ-HWB', 'HWB'],
]

function instrumentMatrix(studies, width, height){
  const compact = width < 560
  const instruments = compact ? INSTRUMENTS.slice(0, 5) : INSTRUMENTS
  const n = instruments.length
  const left = compact ? 88 : 140
  const top = compact ? 46 : 58
  const bottom = 42
  const cell = Math.min((width - left - 18) / n, (height - top - bottom) / n)
  const x0 = left + Math.max(0, (width - left - 18 - cell * n) / 2)
  const y0 = top
  const values = []
  for (let row = 0; row < n; row++){
    for (let column = 0; column <= row; column++){
      const value = row === column
        ? countWhere(studies, study => hasValue(study, 'instruments', instruments[row][0]))
        : countWhere(studies, study => hasValue(study, 'instruments', instruments[row][0]) && hasValue(study, 'instruments', instruments[column][0]))
      values.push({ row, column, value })
    }
  }
  const max = Math.max(...values.map(item => item.value), 1)
  const labels = instruments.map(([full, short], index) => `
    <text class="viz-axis is-strong" x="${x0 + index * cell + cell / 2}" y="${top - 20}" text-anchor="middle">${escapeText(short)}</text>
    <text class="viz-label" x="${x0 - 10}" y="${y0 + index * cell + cell * .6}" text-anchor="end">${escapeText(compact ? short : full)}</text>`).join('')
  const cells = values.map(item => {
    const opacity = .1 + .82 * Math.sqrt(item.value / max)
    const textClass = opacity > .55 ? 'is-reverse' : ''
    return `
      <rect class="viz-matrix-cell ${item.row === item.column ? 'is-amber' : 'is-teal'}" style="opacity:${opacity.toFixed(3)}" x="${x0 + item.column * cell + 2}" y="${y0 + item.row * cell + 2}" width="${Math.max(5, cell - 4)}" height="${Math.max(5, cell - 4)}" rx="3" />
      <text class="viz-cell-value ${textClass}" x="${x0 + item.column * cell + cell / 2}" y="${y0 + item.row * cell + cell * .61}" text-anchor="middle">${item.value}</text>`
  }).join('')
  return chartFrame(width, height, labels + cells, 'Diagonal: all uses. Lower triangle: studies that used both instruments.')
}

function methodBundles(studies, width, height){
  const dce = study => hasValue(study, 'methods', 'DCE')
  const ctto = study => hasValue(study, 'methods', 'cTTO')
  const segments = [
    { label:'DCE only', value:countWhere(studies, study => dce(study) && !ctto(study)), cls:'is-amber' },
    { label:'Both', value:countWhere(studies, study => dce(study) && ctto(study)), cls:'is-ink' },
    { label:'cTTO only', value:countWhere(studies, study => !dce(study) && ctto(study)), cls:'is-teal' },
  ]
  const total = segments.reduce((sum, item) => sum + item.value, 0)
  const compact = height < 360
  const marginX = width < 560 ? 0 : 12
  const barY = height * (compact ? .2 : .16)
  const barH = Math.max(62, Math.min(92, height * .18))
  const barW = width - marginX * 2
  let cursor = marginX
  const blocks = segments.map(item => {
    const segmentW = item.value / total * barW
    const center = cursor + segmentW / 2
    const percent = Math.round(item.value / total * 100)
    const label = segmentW > 90
      ? `<text class="viz-segment-label is-reverse" x="${center}" y="${barY + barH * .42}" text-anchor="middle">${escapeText(item.label)}</text>`
      : ''
    const value = `<text class="viz-segment-value is-reverse" x="${center}" y="${barY + barH * .72}" text-anchor="middle">${item.value} · ${percent}%</text>`
    const block = `<rect class="viz-segment ${item.cls}" x="${cursor}" y="${barY}" width="${segmentW}" height="${barH}" />${label}${value}`
    cursor += segmentW
    return block
  }).join('')

  if (compact){
    const labels = segments.map((item, index) => {
      const before = segments.slice(0, index).reduce((sum, row) => sum + row.value, 0)
      const center = marginX + (before + item.value / 2) / total * barW
      return `<text class="viz-axis is-strong" x="${center}" y="${barY + barH + 20}" text-anchor="middle">${escapeText(item.label)}</text>`
    }).join('')
    return chartFrame(width, height, blocks + labels, `${total} studies used DCE and/or cTTO.`)
  }

  const otherMethods = ['Spearman correlation', 'TTO', 'intraclass correlation coefficient', 'thematic analysis', 'semi-structured interview']
    .map(label => ({ label, value:countWhere(studies, study => hasValue(study, 'methods', label)) }))
  const max = Math.max(...otherMethods.map(item => item.value), 1)
  const listTop = barY + barH + Math.max(64, height * .12)
  const rowH = Math.min(36, (height - listTop - 34) / otherMethods.length)
  const labelW = Math.min(205, width * .42)
  const barMax = width - labelW - 38
  const list = otherMethods.map((item, index) => {
    const y = listTop + index * rowH
    return `
      <text class="viz-label" x="${labelW - 10}" y="${y + 10}" text-anchor="end">${escapeText(item.label.replace('intraclass correlation coefficient', 'Intraclass correlation'))}</text>
      <rect class="viz-minibar" x="${labelW}" y="${y}" width="${item.value / max * barMax}" height="14" rx="2" />
      <text class="viz-value" x="${labelW + item.value / max * barMax + 7}" y="${y + 11}">${item.value}</text>`
  }).join('')
  const sectionLabel = `<text class="viz-kicker" x="0" y="${listTop - 23}">OTHER RECURRENT METHODS · ALL ${studies.length} STUDIES</text>`
  return chartFrame(width, height, blocks + sectionLabel + list, `Top bar: all ${total} studies that used DCE and/or cTTO.`)
}

const METHOD_ROWS = [
  'valuation study', 'psychometric study', 'qualitative study',
  'comparative study', 'longitudinal study', 'secondary analysis',
]
const METHOD_COLUMNS = [
  ['DCE', 'DCE'], ['cTTO', 'cTTO'], ['Spearman correlation', 'Spearman'],
  ['intraclass correlation coefficient', 'ICC'], ['thematic analysis', 'Themes'],
  ['semi-structured interview', 'Interviews'],
]

function methodProfiles(studies, width, height){
  return categoricalMatrix(studies, width, height, METHOD_ROWS, METHOD_COLUMNS, 'methods',
    'Counts show studies with each family–method combination. Both dimensions are non-exclusive.')
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

const CONCEPTS = [
  ['proxy reporting', 'Proxy reporting'],
  ['states worse than dead', 'States worse than dead'],
  ['ceiling effects', 'Ceiling effects'],
  ['health-related quality of life', 'Health-related quality of life'],
  ['child health valuation', 'Child health valuation'],
  ['health inequality', 'Health inequality'],
]

function conceptAtlas(studies, width, height){
  const idsFor = key => new Set(studies.filter(study => (study.concepts || []).some(raw => {
    const value = String(raw).toLowerCase().trim()
    if (key === 'ceiling effects') return value === 'ceiling effect' || value === 'ceiling effects'
    return value === key
  })).map(study => study.id))
  const rows = CONCEPTS.map(([key, label]) => ({ key, label, ids:idsFor(key) }))
  const types = [
    ['valuation study', 'Valuation'], ['psychometric study', 'Psychometric'],
    ['qualitative study', 'Qualitative'], ['secondary analysis', 'Secondary'],
  ]
  const compact = width < 560
  const left = compact ? 138 : 205
  const right = compact ? width - 76 : width - 116
  const top = 35
  const bottom = 36
  const rowH = (height - top - bottom) / rows.length
  const familyH = (height - top - bottom) / types.length
  const max = Math.max(...rows.flatMap(row => types.map(([type]) => countWhere(
    studies, study => row.ids.has(study.id) && hasValue(study, 'studyTypes', type),
  ))), 1)
  const familyLabels = types.map(([, label], index) => {
    const y = top + index * familyH + familyH / 2
    return `<circle class="viz-family-anchor" cx="${right}" cy="${y}" r="4" />
      <text class="viz-label" x="${right + 11}" y="${y + 4}">${escapeText(compact ? label.slice(0, 7) : label)}</text>`
  }).join('')
  const connections = rows.flatMap((row, rowIndex) => types.map(([type], typeIndex) => {
    const value = countWhere(studies, study => row.ids.has(study.id) && hasValue(study, 'studyTypes', type))
    if (!value) return ''
    const y1 = top + rowIndex * rowH + rowH / 2
    const y2 = top + typeIndex * familyH + familyH / 2
    const x1 = left + 26
    const bend = (right - x1) * .48
    return `<path class="viz-concept-link" style="stroke-width:${(1.2 + 10 * value / max).toFixed(2)}" d="M ${x1} ${y1} C ${x1 + bend} ${y1}, ${right - bend} ${y2}, ${right} ${y2}" />`
  })).join('')
  const conceptLabels = rows.map((row, index) => {
    const y = top + index * rowH + rowH / 2
    return `<text class="viz-label" x="${left - 10}" y="${y + 4}" text-anchor="end">${escapeText(row.label)}</text>
      <text class="viz-value is-amber-text" x="${left}" y="${y + 4}">${row.ids.size}</text>
      <circle class="viz-concept-anchor" cx="${left + 26}" cy="${y}" r="4" />`
  }).join('')
  return chartFrame(width, height, connections + familyLabels + conceptLabels,
    'Line width shows the number of studies. Concept and study-family labels can overlap.')
}

function productLandscape(studies, width, height){
  const valueSet = countWhere(studies, study => study.hasValueSet)
  const other = countWhere(studies, study => study.hasProduct && !study.hasValueSet)
  const none = studies.length - valueSet - other
  const rows = [
    { label:'Value set or tariff', value:valueSet, cls:'is-amber' },
    { label:'Other research output', value:other, cls:'is-teal' },
    { label:'No separate output', value:none, cls:'is-muted' },
  ]
  const left = width < 560 ? 150 : 220
  const right = 28
  const top = Math.max(34, height * .13)
  const innerW = width - left - right
  const rowH = Math.min(92, (height - top - 56) / rows.length)
  const max = studies.length
  const grid = [0, .25, .5, .75, 1].map(part => {
    const x = left + part * innerW
    return `<line class="viz-gridline" x1="${x}" x2="${x}" y1="${top - 10}" y2="${top + rows.length * rowH - rowH * .2}" />
      <text class="viz-axis" x="${x}" y="${top - 17}" text-anchor="middle">${Math.round(part * 100)}%</text>`
  }).join('')
  const bars = rows.map((row, index) => {
    const y = top + index * rowH
    const barW = row.value / max * innerW
    return `<text class="viz-label" x="${left - 12}" y="${y + rowH * .48}" text-anchor="end">${escapeText(row.label)}</text>
      <rect class="viz-output-bar ${row.cls}" x="${left}" y="${y + 7}" width="${Math.max(2, barW)}" height="${Math.max(22, rowH * .48)}" rx="3" />
      <text class="viz-value" x="${Math.min(width - 2, left + barW + 9)}" y="${y + rowH * .48}">${row.value} · ${Math.round(row.value / max * 100)}%</text>`
  }).join('')
  return chartFrame(width, height, grid + bars, `Share of all ${studies.length} studies. Categories are mutually exclusive.`)
}

const COVERAGE_ROWS = [
  'valuation study', 'psychometric study', 'comparative study',
  'cross-sectional study', 'longitudinal study', 'qualitative study',
]
const COVERAGE_COLUMNS = INSTRUMENTS

function coverageMatrix(studies, width, height){
  const compact = width < 560
  const left = compact ? 100 : 150
  const top = compact ? 68 : 74
  const bottom = 36
  const cellW = (width - left - 8) / COVERAGE_COLUMNS.length
  const cellH = (height - top - bottom) / COVERAGE_ROWS.length
  const columnTotals = COVERAGE_COLUMNS.map(([instrument]) => countWhere(
    studies, study => hasValue(study, 'instruments', instrument),
  ))
  const cells = COVERAGE_ROWS.flatMap((row, rowIndex) => COVERAGE_COLUMNS.map(([instrument], columnIndex) => {
    const value = matrixCount(studies, 'studyTypes', row, 'instruments', instrument)
    return { rowIndex, columnIndex, value, share:value / Math.max(1, columnTotals[columnIndex]) }
  }))
  const labels = COVERAGE_ROWS.map((row, index) => `<text class="viz-label" x="${left - 10}" y="${top + index * cellH + cellH * .62}" text-anchor="end">${escapeText(titleCase(row))}</text>`).join('')
    + COVERAGE_COLUMNS.map(([, short], index) => `<text class="viz-axis is-strong" x="${left + index * cellW + cellW / 2}" y="${top - 35}" text-anchor="middle">${escapeText(short)}</text>
      <text class="viz-axis" x="${left + index * cellW + cellW / 2}" y="${top - 20}" text-anchor="middle">n=${columnTotals[index]}</text>`).join('')
  const marks = cells.map(item => {
    const opacity = item.value ? .12 + .84 * Math.sqrt(item.share) : .03
    return `<rect class="viz-matrix-cell is-teal" style="opacity:${opacity.toFixed(3)}" x="${left + item.columnIndex * cellW + 2}" y="${top + item.rowIndex * cellH + 2}" width="${Math.max(4, cellW - 4)}" height="${Math.max(4, cellH - 4)}" rx="3" />
      <text class="viz-cell-value ${opacity > .55 ? 'is-reverse' : ''}" x="${left + item.columnIndex * cellW + cellW / 2}" y="${top + item.rowIndex * cellH + cellH * .62}" text-anchor="middle">${item.value || '—'}</text>`
  }).join('')
  return chartFrame(width, height, labels + marks,
    'Number: study count. Colour: share of instrument studies. Study families can overlap.')
}

const RENDERERS = {
  fieldShape,
  instrumentMatrix,
  methodBundles,
  methodProfiles,
  conceptAtlas,
  productLandscape,
  coverageMatrix,
}

export function createStoryCharts(data, root){
  const host = root.querySelector('[data-charts]')
  const studies = data.nodes.filter(node => node.type === 'study')
  if (!host) return { resize(){}, show(){}, destroy(){} }

  host.innerHTML = Object.keys(RENDERERS).map(id => `
    <div class="sh-chart-scene" data-chart="${id}"><svg /></div>`).join('')
  const scenes = new Map([...host.querySelectorAll('[data-chart]')].map(scene => [scene.dataset.chart, scene]))

  function resize(){
    const width = Math.round(host.clientWidth)
    const height = Math.round(host.clientHeight)
    if (!width || !height) return
    for (const [id, render] of Object.entries(RENDERERS)){
      scenes.get(id).innerHTML = render(studies, width, height)
    }
  }

  function show(from, to = from, progress = 0){
    for (const [id, scene] of scenes){
      let opacity = 0
      if (from === to && id === from) opacity = 1
      else if (id === from) opacity = Math.max(0, 1 - progress * 2.4)
      else if (id === to) opacity = Math.max(0, (progress - .58) / .42)
      scene.style.opacity = opacity.toFixed(3)
    }
  }

  return { resize, show, destroy(){ host.innerHTML = '' } }
}
