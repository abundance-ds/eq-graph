/* ═══════════════════════════════════════════════════════════════════
   THE GLOBE — where the research actually happened.

   The first thing on the page, present from the moment it loads. Every
   country EuroQol-funded research has run in, lit in proportion to how much
   of it. The data sets the counts, rank, and labels at run time.

   Orthographic projection on a canvas, turning slowly. Land is a faint
   outline; the lit countries are filled and haloed, so the shape you see is
   the reach of the portfolio rather than a decorative planet.
   ═══════════════════════════════════════════════════════════════════ */
import { geoOrthographic, geoPath, geoGraticule10, geoBounds, geoContains,
         geoCentroid, geoDistance } from 'd3-geo'
import { feature } from 'topojson-client'

const NAME_FIX = {
  'United States':'United States of America', 'Czech Republic':'Czechia',
  'Trinidad And Tobago':'Trinidad and Tobago', 'Dominican Republic':'Dominican Rep.',
  'Bosnia And Herzegovina':'Bosnia and Herz.', 'South Korea':'South Korea',
}

const rgb = (css, name, fallback) => {
  const v = css.getPropertyValue(name).trim()
  const parts = (v || fallback).split(',').map(Number)
  return parts.length === 3 && parts.every(n => Number.isFinite(n)) ? parts.join(',') : fallback
}

