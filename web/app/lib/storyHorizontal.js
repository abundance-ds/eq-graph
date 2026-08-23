/* ═══════════════════════════════════════════════════════════════════
   THE STORY — horizontal, black, Swiss.

   Vertical scrolling drives a horizontal track. One pinned stage and thirteen
   panels move from funded projects to corpus-level research views. Dots carry
   the opening scenes; SVG charts carry the statistical comparisons.
   ═══════════════════════════════════════════════════════════════════ */

import { geoNaturalEarth1, geoPath, geoContains } from 'd3-geo'
import { drawBeatArt } from './beatArt.js'
import { createStoryCharts } from './storyCharts.js'
import { feature } from 'topojson-client'

const lerp = (a, b, t) => a + (b - a) * t
const ease = t => t * t * (3 - 2 * t)

/* A scrollytelling scene needs time in which nothing moves. The old timeline
   used every pixel between two beats for interpolation. A completed visual
   therefore existed at one exact scroll position. These values make the
   settled scene the main state and keep the change short. Mobile gets more
   room because the copy wraps to more lines. */
const storyTiming = () => window.innerWidth <= 640
  ? { intro:1.45, hold:0.94, transition:0.26, handover:1 }
  : { intro:1.35, hold:0.78, transition:0.22, handover:1 }

/* The palette lives in CSS — see the token block in story-h.css. Canvas
   cannot read a custom property, so we read them once here. Nothing in the
   drawing code below states a colour of its own. */
const rgb = (css, name, fallback) => {
  const v = css.getPropertyValue(name).trim()
  const parts = (v || fallback).split(',').map(Number)
  return parts.length === 3 && parts.every(n => Number.isFinite(n)) ? parts : fallback.split(',').map(Number)
}

