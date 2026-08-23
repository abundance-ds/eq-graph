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
  // The row label reads like "74 of 266 · 28%", so the plot has to stop
  // well short of the frame or it writes itself off the edge.
  const plotW = width - left - 150

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
    'A project is counted once, in the group that funded it. Projects shared between groups are grouped together.')
}


/* The co-authorship network.

   Structurally Paul's, including his force parameters: link distance falls as
   the square root of shared papers, charge scales with paper count, and a
   collision radius keeps circles off each other. The first version of this
   chart clamped every node inside a box, which is why they all ended up
   pinned around the edge with the links crossing the middle — a boundary that
   hard is a wall the simulation presses against rather than a frame it settles
   inside. There is no clamp now; the centring force does that job.

   Visually it follows the earlier light knowledge-graph screen rather than his
   dark cloud.

   Roughly ninety authors are drawn but only the largest are named. A network
   should look like a network — a dense middle with a periphery — and labelling
   every node turns it into a diagram of labels. The ones worth naming are the
   ones a reader can already see are large. */
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
      const rest = 150 / Math.sqrt(e.coauthored_paper_count)
      const k = Math.min(0.9, 0.22 + e.coauthored_paper_count * 0.075)
      const f = (d - rest) * k * 0.045 * cool
      const ux = dx / d, uy = dy / d
      A.vx += ux * f; A.vy += uy * f
      B.vx -= ux * f; B.vy -= uy * f
    }
    for (const A of nodes){ A.x += A.vx; A.y += A.vy; A.vx *= 0.62; A.vy *= 0.62 }
  }

  // keep the drawing inside the frame by scaling what settled, not by clamping
  const xs = nodes.map(n => n.x), ys = nodes.map(n => n.y)
  const sx = Math.max(...xs) - Math.min(...xs), sy = Math.max(...ys) - Math.min(...ys)
  const k = Math.min((w - 90) / (sx || 1), (h - 30) / (sy || 1), 2.4)
  const ox = cx - ((Math.min(...xs) + Math.max(...xs)) / 2) * k
  const oy = cy - ((Math.min(...ys) + Math.max(...ys)) / 2) * k
  for (const n of nodes){ n.x = n.x * k + ox; n.y = n.y * k + oy }

  const heaviest = Math.max(1, ...links.map(l => l.coauthored_paper_count))
  const wire = links.map((e, i) => {
    const A = at.get(e.source), B = at.get(e.target)
    return `<line class="viz-net-link" data-a="${e.source}" data-b="${e.target}" x1="${A.x.toFixed(1)}" y1="${A.y.toFixed(1)}" x2="${B.x.toFixed(1)}" y2="${B.y.toFixed(1)}" style="stroke-width:${(0.4 + (e.coauthored_paper_count / heaviest) * 2.6).toFixed(2)}" />`
  }).join('')

  const named = new Set([...nodes].sort((a, b) => b.p.paper_count - a.p.paper_count).slice(0, 9).map(n => n.id))
  const marks = nodes.map(n => {
    const cls = n.p.euroqol_member ? 'is-member' : 'is-other'
    const ring = n.p.project_leader
      ? `<circle class="viz-net-ring" data-id="${n.id}" cx="${n.x.toFixed(1)}" cy="${n.y.toFixed(1)}" r="${(n.r + 2.6).toFixed(1)}" />` : ''
    const name = named.has(n.id)
      ? `<text class="viz-net-name" data-id="${n.id}" x="${n.x.toFixed(1)}" y="${(n.y + n.r + 12).toFixed(1)}" text-anchor="middle">${escapeText(n.p.name)}</text>` : ''
    // The count goes inside wherever the circle can hold it legibly. Below
    // about eleven pixels the digits would be smaller than the label beneath,
    // and a number too small to read is just texture.
    const count = n.r >= 11
      ? `<text class="viz-net-count" x="${n.x.toFixed(1)}" y="${(n.y + n.r * 0.32).toFixed(1)}" text-anchor="middle" style="font-size:${Math.max(10, n.r * 0.82).toFixed(1)}px">${n.p.paper_count}</text>`
      : ''
    return `${ring}<circle class="viz-net-node ${cls}" data-id="${n.id}" data-name="${escapeText(n.p.name)}" data-papers="${n.p.paper_count}" cx="${n.x.toFixed(1)}" cy="${n.y.toFixed(1)}" r="${n.r.toFixed(1)}" />${count}${name}`
  }).join('')

  /* A legend that shows the encoding instead of describing it.

     "Circle size is papers, line thickness is papers written together" is a
     sentence asking the reader to hold two mappings in their head and apply
     them to a picture. Drawing a small circle beside a large one, and a thin
     line beside a thick one, states the same thing in the form the reader is
     about to meet. It is also the only version that survives being skimmed. */
  const members = people.filter(p => p.euroqol_member).length
  const smallest = Math.min(...people.map(p => p.paper_count))
  const kx = 8, ky = 20
  const key = `
    <circle class="viz-net-node is-member" cx="${kx + 6}" cy="${ky}" r="6" />
    <text class="viz-net-key" x="${kx + 18}" y="${ky + 4}">EuroQol member</text>
    <circle class="viz-net-node is-other" cx="${kx + 140}" cy="${ky}" r="6" />
    <text class="viz-net-key" x="${kx + 152}" y="${ky + 4}">other author</text>
    <circle class="viz-net-ring" cx="${kx + 258}" cy="${ky}" r="7.5" />
    <text class="viz-net-key" x="${kx + 271}" y="${ky + 4}">project leader</text>

    <circle class="viz-net-node is-member" cx="${kx + 392}" cy="${ky}" r="4" />
    <circle class="viz-net-node is-member" cx="${kx + 412}" cy="${ky}" r="10" />
    <text class="viz-net-key" x="${kx + 428}" y="${ky + 4}">${smallest} to ${maxPapers} papers</text>

    <line class="viz-net-link" x1="${kx + 552}" y1="${ky - 4}" x2="${kx + 580}" y2="${ky - 4}" style="stroke-width:.6" />
    <line class="viz-net-link" x1="${kx + 552}" y1="${ky + 4}" x2="${kx + 580}" y2="${ky + 4}" style="stroke-width:3" />
    <text class="viz-net-key" x="${kx + 590}" y="${ky + 4}">written together, more often</text>

    <text class="viz-net-key is-quiet" x="${width - 6}" y="${ky + 4}" text-anchor="end">${people.length} of ${coauthors.nodes.length} authors</text>`

  return chartFrame(width, height, key + wire + marks, 'Click anyone to see who they work with.')
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

  /* Selecting an author.

     One click lights that person and everyone they have written with, and
     dims the rest. That is the whole interaction, and it answers the only
     question this picture provokes: who does this person work with? A panel
     names the strongest links, because a thick line tells you a bond is strong
     without telling you whose. Clicking the background lets go. */
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

  function clearPick(scene){
    scene.querySelectorAll('.is-picked, .is-faded').forEach(el => el.classList.remove('is-picked', 'is-faded'))
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
      <span>${node?.dataset.papers || 0} papers · ${partners.length} co-authors</span>
      ${strongest ? `<span>Most often with ${strongest}</span>` : ''}
      <button type="button" aria-label="Close">×</button>`
    panel.querySelector('button').onclick = () => clearPick(scene)
    scene.appendChild(panel)
  }

  host.addEventListener('click', ev => {
    const scene = ev.target.closest('.sh-chart-scene')
    if (!scene) return
    const hit = ev.target.closest('circle[data-id]')
    if (hit) pick(scene, hit.dataset.id)
    else clearPick(scene)
  })

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
      /* The old curve left a hole. The outgoing chart was gone by 42% of the
         transition and the incoming one did not start until 58%, so a reader
         who stopped scrolling in between was left looking at nothing and had
         to scroll further to get anything back. The two now cross over: one is
         always carrying the fold, and the pair always sums to one. */
      let opacity = 0
      const e = Math.max(0, Math.min(1, (progress - .12) / .56))
      const eased = e * e * (3 - 2 * e)
      if (from === to && id === from) opacity = 1
      else if (id === from) opacity = 1 - eased
      else if (id === to) opacity = eased
      scene.style.opacity = opacity.toFixed(3)
    }
  }

  return { resize, show, destroy(){ host.innerHTML = '' } }
}
