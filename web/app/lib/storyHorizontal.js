/* Vertical scroll drives a horizontal track: one pinned stage, five beats.
   Dots carry the opening; SVG charts carry the comparisons. */

import { geoNaturalEarth1, geoPath, geoContains } from 'd3-geo'
import { drawBeatArt } from './beatArt.js'
import { createStoryCharts } from './storyCharts.js'
import { feature } from 'topojson-client'

const lerp = (a, b, t) => a + (b - a) * t
const ease = t => t * t * (3 - 2 * t)

/* Most of the runway is hold, not transition. Give the change more room and a
   settled scene exists at one scroll position only, which reads as broken. */
const storyTiming = () => window.innerWidth <= 640
  ? { intro:1.45, hold:0.86, transition:0.34, handover:1 }
  : { intro:1.35, hold:0.68, transition:0.32, handover:1 }

// Read once from the CSS tokens. Never state a colour below this line.
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

  /* A study recorded against a region ("East Asia") cannot be placed. Count it
     as unplaced rather than dropping it. */
  const NAME_FIX = {
    'United States':'United States of America', 'Czech Republic':'Czechia',
    'Trinidad And Tobago':'Trinidad and Tobago', 'Bosnia And Herzegovina':'Bosnia and Herz.',
    'Saint Vincent And The Grenadines':'St. Vin. and Gren.', 'Dominican Republic':'Dominican Rep.',
    'South Korea':'South Korea', 'Republic Of Korea':'South Korea', 'Russia':'Russia',
  }
  const countryOfProject = {}, countryOfStudy = {}
  /* Two different edges on purpose: projects SUPPORTED_EVIDENCE_IN, studies
     CONDUCTED_IN. The gap between them is how much has been read. */
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
  /* How far the EQ family has travelled, country by country.

     Reviews are excluded on purpose. A systematic review of value sets is
     linked to every country it covers — one compendium alone is linked to
     twenty-one — and counting that as "the instrument was used there" would
     credit a country for a paper that collected nothing in it. Only studies
     that were actually run somewhere count here.

     Instruments are matched on a pattern for the same reason the matrix is:
     the pipeline stores the name as the paper wrote it, so one instrument
     arrives under a dozen spellings. A label naming no level matches nothing,
     because assigning it would be a guess. */
  /* Four instruments, plus one still in development.

     EuroQol names four on its own instruments page: EQ-5D-3L, EQ-5D-5L,
     EQ-5D-Y-3L and EQ-5D-Y-5L. The EQ VAS is not among them, because it is a
     component of the EQ-5D questionnaire rather than a separate instrument, and
     EQ-HWB sits under instruments in development. So HWB is shown, because it
     is genuinely in use, but it is marked rather than counted alongside the
     four. Anything else would state a number EuroQol does not. */
  const FAMILY = [
    ['EQ-5D-3L',   '3L',   /\bEQ[\s-]*5[\s-]*D[\s-]*3[\s-]*L\b/i],
    ['EQ-5D-5L',   '5L',   /\bEQ[\s-]*5[\s-]*D[\s-]*5[\s-]*L\b/i],
    ['EQ-5D-Y-3L', 'Y-3L', /\bEQ[\s-]*5[\s-]*D[\s-]*Y[\s-]*3[\s-]*L\b/i],
    ['EQ-5D-Y-5L', 'Y-5L', /\bEQ[\s-]*5[\s-]*D[\s-]*Y[\s-]*5[\s-]*L\b/i],
    ['EQ-HWB',     'HWB',  /\bEQ[\s-]*HWB\b/i, 'in development'],
  ]
  const ESTABLISHED = FAMILY.filter(f => !f[3])
  const isReview = study => (study.studyTypes || []).includes('EVIDENCE_SYNTHESIS')
  const familyIn = {}          // country -> Set of short names
  const familyReach = {}       // short name -> Set of countries
  for (const [, short] of FAMILY) familyReach[short] = new Set()
  for (const study of studies){
    if (isReview(study)) continue
    const here = (countryOfStudy[study.id] || []).map(n => NAME_FIX[n] || n)
    if (!here.length) continue
    for (const [, short, re] of FAMILY){
      if (!(study.instruments || []).some(i => re.test(String(i)))) continue
      for (const c of here){
        (familyIn[c] || (familyIn[c] = new Set())).add(short)
        familyReach[short].add(c)
      }
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

  /* The same rule the working-group chart uses, so the headline number and the
     rows under it cannot disagree. A project counts in every group it names,
     and the administrative categories in that field are not groups. */
  const NOT_A_GROUP = new Set(['others', 'oa fee', 'unassigned'])
  const groups = (() => {
    const m = new Map()
    for (const p of projects)
      for (const part of String(p.wg || '').split(',')){
        const name = part.trim()
        if (!name || NOT_A_GROUP.has(name.toLowerCase())) continue
        m.set(name, (m.get(name) || 0) + 1)
      }
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

  const eqInstruments = (series.instruments || []).filter(row => /^EQ[- ]/i.test(row.label || ''))
  const eqStudies = studies.filter(s => (s.instruments || []).some(i => /^EQ[- ]/i.test(String(i))))
  const eqShare = studies.length ? Math.round((eqStudies.length / studies.length) * 100) : 0

  /* Five folds, in order: where, when, who, what it measures, what is left.
     Each carries `num` with its `unit` at the same size, and a `so` line that
     says why the number matters. Do not add `art:` — it draws decoration over
     the chart. */
  const BEATS = [
    /* Fold 1 counts instruments, so its number is an instrument number. The
       countries are the reach, not the subject. */
    { num:String(ESTABLISHED.length), unit:'instruments', head:'One scale, in use in 35 countries.',
      body:`EuroQol maintains four instruments. A country is shaded by how many of them are in use there, and the strip below counts the countries each measure has reached.`,
      so:`<b>EQ-5D-5L</b> is at work in <b>${familyReach['5L'].size}</b> countries and <b>EQ-5D-3L</b> in <b>${familyReach['3L'].size}</b>, which is what lets a health outcome in Japan be set beside one in Brazil. The youth versions carry that into paediatrics in <b>${familyReach['Y-3L'].size}</b> and <b>${familyReach['Y-5L'].size}</b> countries, and <b>EQ-HWB</b> has reached <b>${familyReach['HWB'].size}</b> while still in development.`,
      layout:'projectMap' },

    { num:fmt(projects.length), unit:'projects', head:'Funded every single year since 2012.',
      body:`<b>${fmt(datedProjects.length)}</b> projects carry a start year, from ${projectYears[0]} to ${projectYears[projectYears.length - 1]}. Each dot is one project, and beside it each year's papers, one dot each.`,
      so:`The busiest year was <b>${busiestProjectYear[0]}</b> with <b>${fmt(busiestProjectYear[1])}</b> projects, and <b>${projectYears[projectYears.length - 1]}</b> is already funded. <b>${fmt(studies.length)}</b> of those projects have had their papers read in full and turned into structured evidence, and that number grows with every pass through the corpus.`,
      layout:'projectYears' },

    { num:fmt((options.coauthors && options.coauthors.nodes && options.coauthors.nodes.length) || 0), unit:'researchers',
      head:'A field that keeps working with itself.',
      body:`<b>${fmt(evidence.publications || 0)}</b> published papers carry <b>${fmt(evidence.findings || 0)}</b> extracted findings, written by researchers who return to each other again and again.`,
      so:`Each circle is an author and its size is their published work. A line means two people wrote a paper together, and it thickens the more often they did. What it shows is a dense middle, which is what two decades of funding builds: not a list of grant holders, but a field that collaborates.`,
      layout:'chartBlank', chart:'coauthorNetwork' },

    { num:fmt(studies.length), unit:'studies read', head:'Read in full, and turned into evidence you can query.',
      body:`<b>${fmt(studies.length)}</b> studies have been read end to end and structured, from a portfolio of <b>${fmt(projects.length)}</b> funded projects. The totals show how much each instrument carries, and how large each kind of research is.`,
      so:`<b>${fmt(eqStudies.length)}</b> of them put a EuroQol instrument to work. Measurement property evaluation is the largest body at <b>${fmt((series.studyTypes || []).find(r => /measurement/i.test(r.label))?.value || 0)}</b> studies, which is the work that earns an instrument its place in a trial or a national survey.`,
      layout:'chartBlank', chart:'coverageMatrix' },

    { num:String(groups.length), unit:'working groups', head:'Seven programmes, each with its own line of work.',
      body:`Every funded project sits with a working group. Each dot is one project, so the length of a row is what that group has funded.`,
      so:`<b>${leadingGroups[0]?.[0] || '—'}</b> leads with <b>${fmt(leadingGroups[0]?.[1] || 0)}</b> projects, followed by <b>${leadingGroups[1]?.[0] || '—'}</b> at <b>${fmt(leadingGroups[1]?.[1] || 0)}</b>. Roughly a fifth of the portfolio is funded by two groups together, which is where valuation methods meet youth measurement and new instruments get built.`,
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

  /* Hit-test against the same projection that drew the map. `liveMap` is set
     only while a map is on screen, so clicks do nothing on other folds. */
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
    /* A country with nothing in it opens nothing. Clicking unshaded ground was
       returning a card of three zeros, which tells the reader the click worked
       and nothing else. The shading already says where the research is. */
    const row = liveMap.detail[name]
    if (!row || !(row.projects || row.studies || row.findings)){ onSelectCountry(null); return }

    // The card carries which versions have been used, in family order, so a
    // reader can answer "is the one I need in use here" without leaving the map.
    const have = liveMap.familyIn?.[name]
    onSelectCountry({
      name,
      ...row,
      family: liveMap.reach ? liveMap.reach.map(r => ({ short:r.short, has:!!have?.has(r.short) })) : null,
    })
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
    /* How far About has to travel to sit against the right edge, where Skip
       will later replace it. Measured rather than written down: it depends on
       the width of the word and of the stage, and a wrong guess would leave it
       short of the corner or past it. */
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
  /* Antarctica is a third of the world's height and holds no research. Fitting
     the map to it shrank everything else and pushed the inhabited world up into
     the top half of the frame, which is what made the map look small and badly
     placed. The projection is fitted to, and the map drawn from, the land people
     actually live on. */
  const inhabited = { type:'FeatureCollection',
    features: land.features.filter(f => f.properties.name !== 'Antarctica') }

  const layouts = []
  let furniture = []
  /* Which series fold 2 is showing. Not a filter over one dataset: projects are
     counted by the year they were funded, papers by the year they appeared. */
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
      /* Both series, per year, as dots.

         Projects on the left of each year, papers on the right, on ONE shared
         count axis. No second axis: rescaling the shorter series until it
         matched the taller would invent a parity that is not there.

         The papers column IS much shorter, and that is the honest picture. It
         is not output lagging funding, it is our reading lagging both, because
         only a fifth of the portfolio has been read. The copy says so, because
         a chart cannot.

         Dots rather than bars, and one dot is one project or one paper, so the
         columns are counts you could check by eye rather than lengths you have
         to trust. */
      const perYearProjects = {}, perYearPapers = {}
      for (const project of datedProjects){
        const y = projectYearOf(project)
        perYearProjects[y] = (perYearProjects[y] || 0) + 1
      }
      for (const study of studies){
        const y = studyYearOf(study)
        if (y) perYearPapers[y] = (perYearPapers[y] || 0) + 1
      }

      const years = projectYears, cols = years.length || 1, colW = bw / cols
      const subW = colW * 0.38                    // two columns per year, with air
      const peak = Math.max(1, ...years.map(y =>
        Math.max(perYearProjects[y] || 0, perYearPapers[y] || 0)))

      /* A square grid, sized so the tallest column fills the height and the
         dots very nearly touch.

         The width of a column and the height of the stack are not independent:
         n dots across a column of width subW, packed square, hold n²·h/subW in
         total. So the number per row follows from the count, and picking it any
         other way leaves the dots either overflowing or floating in air. Before
         this the pitch was set from the height alone and the radius was capped
         at 2.1px, which left a 4px dot in a 9px cell — half air, so a column
         read as a dotted line rather than a filled bar. */
      const availH = bh * 0.92
      const perRow = Math.max(2, Math.round(Math.sqrt(peak * subW / availH)))
      const rows = Math.ceil(peak / perRow)
      // One pitch for both axes, tightened if the stack would overflow.
      const pitch = Math.min(subW / perRow, availH / Math.max(1, rows))
      const rowH = pitch, stepX = pitch
      const dotR = Math.max(0.9, pitch * 0.42)   // ~16% of the pitch as air

      const place = (n, ci, side) => ({
        x: b.x0 + ci * colW + (side === 'papers' ? colW * 0.54 : colW * 0.06)
           + (n % perRow) * stepX + stepX / 2,
        y: b.y1 - Math.floor(n / perRow) * rowH - dotR,
      })

      const seenP = {}, seenS = {}
      for (let i = 0; i < dots.length; i++){
        const d = dots[i]
        if (d.kind === 'project'){
          const y = d.projectYear
          if (!y){ out[i] = hidden(i); continue }
          const ci = years.indexOf(y)
          const n = (seenP[y] = (seenP[y] || 0) + 1) - 1
          const at = place(n, ci, 'projects')
          out[i] = { ...at, c:TEAL, r:dotR }
        } else if (d.kind === 'study'){
          const y = d.studyYear
          const ci = y ? years.indexOf(y) : -1
          if (ci < 0){ out[i] = hidden(i); continue }
          const n = (seenS[y] = (seenS[y] || 0) + 1) - 1
          const at = place(n, ci, 'papers')
          out[i] = { ...at, c:YELLOW, r:dotR, a:0.9 }
        } else out[i] = hidden(i)
      }

      const yOf = v => b.y1 - (v / perRow) * rowH
      const tickEvery = peak > 120 ? 50 : peak > 60 ? 25 : 10
      const ticks = []
      for (let v = tickEvery; v <= peak; v += tickEvery) ticks.push({ v, y:yOf(v) })

      out.furn = { kind:'years', b, cols, colW, years, ticks, peak,
                   pairs:years.map((y, i) => ({ year:y, ci:i,
                     projects:perYearProjects[y] || 0, papers:perYearPapers[y] || 0 })) }
      return { pos: out, furn: out.furn }
    }
    else if (kind === 'projectMap' || kind === 'studyMap'){
      /* How much of the EQ family has reached each country.

         The landing globe already shades by how much research a country has,
         so shading by that again here says the same thing twice. This asks a
         different question of the same geography: not how much, but how many
         of the five instruments have actually been used. */
      /* The world is about twice as wide as it is tall, and the field is not,
         so width always binds and the map is left floating in the middle of the
         box with dead air above and below. Fit to the width, then lift it to
         the top so the space it does not need is all in one place, under the
         map, where the strip goes. */
      const proj = geoNaturalEarth1().fitWidth(b.x1 - b.x0, inhabited)
      const fitted = geoPath(proj).bounds(inhabited)
      const mapH = fitted[1][1] - fitted[0][1]
      const STRIP_H = 5 * 12 + 30              // five rows and the caption
      // Map and strip travel together as one block, centred in the field, so
      // the space the map cannot use is shared above and below rather than all
      // dumped underneath it.
      const top = b.y0 + Math.max(0, (bh - mapH - STRIP_H) / 2)
      const tr = proj.translate()
      proj.translate([tr[0] + (b.x0 - fitted[0][0]), tr[1] + (top - fitted[0][1])])
      /* The projection preserves the world's aspect ratio, so it never fills
         the box: it leaves a band above and below. Measure where the drawing
         actually ends and hang the strip off that, or the strip floats a long
         way under the map with nothing between them. */
      const mapBox = geoPath(proj).bounds(inhabited)
      for (let i = 0; i < dots.length; i++) out[i] = hidden(i)
      const per = {}
      for (const [c, set] of Object.entries(familyIn))
        per[c] = ESTABLISHED.filter(([, short]) => set.has(short)).length
      const centroid = {}
      for (const f of inhabited.features){
        const c = geoPath(proj).centroid(f)
        if (!isNaN(c[0])) centroid[f.properties.name] = c
      }
      // The strip under the map: how many countries each version has reached.
      // It is the finding the map alone cannot state, that the newest members
      // of the family are in half as many places as the flagship.
      const reach = FAMILY.map(([, short, , note]) => ({ short, note, n:familyReach[short].size }))
      out.furn = { kind:'map', b, proj, centroid, per, unplaced:0, entityKind:'instrument',
                   peak: ESTABLISHED.length, detail: countryDetail, familyIn, reach,
                   mapBottom: mapBox[1][1],
                   totalCountries: Object.keys(countryDetail).length }
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
     Drawn to an offscreen canvas and sampled into the same data dots, so the
     words become the research field. The field has to be settled and readable
     BEFORE the text finishes leaving, not after: dissolve from 1%, across the
     words by 31%, last dot home by 87%. The rest is hold. */
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

            /* Do not multiply by the home alpha. On a beat that hides its dots that
             is zero and the whole flight goes invisible. Fade on landing. */
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

  // Axes, ticks, coastlines. Only drawn at rest, so it never smears mid-move.
  /* Painted before the dots so they sit on it rather than under a wash. */
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

      if (f.ticks){
        ctx.textAlign = 'left'
        f.ticks.forEach(t => {
          ctx.strokeStyle = ink(.08)
          ctx.beginPath(); ctx.moveTo(f.b.x0, t.y); ctx.lineTo(f.b.x1, t.y); ctx.stroke()
          ctx.fillStyle = ink(.32)
          ctx.fillText(String(t.v), f.b.x0 + 3, t.y - 7)
        })

        /* The key draws the two marks rather than naming their colours, so it
           is read in the same form as the chart it explains. */
        const ky = f.b.y0 + 8
        ctx.fillStyle = `rgba(${TEAL[0]},${TEAL[1]},${TEAL[2]},.95)`
        ctx.beginPath(); ctx.arc(f.b.x0 + 4, ky, 2.6, 0, 6.283); ctx.fill()
        ctx.fillStyle = ink(.62); ctx.textAlign = 'left'
        ctx.fillText('projects funded', f.b.x0 + 13, ky)
        const w = ctx.measureText('projects funded').width + 34
        ctx.fillStyle = `rgba(${YELLOW[0]},${YELLOW[1]},${YELLOW[2]},.95)`
        ctx.beginPath(); ctx.arc(f.b.x0 + w, ky, 2.6, 0, 6.283); ctx.fill()
        ctx.fillStyle = ink(.62)
        ctx.fillText('papers read', f.b.x0 + w + 9, ky)
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
      ctx.beginPath(); path(inhabited)
      ctx.fillStyle = ink(.045); ctx.fill()
      ctx.strokeStyle = ink(.10); ctx.lineWidth = .6; ctx.stroke()

          /* Square-root ramp. Linear leaves everything below the leader blank. */
      for (const feat of inhabited.features){
        const n = f.per[feat.properties.name]
        if (!n) continue
        const t = Math.sqrt(n / f.peak)
        ctx.beginPath(); path(feat)
        ctx.fillStyle = `rgba(${TEAL[0]},${TEAL[1]},${TEAL[2]},${(0.16 + t * 0.74).toFixed(3)})`
        ctx.fill()
        ctx.strokeStyle = ink(.14); ctx.lineWidth = .5; ctx.stroke()
      }

          /* Measured, tested against every box already placed, and dropped if it
             still overlaps after four candidate positions. Centroids alone put
             the UK on top of the Netherlands. */
      const top = W <= 640 ? [] : Object.entries(f.per).sort((a, b) => b[1] - a[1]).slice(0, 9)
      ctx.textAlign = 'left'; ctx.textBaseline = 'middle'
      const placed = []
      const clashes = (x, y, w, h) => placed.some(r =>
        x < r.x + r.w + 4 && x + w + 4 > r.x && y < r.y + r.h + 3 && y + h + 3 > r.y)

      for (const [name, n] of top){
        const c = f.centroid[name]; if (!c) continue
        const text = f.reach ? `${name} ${n}/${f.peak}` : `${name} ${n}`
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

      /* The strip under the map. The map answers "how far has the family got
         here"; this answers "how far has each member got", which the shading
         cannot say. One dot is one country, the same mark the other folds use. */
      if (f.reach){
        const y0 = (f.mapBottom || f.b.y1 - 90) + 30
        const labelW = 46
        const maxN = Math.max(1, ...f.reach.map(r => r.n))
        const room = f.b.x1 - f.b.x0 - labelW - 44
        const step = Math.min(7, room / maxN)
        const dr = Math.max(1.4, step * 0.40)
        ctx.textAlign = 'right'; ctx.textBaseline = 'middle'
        ctx.font = `500 10px 'IBM Plex Mono', ui-monospace, monospace`
        f.reach.forEach((r, i) => {
          const y = y0 + i * 12
          ctx.fillStyle = ink(.55)
          ctx.fillText(r.short, f.b.x0 + labelW - 8, y)
          ctx.fillStyle = `rgba(${TEAL[0]},${TEAL[1]},${TEAL[2]},.85)`
          for (let k = 0; k < r.n; k++){
            ctx.beginPath()
            ctx.arc(f.b.x0 + labelW + k * step + step / 2, y, dr, 0, 6.283)
            ctx.fill()
          }
          ctx.fillStyle = ink(.42); ctx.textAlign = 'left'
          ctx.fillText(`${r.n}${r.note ? `  ${r.note}` : ''}`,
                       f.b.x0 + labelW + r.n * step + 7, y)
          ctx.textAlign = 'right'
        })
        ctx.textAlign = 'left'; ctx.fillStyle = ink(.34)
        ctx.font = `500 11px 'IBM Plex Mono', ui-monospace, monospace`
        ctx.fillText(`countries where each measure has been used, of ${f.totalCountries}`,
                     f.b.x0, y0 + 5 * 12 + 6)
        ctx.textBaseline = 'alphabetic'
      }
      else if (f.unplaced){
        ctx.fillStyle = ink(.4)
        ctx.fillText(`${f.unplaced} are not tied to one country`, f.b.x0, f.b.y1 + 16)
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

    /* Between folds the field comes apart and puts itself back together.

       Three of the five folds hide every dot, because their chart is an SVG
       drawn over the top, so a straight interpolation from hidden to hidden had
       nothing moving in it at all: the fold simply cross-faded. This lifts the
       particles out for the crossing and settles them again.

       It is a departure from the resting layout, not a change to it. `burst` is
       zero at both ends by construction, so every settled fold is exactly what
       it was, and nothing here can spoil an arrangement that already works. */
    const burst = i0 === i1 ? 0 : Math.sin(rawT * Math.PI)
    const scatter = burst * Math.min(W, H) * 0.09

    for (let i = 0; i < dots.length; i++){
      const a = A[i], b = B[i]
      let x = lerp(a.x, b.x, t), y = lerp(a.y, b.y, t)
      const r = lerp(a.r, b.r, t)
      const c = [lerp(a.c[0],b.c[0],t), lerp(a.c[1],b.c[1],t), lerp(a.c[2],b.c[2],t)]
      let alpha = lerp(a.a == null ? .85 : a.a, b.a == null ? .85 : b.a, t)
      if (burst > 0.004){
        // Stable per dot, so the cloud is the same shape every time rather than
        // boiling, and each one leaves on its own heading.
        const ang = (i % 97) * 0.0647 + i * 0.011
        const reach = 0.35 + ((i * 37) % 100) / 154
        /* A dot both folds hide is parked on the baseline at each end, so
           scattering from where it sits produced a smear along the floor rather
           than a field coming apart. Those cross through the frame instead. */
        if (a.a === 0 && b.a === 0){
          const hx = box.x0 + (((i * 61) % 233) / 233) * (box.x1 - box.x0)
          const hy = box.y0 + (((i * 97) % 179) / 179) * (box.y1 - box.y0)
          x = lerp(x, hx, burst)
          y = lerp(y, hy, burst)
        }
        x += Math.cos(ang) * scatter * reach
        y += Math.sin(ang) * scatter * reach * 0.72
        // A dot the next fold will not show still has to be visible while it
        // travels, or the crossing is empty again.
        alpha = Math.max(alpha, burst * 0.34)
      }
      ctx.beginPath()
      ctx.arc(x, y, r, 0, 6.283)
      ctx.fillStyle = `rgba(${c[0]|0},${c[1]|0},${c[2]|0},${alpha})`
      ctx.fill()
    }

    /* Must be cleared each frame. If it persists, clicks on later folds still
       hit-test the map and open a country card over a chart. */
    liveMap = null

    // Chart labels stay at full strength for the hold. During the short
    // change, the old labels leave early and the new labels arrive late.
    if (i0 === i1){
      drawFurniture(furniture[i0], 1)
    } else {
      drawFurniture(furniture[i0], Math.max(0, 1 - rawT * 3.4))
      drawFurniture(furniture[i1], Math.max(0, (rawT - .7) / .3))
    }

    /* `.sh-field` is pointer-events:none, so this canvas has to claim the
       pointer itself — and only while a map is drawn, or it covers the globe. */
    canvas.style.pointerEvents = liveMap ? 'auto' : 'none'
    canvas.style.cursor = liveMap ? 'pointer' : ''

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

  /* The story is rendered from a position that chases the scroll rather than
     from the scroll itself.

     A trackpad delivers scroll in uneven lumps, and a transition here is about
     a fifth of a screen, so one flick could cross a whole change in a couple of
     frames: the chart appeared to jump and the sentence with it. The rendered
     position now eases toward the real one, so the same flick becomes a glide
     and nothing crosses faster than the eye can follow.

     The page itself never moves differently — the stage is pinned. Only the
     story inside it is damped, so this costs nothing in scroll feel. */
  let shownAt = null
  function update(){
    ticking = false
    const vh = window.innerHeight
    const r = scroller.getBoundingClientRect()
    const timing = storyTiming()
    const introLen = timing.intro * vh
    const target = -r.top

    if (shownAt === null) shownAt = target
    const gap = target - shownAt
    // Snap when close, or it creeps for ever and never settles.
    if (Math.abs(gap) < 0.6) shownAt = target
    else shownAt += gap * 0.16
    // Never fall more than a screen behind, so a long fling still lands.
    if (Math.abs(target - shownAt) > vh) shownAt = target - Math.sign(gap) * vh
    const scrolled = shownAt
    // Keep drawing until it has caught up.
    if (shownAt !== target && !ticking){ ticking = true; requestAnimationFrame(update) }

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

      /* Beat i is settled at exactly i/(beats-1) of the runway. Land on that,
         or you arrive mid-transition and it reads as broken. */
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
