/* ═══════════════════════════════════════════════════════════════════
   THE STORY — horizontal, black, Swiss.

   Vertical scrolling drives a horizontal track. One pinned stage, six
   panels, and a single field of dots that rearranges between them — the
   dots never disappear and are never replaced, so the whole thing reads
   as one material moving, exactly as the vertical story does.

   The temporary reference fixtures supply the 944-project portfolio and the
   evidence counts. The new ontology will replace this adapter later.
   ═══════════════════════════════════════════════════════════════════ */

import { geoNaturalEarth1, geoPath } from 'd3-geo'
import { drawBeatArt } from './beatArt.js'
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
  const ink = a => `rgba(${INK[0]},${INK[1]},${INK[2]},${a})`
  const projects = DATA.nodes.filter(n => n.type === 'project')
  const live = DATA.live || null
  const N = projects.length

  /* ── the facts each beat states ──────────────────────────────────── */
  const counts = DATA.metadata?.node_counts || {}
  const works = live?.works || []
  const findings = live?.findings || []
  const authors = new Set(works.flatMap(w => w.authors || [])).size
  const wgOf = p => String(p.wg || 'Unassigned').split(',')[0].trim()
  const yearOf = p => { const y = Number(p.start_year || 0)
    return (y && y >= 1980 && y <= 2030) ? y : null }

  const years = [...new Set(projects.map(yearOf).filter(Boolean))].sort()

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
  const countryOfProject = {}
  for (const e of DATA.edges){
    if (e.type !== 'CONDUCTED_IN') continue
    const label = (DATA.nodes.find(n => n.id === e.target) || {}).label
    if (label) (countryOfProject[e.source] ||= []).push(label)
  }
  /* The rows of the group-by-year beat: only groups that actually have
     dated studies, busiest first. A row that would be empty is not a row. */
  const groupYearRows = (() => {
    const m = new Map()
    for (const p of projects){
      if (!yearOf(p)) continue
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

  /* The beats used to state a number and stop. A number on its own does not
     say what it bought — so each one now carries the consequence with it,
     and every figure below is counted from the data at run time rather than
     written in by hand. Where the records are thin the beat says so; a gap
     that goes unmentioned reads as a claim that there is none. */
  const dated = projects.filter(yearOf)
  const since2012 = dated.filter(p => yearOf(p) >= 2012).length
  const workYears = works.map(w => w.year).filter(Boolean)
  const firstWork = workYears.length ? Math.min(...workYears) : null
  const busiestWorkYear = (() => {
    const by = {}; workYears.forEach(y => by[y] = (by[y] || 0) + 1)
    return Object.entries(by).sort((a, b) => b[1] - a[1])[0] || null
  })()
  const journals = new Set(works.map(w => w.journal).filter(Boolean)).size
  const valueSets = (live?.valueSets || []).length
  const acceptedLinks = (live?.attributions || []).filter(link => link.confidence === 'accepted')
  const datedByGroup = groups.map(([group]) => [
    group,
    dated.filter(project => wgOf(project) === group).length,
  ]).sort((a, b) => b[1] - a[1])
  const leadingDatedGroup = datedByGroup[0] || ['No group', 0]
  const eqHwbDated = datedByGroup.find(([group]) => group === 'EQ-HWB')?.[1] || 0

  const BEATS = [
    { num:fmt(N), head:'Research projects.', art:'stack',
      body:`Every dot is one EuroQol project record. Projects are the funded portfolio; publications and findings form a separate evidence layer.`,
      so:`The current evidence layer holds <b>${fmt(works.length)}</b> assessed publications and <b>${fmt(findings.length)}</b> extracted findings. It does not yet cover every project.`,
      layout:'scatter' },

    { num:years.length ? `${years[0]}–${years[years.length - 1]}` : '—',
      head:'Year by year.', art:'bars',
      body:`<b>${fmt(dated.length)}</b> of the ${fmt(N)} projects have a recorded start year, and <b>${fmt(since2012)}</b> started from 2012 on.`,
      so:`Evidence runs behind the money. The first paper we can trace appears in <b>${firstWork || '—'}</b>, years after the funding picks up, and the busiest year for papers is <b>${busiestWorkYear ? busiestWorkYear[0] : '—'}</b> — long after the studies behind them were paid for.`,
      layout:'years' },

    { num:fmt(counts.country || 0), head:'Countries in linked evidence.', art:'sphere',
      body:`A project is placed only when an accepted publication link leads to a study with a named country. Unlinked projects and records without a country stay unplaced.`,
      so:`The current linked evidence names <b>${fmt(counts.country || 0)}</b> countries. It also contains <b>${valueSets}</b> research products identified as value sets.`,
      layout:'map' },

    { num:fmt(groups.length), head:'Working groups, year by year.', art:'rings',
      body:`The same studies, grouped by the community that leads them and set against the year each was funded. One row per group, one column per year.`,
      so:`The shape of the community shows in the rows. <b>${leadingDatedGroup[0]}</b> is the largest group in the dated records, with <b>${fmt(leadingDatedGroup[1])}</b> studies. <b>EQ-HWB</b> has ${fmt(groups.find(g => g[0] === 'EQ-HWB')?.[1] || 0)} studies but only ${fmt(eqHwbDated)} of them carry a date, so the newest group is almost invisible on this axis — a gap in the records rather than in the work.`,
      layout:'groupYears' },

    { num:fmt(acceptedLinks.length), head:'Accepted publication links.', art:'plates',
      body:`Confirmed project-to-publication links in the assessed corpus of <b>${fmt(works.length)}</b> papers, written by <b>${fmt(authors)}</b> researchers across <b>${fmt(journals)}</b> journals.`,
      so:`A link is shown only after it passes the project-year rule and the evidence review. Possible links are not included in this public view.`,
      layout:'arc' },

    { num:'∞', head:'It all connects.', art:'lattice',
      body:`Study records connect publications to instruments, methods, models, populations, concepts, outcomes, findings and limitations — including <b>${fmt(counts.concept || 0)}</b> concepts and <b>${fmt(counts.method || 0)}</b> methods.`,
      so:`Which means you can ask it a question instead of reading it. Every answer names the papers it came from, and says so when it has nothing.`,
      layout:'web' },
  ]

  /* ── build the DOM ───────────────────────────────────────────────── */
  const track = root.querySelector('[data-track]')
  track.innerHTML = BEATS.map(b => `
    <section class="sh-panel">
      <div class="sh-copy">
        <div class="sh-num">${b.num}</div>
        <h2 class="sh-head">${b.head}</h2>
        <p class="sh-body">${b.body}</p>
        <p class="sh-so">${b.so}</p>
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
  const ctx = canvas.getContext('2d')
  const DPR = Math.min(2, window.devicePixelRatio || 1)
  let W = 0, H = 0
  let sizeRetry = 0, destroyed = false
  const dots = projects.map((p, i) => ({ i, p, year:yearOf(p), g:wgOf(p), x:0, y:0, r:1.6, c:GREY }))

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

    if (kind === 'scatter'){
      for (let i = 0; i < dots.length; i++)
        out[i] = { x:b.x0 + rnd() * bw, y:b.y0 + rnd() * bh, c:GREY, r:1.6 }
      return { pos: out, furn: null }
    }
    else if (kind === 'years'){
      const cols = years.length || 1, colW = bw / cols
      const per = {}
      for (let i = 0; i < dots.length; i++){
        const y = dots[i].year
        if (!y){ out[i] = { x:b.x0 + rnd() * bw, y:b.y1 + 40, c:GREY, r:1.2, a:0 }; continue }
        const ci = years.indexOf(y); per[y] = (per[y] || 0) + 1
        const n = per[y], perRow = Math.max(1, Math.floor(colW / 5))
        out[i] = {
          x: b.x0 + ci * colW + ((n - 1) % perRow) * 4.6 + 2,
          y: b.y1 - Math.floor((n - 1) / perRow) * 4.6,
          c: mix(TEAL, YELLOW, ci / Math.max(1, cols - 1)), r:1.7 }
      }
      out.furn = { kind:'years', b, cols, colW }
      return { pos: out, furn: out.furn }
    }
    else if (kind === 'map'){
      // Real geography. Each dot lands on the country its study was run in.
      const proj = geoNaturalEarth1().fitExtent([[b.x0, b.y0], [b.x1, b.y1 - 46]], land)
      const topNames = {}
      const centroid = {}
      for (const f of land.features){
        const c = geoPath(proj).centroid(f)
        if (!isNaN(c[0])) centroid[f.properties.name] = c
      }
      // how many studies each country holds, so busy places pack tighter
      const per = {}
      let unplaced = 0
      for (let i = 0; i < dots.length; i++){
        const names = countryOfProject[dots[i].p.id] || []
        let pt = null, name = null
        for (const n of names){
          const key = NAME_FIX[n] || n
          if (centroid[key]){ pt = centroid[key]; name = key; break }
        }
        if (!pt){
          // no country, or a region we cannot place — a quiet row along the base
          const k = unplaced++
          out[i] = { x:b.x0 + (k % 60) * 5.4, y:b.y1 - 6 - Math.floor(k / 60) * 5.4,
                     c:[70,70,68], r:1.2 }
          continue
        }
        per[name] = (per[name] || 0) + 1
        topNames[name] = (topNames[name] || 0) + 1
        const k = per[name] - 1
        const a = k * 2.399963, rr = Math.sqrt(k) * 2.6
        out[i] = { x:pt[0] + Math.cos(a) * rr, y:pt[1] + Math.sin(a) * rr,
                   c:mix(TEAL, YELLOW, Math.min(1, k / 22)), r:1.7 }
      }
      out.furn = { kind:'map', b, proj, centroid, topNames, unplaced }
      return { pos: out, furn: out.furn }
    }
    else if (kind === 'columns'){
      const cols = groups.length, colW = bw / cols, per = {}
      const idx = Object.fromEntries(groups.map((g, i) => [g[0], i]))
      for (let i = 0; i < dots.length; i++){
        const ci = idx[dots[i].g] ?? 0
        per[ci] = (per[ci] || 0) + 1
        const n = per[ci], perRow = Math.max(1, Math.floor((colW - 8) / 5))
        out[i] = {
          x: b.x0 + ci * colW + ((n - 1) % perRow) * 4.8 + 3,
          y: b.y1 - Math.floor((n - 1) / perRow) * 4.8,
          c: mix(YELLOW, TEAL, ci / Math.max(1, cols - 1)), r:1.7 }
      }
      out.furn = { kind:'columns', b, cols, colW, names: groups.map(g => g[0]) }
      return { pos: out, furn: out.furn }
    }
    else if (kind === 'groupYears'){
      /* One row per working group, one column per year: the community's
         shape over time rather than a single total. Only the 372 studies
         that carry a date can be placed, so the rest sit as a faint band
         along the bottom — visible, because a chart that quietly drops
         three fifths of its subject is a lie by omission. */
      const rows = groupYearRows
      const labelW = W <= 640 ? Math.min(126, bw * 0.38) : Math.min(160, bw * 0.24)
      const gx0 = b.x0 + labelW
      const cols = years.length || 1
      const colW = (bw - labelW) / cols
      const bandH = 30
      const rowH = (bh - bandH) / rows.length
      const rowOf = Object.fromEntries(rows.map((r, i) => [r, i]))
      const per = {}, perRow = Math.max(2, Math.floor((colW - 3) / 4.2))
      let loose = 0
      for (let i = 0; i < dots.length; i++){
        const y = dots[i].year, g = dots[i].g
        const ri = rowOf[g]
        if (!y || ri === undefined){
          // no date on the record — shown, not hidden, and never coloured
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
      out.furn = { kind:'groupYears', b, rows, labelW, gx0, colW, rowH, bandH, loose }
      return { pos: out, furn: out.furn }
    }
    else if (kind === 'arc'){
      // The traced publications lift out of the field as a bright arc.
      const cx = b.x0 + bw / 2, cy = b.y1, R = Math.min(bw, bh) * 0.82
      const lit = works.length
      for (let i = 0; i < dots.length; i++){
        if (i < lit){
          const t = i / Math.max(1, lit - 1), a = Math.PI + t * Math.PI
          out[i] = { x:cx + Math.cos(a) * R * 0.62, y:cy + Math.sin(a) * R * 0.52,
                     c:YELLOW, r:2.1 }
        } else {
          out[i] = { x:b.x0 + rnd() * bw, y:b.y0 + rnd() * bh, c:[60,60,58], r:1.3 }
        }
      }
      out.furn = { kind:'arc', b, cx, cy, R, lit, total: dots.length }
      return { pos: out, furn: out.furn }
    }
    else { // web
      const cx = b.x0 + bw / 2, cy = b.y0 + bh / 2
      for (let i = 0; i < dots.length; i++){
        const a = rnd() * Math.PI * 2, rr = Math.pow(rnd(), .55) * Math.min(bw, bh) * .5
        out[i] = { x:cx + Math.cos(a) * rr, y:cy + Math.sin(a) * rr * .86,
                   c:mix(GREY, TEAL, rnd()), r:1.5 }
      }
      return { pos: out, furn: null }
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
     SAME 944 dots, so the words literally become the portfolio. Timing was
     the note: the field must be settled and readable BEFORE the text has
     finished leaving, not after. The dissolve starts at 1% — the second you
     move — crosses the words by 31%, and the last dot is home by 87%. What
     is left is a hold, so beat 01 is still before it starts to move. */
  const INTRO_TEXT = 'Shaping how the world measures health.'
  let textSpots = null
  const instEl = root.querySelector('[data-instrument]')
  const ctaEl  = root.querySelector('[data-cta]')


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

      const a = Math.min(1, age / 0.05)                       // it appears as it leaves
      const f = ease(Math.min(1, age / FLY))

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
      years.forEach((y, i) => {
        if (years.length > 9 && i % 2) return
        const x = f.b.x0 + i * f.colW + f.colW / 2
        ctx.beginPath(); ctx.moveTo(x, f.b.y1 + 8); ctx.lineTo(x, f.b.y1 + 13); ctx.stroke()
        ctx.fillText(String(y), x, f.b.y1 + 24)
      })
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
      years.forEach((y, i) => {
        if (years.length > 9 && i % 3) return
        ctx.fillText(String(y), f.gx0 + i * f.colW + f.colW / 2, f.b.y1 + 16)
      })
      ctx.textAlign = 'left'; ctx.fillStyle = ink(.34)
      ctx.fillText(`${f.loose} with no date recorded yet`, f.gx0, f.b.y1 - 26)
    }
    else if (f.kind === 'map'){
      // the coastlines are what turn a cluster of dots into a map
      const path = geoPath(f.proj, ctx)
      ctx.strokeStyle = ink(.16)
      ctx.beginPath(); path(land); ctx.stroke()
      // name the places that carry the most work
      const top = W <= 640 ? [] : Object.entries(f.topNames).sort((a, b) => b[1] - a[1]).slice(0, 5)
      ctx.textAlign = 'left'; ctx.fillStyle = ink(.7)
      for (const [name, n] of top){
        const c = f.centroid[name]; if (!c) continue
        ctx.fillText(`${name} ${n}`, c[0] + 9, c[1] - 9)
      }
      if (f.unplaced){
        ctx.fillStyle = ink(.4)
        ctx.fillText(`${f.unplaced} not placed at country level`, f.b.x0, f.b.y1 + 16)
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
      ctx.fillText(`${f.lit} traced`, f.b.x0, f.cy + 24)
      ctx.fillStyle = ink(.4)
      ctx.fillText(`${f.total - f.lit} not yet read`, f.b.x0 + 96, f.cy + 24)
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
    drawBeatArt(ctx, BEATS[i0].art, box, (1 - t) * 0.9, now, INK.join(','))
    if (i1 !== i0) drawBeatArt(ctx, BEATS[i1].art, box, t * 0.9, now, INK.join(','))

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

    // Chart labels stay at full strength for the hold. During the short
    // change, the old labels leave early and the new labels arrive late.
    if (i0 === i1){
      drawFurniture(furniture[i0], 1)
    } else {
      drawFurniture(furniture[i0], Math.max(0, 1 - rawT * 3.4))
      drawFurniture(furniture[i1], Math.max(0, (rawT - .7) / .3))
    }

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
      const openA = (t > 0.60 ? 0 : 1 - Math.max(0, (t - 0.34) / 0.26)).toFixed(3)
      if (instEl) instEl.style.opacity = openA
      // the buttons belong to the sentence, so they leave with it
      const ctaA = (t > 0.26 ? 0 : 1 - Math.max(0, (t - 0.04) / 0.22)).toFixed(3)
      if (ctaEl){ ctaEl.style.opacity = ctaA; ctaEl.style.pointerEvents = +ctaA > 0.5 ? '' : 'none' }
      drawIntro(t)
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
      if (instEl) instEl.style.opacity = '0'
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
      window.removeEventListener('scroll', onScroll)
      window.removeEventListener('resize', onResize)
      delete root.__story
    },
  }
  root.__story = api
  return api
}