export function initGlobe(canvas, DATA, TOPO){
  const ctx = canvas.getContext('2d')

  /* Colour comes from the CSS token block, never from here — that is what
     makes a light theme a change of tokens rather than a second globe. */
  const css = window.getComputedStyle(canvas)
  const LIT  = rgb(css, '--globe-lit-rgb', '124,246,222')
  const LAND = rgb(css, '--globe-land-rgb', '150,214,200')
  const PIN  = rgb(css, '--globe-pin-rgb', '198,255,240')
  const INK  = rgb(css, '--ink-rgb', '244,244,242')
  const GROUND = rgb(css, '--ground-rgb', '0,0,0')
  const BODY = [rgb(css, '--globe-body', '18,52,48'),
                rgb(css, '--globe-body-mid', '6,20,19'),
                rgb(css, '--globe-body-far', '3,10,10')]
  const BODY_A = (css.getPropertyValue('--globe-body-a').trim() || '.72')
  // A hairline that reads on black is nearly invisible on paper. One number,
  // set per theme, scales the outlines rather than forking the drawing.
  const LB = Number(css.getPropertyValue('--globe-line-boost').trim()) || 1
  const la = a => Math.min(1, a * LB).toFixed(3)
  const DPR = Math.min(2, window.devicePixelRatio || 1)
  let W = 0, H = 0

  const land = feature(TOPO, TOPO.objects.countries)

  // studies per country, from the real CONDUCTED_IN edges
  const byName = {}
  const nodeById = Object.fromEntries(DATA.nodes.map(n => [n.id, n]))
  for (const e of DATA.edges){
    if (e.type !== 'CONDUCTED_IN') continue
    const n = nodeById[e.target]
    if (n) byName[n.label] = (byName[n.label] || 0) + 1
  }
  const counts = {}
  for (const [k, v] of Object.entries(byName)) counts[NAME_FIX[k] || k] = v
  const max = Math.max(...Object.values(counts), 1)

  const lit = land.features.filter(f => counts[f.properties.name])
  lit.sort((a, b) => counts[a.properties.name] - counts[b.properties.name])

  const proj = geoOrthographic().clipAngle(90).rotate([-10, -16])
  const path = geoPath(proj, ctx)
  const grat = geoGraticule10()

  // a lon/lat box per lit country, so hit-testing is two polygon tests a
  // frame instead of a hundred and seventeen
  const boxes = lit.map(f => ({ f, b: geoBounds(f), c: geoCentroid(f),
                                n: counts[f.properties.name] }))
  // biggest first, so when pins compete for room the loudest country wins
  const byCount = [...boxes].sort((a, b) => b.n - a.n)

  let tmx = 0, tmy = 0, mx = 0, my = 0
  let park = 0                       // scroll parallax
  let hover = null                   // the country under the cursor
  let drag = null, autoResume = 0    // drag-to-spin
  let live = true                    // is the globe on screen and grabbable
  let active = true                  // false while the chat cockpit owns the page
  let rot = [-10, -16]               // the live rotation
  let pin = 0, pinTo = 0.5           // how strongly the pins are showing
  let last = 0                       // for time-based spin

  function frame(){
    if (!active){ raf = 0; return }
    const now = performance.now()
    const dt = Math.min(0.05, last ? (now - last) / 1000 : 0.016); last = now
    // A gentle, constant turn — five and a half degrees a second, a full
    // rotation in about a minute. Timed in seconds, not frames, so it turns
    // at the same rate on a 120Hz screen as on a 60Hz one.
    if (!drag && now > autoResume) rot[0] -= dt * SPIN
    pin += (pinTo - pin) * Math.min(1, dt * 7)
    mx += (tmx - mx) * 0.05; my += (tmy - my) * 0.05
    proj.rotate(rot)
    ctx.clearRect(0, 0, W, H)

    // lower in the frame, and drifting — the parallax you asked for
    const cx = W * 0.70 + mx * 26
    const cy = H * 0.58 + my * 16 + park * 74
    proj.translate([cx, cy])
    const R = proj.scale()

    // once the globe has faded out it must stop swallowing the pointer
    const vis = +(canvas.parentNode.style.opacity || 1) > 0.12
    if (vis !== live){ live = vis; canvas.style.pointerEvents = vis ? 'auto' : 'none'
                       if (!vis){ px = py = null; setHover(null) } }

    // the sphere: a dark glass ball with a teal rim
    ctx.beginPath(); path({ type:'Sphere' })
    const body = ctx.createRadialGradient(cx - R * .35, cy - R * .4, R * .1, cx, cy, R)
    body.addColorStop(0, `rgba(${BODY[0]},${BODY_A})`)
    body.addColorStop(.72, `rgba(${BODY[1]},${BODY_A})`)
    body.addColorStop(1, `rgba(${BODY[2]},${BODY_A})`)
    ctx.fillStyle = body; ctx.fill()

    // graticule, very faint — it reads as a measuring instrument
    ctx.beginPath(); path(grat)
    ctx.strokeStyle = `rgba(${LIT},${la(.08)})`; ctx.lineWidth = 0.6; ctx.stroke()

    // every country, as a thin outline
    ctx.beginPath(); path(land)
    ctx.strokeStyle = `rgba(${LAND},${la(.20)})`; ctx.lineWidth = 0.55; ctx.stroke()

    // the ones with research in them, lit by how much
    for (const f of lit){
      const t = Math.pow(counts[f.properties.name] / max, 0.45)
      const on = hover && hover.properties.name === f.properties.name
      ctx.beginPath(); path(f)
      ctx.fillStyle = on ? `rgba(${PIN},.94)`
                         : `rgba(${LIT},${(0.14 + t * 0.60).toFixed(3)})`
      ctx.fill()
      ctx.strokeStyle = on ? `rgba(${INK},1)`
                           : `rgba(${LIT},${(0.22 + t * 0.5).toFixed(3)})`
      ctx.lineWidth = on ? 1.6 : 0.6 + t * 0.7
      ctx.stroke()
    }

    // ── what is under the cursor, recomputed every frame so it keeps up
    //    with the rotation rather than only updating when you move
    if (px !== null){
      const dxp = px - cx, dyp = py - cy
      const near = dxp * dxp + dyp * dyp <= (R + 30) * (R + 30)
      if (!drag) pinTo = near ? 0.85 : 0.5
      let found = null
      if (dxp * dxp + dyp * dyp <= R * R){
        const ll = proj.invert([px, py])
        if (ll){
          const [lo, la] = ll
          for (const bx of boxes){
            const [[w, s0], [e, n0]] = bx.b
            if (la < s0 - 1 || la > n0 + 1) continue
            const inLon = w <= e ? (lo >= w - 1 && lo <= e + 1) : (lo >= w - 1 || lo <= e + 1)
            if (!inLon) continue
            if (geoContains(bx.f, ll)){ found = bx; break }
          }
        }
      }
      setHover(found)
    }

    /* ── the pins ────────────────────────────────────────────────────
       Every country facing you carries a small card: its name, and how many
       studies were funded there. They are placed biggest-first and any card
       that would land on one already placed is dropped — a card sitting on
       another card is worse than a missing one — so the ones you see are
       always the loudest countries in view. Turn the globe and the set
       changes with it. */
    if (pin > 0.01){
      const centre = [-rot[0], -rot[1]]
      const placed = []
      let cards = 0
      for (const bx of byCount){
        const d = geoDistance(bx.c, centre)
        if (d > 1.30) continue                       // round the back, or on the limb
        const p = proj(bx.c); if (!p) continue
        const edge = Math.min(1, (1.30 - d) / 0.30)  // fades in away from the rim
        const on = hover && hover.properties.name === bx.f.properties.name
        const a = pin * edge
        if (a < 0.04) continue

        // the pin itself
        ctx.beginPath(); ctx.arc(p[0], p[1], on ? 3.4 : 2, 0, 6.283)
        ctx.fillStyle = `rgba(${PIN},${(a * (on ? 1 : .85)).toFixed(3)})`
        ctx.fill()

        const cardLimit = W <= 640 ? 4 : 8
        if (cards >= cardLimit && !on) continue

        // the card
        const name = bx.f.properties.name
        const fs = W <= 640 ? 10.5 : 12
        ctx.font = `500 ${fs}px 'Instrument Sans', 'Helvetica Neue', sans-serif`
        const nw = ctx.measureText(name).width
        ctx.font = `500 ${fs}px 'IBM Plex Mono', ui-monospace, monospace`
        const vw = ctx.measureText(String(bx.n)).width
        const cw = nw + vw + (W <= 640 ? 21 : 26), ch = W <= 640 ? 21 : 24
        // upper right of the pin, flipping left when it would run off
        const flip = p[0] + 12 + cw > W - 8
        const bx0 = flip ? p[0] - 12 - cw : p[0] + 12
        const by0 = p[1] - 12 - ch
        // Mobile labels need more air than their exact bounds. Without this
        // reserved gap, two cards can be mathematically separate but read as
        // one crowded label on the small globe.
        const cardGap = W <= 640 ? 10 : 3
        const r = [bx0 - cardGap, by0 - cardGap, cw + cardGap * 2, ch + cardGap * 2]
        if (!on && placed.some(q => r[0] < q[0] + q[2] && r[0] + r[2] > q[0] &&
                                    r[1] < q[1] + q[3] && r[1] + r[3] > q[1])) continue
        placed.push(r); cards++

        ctx.beginPath(); ctx.moveTo(p[0], p[1])
        ctx.lineTo(flip ? bx0 + cw : bx0, by0 + ch)
        ctx.strokeStyle = `rgba(${LIT},${(a * .5).toFixed(3)})`
        ctx.lineWidth = 1; ctx.stroke()

        ctx.beginPath()
        if (ctx.roundRect) ctx.roundRect(bx0, by0, cw, ch, 4)
        else ctx.rect(bx0, by0, cw, ch)
        ctx.fillStyle = `rgba(${GROUND},${(a * .88).toFixed(3)})`
        ctx.fill()
        ctx.strokeStyle = `rgba(${LIT},${(a * (on ? .95 : .45)).toFixed(3)})`
        ctx.lineWidth = 1; ctx.stroke()

        ctx.textBaseline = 'middle'; ctx.textAlign = 'left'
        ctx.font = `500 ${fs}px 'Instrument Sans', 'Helvetica Neue', sans-serif`
        ctx.fillStyle = `rgba(${INK},${a.toFixed(3)})`
        ctx.fillText(name, bx0 + 9, by0 + ch / 2 + .5)
        ctx.font = `500 ${fs}px 'IBM Plex Mono', ui-monospace, monospace`
        ctx.fillStyle = `rgba(${LIT},${a.toFixed(3)})`
        ctx.fillText(String(bx.n), bx0 + 9 + nw + 8, by0 + ch / 2 + .5)
      }
    }

    // rim light around the limb
    ctx.beginPath(); ctx.arc(cx, cy, R, 0, 6.283)
    ctx.strokeStyle = `rgba(${LIT},${la(.40)})`; ctx.lineWidth = 1.1; ctx.stroke()
    ctx.beginPath(); ctx.arc(cx, cy, R + 1.5, 0, 6.283)
    ctx.strokeStyle = `rgba(${LIT},${la(.13)})`; ctx.lineWidth = 5; ctx.stroke()

    raf = requestAnimationFrame(frame)
  }

  let raf = 0
  function size(){
    W = canvas.clientWidth; H = canvas.clientHeight
    if (!W || !H) return
    canvas.width = W * DPR; canvas.height = H * DPR
    ctx.setTransform(DPR, 0, 0, DPR, 0, 0)
    // big — most of the fold — but never so big it runs off the bottom
    proj.scale(Math.min(H * 0.40, W * 0.29)).translate([W / 2, H / 2])
  }

  const onWindowPointerMove = ev => {
    tmx = (ev.clientX / window.innerWidth - 0.5)
    tmy = (ev.clientY / window.innerHeight - 0.5)
  }
  window.addEventListener('pointermove', onWindowPointerMove, { passive: true })

  /* Hover is what brightens a country and its card; there is no separate
     DOM tooltip any more, because two things saying the same number is one
     thing too many. */
  let px = null, py = null          // cursor, in canvas pixels
  function setHover(bx){ hover = bx ? bx.f : null }

  const onCanvasPointerMove = ev => {
    const r = canvas.getBoundingClientRect()
    px = ev.clientX - r.left; py = ev.clientY - r.top
    if (drag){
      // hold it and turn it — 0.28° of globe per pixel of cursor
      rot[0] = drag.r0 + (px - drag.x) * 0.28
      rot[1] = Math.max(-78, Math.min(78, drag.r1 - (py - drag.y) * 0.28))
    }
  }
  const onCanvasPointerLeave = () => { px = py = null; pinTo = 0.5; setHover(null) }
  canvas.addEventListener('pointermove', onCanvasPointerMove)
  canvas.addEventListener('pointerleave', onCanvasPointerLeave)

  const onCanvasPointerDown = ev => {
    const r = canvas.getBoundingClientRect()
    drag = { x: ev.clientX - r.left, y: ev.clientY - r.top, r0: rot[0], r1: rot[1] }
    canvas.setPointerCapture(ev.pointerId)
    canvas.classList.add('is-dragging')
    pinTo = 1
  }
  canvas.addEventListener('pointerdown', onCanvasPointerDown)
  const release = () => {
    if (!drag) return
    drag = null
    canvas.classList.remove('is-dragging')
    autoResume = performance.now() + 1100   // a beat of stillness, then it drifts on
  }
  canvas.addEventListener('pointerup', release)
  canvas.addEventListener('pointercancel', release)

  /* Keep the render loop for pointer interaction. Stop only the automatic
     turn when the operating system requests reduced motion. */
  const SPIN = window.matchMedia('(prefers-reduced-motion: reduce)').matches ? 0 : 5.5

  /* The stage is pinned, so nothing on it moves as you scroll. Sinking the
     globe a little while the words leave gives the fold its depth — it lags
     behind the type instead of being stapled to it. */
  const onScroll = () => {
    park = Math.max(0, Math.min(1, window.scrollY / (window.innerHeight * 1.6)))
  }
  window.addEventListener('scroll', onScroll, { passive: true })

  size()
  raf = requestAnimationFrame(frame)

  let rz
  const onResize = () => { clearTimeout(rz); rz = setTimeout(size, 200) }
  window.addEventListener('resize', onResize)

  return {
    facts(){ return { countries: Object.keys(counts).length, top: Object.entries(counts).sort((a,b)=>b[1]-a[1])[0] } },
    setParallax(p){ park = p },
    setActive(next){
      active = Boolean(next)
      if (!active){
        cancelAnimationFrame(raf)
        raf = 0
        return
      }
      last = 0
      size()
      if (!raf) raf = requestAnimationFrame(frame)
    },
    destroy(){
      active = false
      cancelAnimationFrame(raf)
      clearTimeout(rz)
      window.removeEventListener('pointermove', onWindowPointerMove)
      window.removeEventListener('scroll', onScroll)
      window.removeEventListener('resize', onResize)
      canvas.removeEventListener('pointermove', onCanvasPointerMove)
      canvas.removeEventListener('pointerleave', onCanvasPointerLeave)
      canvas.removeEventListener('pointerdown', onCanvasPointerDown)
      canvas.removeEventListener('pointerup', release)
      canvas.removeEventListener('pointercancel', release)
    },
  }
}
