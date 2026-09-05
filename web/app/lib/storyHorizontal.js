/* Native document scroll activates one visual at a fixed viewport line. */

import { geoNaturalEarth1, geoPath, geoContains } from 'd3-geo'
import { createStoryCharts } from './storyCharts.js'
import { feature } from 'topojson-client'
import { submitChatOnEnter } from '../utils/chatComposer'
import { initGraphTeaser } from './graphTeaser.js'
import { researchWorkingGroups } from '../../shared/utils/workingGroups'

const lerp = (a, b, t) => a + (b - a) * t
const ease = t => t * t * (3 - 2 * t)
const escapeHtml = value => String(value ?? '')
  .replaceAll('&', '&amp;').replaceAll('<', '&lt;').replaceAll('>', '&gt;').replaceAll('"', '&quot;')
// Every fold comes apart into this, whatever size its own marks are drawn at.
const PARTICLE_R = 1.5

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
  const wgOf = p => researchWorkingGroups(p.wg)[0] || 'Unassigned'
  const projectYearOf = p => { const y = Number(p.start_year || 0)
    return (y && y >= 1980 && y <= 2030) ? y : null }
  const studyYearOf = s => { const y = Number(s.year || 0)
    return (y && y >= 1980 && y <= 2030) ? y : null }

  const projectYears = [...new Set(projects.map(projectYearOf).filter(Boolean))].sort()

  /* A study recorded against a region ("East Asia") cannot be placed.  */
  const NAME_FIX = {
    'United States':'United States of America', 'Czech Republic':'Czechia',
    'Trinidad And Tobago':'Trinidad and Tobago', 'Bosnia And Herzegovina':'Bosnia and Herz.',
    'Saint Vincent And The Grenadines':'St. Vin. and Gren.', 'Dominican Republic':'Dominican Rep.',
    'South Korea':'South Korea', 'Republic Of Korea':'South Korea', 'Russia':'Russia',
  }
  const countryOfProject = {}, countryOfStudy = {}
  /* Two different edges on purpose: projects SUPPORTED_EVIDENCE_IN, studies CONDUCTED_IN.  */
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
  /* How far the EQ family has travelled, country by country.  */
  /* Four instruments, plus one still in development.  */
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

  /* The rows of the group-by-year beat: only groups that actually have dated studies, busiest first.  */
  const groupYearRows = (() => {
    const m = new Map()
    for (const p of projects){
      if (!projectYearOf(p)) continue
      const k = wgOf(p); m.set(k, (m.get(k) || 0) + 1)
    }
    return [...m.entries()].sort((a, b) => b[1] - a[1]).map(g => g[0])
  })()

  /* The same rule the working-group chart uses, so the headline number and the rows under it cannot disagree.  */
  const groups = (() => {
    const m = new Map()
    for (const p of projects)
      for (const name of researchWorkingGroups(p.wg)){
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
  const eqStudies = studies.filter(s => (s.instruments || []).some(i => /^EQ[- ]/i.test(String(i))))
  const citationShare = options.cites?.totalCitations
    ? Math.round((options.cites.papers.reduce((sum, paper) => sum + paper.citations, 0) / options.cites.totalCitations) * 100)
    : 0
  const citedPapersShown = Math.min(12, options.cites?.papers?.length || 0)
  const exampleQuestions = [...(DATA.metadata?.questions || [])]
  for (let i = exampleQuestions.length - 1; i > 0; i--){
    const j = Math.floor(Math.random() * (i + 1))
    ;[exampleQuestions[i], exampleQuestions[j]] = [exampleQuestions[j], exampleQuestions[i]]
  }
  const chipQuestions = exampleQuestions.slice(0, 2)

  /* Each sentence adds a reading rule, boundary, or result that the chart does not state. */
  const BEATS = [
    { num:fmt((options.coauthors && options.coauthors.totalResearchers) || 0), unit:'researchers',
      label:'Research community',
      head:'Recurring collaborations form a dense centre within the wider research community.',
      body:'The layout groups the 220 most active researchers by the strength of their co-authorship links.',
      layout:'chartBlank', chart:'coauthorNetwork' },

    { label:'Research programmes',
      head:'The funded-project portfolio spans several research working groups.',
      body:'Valuation and Descriptive Systems contain the largest recorded project portfolios.',
      layout:'chartBlank', chart:'groupPapers' },

    { label:'Research over time',
      head:'More projects started and more studies were published in 2025 than in any earlier year.',
      body:'Projects are counted by start year and studies by publication year. Together the two series show how the portfolio has grown.',
      layout:'projectYears' },

    { label:'Citation reach',
      head:`${citedPapersShown} publications account for ${citationShare}% of recorded citations.`,
      body:'Several of the most-cited papers introduced instruments, scoring methods, or national value sets that later studies could reuse.',
      layout:'chartBlank', chart:'citedWork' },

    { label:'Measure use',
      head:'How each EQ measure is used across research types.',
      body:'Compare where each measure has been developed, valued, evaluated, or applied. Cell counts show studies; colour shows the share within each measure.',
      layout:'chartBlank', chart:'coverageMatrix' },
  ]

  /* ── build the DOM ───────────────────────────────────────────────── */
  const stepsHost = root.querySelector('[data-steps]')
  stepsHost.innerHTML = BEATS.map((b, index) => `
    <section class="sh-panel" data-step="${index}" aria-label="${escapeHtml(b.label)}">
      <div class="sh-copy">
        <p class="sh-step-kicker"><span>${String(index + 1).padStart(2, '0')}</span>${escapeHtml(b.label)}</p>
        ${b.num ? `<div class="sh-num">${b.num}${b.unit ? `<span class="sh-unit">${b.unit}</span>` : ''}</div>` : ''}
        <h2 class="sh-head">${b.head}</h2>
        <p class="sh-body">${b.body}</p>
      </div>
    </section>`).join('') + `
    <section class="sh-panel sh-end" data-story-end>
      <div class="sh-copy">
        <h2 class="sh-head">Explore the research graph.</h2>
        <p class="sh-body">Ask a question about the evidence, or browse the connections yourself.</p>
        <div class="sh-handoff-grid">
          <form class="sh-path sh-path-ask" data-handoff-form aria-labelledby="sh-ask-title">
            <span class="sh-path-text">
              <b id="sh-ask-title">Ask a question</b>
              <small>Get an answer with the studies behind it.</small>
            </span>
            <label class="sh-path-input">
              <textarea rows="2" aria-label="Question for the research graph" required></textarea>
              <span class="sh-path-ghost" data-handoff-ghost aria-hidden="true"></span>
            </label>
            <span class="sh-path-foot">
              <span class="sh-path-chips" aria-label="Example questions">
                ${chipQuestions.map(question => `<button type="button" data-sample-question="${escapeHtml(question)}">${escapeHtml(question)}</button>`).join('')}
              </span>
              <button type="submit" class="sh-path-action">
                <span>Ask</span>
                <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
              </button>
            </span>
          </form>
          <a class="sh-path sh-path-graph" href="/graph" data-graph-cta>
            <canvas data-graph-teaser aria-hidden="true"></canvas>
            <span class="sh-path-text">
              <b>Browse the graph</b>
              <small>Explore people, instruments, funding, and more.</small>
            </span>
            <span class="sh-path-foot sh-path-foot-end">
              <span class="sh-path-action">
                <span>Open graph</span>
                <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6" /></svg>
              </span>
            </span>
          </a>
        </div>
      </div>
    </section>`

  const openExplorer = question => {
    if (typeof options.onEnterChat !== 'function') return
    options.onEnterChat({ returnY:window.scrollY, question:question || undefined })
  }
  const handoffForm = stepsHost.querySelector('[data-handoff-form]')
  const handoffInput = handoffForm?.querySelector('textarea')
  const handoffGhost = handoffForm?.querySelector('[data-handoff-ghost]')

  /* The empty field types the curated questions on a loop, so the card moves like the graph beside it. */
  const ghost = (() => {
    const reduced = typeof matchMedia === 'function' && matchMedia('(prefers-reduced-motion: reduce)').matches
    let timer = 0, i = 0, pos = 0, phase = 'type', running = false
    const q = () => exampleQuestions[i % exampleQuestions.length]
    const step = () => {
      if (!running) return
      const text = q()
      if (phase === 'type'){
        pos += 1
        handoffGhost.textContent = text.slice(0, pos)
        if (pos >= text.length){ phase = 'hold'; timer = setTimeout(step, 2400); return }
        timer = setTimeout(step, 26 + Math.random() * 44)
        return
      }
      if (phase === 'hold'){ phase = 'erase'; timer = setTimeout(step, 0); return }
      pos = Math.max(0, pos - 3)
      handoffGhost.textContent = text.slice(0, pos)
      if (pos === 0){ i += 1; phase = 'type'; timer = setTimeout(step, 420); return }
      timer = setTimeout(step, 14)
    }
    return {
      start(){
        if (!handoffGhost || !exampleQuestions.length) return
        if (reduced){ handoffGhost.textContent = 'Type your question…'; return }
        if (running) return
        running = true
        step()
      },
      stop(){ running = false; clearTimeout(timer) },
    }
  })()
  const syncHandoffState = () => {
    if (!handoffForm) return
    const focused = document.activeElement === handoffInput
    const hasValue = Boolean(handoffInput?.value.trim())
    handoffForm.classList.toggle('is-focused', focused)
    handoffForm.classList.toggle('has-value', hasValue)
    if (handoffInput) handoffInput.placeholder = focused && !hasValue ? 'Type your question…' : ''
    if (focused || hasValue) ghost.stop()
    else ghost.start()
  }
  handoffForm?.addEventListener('submit', event => {
    event.preventDefault()
    const question = handoffInput?.value.trim()
    if (question) openExplorer(question)
    else handoffInput?.focus()
  })
  handoffInput?.addEventListener('input', syncHandoffState)
  handoffInput?.addEventListener('focus', syncHandoffState)
  handoffInput?.addEventListener('blur', syncHandoffState)
  handoffInput?.addEventListener('keydown', event => {
    submitChatOnEnter(event, () => handoffForm?.requestSubmit())
  })
  stepsHost.querySelectorAll('[data-sample-question]').forEach(button => {
    button.addEventListener('click', () => openExplorer(button.dataset.sampleQuestion))
  })
  /* The loop runs only while the closing scene is on screen. */
  const endPanel = stepsHost.querySelector('[data-story-end]')
  const endObserver = endPanel && typeof IntersectionObserver === 'function'
    ? new IntersectionObserver(entries => {
        if (entries.some(entry => entry.isIntersecting)) syncHandoffState()
        else ghost.stop()
      }, { threshold:0.2 })
    : null
  if (endObserver) endObserver.observe(endPanel)
  else syncHandoffState()
  const teaserCanvas = stepsHost.querySelector('[data-graph-teaser]')
  const teaser = teaserCanvas ? initGraphTeaser(teaserCanvas) : null
  root.querySelector('[data-dots]').innerHTML = BEATS.map((b, i) => `
    <button type="button" class="${i ? '' : 'on'}" aria-label="Go to ${b.head}" ${i ? '' : 'aria-current="step"'}></button>
  `).join('')
  const totalEl = root.querySelector('[data-total]')
  if (totalEl) totalEl.textContent = String(BEATS.length).padStart(2, '0')

  /* ── the field ───────────────────────────────────────────────────── */
  const canvas = root.querySelector('[data-canvas]')
  const dataTip = root.querySelector('[data-data-tip]')

  /* Hit-test against the same projection that drew the map.  */
  let liveMap = null
  let liveYears = null
  let hoverYear = -1
  const onSelectCountry = typeof options.onSelectCountry === 'function' ? options.onSelectCountry : () => {}

  function yearIndexAt(ev){
    if (!liveYears) return -1
    const rect = canvas.getBoundingClientRect()
    const x = ev.clientX - rect.left, y = ev.clientY - rect.top
    if (x < liveYears.b.x0 || x > liveYears.b.x1 || y < liveYears.b.y0 || y > liveYears.b.y1) return -1
    return Math.max(0, Math.min(liveYears.years.length - 1, Math.floor((x - liveYears.b.x0) / liveYears.colW)))
  }

  function showYearTip(index){
    if (!dataTip || !liveYears || index < 0){ if (dataTip) dataTip.hidden = true; return }
    const row = liveYears.pairs[index]
    if (!row){ dataTip.hidden = true; return }
    dataTip.innerHTML = `<strong>${row.year}</strong><span><b>${row.projects}</b> funded projects</span><span><b>${row.papers}</b> published studies</span>`
    const stage = root.querySelector('[data-stage]')?.getBoundingClientRect()
    const field = canvas.getBoundingClientRect()
    if (!stage) return
    const x = field.left - stage.left + liveYears.b.x0 + (index + .5) * liveYears.colW
    const y = field.top - stage.top + liveYears.b.y0 - 10
    dataTip.style.left = `${Math.max(150, Math.min(stage.width - 150, x))}px`
    dataTip.style.top = `${Math.max(74, y)}px`
    dataTip.hidden = false
  }

  function redrawActiveBeat(){
    if (activeBeat === 2) drawBeat(activeBeat)
  }

  canvas.addEventListener('pointermove', ev => {
    if (!liveYears) return
    const next = yearIndexAt(ev)
    if (next === hoverYear) return
    hoverYear = next
    showYearTip(next)
    redrawActiveBeat()
  })
  canvas.addEventListener('pointerleave', () => {
    if (!liveYears) return
    hoverYear = -1
    showYearTip(-1)
    redrawActiveBeat()
  })

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
    /* A country with nothing in it opens nothing.  */
    const row = liveMap.detail[name]
    if (!row || !(row.projects || row.studies || row.findings)){ onSelectCountry(null); return }

    // The card carries which versions have been used, in family order, so a reader can answer "is the one I need in use here" without leaving the map.
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
  const charts = createStoryCharts(DATA, root, options.coauthors || null, options.cites || null)
  const dots = entities.map((p, i) => ({
    i, p, kind:p.type, projectYear:projectYearOf(p), studyYear:studyYearOf(p),
    g:p.type === 'project' ? wgOf(p) : null, x:0, y:0, r:1.6, c:GREY,
  }))

  /* Rebuilding costs about two and a half seconds: nine charts re-rendered, the co-author network re-settled under its physics, and five folds re-sampled into particles.  */
  let builtW = 0, builtH = 0
  function size(force = false){
    W = canvas.clientWidth; H = canvas.clientHeight
    if (W && H && !force && W === builtW && H === builtH && layouts.length) return true
    if (!W || !H){
      if (!destroyed){
        cancelAnimationFrame(sizeRetry)
        sizeRetry = requestAnimationFrame(() => { if (size(true)) update() })
      }
      return false
    }
    canvas.width = W * DPR; canvas.height = H * DPR
    ctx.setTransform(DPR, 0, 0, DPR, 0, 0)
    // The charts are drawn first, because the layouts are now sampled from them.
    charts.resize()
    builtW = W; builtH = H
    layouts.length = 0; furniture.length = 0
    BEATS.forEach((b, bi) => { const r = buildLayout(b.layout, b.chart, bi)
      layouts.push(r.pos || r); furniture.push(r.furn || null) })
    /* How far About has to travel to sit against the right edge, where Skip will later replace it.  */
    textMeta = buildText()
    return true
  }

  /* Where the SVG charts actually sit, in canvas pixels, and the coordinate space they draw in.  */
  const chartHost = root.querySelector('[data-charts]')
  function chartBox(){
    const a = chartHost?.getBoundingClientRect()
    const b = canvas.getBoundingClientRect()
    if (!a || !b) return { x:0, y:0, w:W, h:H }
    return { x:a.left - b.left, y:a.top - b.top, w:a.width, h:a.height }
  }
  function chartViewBox(id){
    const svg = chartHost?.querySelector(`[data-chart="${id}"] svg`)
    const vb = svg && svg.viewBox && svg.viewBox.baseVal
    return vb && vb.width ? { w:vb.width, h:vb.height } : null
  }

  /* The fold's words, sampled into the same particles as its picture.  */
  function sampleCopy(index){
    const panel = stepsHost.children[index]
    if (!panel || !W || !H) return []
    const pRect = panel.getBoundingClientRect()
    if (!pRect.width) return []
    const off = document.createElement('canvas')
    off.width = W; off.height = H
    const o = off.getContext('2d')
    o.fillStyle = '#000'; o.textAlign = 'left'; o.textBaseline = 'top'

    for (const el of panel.querySelectorAll('.sh-num, .sh-unit, .sh-head, .sh-body')){
      const text = (el.textContent || '').trim()
      if (!text) continue
      const cs = getComputedStyle(el)
      const r = el.getBoundingClientRect()
      const size = parseFloat(cs.fontSize) || 16
      const lh = parseFloat(cs.lineHeight) || size * 1.4
      o.font = `${cs.fontWeight} ${size}px ${cs.fontFamily}`
      // The unit is inline inside the number, so it would be drawn twice.
      if (el.classList.contains('sh-num')){
        const unit = el.querySelector('.sh-unit')
        if (unit) o.fillText(text.replace((unit.textContent || '').trim(), '').trim(),
                             r.left - pRect.left, r.top - pRect.top)
        else o.fillText(text, r.left - pRect.left, r.top - pRect.top)
        continue
      }
      // Everything else wraps inside its own box, at its own measure.
      const words = text.split(/\s+/)
      let line = '', y = r.top - pRect.top
      const x = r.left - pRect.left
      for (const w of words){
        const t = line ? line + ' ' + w : w
        if (o.measureText(t).width > r.width && line){
          o.fillText(line, x, y); y += lh; line = w
        } else line = t
      }
      if (line) o.fillText(line, x, y)
    }

    const d = o.getImageData(0, 0, W, H).data, pts = []
    for (let py = 0; py < H; py += 3)
      for (let px = 0; px < W; px += 3)
        if (d[(py * W + px) * 4 + 3] > 120) pts.push([px, py])
    return pts
  }

  // The field always sits in columns 6–12, so the words keep the left.
  const fieldBox = () => {
    const pad = W > 900 ? 48 : 24
    if (W <= 640) return { x0:pad, x1:W - pad, y0:H * 0.58, y1:H * 0.86 }
    const left = W * 0.46
    return { x0:left, x1:W - pad, y0:H * 0.16, y1:H * 0.86 }
  }

  const land = feature(TOPO, TOPO.objects.countries)
  /* Antarctica is a third of the world's height and holds no research.  */
  const inhabited = { type:'FeatureCollection',
    features: land.features.filter(f => f.properties.name !== 'Antarctica') }

  const layouts = []
  let furniture = []

  /* Words and picture become one field.  */
  function placeCloud(out, copyPts, artPts, artBox){
    const total = copyPts.length + artPts.length
    if (!total) return false
    const forCopy = Math.round(dots.length * (copyPts.length / total))
    const takeAt = (arr, k, count) => arr[Math.min(arr.length - 1,
      Math.floor(k * (arr.length / Math.max(1, count))))]
    for (let i = 0; i < dots.length; i++){
      const c = dots[i].kind === 'project' ? TEAL : YELLOW
      if (i < forCopy && copyPts.length){
        const q = takeAt(copyPts, i, forCopy)
        out[i] = { x:q[0], y:q[1], c, r:1.5, a:0 }
      } else if (artPts.length){
        const q = takeAt(artPts, i - forCopy, dots.length - forCopy)
        out[i] = artBox
          ? { x:artBox.x + q[0] * artBox.kx, y:artBox.y + q[1] * artBox.ky, c, r:1.5, a:0 }
          : { x:q[0], y:q[1], c, r:1.5, a:0 }
      } else {
        const q = takeAt(copyPts, i, dots.length)
        out[i] = { x:q[0], y:q[1], c, r:1.5, a:0 }
      }
    }
    return true
  }
  /* Which series fold 2 is showing.  */
  function buildLayout(kind, chartId, beatIndex = 0){
    const b = fieldBox(), bw = b.x1 - b.x0, bh = b.y1 - b.y0
    const out = new Array(dots.length)
    const rnd = mulberry(1234)

    /* `park` marks a dot this fold has no use for at all.  */
    const hidden = i => ({
      x:b.x0 + ((i * 17) % Math.max(1, Math.floor(bw))), y:b.y1 + 24,
      c:GREY, r:.6, a:0, park:true,
    })
    const scatter = (entityKind, colour = () => GREY, radius = () => 1.6) => {
      for (let i = 0; i < dots.length; i++){
        if (dots[i].kind !== entityKind){ out[i] = hidden(i); continue }
        out[i] = { x:b.x0 + rnd() * bw, y:b.y0 + rnd() * bh,
                   c:colour(dots[i]), r:radius(dots[i]) }
      }
    }

    if (kind === 'chartBlank'){
      /* Only the opening network needs a particle target. Other charts cross-fade as SVG. */
      if (beatIndex === 0){
        const pts = chartId ? charts.sample(chartId) : []
        const box = chartBox()
        const svg = chartViewBox(chartId)
        const fitted = { x:box.x, y:box.y, kx:svg ? box.w / svg.w : 1, ky:svg ? box.h / svg.h : 1 }
        if (placeCloud(out, sampleCopy(beatIndex), pts, fitted)) return { pos:out, furn:null }
      }
      for (let i = 0; i < dots.length; i++) out[i] = hidden(i)
      return { pos:out, furn:null }
    }
    if (kind === 'projectScatter'){
      scatter('project')
      return { pos:out, furn:null }
    }
    else if (kind === 'projectYears'){
      /* Both series, per year, as dots.  */
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

      /* A square grid, sized so the tallest column fills the height and the dots very nearly touch.  */
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
      /* How much of the EQ family has reached each country.  */
      /* The world is about twice as wide as it is tall, and the field is not, so width always binds and the map is left floating in the middle of the box with dead air above and below.  */
      const proj = geoNaturalEarth1().fitWidth(b.x1 - b.x0, inhabited)
      const fitted = geoPath(proj).bounds(inhabited)
      const mapH = fitted[1][1] - fitted[0][1]
      const STRIP_H = 5 * 12 + 30              // five rows and the caption
      // Map and strip travel together as one block, centred in the field, so the space the map cannot use is shared above and below rather than all dumped underneath it.
      const top = b.y0 + Math.max(0, (bh - mapH - STRIP_H) / 2)
      const tr = proj.translate()
      proj.translate([tr[0] + (b.x0 - fitted[0][0]), tr[1] + (top - fitted[0][1])])
      /* The projection preserves the world's aspect ratio, so it never fills the box: it leaves a band above and below.  */
      const mapBox = geoPath(proj).bounds(inhabited)
      const per = {}
      for (const [c, set] of Object.entries(familyIn))
        per[c] = ESTABLISHED.filter(([, short]) => set.has(short)).length
      const centroid = {}
      for (const f of inhabited.features){
        const c = geoPath(proj).centroid(f)
        if (!isNaN(c[0])) centroid[f.properties.name] = c
      }
      // The strip under the map: how many countries each version has reached. 
      const reach = FAMILY.map(([, short, , note]) => ({ short, note, n:familyReach[short].size }))
      /* The map has to come apart like every other fold, and it is drawn on the canvas rather than in SVG, so there is no chart to read.  */
      const shaded = inhabited.features.filter(f => per[f.properties.name])
      const mapPts = []
      const PITCH = 5.4
      for (const feat of shaded){
        const bb = geoPath(proj).bounds(feat)
        for (let y = bb[0][1]; y <= bb[1][1]; y += PITCH)
          for (let x = bb[0][0]; x <= bb[1][0]; x += PITCH){
            const ll = proj.invert([x, y])
            if (ll && geoContains(feat, ll)) mapPts.push([x, y])
          }
      }
      if (!placeCloud(out, sampleCopy(beatIndex), mapPts, null))
        for (let i = 0; i < dots.length; i++) out[i] = hidden(i)

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

  /* ── the intro ─────────────────────────────────────────────────────── */
  /* Drawn to an offscreen canvas and sampled into the same data dots, so the words become the research field. */
  const INTRO_TEXT = 'A knowledge graph of EuroQol-funded research'
  let textSpots = null
  const instEl = root.querySelector('[data-instrument]')

  /* The globe is not transformed by the story any more.  */

  const ctaEl  = root.querySelector('[data-cta]')
  const subEl  = root.querySelector('[data-sub]')
  const scopeEl = root.querySelector('[data-scope]')
  const heroKickerEl = root.querySelector('[data-hero-kicker]')

  function buildText(){
    const off = document.createElement('canvas')
    off.width = W; off.height = H
    const o = off.getContext('2d')
    o.clearRect(0, 0, W, H)
    const pad = W > 900 ? 48 : 24
    /* The headline, sized by the room it actually has.  */
    const byWidth  = W * 0.052
    const byHeight = H * 0.092
    const fs = Math.max(30, Math.min(96, byWidth, byHeight))
    o.font = `500 ${fs}px 'Instrument Sans', 'Helvetica Neue', sans-serif`
    o.fillStyle = ink(1); o.textAlign = 'left'; o.textBaseline = 'middle'
    const words = INTRO_TEXT.split(' '); const lines = []; let line = ''
    for (const w of words){
      const t = line ? line + ' ' + w : w
      if (o.measureText(t).width > W * 0.53 && line){ lines.push(line); line = w } else line = t
    }
    if (line) lines.push(line)
    const lh = fs * 0.98
    let y = H * 0.16
    if (heroKickerEl) heroKickerEl.style.top = Math.max(78, Math.round(y - 34)) + 'px'
    lines.forEach(l => { o.fillText(l, pad, y + lh / 2); y += lh })

    const textW = Math.max(...lines.map(l => o.measureText(l).width))

    const d = o.getImageData(0, 0, W, H).data, cand = []
    for (let py = 0; py < H; py += 4) for (let px = 0; px < W; px += 4)
      if (d[(py * W + px) * 4 + 3] > 130) cand.push([px, py])
    const step = cand.length / dots.length
    textSpots = dots.map((_, i) => cand[Math.min(cand.length - 1, (i * step) | 0)] || [W / 2, H / 2])
    // where the words actually finish, so the buttons can sit under them
    const bottom = H * 0.16 + lines.length * lh
    // The line under the headline, then the buttons under that. 
    if (subEl) subEl.style.top = Math.round(bottom + fs * 0.24) + 'px'
    const subH = subEl ? subEl.offsetHeight : 0
    if (scopeEl) scopeEl.style.top = Math.round(bottom + fs * 0.24 + subH + fs * 0.18) + 'px'
    const scopeH = scopeEl ? scopeEl.offsetHeight : 0
    if (ctaEl) ctaEl.style.top = Math.round(bottom + fs * 0.24 + subH + fs * 0.18 + scopeH + fs * 0.28) + 'px'
    // Below 640px the CTA stacks into three rows (instead of wrapping mid-row), so the globe
    // is parked wherever that block actually ends rather than at a guessed percentage.
    if (instEl){
      if (W <= 640 && ctaEl) instEl.style.top = Math.round(parseFloat(ctaEl.style.top) + ctaEl.offsetHeight + fs * 0.6) + 'px'
      else instEl.style.top = ''
    }
    return { lines, lh, fs, pad, bottom, textW, img:off, font:o.font }
  }
  let textMeta = null

  /* The words do not fade while a layer of dots sits on top of them — that reads as dust on the type.  */
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

            /* Do not multiply by the home alpha.  */
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
    // Carries the whole fold now that the dots are hidden, so it is stronger than a wash. 
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
      if (alpha > .5) liveYears = f
      const focusYear = hoverYear
      if (focusYear >= 0 && focusYear < f.years.length){
        const x = f.b.x0 + focusYear * f.colW
        ctx.fillStyle = `rgba(${TEAL[0]},${TEAL[1]},${TEAL[2]},.055)`
        ctx.fillRect(x, f.b.y0, f.colW, f.b.y1 - f.b.y0)
        ctx.strokeStyle = `rgba(${TEAL[0]},${TEAL[1]},${TEAL[2]},.42)`
        ctx.strokeRect(x + .5, f.b.y0 + .5, Math.max(1, f.colW - 1), Math.max(1, f.b.y1 - f.b.y0 - 1))
      }
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

        /* The key draws the two marks rather than naming their colours, so it is read in the same form as the chart it explains. */
        const ky = f.b.y0 + 8
        ctx.fillStyle = `rgba(${TEAL[0]},${TEAL[1]},${TEAL[2]},.95)`
        ctx.beginPath(); ctx.arc(f.b.x0 + 4, ky, 2.6, 0, 6.283); ctx.fill()
        ctx.fillStyle = ink(.62); ctx.textAlign = 'left'
        ctx.fillText('funded projects', f.b.x0 + 13, ky)
        const w = ctx.measureText('funded projects').width + 34
        ctx.fillStyle = `rgba(${YELLOW[0]},${YELLOW[1]},${YELLOW[2]},.95)`
        ctx.beginPath(); ctx.arc(f.b.x0 + w, ky, 2.6, 0, 6.283); ctx.fill()
        ctx.fillStyle = ink(.62)
        ctx.fillText('published studies', f.b.x0 + w + 9, ky)
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

      // Every country first, as the quietest possible ground. 
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

          /* Measured, tested against every box already placed, and dropped if it still overlaps after four candidate positions.  */
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

      /* The strip under the map.  */
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
      ctx.font = `500 15px 'Instrument Sans', sans-serif`
      let x = f.b.x0
      let y = f.b.y1 + 22
      for (const entry of f.entries){
        const width = Math.max(112, ctx.measureText(entry.label).width + 38)
        if (x > f.b.x0 && x + width > f.b.x1){ x = f.b.x0; y += 24 }
        ctx.beginPath(); ctx.arc(x + 4, y, 4, 0, 6.283)
        ctx.fillStyle = `rgba(${entry.colour[0]},${entry.colour[1]},${entry.colour[2]},.92)`
        ctx.fill()
        ctx.fillStyle = ink(.58)
        ctx.fillText(entry.label, x + 16, y)
        x += width
      }
    }
    ctx.restore()
  }

  /* ── draw ────────────────────────────────────────────────────────── */
  function drawBeat(index){
    const span = BEATS.length - 1
    const layout = layouts[index]
    if (!layout) return

    ctx.clearRect(0, 0, W, H)

    const paintLayout = (points, furn) => {
      drawAreaFill(furn, 1)
      for (const point of points){
        if (point.park === true) continue
        const c = point.c
        const a = point.a == null ? .85 : point.a
        ctx.beginPath()
        ctx.arc(point.x, point.y, point.r, 0, 6.283)
        ctx.fillStyle = `rgba(${c[0]|0},${c[1]|0},${c[2]|0},${a})`
        ctx.fill()
      }
      drawFurniture(furn, 1)
    }

    liveMap = null
    liveYears = null
    if (!BEATS[index].chart) paintLayout(layout, furniture[index])

    /* `.sh-field` is pointer-events:none, so this canvas has to claim the pointer itself — and only while a map is drawn, or it covers the globe. */
    canvas.style.pointerEvents = liveMap || liveYears ? 'auto' : 'none'
    canvas.style.cursor = liveMap ? 'pointer' : liveYears ? 'crosshair' : ''
    if (!liveYears && dataTip){
      dataTip.hidden = true
      hoverYear = -1
    }

    root.querySelectorAll('[data-dots] button').forEach((d, i) => {
      d.classList.toggle('on', i === index)
      if (i === index) d.setAttribute('aria-current', 'step')
      else d.removeAttribute('aria-current')
    })
    const cur = root.querySelector('[data-current]')
    if (cur) cur.textContent = String(index + 1).padStart(2, '0')

    // the blooms drift with the story rather than on a timer
    const p = span ? index / span : 0
    const g = root.querySelector('[data-glow]')
    g.children[0].style.transform = `translate3d(${(12 - p * 34)}vw, ${(6 + p * 10)}vh, 0)`
    g.children[1].style.transform = `translate3d(${(58 - p * 26)}vw, ${(44 - p * 18)}vh, 0)`
  }

  /* ── native scrollytelling ───────────────────────────────────────── */
  const scroller = root.querySelector('[data-scroll]')
  const fieldEl = root.querySelector('.sh-field')
  const stepEls = [...stepsHost.querySelectorAll('[data-step]')]
  const endEl = stepsHost.querySelector('[data-story-end]')
  const controlsEl = root.querySelector('.sh-controls')
  const dotsEl = root.querySelector('[data-dots]')
  const reducedMotion = () => window.matchMedia('(prefers-reduced-motion: reduce)').matches
  let activeBeat = 0
  let ticking = false

  /* One step owns one visual. Its entry and exit each use about 40% of a viewport. */
  const TIMELINE = Object.freeze({
    visualInEnd:.42,
    visualOutStart:.58,
    copyInEnd:.22,
    copyOutStartY:.12,
    copyOutEndY:-.05,
    interactiveAt:.72,
  })
  const clamp01 = value => Math.max(0, Math.min(1, value))

  function setInert(element, inactive){
    element?.toggleAttribute('inert', Boolean(inactive))
  }

  function publishState(phase, beat, progress = 0){
    root.dataset.storyPhase = phase
    root.dataset.storyBeat = String(beat + 1)
    root.dataset.storyTransition = progress.toFixed(3)
    setInert(controlsEl, phase !== 'step')
    setInert(dotsEl, phase !== 'step')
    setInert(endEl, phase !== 'end')
  }

  function updateStepControls(beat, atEnd = false){
    const buttons = root.querySelectorAll('.sh-step button')
    if (buttons[0]) buttons[0].disabled = !atEnd && beat <= 0
    if (buttons[1]) buttons[1].disabled = atEnd
  }

  function copyState(copy, progress, stays = false){
    if (reducedMotion()) return { opacity:1, y:0 }
    const enter = ease(clamp01(progress / TIMELINE.copyInEnd))
    const top = copy?.getBoundingClientRect().top || 0
    const exitStart = window.innerHeight * TIMELINE.copyOutStartY
    const exitEnd = window.innerHeight * TIMELINE.copyOutEndY
    const leave = stays ? 1 : ease(clamp01((top - exitEnd) / (exitStart - exitEnd)))
    return {
      opacity:Math.min(enter, leave),
      y:(1 - enter) * 14,
    }
  }

  function setCopyState(index = -1, progress = 0, atEnd = false){
    stepEls.forEach((step, stepIndex) => {
      const copy = step.querySelector('.sh-copy')
      if (!copy) return
      const active = !atEnd && stepIndex === index
      const state = copyState(copy, progress)
      copy.style.opacity = active ? state.opacity.toFixed(3) : '0'
      copy.style.transform = active ? `translate3d(0, ${state.y.toFixed(2)}px, 0)` : 'none'
    })
    const endCopy = endEl?.querySelector('.sh-copy')
    if (endCopy){
      const state = copyState(endCopy, progress, true)
      endCopy.style.opacity = atEnd ? state.opacity.toFixed(3) : '0'
      endCopy.style.transform = atEnd ? `translate3d(0, ${state.y.toFixed(2)}px, 0)` : 'none'
    }
  }

  function visualOpacity(index, progress){
    if (reducedMotion()) return 1
    const enter = index === 0
      ? 1
      : ease(clamp01(progress / TIMELINE.visualInEnd))
    const leave = 1 - ease(clamp01(
      (progress - TIMELINE.visualOutStart) / (1 - TIMELINE.visualOutStart),
    ))
    return Math.min(enter, leave)
  }

  function setOpeningVisibility(t){
    const openA = Math.max(0, 1 - Math.max(0, (t - .42) / .34)).toFixed(3)
    const copyA = Math.max(0, 1 - Math.max(0, (t - .08) / .40)).toFixed(3)
    if (instEl){ instEl.style.opacity = openA; instEl.style.pointerEvents = +openA > .35 ? '' : 'none' }
    if (ctaEl){
      ctaEl.style.opacity = copyA
      ctaEl.style.pointerEvents = +copyA > .5 ? '' : 'none'
      setInert(ctaEl, +copyA <= .5)
    }
    if (heroKickerEl) heroKickerEl.style.opacity = copyA
    if (subEl) subEl.style.opacity = copyA
    if (scopeEl) scopeEl.style.opacity = copyA
  }

  function renderIntro(t){
    setOpeningVisibility(t)
    if (fieldEl) fieldEl.style.opacity = '1'
    drawIntro(t)
    charts.show(null, 0)
    chartHost.style.opacity = '0'
    stepEls.forEach(step => step.classList.remove('is-active'))
    endEl?.classList.remove('is-active')
    setCopyState()
    updateStepControls(0)
    publishState('intro', 0, t)
  }

  function renderStoryStep(index, progress){
    const next = Math.max(0, Math.min(BEATS.length - 1, index))
    const position = clamp01(progress)
    const opacity = visualOpacity(next, position)
    const chart = BEATS[next].chart
    activeBeat = next
    setOpeningVisibility(1)
    drawBeat(next)
    charts.show(chart, opacity)
    chartHost.style.opacity = chart ? opacity.toFixed(3) : '0'
    if (fieldEl) fieldEl.style.opacity = chart ? '0' : opacity.toFixed(3)
    if (opacity < TIMELINE.interactiveAt) canvas.style.pointerEvents = 'none'
    setCopyState(next, position)
    stepEls.forEach((step, i) => step.classList.toggle('is-active', i === next))
    endEl?.classList.remove('is-active')
    updateStepControls(next)
    publishState('step', next, position)
  }

  function renderEnd(progress){
    const t = clamp01(progress)
    activeBeat = BEATS.length - 1
    setOpeningVisibility(1)
    ctx.clearRect(0, 0, W, H)
    charts.show(null, 0)
    chartHost.style.opacity = '0'
    if (fieldEl) fieldEl.style.opacity = '0'
    canvas.style.pointerEvents = 'none'
    setCopyState(-1, t, true)
    stepEls.forEach(step => {
      step.classList.remove('is-active')
    })
    endEl?.classList.add('is-active')
    updateStepControls(activeBeat, true)
    publishState('end', activeBeat, t)
  }

  function syncToScroll(){
    ticking = false
    const vh = window.innerHeight
    const local = -scroller.getBoundingClientRect().top
    const introEnd = vh * .44
    if (local < introEnd){
      renderIntro(Math.max(0, Math.min(1, local / introEnd)))
      return
    }

    const trigger = window.scrollY + vh * .56
    const tops = stepEls.map(step => step.getBoundingClientRect().top + window.scrollY)
    const endTop = endEl ? endEl.getBoundingClientRect().top + window.scrollY : Infinity
    if (!tops.length) return

    /* Each panel supplies one complete and reversible story timeline. */
    for (let index = 0; index < stepEls.length; index++){
      const nextTop = index < stepEls.length - 1 ? tops[index + 1] : endTop
      if (trigger >= nextTop) continue
      const span = Math.max(1, nextTop - tops[index])
      const position = Math.max(0, Math.min(1, (trigger - tops[index]) / span))
      renderStoryStep(index, position)
      return
    }

    const endSpan = Math.max(1, (endEl?.getBoundingClientRect().height || vh) * .5)
    renderEnd((trigger - endTop) / endSpan)
  }

  function scheduleSync(){
    if (ticking) return
    ticking = true
    requestAnimationFrame(() => syncToScroll())
  }

  /* The observer supplies one stable activation band. Geometry resolves fast jumps. */
  const observer = new IntersectionObserver(scheduleSync, {
    root:null,
    rootMargin:'-54% 0px -45% 0px',
    threshold:0,
  })
  stepEls.forEach(step => observer.observe(step))
  if (endEl) observer.observe(endEl)

  function storyYForBeat(index){
    const safeIndex = Math.max(0, Math.min(stepEls.length - 1, index))
    const step = stepEls[safeIndex]
    const top = step.getBoundingClientRect().top + window.scrollY
    const next = safeIndex < stepEls.length - 1 ? stepEls[safeIndex + 1] : endEl
    const nextTop = next
      ? next.getBoundingClientRect().top + window.scrollY
      : top + step.getBoundingClientRect().height
    const centre = top + (nextTop - top) * .5
    return Math.max(0, centre - window.innerHeight * .56)
  }

  function scrollTo(target){
    window.scrollTo({ top:target, behavior:reducedMotion() ? 'auto' : 'smooth' })
  }

  function goToBeat(index){
    if (index >= BEATS.length && endEl){
      const top = endEl.getBoundingClientRect().top + window.scrollY
      scrollTo(top)
      return
    }
    scrollTo(storyYForBeat(index))
  }

  if (size()) syncToScroll()
  root.querySelectorAll('[data-dots] button').forEach((button, i) => {
    button.addEventListener('click', () => goToBeat(i))
  })
  window.addEventListener('scroll', scheduleSync, { passive:true })

  let rz
  const onResize = () => {
    clearTimeout(rz)
    rz = setTimeout(() => { if (size()) syncToScroll() }, 180)
  }
  window.addEventListener('resize', onResize)

  const api = {
    goToBeat,
    jumpToExplorer(){
      if (!endEl) return
      const top = endEl.getBoundingClientRect().top + window.scrollY
      window.scrollTo(0, top)
      syncToScroll()
    },
    goHome(){
      const top = scroller.getBoundingClientRect().top + window.scrollY
      window.scrollTo(0, top)
      syncToScroll()
    },
    currentBeat(){ return activeBeat },
    scrollTo,
    state:() => ({
      phase:root.dataset.storyPhase,
      beat:Number(root.dataset.storyBeat || 1),
      transition:Number(root.dataset.storyTransition || 0),
    }),
    refresh(){
      if (size()) syncToScroll()
    },
    destroy(){
      destroyed = true
      cancelAnimationFrame(sizeRetry)
      observer.disconnect()
      clearTimeout(rz)
      charts.destroy()
      teaser?.destroy()
      ghost.stop()
      endObserver?.disconnect()
      window.removeEventListener('scroll', scheduleSync)
      window.removeEventListener('resize', onResize)
      delete root.__story
    },
  }
  root.__story = api
  return api
}
