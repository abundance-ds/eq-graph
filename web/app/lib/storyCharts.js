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

const INSTRUMENTS = [
  ['EQ-5D-5L', '5L'], ['EQ VAS', 'VAS'], ['EQ-5D-3L', '3L'],
  ['EQ-5D-Y-3L', 'Y-3L'], ['EQ-5D-Y-5L', 'Y-5L'], ['EQ-HWB', 'HWB'],
]

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
    'Number: study count. Colour: share of instrument studies. Each study has one primary family.')
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
