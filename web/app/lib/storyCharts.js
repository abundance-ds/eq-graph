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
  /* The cross-tab, with its margins.

     Rows are research types, columns are instruments, and a cell counts the
     studies that are both. The two totals lines are what turn a grid of cells
     into a table you can actually reason from: the bottom row says how much
     each instrument carries overall, the right column how large each research
     type is. Without them a reader has to add six numbers in their head to
     answer "which instrument is used most", which is the first question anyone
     asks of a matrix like this.

     The instrument fold used to be a separate beat. It said the same thing the
     bottom row now says, in a whole screen of its own. */
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
    /* Axis titles where a chart puts them: the group name centred over the
       columns it names, and the margin's meaning rotated alongside the column
       it belongs to. "All instruments" sitting on top of the totals column was
       naming the wrong thing — it read as a seventh instrument. */
    + `<text class="viz-axis-title" x="${left + (COVERAGE_COLUMNS.length * cellW) / 2}" y="${top - 44}" text-anchor="middle">Instruments</text>`
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



/* Papers per working group, against the size of the group.

   Two bars on one row, not two charts. The question a reader has here is not
   "how many papers" — it is "how much of what this group funded has reached
   the literature", and that is a comparison, so the two quantities have to
   share a baseline and a scale. Valuation looks large either way; EQ-HWB is
   large in projects and nearly absent in papers, which is the actual finding
   and is invisible if you only plot one of them. */
function groupPapers(studies, width, height, data){
  const projects = (data?.nodes || []).filter(node => node.type === 'project')
  const totals = new Map()
  for (const project of projects){
    if (!project.wg) continue
    const key = String(project.wg).includes(',') ? 'Several groups' : String(project.wg)
    const row = totals.get(key) || { funded:0, published:0 }
    row.funded += 1
    if (project.hasPublication) row.published += 1
    totals.set(key, row)
  }
  const rows = [...totals.entries()]
    .map(([label, row]) => ({ label, ...row }))
    .sort((a, b) => b.published - a.published)
    .slice(0, 7)

  const compact = width < 560
  const left = compact ? 108 : 190
  const top = 46
  const bottom = 44
  const peak = Math.max(1, ...rows.map(r => r.funded))
  const bandH = (height - top - bottom) / Math.max(1, rows.length)
  const barH = Math.min(9, bandH * 0.30)
  const plotW = width - left - 64

  const marks = rows.map((row, index) => {
    const y = top + index * bandH + bandH / 2
    const fundedW = (row.funded / peak) * plotW
    const pubW = (row.published / peak) * plotW
    const share = row.funded ? Math.round((row.published / row.funded) * 100) : 0
    return `<text class="viz-label" x="${left - 12}" y="${y + 1}" text-anchor="end">${escapeText(row.label)}</text>
      <rect class="viz-matrix-cell" style="opacity:.16" x="${left}" y="${y - barH - 1}" width="${Math.max(1, fundedW).toFixed(1)}" height="${barH}" rx="2" />
      <rect class="viz-matrix-cell is-teal" style="opacity:.92" x="${left}" y="${y + 1}" width="${Math.max(1, pubW).toFixed(1)}" height="${barH}" rx="2" />
      <text class="viz-cell-total" x="${left + Math.max(fundedW, pubW) + 10}" y="${y + 1}" text-anchor="start">${row.published} of ${row.funded} · ${share}%</text>`
  }).join('')

  const key = `<rect class="viz-matrix-cell" style="opacity:.16" x="${left}" y="${top - 30}" width="10" height="7" rx="2" />
    <text class="viz-axis" x="${left + 16}" y="${top - 24}">projects funded</text>
    <rect class="viz-matrix-cell is-teal" style="opacity:.92" x="${left + 118}" y="${top - 30}" width="10" height="7" rx="2" />
    <text class="viz-axis" x="${left + 134}" y="${top - 24}">with a published paper</text>`

  return chartFrame(width, height, key + marks,
    'Projects grouped by working group. A project counted once, in the group that funded it.')
}