export function initStory(DATA, TOPO, root, options = {}){
  const css = window.getComputedStyle(root)
  const INK    = rgb(css, '--ink-rgb', '244,244,242')
  const YELLOW = rgb(css, '--dot-yellow-rgb', '232,179,58')
  const TEAL   = rgb(css, '--dot-teal-rgb', '47,158,132')
  const GREY   = rgb(css, '--dot-grey-rgb', '150,150,146')
  const GROUND = rgb(css, '--ground-rgb', '244,243,239')   // the page, for label plates
  const ink = a => `rgba(${INK[0]},${INK[1]},${INK[2]},${a})`
  const projects = DATA.nodes.filter(n => n.type === 'project')
  const studies = DATA.nodes.filter(n => n.type === 'study')
  const entities = [...projects, ...studies]

  /* ── the facts each beat states ──────────────────────────────────── */
  const counts = DATA.metadata?.node_counts || {}
  const evidence = DATA.metadata?.evidence || {}
  const projectEvidence = DATA.metadata?.projectEvidence || {}
  const series = DATA.metadata?.series || {}
  const wgOf = p => String(p.wg || 'Unassigned').split(',')[0].trim()
  const projectYearOf = p => { const y = Number(p.start_year || 0)
    return (y && y >= 1980 && y <= 2030) ? y : null }
  const studyYearOf = s => { const y = Number(s.year || 0)
    return (y && y >= 1980 && y <= 2030) ? y : null }

  const projectYears = [...new Set(projects.map(projectYearOf).filter(Boolean))].sort()

  /* Where each study was actually run. CONDUCTED_IN edges give the country;
     the topojson gives us where that country is. A study with no country, or
     one recorded as a region ("East Asia"), cannot be placed and is shown
     separately rather than dropped or faked. */
  const NAME_FIX = {
    'United States':'United States of America', 'Czech Republic':'Czechia',
    'Trinidad And Tobago':'Trinidad and Tobago', 'Bosnia And Herzegovina':'Bosnia and Herz.',
    'Saint Vincent And The Grenadines':'St. Vin. and Gren.', 'Dominican Republic':'Dominican Rep.',
    'South Korea':'South Korea', 'Republic Of Korea':'South Korea', 'Russia':'Russia',
  }
  const countryOfProject = {}, countryOfStudy = {}
  /* The three numbers a country card shows. Projects and studies come from
     different edges on purpose: a project SUPPORTED_EVIDENCE_IN a country,
     a study was CONDUCTED_IN one, and the gap between them is how much of the
     funded work has actually been read there. */
  const countryDetail = {}
  const nodeById = Object.fromEntries(DATA.nodes.map(n => [n.id, n]))
  const seenProject = {}
  for (const e of DATA.edges){
    const target = nodeById[e.target]
    const label = target && target.label
    if (!label) continue
    const key = NAME_FIX[label] || label
    const row = countryDetail[key] || (countryDetail[key] = { projects:0, studies:0, findings:0 })
    if (e.type === 'SUPPORTED_EVIDENCE_IN'){
      (countryOfProject[e.source] ||= []).push(label)
      const seen = seenProject[key] || (seenProject[key] = new Set())
      if (!seen.has(e.source)){ seen.add(e.source); row.projects += 1 }
    }
    if (e.type === 'CONDUCTED_IN'){
      (countryOfStudy[e.source] ||= []).push(label)
      row.studies += 1
      row.findings += (nodeById[e.source] || {}).findingCount || 0
    }
  }
  /* The rows of the group-by-year beat: only groups that actually have
     dated studies, busiest first. A row that would be empty is not a row. */
  const groupYearRows = (() => {
    const m = new Map()
    for (const p of projects){
      if (!projectYearOf(p)) continue
      const k = wgOf(p); m.set(k, (m.get(k) || 0) + 1)
    }
    return [...m.entries()].sort((a, b) => b[1] - a[1]).map(g => g[0])
  })()

  const groups = (() => {
    const m = new Map()
    projects.forEach(p => m.set(wgOf(p), (m.get(wgOf(p)) || 0) + 1))
    return [...m.entries()].sort((a, b) => b[1] - a[1])
  })()

  const fmt = n => n.toLocaleString('en')
  const seriesValue = (name, label) => Number((series[name] || []).find(row => row.label === label)?.value || 0)

  const datedProjects = projects.filter(projectYearOf)
  const busiestProjectYear = (() => {
    const byYear = new Map()
    for (const project of datedProjects){
      const year = projectYearOf(project)
      byYear.set(year, (byYear.get(year) || 0) + 1)
    }
    return [...byYear.entries()].sort((a, b) => b[1] - a[1])[0] || ['—', 0]
  })()
  const leadingGroups = groups.slice(0, 3)
  const instrumentCount = label => seriesValue('instruments', label)
  const countryCount = label => seriesValue('countries', label)
  const valuationFiveL = studies.filter(s => {
    const types = new Set((s.studyTypes || []).map(value => String(value).toLowerCase()))
    const instruments = new Set(s.instruments || [])
    return types.has('value_set_development') && instruments.has('EQ-5D-5L')
  }).length
  const primaryFamilies = series.studyTypes || []
  const largestFamily = primaryFamilies[0] || { label:'—', value:0 }
  const conceptCount = labels => studies.filter(s => (s.concepts || []).some(value => labels.includes(String(value).toLowerCase()))).length

  /* ── Five folds ───────────────────────────────────────────────────────
     Thirteen beats was an inventory: here is a facet, here is another. Five
     is a story, and a story needs an argument. This one is: EuroQol funded
     work, it spread, it produced evidence, that evidence measures health in
     a common language — and most of it is still unread.

     The order is deliberate. Geography first, because the globe is already
     on screen from the opening fold and carrying it forward means the reader
     never loses the object they arrived with. Then time, then what came out
     of it, then what it measures, then the honest gap.

     Every beat keeps its number tied to a consequence. A number alone —
     "1,024 projects" — tells you nothing about whether that is a lot, or what
     it bought. The `so` line is where the number is made to mean something.

     No `art:` on any of them. Those drew decorative rings, plates and stacks
     over the top of the real chart, so the first thing the eye met was a grey
     shape carrying no data. */
  /* ── Five folds ───────────────────────────────────────────────────────
     The argument: EuroQol funds work, that work spreads, it produces evidence
     other people can use, it rests on a family of instruments built over
     decades, and there is more of it still to read.

     Every fold carries its number WITH its noun. A number alone is a riddle —
     "35" makes the reader hunt the sentence below for what was counted, and a
     display number that has to be decoded is not doing its job. The unit sits
     beside the figure, slightly smaller, so the pair reads as one object.

     The closing line is where the number is made to matter. "1,024 projects"
     says nothing about whether that is many or what it bought. */
  const eqInstruments = (series.instruments || []).filter(row => /^EQ[- ]/i.test(row.label || ''))
  const eqStudies = studies.filter(s => (s.instruments || []).some(i => /^EQ[- ]/i.test(String(i))))
  const eqShare = studies.length ? Math.round((eqStudies.length / studies.length) * 100) : 0

  const BEATS = [
    { num:fmt(counts.country || 0), unit:'countries', head:'EuroQol-funded research now runs on every continent.',
      body:`EuroQol has funded <b>${fmt(projects.length)}</b> projects, and that work now underpins evidence in <b>${fmt(counts.country || 0)}</b> countries and territories.`,
      so:`The <b>${fmt(countryCount('United Kingdom'))}</b> studies in the United Kingdom, <b>${fmt(countryCount('Netherlands'))}</b> in the Netherlands and <b>${fmt(countryCount('Australia'))}</b> in Australia all report on the same scale — which is what lets a health outcome in one country be set beside another.`,
      // No chart. The globe from the opening fold travels down into this space
      // and IS the visual — the reader keeps the object they arrived with
      // instead of watching it fade and a flat grey map take its place.
      layout:'projectMap' },

    { num:fmt(projects.length), unit:'projects', head:'Every year is built on the one before it.',
      body:`<b>${fmt(datedProjects.length)}</b> projects carry a recorded start year, running from ${projectYears[0]} to ${projectYears[projectYears.length - 1]}. Each year stacks on top of the last, so the height is the running total, not that year alone.`,
      so:`The busiest single year was <b>${busiestProjectYear[0]}</b>, with <b>${fmt(busiestProjectYear[1])}</b> projects. But no year stands on its own: a project funded in ${projectYears[0]} still counts today, which is why a quiet year is a slower climb rather than a gap, and why the evidence base compounds instead of dating.`,
      layout:'projectYears' },

    { num:fmt((options.coauthors && options.coauthors.nodes && options.coauthors.nodes.length) || 0), unit:'researchers',
      head:'The research is done by a community, not by one group.',
      body:`<b>${fmt(evidence.publications || 0)}</b> published papers carry <b>${fmt(evidence.findings || 0)}</b> extracted findings, written by researchers who keep working with each other.`,
      so:`The circles are the busiest authors and their size is how many papers they have. A line means two people wrote together, and it thickens the more often they did. What it shows is a field with a dense middle, which is what a funded community looks like after two decades.`,
      layout:'chartBlank', chart:'coauthorNetwork' },

    { num:fmt(studies.length), unit:'studies read', head:'Every study read so far, by what it studied and what it used.',
      body:`<b>${fmt(studies.length)}</b> studies have been read in full and structured, from a portfolio of <b>${fmt(projects.length)}</b> funded projects. The totals show how much each instrument carries, and how large each kind of research is.`,
      so:`<b>${fmt(eqStudies.length)}</b> of them use at least one EuroQol instrument. The family runs from EQ-5D-5L through the youth versions to EQ-HWB, each built for people the version before it did not serve.`,
      layout:'chartBlank', chart:'coverageMatrix' },

    { num:'7', unit:'working groups', head:'Each group is at a different stage of its life.',
      body:`Every funded project sits with a working group. The bars compare what each group has funded against how much of it now carries a published paper.`,
      so:`Valuation is the oldest programme and has published the most. EQ-HWB is the newest, with a great deal funded and almost nothing out yet, which is what the beginning of a programme looks like rather than a failure in one.`,
      layout:'chartBlank', chart:'groupPapers' },
  ]



  /* ── build the DOM ───────────────────────────────────────────────── */
  const track = root.querySelector('[data-track]')
  track.innerHTML = BEATS.map(b => `
    <section class="sh-panel">
      <div class="sh-copy">
        <div class="sh-num">${b.num}${b.unit ? `<span class="sh-unit">${b.unit}</span>` : ''}</div>
        <h2 class="sh-head">${b.head}</h2>
        <p class="sh-body">${b.body}</p>
      </div>
    </section>`).join('')

  root.querySelector('[data-dots]').innerHTML = BEATS.map((b, i) => `
    <button type="button" class="${i ? '' : 'on'}" aria-label="Go to ${b.head}" ${i ? '' : 'aria-current="step"'}></button>
  `).join('')
  const totalEl = root.querySelector('[data-total]')
  if (totalEl) totalEl.textContent = String(BEATS.length).padStart(2, '0')

  // The CSS value prevents a layout jump before JavaScript starts. This value
  // is the exact runway for the current viewport and beat count.
  const setRunway = () => {
    const timing = storyTiming()
    const travel = timing.intro + BEATS.length * timing.hold + (BEATS.length - 1) * timing.transition + timing.handover
    root.querySelector('[data-scroll]').style.height = ((travel + 1) * 100) + 'vh'
  }
  setRunway()

  /* ── the field ───────────────────────────────────────────────────── */
  const canvas = root.querySelector('[data-canvas]')

  /* The map is drawn on this canvas, so a click has to be hit-tested against
     the same projection that drew it. `liveMap` holds the furniture of the
     currently drawn map beat — projection, counts, bounds — and is null on
     every other beat, which is also what stops clicks doing anything on folds
     that have no map. */
  let liveMap = null
  const onSelectCountry = typeof options.onSelectCountry === 'function' ? options.onSelectCountry : () => {}

  function mapClick(ev){
    if (!liveMap) return
    const r = canvas.getBoundingClientRect()
    const x = ev.clientX - r.left, y = ev.clientY - r.top
    const { b } = liveMap
    if (x < b.x0 || x > b.x1 || y < b.y0 || y > b.y1){ onSelectCountry(null); return }
    const ll = liveMap.proj.invert([x, y])
    if (!ll){ onSelectCountry(null); return }
    const hit = land.features.find(feat => geoContains(feat, ll))
    if (!hit){ onSelectCountry(null); return }
    const name = hit.properties.name
    onSelectCountry({ name, ...(liveMap.detail[name] || { projects:0, studies:0, findings:0 }) })
  }
  canvas.addEventListener('click', mapClick)
  const ctx = canvas.getContext('2d')
  const DPR = Math.min(2, window.devicePixelRatio || 1)
  let W = 0, H = 0
  let sizeRetry = 0, destroyed = false
  const charts = createStoryCharts(DATA, root, options.coauthors || null)
  const dots = entities.map((p, i) => ({
    i, p, kind:p.type, projectYear:projectYearOf(p), studyYear:studyYearOf(p),
    g:p.type === 'project' ? wgOf(p) : null, x:0, y:0, r:1.6, c:GREY,
  }))

  function size(){
    W = canvas.clientWidth; H = canvas.clientHeight
    if (!W || !H){
      if (!destroyed){
        cancelAnimationFrame(sizeRetry)
        sizeRetry = requestAnimationFrame(() => { if (size()) update() })
      }
      return false
    }
    canvas.width = W * DPR; canvas.height = H * DPR
    ctx.setTransform(DPR, 0, 0, DPR, 0, 0)
    layouts.length = 0; furniture.length = 0
    BEATS.forEach(b => { const r = buildLayout(b.layout)
      layouts.push(r.pos || r); furniture.push(r.furn || null) })
    charts.resize()
    textMeta = buildText()
    return true
  }

  // The field always sits in columns 6–12, so the words keep the left.
  const fieldBox = () => {
    const pad = W > 900 ? 48 : 24
    if (W <= 640) return { x0:pad, x1:W - pad, y0:H * 0.58, y1:H * 0.86 }
    const left = W * 0.46
    return { x0:left, x1:W - pad, y0:H * 0.16, y1:H * 0.86 }
  }

  const land = feature(TOPO, TOPO.objects.countries)

  const layouts = []
  let furniture = []
  function buildLayout(kind){
    const b = fieldBox(), bw = b.x1 - b.x0, bh = b.y1 - b.y0
    const out = new Array(dots.length)
    const rnd = mulberry(1234)

    const hidden = i => ({
      x:b.x0 + ((i * 17) % Math.max(1, Math.floor(bw))), y:b.y1 + 24,
      c:GREY, r:.6, a:0,
    })
    const scatter = (entityKind, colour = () => GREY, radius = () => 1.6) => {
      for (let i = 0; i < dots.length; i++){
        if (dots[i].kind !== entityKind){ out[i] = hidden(i); continue }
        out[i] = { x:b.x0 + rnd() * bw, y:b.y0 + rnd() * bh,
                   c:colour(dots[i]), r:radius(dots[i]) }
      }
    }

    if (kind === 'chartBlank'){
      for (let i = 0; i < dots.length; i++) out[i] = hidden(i)
      return { pos:out, furn:null }
    }
    if (kind === 'projectScatter'){
      scatter('project')
      return { pos:out, furn:null }
    }
    else if (kind === 'projectYears'){
      /* One filled area, cumulative.

         Counted year by year this read as short stacks with gaps, and a quiet
         year looked like a failure. That is wrong: a project funded in 2014 did
         not stop counting in 2015. So the height at any year is everything
         funded up to that point, climbing to the full portfolio.

         The dots are hidden here, the same as on the map fold, because the area
         IS the measurement. Drawing each project as a dot on top of the fill put
         a block of texture at every step, and a block sitting on a baseline
         reads as a bar however it was built — which fought the one thing this
         chart is for.

         The y axis is scaled to the final total rather than to a rounded number
         above it, so the curve reaches the top of the frame and the growth is
         read at full height instead of in the bottom two thirds. */
      for (let i = 0; i < dots.length; i++) out[i] = hidden(i)

      const countOf = {}
      for (const project of datedProjects){
        const y = projectYearOf(project)
        countOf[y] = (countOf[y] || 0) + 1
      }
      const years = projectYears, cols = years.length || 1, colW = bw / cols

      let run = 0
      const steps = years.map((y, i) => {
        run += countOf[y] || 0
        return { year:y, ci:i, count:countOf[y] || 0, total:run }
      })
      const total = run || 1
      const yOf = v => b.y1 - (v / total) * bh
      steps.forEach(s => { s.y = yOf(s.total) })

      // Gridlines at round numbers, so the height can be read off rather than
      // guessed. The last one is dropped if it would collide with the total.
      const tickEvery = total > 800 ? 250 : total > 400 ? 100 : 50
      const ticks = []
      for (let v = tickEvery; v < total * 0.93; v += tickEvery) ticks.push({ v, y:yOf(v) })

      out.furn = { kind:'years', b, cols, colW, years, steps, total, ticks }
      return { pos: out, furn: out.furn }
    }
    else if (kind === 'projectMap' || kind === 'studyMap'){
      /* A choropleth, not a dot scatter.

         The old version drew a hairline coastline and then piled little dots
         on each country's centroid. Two problems: a dot cluster encodes
         quantity by area, which the eye reads badly, and it left the country
         itself — the actual shape being measured — as an empty grey outline.
         Shading the country IS the measurement, and it needs no legend to be
         understood. Same logic as the heatmap later in the story, laid flat on
         geography instead of a grid. */
      const entityKind = kind === 'projectMap' ? 'project' : 'study'
      const countryMap = entityKind === 'project' ? countryOfProject : countryOfStudy
      const proj = geoNaturalEarth1().fitExtent([[b.x0, b.y0], [b.x1, b.y1 - 30]], land)
      const per = {}
      let unplaced = 0
      for (let i = 0; i < dots.length; i++){
        if (dots[i].kind !== entityKind){ out[i] = hidden(i); continue }
        const names = countryMap[dots[i].p.id] || []
        const hit = names.map(n => NAME_FIX[n] || n).find(Boolean)
        if (!hit){ unplaced++ }
        else per[hit] = (per[hit] || 0) + 1
        out[i] = hidden(i)          // the map carries the data; the dots do not
      }
      const centroid = {}
      for (const f of land.features){
        const c = geoPath(proj).centroid(f)
        if (!isNaN(c[0])) centroid[f.properties.name] = c
      }
      out.furn = { kind:'map', b, proj, centroid, per, unplaced, entityKind,
                   peak: Math.max(1, ...Object.values(per)), detail: countryDetail }
      return { pos: out, furn: out.furn }
    }
    else if (kind === 'projectGroupYears'){
      const rows = groupYearRows
      const labelW = W <= 640 ? Math.min(126, bw * 0.38) : Math.min(160, bw * 0.24)
      const gx0 = b.x0 + labelW
      const years = projectYears, cols = years.length || 1
      const colW = (bw - labelW) / cols
      const bandH = 30
      const rowH = (bh - bandH) / rows.length
      const rowOf = Object.fromEntries(rows.map((r, i) => [r, i]))
      const per = {}, perRow = Math.max(2, Math.floor((colW - 3) / 4.2))
      let loose = 0
      for (let i = 0; i < dots.length; i++){
        if (dots[i].kind !== 'project'){ out[i] = hidden(i); continue }
        const y = dots[i].projectYear, g = dots[i].g
        const ri = rowOf[g]
        if (!y || ri === undefined){
          const k = loose++
          out[i] = { x:gx0 + (k % 96) * ((bw - labelW) / 96),
                     y:b.y1 - 2 - Math.floor(k / 96) * 4.2,
                     c:GREY, r:1.1, a:0.16 }
          continue
        }
        const ci = years.indexOf(y)
        const key = ri + ':' + ci
        per[key] = (per[key] || 0) + 1
        const n = per[key] - 1
        const base = b.y0 + (ri + 1) * rowH - bandH * 0.34
        out[i] = {
          x: gx0 + ci * colW + (n % perRow) * 4.2 + 2,
          y: base - Math.floor(n / perRow) * 4.2,
          c: TEAL, r:1.7 }
      }
      out.furn = { kind:'groupYears', b, rows, labelW, gx0, colW, rowH, bandH, loose, years }
      return { pos: out, furn: out.furn }
    }
    else if (kind === 'projectPapers'){
      const cx = b.x0 + bw / 2, cy = b.y1, R = Math.min(bw, bh) * 0.82
      const lit = projects.filter(project => project.hasPublication).length
      let onArc = 0
      for (let i = 0; i < dots.length; i++){
        if (dots[i].kind !== 'project'){ out[i] = hidden(i); continue }
        if (dots[i].p.hasPublication){
          const t = onArc++ / Math.max(1, lit - 1), a = Math.PI + t * Math.PI
          out[i] = { x:cx + Math.cos(a) * R * 0.62, y:cy + Math.sin(a) * R * 0.52,
                     c:YELLOW, r:2.1 }
        } else {
          out[i] = { x:b.x0 + rnd() * bw, y:b.y0 + rnd() * bh, c:[60,60,58], r:1.3 }
        }
      }
      out.furn = { kind:'arc', b, cx, cy, R, lit, total: projects.length }
      return { pos: out, furn: out.furn }
    }
    else if (kind === 'projectWeb'){
      const cx = b.x0 + bw / 2, cy = b.y0 + bh / 2
      for (let i = 0; i < dots.length; i++){
        const a = rnd() * Math.PI * 2, rr = Math.pow(rnd(), .55) * Math.min(bw, bh) * .5
        out[i] = { x:cx + Math.cos(a) * rr, y:cy + Math.sin(a) * rr * .86,
                   c:dots[i].kind === 'study' ? TEAL : GREY,
                   r:dots[i].kind === 'study' ? 1.9 : 1.35 }
      }
      return { pos:out, furn:{ kind:'legend', b, entries:[
        { label:'Funded projects', colour:GREY }, { label:'Research studies', colour:TEAL },
      ] } }
    }
    else if (kind === 'studyTypes'){
      scatter('study', dot => {
        const values = new Set((dot.p.studyTypes || []).map(v => String(v).toLowerCase()))
        const valuation = values.has('valuation study'), psychometric = values.has('psychometric study')
        if (valuation && psychometric) return INK
        if (valuation) return YELLOW
        if (psychometric) return TEAL
        return GREY
      }, () => 1.9)
      return { pos:out, furn:{ kind:'legend', b, entries:[
        { label:'Valuation', colour:YELLOW }, { label:'Psychometric', colour:TEAL },
        { label:'Both', colour:INK }, { label:'Other study types', colour:GREY },
      ] } }
    }
    else if (kind === 'studyInstruments'){
      scatter('study', dot => {
        const values = new Set(dot.p.instruments || [])
        const fiveL = values.has('EQ-5D-5L'), vas = values.has('EQ VAS')
        if (fiveL && vas) return INK
        if (fiveL) return YELLOW
        if (vas) return TEAL
        return GREY
      }, () => 1.9)
      return { pos:out, furn:{ kind:'legend', b, entries:[
        { label:'EQ-5D-5L', colour:YELLOW }, { label:'EQ VAS', colour:TEAL },
        { label:'Both', colour:INK }, { label:'Other instruments', colour:GREY },
      ] } }
    }
    else if (kind === 'studyMethods'){
      scatter('study', dot => {
        const values = new Set((dot.p.methods || []).map(v => String(v).toLowerCase()))
        const dce = values.has('dce'), ctto = values.has('ctto')
        if (dce && ctto) return INK
        if (dce) return YELLOW
        if (ctto) return TEAL
        return GREY
      }, () => 1.9)
      return { pos:out, furn:{ kind:'legend', b, entries:[
        { label:'DCE', colour:YELLOW }, { label:'cTTO', colour:TEAL },
        { label:'Both', colour:INK }, { label:'Other methods', colour:GREY },
      ] } }
    }
    else if (kind === 'studyProducts'){
      scatter('study', dot => dot.p.hasValueSet ? YELLOW : dot.p.hasProduct ? TEAL : GREY, () => 1.9)
      return { pos:out, furn:{ kind:'legend', b, entries:[
        { label:'Value set or tariff', colour:YELLOW }, { label:'Other research product', colour:TEAL },
        { label:'No named product', colour:GREY },
      ] } }
    }
    else if (kind === 'studyWeb'){
      const cx = b.x0 + bw / 2, cy = b.y0 + bh / 2
      for (let i = 0; i < dots.length; i++){
        if (dots[i].kind !== 'study'){ out[i] = hidden(i); continue }
        const a = rnd() * Math.PI * 2, rr = Math.pow(rnd(), .55) * Math.min(bw, bh) * .5
        const weight = Math.min(1, Number(dots[i].p.findingCount || 0) / 8)
        out[i] = { x:cx + Math.cos(a) * rr, y:cy + Math.sin(a) * rr * .86,
                   c:mix(TEAL, YELLOW, weight), r:1.5 + weight * 1.3 }
      }
      return { pos:out, furn:null }
    }
    return { pos: out, furn: null }
  }

  function mulberry(seed){ let a = seed >>> 0
    return () => { a = (a + 0x6D2B79F5) | 0; let t = Math.imul(a ^ (a >>> 15), 1 | a)
      t = (t + Math.imul(t ^ (t >>> 7), 61 | t)) ^ t; return ((t ^ (t >>> 14)) >>> 0) / 4294967296 } }
  function mix(a, b, t){ return [lerp(a[0],b[0],t), lerp(a[1],b[1],t), lerp(a[2],b[2],t)] }

  /* ── the intro ───────────────────────────────────────────────────────
     The line no longer names EuroQol — the mark in the corner does that, and
     the sentence is stronger for being about the work rather than the body.

     It is drawn to an offscreen canvas and sampled into the
     the same data dots, so the words become the research field. Timing was
     the note: the field must be settled and readable BEFORE the text has
     finished leaving, not after. The dissolve starts at 1% — the second you
     move — crosses the words by 31%, and the last dot is home by 87%. What
     is left is a hold, so beat 01 is still before it starts to move. */
  const INTRO_TEXT = 'Shaping how the world measures health.'
  let textSpots = null
  const instEl = root.querySelector('[data-instrument]')

  /* The globe is not transformed by the story any more. It sizes and places
     itself, and scaling it from here only ever fought that — it came out small
     and clipped. The story decides when it is on screen; the globe decides
     where it sits. */

  const ctaEl  = root.querySelector('[data-cta]')
  const keyEl  = root.querySelector('[data-key]')


  function buildText(){
    const off = document.createElement('canvas')
    off.width = W; off.height = H
    const o = off.getContext('2d')
    o.clearRect(0, 0, W, H)
    const pad = W > 900 ? 48 : 24
    const fs = Math.max(32, Math.min(104, W * 0.062))
    o.font = `500 ${fs}px 'Instrument Sans', 'Helvetica Neue', sans-serif`
    o.fillStyle = ink(1); o.textAlign = 'left'; o.textBaseline = 'middle'
    const words = INTRO_TEXT.split(' '); const lines = []; let line = ''
    for (const w of words){
      const t = line ? line + ' ' + w : w
      if (o.measureText(t).width > W * 0.50 && line){ lines.push(line); line = w } else line = t
    }
    if (line) lines.push(line)
    const lh = fs * 0.98
    let y = H * 0.16
    lines.forEach(l => { o.fillText(l, pad, y + lh / 2); y += lh })

    const textW = Math.max(...lines.map(l => o.measureText(l).width))

    const d = o.getImageData(0, 0, W, H).data, cand = []
    for (let py = 0; py < H; py += 4) for (let px = 0; px < W; px += 4)
      if (d[(py * W + px) * 4 + 3] > 130) cand.push([px, py])
    const step = cand.length / dots.length
    textSpots = dots.map((_, i) => cand[Math.min(cand.length - 1, (i * step) | 0)] || [W / 2, H / 2])
    // where the words actually finish, so the buttons can sit under them
    const bottom = H * 0.16 + lines.length * lh
    if (ctaEl) ctaEl.style.top = Math.round(bottom + fs * 0.42) + 'px'
    return { lines, lh, fs, pad, bottom, textW, img:off, font:o.font }
  }
  let textMeta = null

  /* The words do not fade while a layer of dots sits on top of them — that
     reads as dust on the type. They are eaten from the left by a soft edge,
     and each dot lets go exactly as the edge reaches the letter it was cut
     from. So at any moment a letter is either solid, or gone and travelling;
     never both. It starts the instant you move, and every dot leaves on its
     own curve rather than the whole field sliding in lockstep. */
  let scratch = null, sctx = null
  function scratchCtx(){
    if (!scratch || scratch.width !== W || scratch.height !== H){
      scratch = document.createElement('canvas')
      scratch.width = W; scratch.height = H
      sctx = scratch.getContext('2d')      // fetching a context every frame is not free
    }
    return sctx
  }

  // one fixed swirl per dot, so the disperse is organic and never re-rolls
  let jitter = null
  function buildJitter(){
    jitter = dots.map((_, i) => {
      const a = Math.sin(i * 12.9898) * 43758.5453
      const b = Math.sin(i * 78.233) * 12345.6789
      return { s:(a - Math.floor(a)) * 2 - 1, u:(b - Math.floor(b)) * 2 - 1 }
    })
  }

  const START = 0.012          // it lets go the second you move
  const SPAN  = 0.30           // how long the wave takes to cross the words
  const FLY   = 0.56           // how long one dot takes to reach its place

  function drawIntro(t){
    ctx.clearRect(0, 0, W, H)
    const m = textMeta
    if (!m) return
    if (!jitter || jitter.length !== dots.length) buildJitter()

    const soft = m.fs * 2.0                       // the width of the dissolving edge
    const wipe = t <= START ? 0 : Math.min(1, (t - START) / SPAN)
    const edge = m.pad - soft + wipe * (m.textW + soft * 2)

    // 1. the words, eaten from the left
    if (wipe < 1){
      const s = scratchCtx()
      s.setTransform(1, 0, 0, 1, 0, 0)
      s.clearRect(0, 0, W, H)
      s.globalCompositeOperation = 'source-over'
      s.drawImage(m.img, 0, 0)
      s.globalCompositeOperation = 'destination-out'
      const g = s.createLinearGradient(edge - soft, 0, edge, 0)
      g.addColorStop(0, 'rgba(0,0,0,1)')
      g.addColorStop(1, 'rgba(0,0,0,0)')
      s.fillStyle = g; s.fillRect(0, 0, W, H)
      ctx.drawImage(scratch, 0, 0)
    }

    // 2. the particles, each born as the edge passes it
    const home = layouts[0]
    for (let i = 0; i < dots.length; i++){
      const sp = textSpots[i], h = home[i], j = jitter[i]
      const local = Math.max(0, Math.min(1, (sp[0] - m.pad + soft * 0.5) / (m.textW + soft)))
      const born = START + local * SPAN
      const age = t - born
      if (age <= 0) continue

      /* When the first beat has no dots of its own — the map draws countries,
         not a scatter — the particle's home alpha is zero, and multiplying by
         it made the whole flight invisible: the sentence dissolved into
         nothing. A particle flying to a beat that will not show it now stays
         visible for the flight and fades as it lands, so the words still come
         apart and the map still arrives clean. */
      const targetA = h.a == null ? 1 : h.a
      const f = ease(Math.min(1, age / FLY))
      const a = Math.min(1, age / 0.05) * (targetA === 0 ? (1 - f) : targetA)

      // a curve, not a straight line: it is thrown clear, then drawn home
      const dx = h.x - sp[0], dy = h.y - sp[1]
      const len = Math.hypot(dx, dy) || 1
      const cx = (sp[0] + h.x) / 2 - (dy / len) * j.s * 90 + j.u * 26
      const cy = (sp[1] + h.y) / 2 + (dx / len) * j.s * 90 - j.s * 34
      const k = 1 - f
      const x = k * k * sp[0] + 2 * k * f * cx + f * f * h.x
      const y = k * k * sp[1] + 2 * k * f * cy + f * f * h.y

      const c0 = lerp(INK[0], h.c[0], f), c1 = lerp(INK[1], h.c[1], f), c2 = lerp(INK[2], h.c[2], f)
      ctx.beginPath(); ctx.arc(x, y, lerp(1.5, h.r, f), 0, 6.283)
      ctx.fillStyle = `rgba(${c0|0},${c1|0},${c2|0},${a.toFixed(3)})`
      ctx.fill()
    }
  }

  /* The chart itself. Dots may be dots while they travel, but the moment
     they arrive they must BE something — a column chart with a baseline and
     year ticks, a map with real coastlines, groups with labels under them.
     Furniture fades in only when a beat is at rest, so it never smears
     across a transition. */
  /* The area under the running total, painted BEFORE the dots so they sit on
     top of it rather than under a wash.

     Without this the year stacks float as separate blocks with a dead field
     underneath, which reads as scattered squares rather than one quantity
     growing. Filling everything below the staircase is what makes it a total:
     the shape is the portfolio, and each year's dots are the fresh edge on top
     of it. */
  function drawAreaFill(f, alpha){
    if (!f || f.kind !== 'years' || !f.steps || alpha <= 0.01) return
    ctx.save()
    ctx.globalAlpha = alpha
    const grad = ctx.createLinearGradient(f.b.x0, 0, f.b.x1, 0)
    // Carries the whole fold now that the dots are hidden, so it is stronger
    // than a wash. Teal at the start and yellow at the end is the same year
    // ramp the rest of the story uses.
    grad.addColorStop(0, `rgba(${TEAL.join(',')},0.30)`)
    grad.addColorStop(1, `rgba(${YELLOW.join(',')},0.46)`)
    ctx.fillStyle = grad
    ctx.beginPath()
    ctx.moveTo(f.b.x0, f.b.y1)
    f.steps.forEach(s => {
      const x0 = f.b.x0 + s.ci * f.colW
      ctx.lineTo(x0, s.y)
      ctx.lineTo(x0 + f.colW, s.y)
    })
    ctx.lineTo(f.b.x0 + f.steps.length * f.colW, f.b.y1)
    ctx.closePath()
    ctx.fill()
    ctx.restore()
  }

  function drawFurniture(f, alpha){
    if (!f || alpha <= 0.01) return
    ctx.save()
    ctx.globalAlpha = alpha
    ctx.strokeStyle = ink(.22)
    ctx.fillStyle   = ink(.55)
    ctx.lineWidth = 1
    ctx.font = `500 11px 'IBM Plex Mono', ui-monospace, monospace`
    ctx.textBaseline = 'middle'

    if (f.kind === 'years'){
      ctx.beginPath(); ctx.moveTo(f.b.x0, f.b.y1 + 8); ctx.lineTo(f.b.x1, f.b.y1 + 8); ctx.stroke()
      ctx.textAlign = 'center'
      f.years.forEach((y, i) => {
        if (f.years.length > 9 && i % 2) return
        const x = f.b.x0 + i * f.colW + f.colW / 2
        ctx.beginPath(); ctx.moveTo(x, f.b.y1 + 8); ctx.lineTo(x, f.b.y1 + 13); ctx.stroke()
        ctx.fillText(String(y), x, f.b.y1 + 24)
      })

      if (f.steps){
        // Gridlines first, underneath the curve. They are the quietest thing
        // here: they let a height be read, they are not the reading.
        ctx.textAlign = 'left'
        f.ticks?.forEach(t => {
          ctx.strokeStyle = ink(.09)
          ctx.beginPath(); ctx.moveTo(f.b.x0, t.y); ctx.lineTo(f.b.x1, t.y); ctx.stroke()
          ctx.fillStyle = ink(.34)
          ctx.fillText(t.v.toLocaleString('en'), f.b.x0 + 4, t.y - 8)
        })

        // The running total. A staircase rather than a smooth curve, because
        // funding arrives in yearly rounds and smoothing would invent months
        // that do not exist.
        ctx.strokeStyle = ink(.34); ctx.lineWidth = 1.4
        ctx.beginPath()
        f.steps.forEach((s, i) => {
          const x0 = f.b.x0 + s.ci * f.colW
          if (i === 0) ctx.moveTo(x0, s.y); else ctx.lineTo(x0, s.y)
          ctx.lineTo(x0 + f.colW, s.y)
        })
        ctx.stroke()

        // The final total, sat on the top gridline at the left where there is
        // always room. Against the right edge it was cut off by the frame.
        ctx.fillStyle = ink(.62)
        ctx.fillText(`${f.total.toLocaleString('en')} projects funded to date`,
                     f.b.x0 + 4, f.b.y0 + 9)
      }
    }
    else if (f.kind === 'groupYears'){
      ctx.textAlign = 'right'
      f.rows.forEach((name, i) => {
        const base = f.b.y0 + (i + 1) * f.rowH - f.bandH * 0.34
        ctx.beginPath(); ctx.moveTo(f.gx0 - 6, base + 3); ctx.lineTo(f.b.x1, base + 3)
        ctx.strokeStyle = ink(.10); ctx.stroke()
        ctx.font = `500 11px 'Instrument Sans', sans-serif`
        ctx.fillStyle = ink(.62)
        ctx.fillText(name.length > 22 ? name.slice(0, 21) + '…' : name, f.gx0 - 12, base - 4)
      })
      ctx.font = `500 11px 'IBM Plex Mono', ui-monospace, monospace`
      ctx.textAlign = 'center'; ctx.fillStyle = ink(.4)
      f.years.forEach((y, i) => {
        if (f.years.length > 9 && i % 3) return
        ctx.fillText(String(y), f.gx0 + i * f.colW + f.colW / 2, f.b.y1 + 16)
      })
      ctx.textAlign = 'left'; ctx.fillStyle = ink(.34)
      if (f.loose) ctx.fillText(`${f.loose} projects without a start year`, f.gx0, f.b.y1 - 26)
    }
    else if (f.kind === 'map'){
      liveMap = f            // this beat can be clicked
      const path = geoPath(f.proj, ctx)

      // Every country first, as the quietest possible ground. It is the shape
      // of the world, not a data mark, so it sits well below the shaded ones.
      ctx.beginPath(); path(land)
      ctx.fillStyle = ink(.045); ctx.fill()
      ctx.strokeStyle = ink(.10); ctx.lineWidth = .6; ctx.stroke()

      /* Then the ones with research in them, filled by how much. The ramp runs
         from the palest brand green to the full one; a square-root scale,
         because a linear one leaves everything below the leader nearly blank
         when one country holds several times the rest. */
      for (const feat of land.features){
        const n = f.per[feat.properties.name]
        if (!n) continue
        const t = Math.sqrt(n / f.peak)
        ctx.beginPath(); path(feat)
        ctx.fillStyle = `rgba(${TEAL[0]},${TEAL[1]},${TEAL[2]},${(0.16 + t * 0.74).toFixed(3)})`
        ctx.fill()
        ctx.strokeStyle = ink(.14); ctx.lineWidth = .5; ctx.stroke()
      }

      /* Labels, placed so they never collide.

         The old version wrote the top five at their centroids and hoped. In
         Europe the centroids are a few pixels apart, so "United Kingdom 17"
         landed on top of "Netherlands 16" and both became unreadable — the
         densest part of the map, which is exactly where the reader looks.

         Each label is measured before it is drawn, tested against every box
         already placed, and dropped if it overlaps. A label that cannot be
         read is worse than an absent one: the country is still shaded, so the
         quantity is on the page either way. Four candidate positions are tried
         first, so a label usually finds room on another side rather than being
         lost. */
      const top = W <= 640 ? [] : Object.entries(f.per).sort((a, b) => b[1] - a[1]).slice(0, 9)
      ctx.textAlign = 'left'; ctx.textBaseline = 'middle'
      const placed = []
      const clashes = (x, y, w, h) => placed.some(r =>
        x < r.x + r.w + 4 && x + w + 4 > r.x && y < r.y + r.h + 3 && y + h + 3 > r.y)

      for (const [name, n] of top){
        const c = f.centroid[name]; if (!c) continue
        const text = `${name} ${n}`
        const tw = ctx.measureText(text).width, th = 12
        // right of the centroid, then left, then above, then below
        const tries = [[c[0] + 8, c[1]], [c[0] - 8 - tw, c[1]], [c[0] - tw / 2, c[1] - 13], [c[0] - tw / 2, c[1] + 13]]
        const spot = tries.find(([x, y]) =>
          x > f.b.x0 && x + tw < f.b.x1 && y - th / 2 > f.b.y0 && y + th / 2 < f.b.y1 && !clashes(x, y - th / 2, tw, th))
        if (!spot) continue
        const [x, y] = spot
        placed.push({ x, y: y - th / 2, w: tw, h: th })
        // a soft plate under the words, so they read over a filled country
        ctx.fillStyle = `rgba(${GROUND[0]},${GROUND[1]},${GROUND[2]},.74)`
        ctx.fillRect(x - 3, y - th / 2 - 1, tw + 6, th + 2)
        ctx.fillStyle = ink(.9)
        ctx.fillText(text, x, y)
      }
      ctx.textBaseline = 'alphabetic'

      if (f.unplaced){
        ctx.fillStyle = ink(.4)
        const label = f.entityKind === 'study'
          ? `${f.unplaced} studies span regions or have no single country`
          : `${f.unplaced} projects are not tied to one country`
        ctx.fillText(label, f.b.x0, f.b.y1 + 16)
      }
    }
    else if (f.kind === 'columns'){
      ctx.beginPath(); ctx.moveTo(f.b.x0, f.b.y1 + 8); ctx.lineTo(f.b.x1, f.b.y1 + 8); ctx.stroke()
      ctx.textAlign = 'center'
      f.names.forEach((n, i) => {
        const x = f.b.x0 + i * f.colW + f.colW / 2
        const label = n.length > 13 ? n.slice(0, 12) + '…' : n
        ctx.fillText(label, x, f.b.y1 + 24)
      })
    }
    else if (f.kind === 'arc'){
      ctx.beginPath(); ctx.moveTo(f.b.x0, f.cy + 8); ctx.lineTo(f.b.x1, f.cy + 8); ctx.stroke()
      ctx.textAlign = 'left'
      ctx.fillStyle = `rgba(${YELLOW[0]},${YELLOW[1]},${YELLOW[2]},.85)`
      ctx.fillText(`${f.lit} represented in publications`, f.b.x0, f.cy + 24)
      ctx.fillStyle = ink(.4)
      ctx.fillText(`${f.total - f.lit} other funded projects`, f.b.x0 + 210, f.cy + 24)
    }
    else if (f.kind === 'legend'){
      ctx.textAlign = 'left'
      ctx.font = `500 11px 'Instrument Sans', sans-serif`
      let x = f.b.x0
      let y = f.b.y1 + 18
      for (const entry of f.entries){
        const width = Math.max(88, ctx.measureText(entry.label).width + 30)
        if (x > f.b.x0 && x + width > f.b.x1){ x = f.b.x0; y += 18 }
        ctx.beginPath(); ctx.arc(x + 3, y, 3, 0, 6.283)
        ctx.fillStyle = `rgba(${entry.colour[0]},${entry.colour[1]},${entry.colour[2]},.92)`
        ctx.fill()
        ctx.fillStyle = ink(.58)
        ctx.fillText(entry.label, x + 12, y)
        x += width
      }
    }
    ctx.restore()
  }

  /* ── draw ────────────────────────────────────────────────────────── */
  function draw(i0, i1, rawT){
    const span = BEATS.length - 1
    const t = i0 === i1 ? 0 : ease(rawT)
    const f = i0 + t
    const A = layouts[i0], B = layouts[i1]
    if (!A || !B) return

    ctx.clearRect(0, 0, W, H)

    /* The object behind the beat, cross-fading with it. It is drawn first
       and kept faint: it is the room the data stands in, not the data. */
    const box = fieldBox(), now = performance.now() / 1000
    if (BEATS[i0].art) drawBeatArt(ctx, BEATS[i0].art, box, (1 - t) * 0.9, now, INK.join(','))
    if (i1 !== i0 && BEATS[i1].art) drawBeatArt(ctx, BEATS[i1].art, box, t * 0.9, now, INK.join(','))

    // Same timing as the labels below, but painted underneath the dots.
    if (i0 === i1){
      drawAreaFill(furniture[i0], 1)
    } else {
      drawAreaFill(furniture[i0], Math.max(0, 1 - rawT * 3.4))
      drawAreaFill(furniture[i1], Math.max(0, (rawT - .7) / .3))
    }

    for (let i = 0; i < dots.length; i++){
      const a = A[i], b = B[i]
      const x = lerp(a.x, b.x, t), y = lerp(a.y, b.y, t)
      const r = lerp(a.r, b.r, t)
      const c = [lerp(a.c[0],b.c[0],t), lerp(a.c[1],b.c[1],t), lerp(a.c[2],b.c[2],t)]
      const alpha = lerp(a.a == null ? .85 : a.a, b.a == null ? .85 : b.a, t)
      ctx.beginPath()
      ctx.arc(x, y, r, 0, 6.283)
      ctx.fillStyle = `rgba(${c[0]|0},${c[1]|0},${c[2]|0},${alpha})`
      ctx.fill()
    }

    /* Cleared every frame and re-set by whichever furniture is actually a map.
       It used to be set once and never unset, so after the map fold had been
       seen, a click anywhere on any later fold still hit-tested the map and
       opened a country card on top of a chart. */
    liveMap = null

    // Chart labels stay at full strength for the hold. During the short
    // change, the old labels leave early and the new labels arrive late.
    if (i0 === i1){
      drawFurniture(furniture[i0], 1)
    } else {
      drawFurniture(furniture[i0], Math.max(0, 1 - rawT * 3.4))
      drawFurniture(furniture[i1], Math.max(0, (rawT - .7) / .3))
    }
    charts.show(BEATS[i0].chart, BEATS[i1].chart, rawT)

    // panels slide; the field stays put and rearranges under them
    track.style.transform = `translate3d(${-(f * 100)}vw,0,0)`

    const active = i0 === i1 || rawT < .5 ? i0 : i1
    root.querySelectorAll('[data-dots] button').forEach((d, i) => {
      d.classList.toggle('on', i === active)
      if (i === active) d.setAttribute('aria-current', 'step')
      else d.removeAttribute('aria-current')
    })
    const cur = root.querySelector('[data-current]')
    if (cur) cur.textContent = String(active + 1).padStart(2, '0')

    // the blooms drift with the story rather than on a timer
    const p = span ? f / span : 0
    const g = root.querySelector('[data-glow]')
    g.children[0].style.transform = `translate3d(${(12 - p * 34)}vw, ${(6 + p * 10)}vh, 0)`
    g.children[1].style.transform = `translate3d(${(58 - p * 26)}vw, ${(44 - p * 18)}vh, 0)`
  }

  /* ── the hand-over ───────────────────────────────────────────────
     The chat below sits at margin-top:-100vh, so its first screen overlaps
     the story's last. Same lesson as before: one fold, not two sections. The
     stage fades as the chat rises through it. */
  const stageEl = root.querySelector('[data-stage]')
  const chatEl  = document.querySelector('.landing-v2-root .xp-root')
  let chatEntered = false

  function handOver(){
    if (!chatEl) return
    const vh = window.innerHeight
    const bottom = scroller.getBoundingClientRect().bottom
    let t = (2 * vh - bottom) / vh
    t = t < 0 ? 0 : t > 1 ? 1 : t
    const e = ease(t)
    stageEl.style.opacity = (1 - e).toFixed(3)
    chatEl.style.opacity = e.toFixed(3)
    chatEl.style.transform = `translateY(${((1 - e) * 24).toFixed(1)}px)`
    chatEl.style.pointerEvents = e > 0.92 ? '' : 'none'
    stageEl.style.visibility = e >= 0.999 ? 'hidden' : ''
    if (t < 0.9) chatEntered = false
    if (t >= 0.999 && !chatEntered){
      chatEntered = true
      const returnY = storyYForBeat(BEATS.length - 1)
      requestAnimationFrame(() => options.onEnterChat?.({ returnY }))
    }
  }

  /* ── scroll ──────────────────────────────────────────────────────── */
  const scroller = root.querySelector('[data-scroll]')
  let ticking = false

  function beatState(units, timing){
    let left = Math.max(0, units)
    const reduced = window.matchMedia('(prefers-reduced-motion: reduce)').matches
    for (let beat = 0; beat < BEATS.length; beat++){
      if (left <= timing.hold || beat === BEATS.length - 1){
        return { phase:'hold', beat, i0:beat, i1:beat, t:0 }
      }
      left -= timing.hold
      if (left <= timing.transition){
        const raw = Math.max(0, Math.min(1, left / timing.transition))
        if (reduced){
          const snap = raw < .5 ? beat : beat + 1
          return { phase:'hold', beat:snap, i0:snap, i1:snap, t:0 }
        }
        return { phase:'transition', beat:raw < .5 ? beat : beat + 1, i0:beat, i1:beat + 1, t:raw }
      }
      left -= timing.transition
    }
    const last = BEATS.length - 1
    return { phase:'hold', beat:last, i0:last, i1:last, t:0 }
  }

  function publishState(state, progress = 0){
    root.dataset.storyPhase = state.phase
    root.dataset.storyBeat = String(state.beat + 1)
    root.dataset.storyTransition = progress.toFixed(3)
  }

  function update(){
    ticking = false
    const vh = window.innerHeight
    const r = scroller.getBoundingClientRect()
    const timing = storyTiming()
    const introLen = timing.intro * vh
    const scrolled = -r.top

    if (scrolled < introLen){
      const t = Math.max(0, scrolled / introLen)
      // the object is the opening image; it clears as the dots take the space
      // Full strength from the very first frame — nothing to scroll for.
      // The globe belongs to the opening screen and leaves with it. Carrying it
      // into the first beat read as the page failing to let go of something.
      const openA = (t > 0.60 ? 0 : 1 - Math.max(0, (t - 0.34) / 0.26)).toFixed(3)
      if (instEl) instEl.style.opacity = openA
      if (keyEl){ keyEl.style.opacity = openA; keyEl.style.pointerEvents = +openA > 0.5 ? '' : 'none' }
      // the buttons belong to the sentence, so they leave with it
      const ctaA = (t > 0.26 ? 0 : 1 - Math.max(0, (t - 0.04) / 0.22)).toFixed(3)
      if (ctaEl){ ctaEl.style.opacity = ctaA; ctaEl.style.pointerEvents = +ctaA > 0.5 ? '' : 'none' }
      drawIntro(t)
      charts.show()
      track.style.transform = 'translate3d(0,0,0)'
      // the first panel's words arrive as the dots settle, not after
      track.style.opacity = (t < 0.7 ? 0 : Math.min(1, (t - 0.7) / 0.25)).toFixed(3)
      root.querySelectorAll('[data-dots] button').forEach((d, i) => {
        d.classList.toggle('on', i === 0)
        if (i === 0) d.setAttribute('aria-current', 'step')
        else d.removeAttribute('aria-current')
      })
      const c0 = root.querySelector('[data-current]')
      if (c0) c0.textContent = '01'
      publishState({ phase:'intro', beat:0 }, t)
    } else {
      if (instEl){ instEl.style.opacity = '0'; instEl.style.pointerEvents = 'none' }
      if (keyEl){ keyEl.style.opacity = '0'; keyEl.style.pointerEvents = 'none' }
      if (ctaEl){ ctaEl.style.opacity = '0'; ctaEl.style.pointerEvents = 'none' }
      track.style.opacity = '1'
      const state = beatState((scrolled - introLen) / vh, timing)
      draw(state.i0, state.i1, state.t)
      publishState(state, state.t)
    }
    handOver()
  }
  function onScroll(){ if (!ticking){ ticking = true; requestAnimationFrame(update) } }

  /* Jumping to a beat has to LAND on one. Arriving mid-transition — text
     already gone, the next chart still flying in — is the thing that reads
     as broken. Beat i is settled at exactly i/(beats-1) of the runway, so
     that is the number we scroll to, on our own eased tween rather than the
     browser's, and any touch of the wheel cancels it. */
  let tween = 0
  let clearTweenEvents = () => {}
  function storyYForBeat(i){
    const vh = window.innerHeight
    const r = scroller.getBoundingClientRect()
    const top = r.top + window.scrollY
    const timing = storyTiming()
    const beat = Math.max(0, Math.min(BEATS.length - 1, i))
    const before = beat * (timing.hold + timing.transition)
    return top + (timing.intro + before + timing.hold * .38) * vh
  }
  function goToBeat(i){
    // Land inside the hold, with the chart and copy fully settled.
    scrollTo(storyYForBeat(i))
  }
  function scrollTo(target){
    cancelAnimationFrame(tween)
    clearTweenEvents()
    const from = window.scrollY
    const dist = target - from
    if (Math.abs(dist) < 2) return
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches){
      window.scrollTo(0, target)
      update()
      return
    }
    const dur = Math.min(1500, 480 + Math.abs(dist) * 0.28)
    let t0 = 0
    const stop = () => { cancelAnimationFrame(tween); off() }
    const off = () => {
      window.removeEventListener('wheel', stop)
      window.removeEventListener('touchstart', stop)
      window.removeEventListener('keydown', stop)
      clearTweenEvents = () => {}
    }
    clearTweenEvents = off
    window.addEventListener('wheel', stop, { passive:true, once:true })
    window.addEventListener('touchstart', stop, { passive:true, once:true })
    window.addEventListener('keydown', stop, { once:true })
    const step = now => {
      if (!t0) t0 = now
      const k = Math.min(1, (now - t0) / dur)
      // slow out of the gate, slow into the landing
      const e = k < 0.5 ? 4 * k * k * k : 1 - Math.pow(-2 * k + 2, 3) / 2
      window.scrollTo(0, from + dist * e)
      if (k < 1) tween = requestAnimationFrame(step); else off()
    }
    tween = requestAnimationFrame(step)
  }

  if (size()) update()
  root.querySelectorAll('[data-dots] button').forEach((button, i) => {
    button.addEventListener('click', () => goToBeat(i))
  })
  window.addEventListener('scroll', onScroll, { passive:true })

  let rz
  const onResize = () => { clearTimeout(rz); rz = setTimeout(() => { setRunway(); if (size()) update() }, 180) }
  window.addEventListener('resize', onResize)

  const api = {
    goToBeat,
    scrollTo,
    state:() => ({
      phase:root.dataset.storyPhase,
      beat:Number(root.dataset.storyBeat || 1),
      transition:Number(root.dataset.storyTransition || 0),
    }),
    refresh(){
      setRunway()
      if (size()) update()
    },
    destroy(){
      destroyed = true
      cancelAnimationFrame(tween)
      clearTweenEvents()
      cancelAnimationFrame(sizeRetry)
      clearTimeout(rz)
      charts.destroy()
      window.removeEventListener('scroll', onScroll)
      window.removeEventListener('resize', onResize)
      delete root.__story
    },
  }
  root.__story = api
  return api
}