/* The co-authorship network.

   Structurally this is Paul's: authors are nodes, sized by how many papers they
   have; two authors are joined when they have published together, and the line
   thickens with the number of shared papers.

   Visually it follows the earlier knowledge-graph screen instead of his dark
   force-directed cloud. Pale filled circles with the count inside and the name
   beneath, on a light ground. The reason is legibility at a glance: a circle
   with its number written in it can be read without a legend and without
   hovering, which is what a story fold needs. A reader is scrolling past, not
   exploring.

   Only the strongest authors are drawn. All 628 people and 3,603 links is a
   hairball at any size that fits on a page, and a hairball says "there is a lot
   of this" and nothing else. Showing the busiest few with their real links says
   who the field is built around, which is the actual finding.

   Positions come from a small spring simulation run here: repulsion between
   every pair, and a spring on each shared-paper link whose rest length is the
   layout distance Paul precomputed. Seeded and deterministic, so the same data
   always draws the same picture. */
function coauthorNetwork(studies, width, height, data, coauthors){
  if (!coauthors || !coauthors.nodes) return chartFrame(width, height, '', 'Co-authorship data not loaded.')

  const TOP = width < 720 ? 18 : 28
  const people = [...coauthors.nodes].sort((a, b) => b.paper_count - a.paper_count).slice(0, TOP)
  const keep = new Set(people.map(p => p.person_id))
  const links = coauthors.edges
    .filter(e => keep.has(e.source) && keep.has(e.target))
    .sort((a, b) => b.coauthored_paper_count - a.coauthored_paper_count)
    .slice(0, 90)

  const pad = 74
  const box = { x0: pad, y0: 54, x1: width - pad, y1: height - 46 }
  const cx = (box.x0 + box.x1) / 2, cy = (box.y0 + box.y1) / 2
  const maxPapers = Math.max(1, ...people.map(p => p.paper_count))
  const rOf = p => 12 + Math.sqrt(p.paper_count / maxPapers) * 21

  // deterministic start: a ring, biggest first, so the layout never jitters
  const at = new Map()
  people.forEach((p, i) => {
    const a = (i / people.length) * Math.PI * 2
    at.set(p.person_id, { x: cx + Math.cos(a) * 150, y: cy + Math.sin(a) * 110, vx: 0, vy: 0, p })
  })

  for (let step = 0; step < 260; step++){
    const cool = 1 - step / 300
    for (const a of at.values()){
      for (const b of at.values()){
        if (a === b) continue
        const dx = a.x - b.x, dy = a.y - b.y
        const d2 = Math.max(120, dx * dx + dy * dy)
        const push = 5200 / d2
        a.vx += dx * push * cool; a.vy += dy * push * cool
      }
      // gently held to the middle, or the whole thing drifts off the frame
      a.vx += (cx - a.x) * 0.006; a.vy += (cy - a.y) * 0.006
    }
    for (const e of links){
      const A = at.get(e.source), B = at.get(e.target)
      const dx = B.x - A.x, dy = B.y - A.y
      const d = Math.max(1, Math.hypot(dx, dy))
      const rest = 62 + (e.layout_distance || 0.5) * 150
      const pull = (d - rest) * 0.012 * cool
      const ux = dx / d, uy = dy / d
      A.vx += ux * pull; A.vy += uy * pull
      B.vx -= ux * pull; B.vy -= uy * pull
    }
    for (const a of at.values()){
      a.x += a.vx * 0.5; a.y += a.vy * 0.5
      a.vx *= 0.82; a.vy *= 0.82
      const r = rOf(a.p)
      a.x = Math.max(box.x0 + r, Math.min(box.x1 - r, a.x))
      a.y = Math.max(box.y0 + r, Math.min(box.y1 - r - 16, a.y))
    }
  }

  const heaviest = Math.max(1, ...links.map(l => l.coauthored_paper_count))
  const wire = links.map(e => {
    const A = at.get(e.source), B = at.get(e.target)
    const w = (0.5 + (e.coauthored_paper_count / heaviest) * 2.2).toFixed(2)
    const mx = (A.x + B.x) / 2, my = (A.y + B.y) / 2 - Math.hypot(B.x - A.x, B.y - A.y) * 0.09
    return `<path class="viz-net-link" d="M ${A.x.toFixed(1)} ${A.y.toFixed(1)} Q ${mx.toFixed(1)} ${my.toFixed(1)} ${B.x.toFixed(1)} ${B.y.toFixed(1)}" style="stroke-width:${w}" />`
  }).join('')

  // Names only where they will not collide, biggest circles first.
  const placed = []
  const marks = [...at.values()].sort((a, b) => b.p.paper_count - a.p.paper_count).map(n => {
    const r = rOf(n.p)
    const cls = n.p.euroqol_member ? 'is-member' : 'is-other'
    const ring = n.p.project_leader ? `<circle class="viz-net-ring" cx="${n.x.toFixed(1)}" cy="${n.y.toFixed(1)}" r="${(r + 3.5).toFixed(1)}" />` : ''
    const nameY = n.y + r + 13
    const short = n.p.name.length > 20 ? n.p.name.slice(0, 19) + '…' : n.p.name
    const halfW = short.length * 3.4
    const clash = placed.some(q => Math.abs(q.x - n.x) < halfW + q.w && Math.abs(q.y - nameY) < 12)
    if (!clash) placed.push({ x: n.x, y: nameY, w: halfW })
    const label = clash ? '' :
      `<text class="viz-net-name" x="${n.x.toFixed(1)}" y="${nameY.toFixed(1)}" text-anchor="middle">${escapeText(short)}</text>`
    return `${ring}
      <circle class="viz-net-node ${cls}" cx="${n.x.toFixed(1)}" cy="${n.y.toFixed(1)}" r="${r.toFixed(1)}" />
      <text class="viz-net-count" x="${n.x.toFixed(1)}" y="${(n.y + r * 0.30).toFixed(1)}" text-anchor="middle" style="font-size:${Math.max(10, r * 0.86).toFixed(1)}px">${n.p.paper_count}</text>
      ${label}`
  }).join('')

  const members = people.filter(p => p.euroqol_member).length
  const key = `<circle class="viz-net-node is-member" cx="${box.x0 + 6}" cy="26" r="5" />
    <text class="viz-axis" x="${box.x0 + 17}" y="30">EuroQol member</text>
    <circle class="viz-net-node is-other" cx="${box.x0 + 128}" cy="26" r="5" />
    <text class="viz-axis" x="${box.x0 + 139}" y="30">other author</text>
    <circle class="viz-net-ring" cx="${box.x0 + 232}" cy="26" r="6.5" fill="none" />
    <text class="viz-axis" x="${box.x0 + 245}" y="30">project leader</text>
    <text class="viz-axis" x="${box.x1}" y="30" text-anchor="end">${people.length} of ${coauthors.nodes.length} authors · ${members} are members</text>`

  return chartFrame(width, height, key + wire + marks,
    'Circle size is papers. Line thickness is papers written together. The busiest ' + people.length + ' authors of ' + coauthors.nodes.length + ' are shown.')
}

const RENDERERS = {
  fieldShape,
  instrumentMatrix,
  methodBundles,
  methodProfiles,
  conceptAtlas,
  productLandscape,
  coverageMatrix,
  groupPapers,
  coauthorNetwork,
}

export function createStoryCharts(data, root, coauthors = null){
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
      // `data` is passed too: most charts only need the studies, but the
      // working-group one counts projects, which are nodes rather than studies.
      scenes.get(id).innerHTML = render(studies, width, height, data, coauthors)
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
