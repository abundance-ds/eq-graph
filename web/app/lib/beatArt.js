/* ═══════════════════════════════════════════════════════════════════
   BEAT ART — the object behind each beat.

   One abstract form per beat, sitting behind the dot field: turned, lit
   from one side, grey, and quiet. It is scenery, not a chart — the numbers
   are always the dots in front of it — but it is never arbitrary either.
   Each form is the beat's subject as an object:

     stack    funded studies      layers that accumulate into a body of work
     bars     over time           a span of years, lit where the funding ran
     sphere   countries           the world, as rings of latitude
     rings    working groups      circles of people, overlapping, unequal
     plates   publications        sheets seen edge-on, a literature stacked
     lattice  the web             everything joined to everything

   Everything is drawn from gradients and single strokes rather than fills,
   because a flat grey shape reads as a hole in the page while a lit edge
   reads as a surface. Alpha stays low by design: at full strength it would
   compete with the data, and the data has to win.
   ═══════════════════════════════════════════════════════════════════ */

const TAU = Math.PI * 2

/* One lit disc, seen at a shallow angle. The gradient across it is what
   makes it read as a surface catching light rather than a grey ellipse. */
function disc(ctx, cx, cy, rx, ry, ink, a, hot){
  ctx.save()
  ctx.beginPath(); ctx.ellipse(cx, cy, rx, ry, 0, 0, TAU)
  const g = ctx.createLinearGradient(cx - rx, cy - ry, cx + rx, cy + ry)
  g.addColorStop(0,   `rgba(${ink},${(a * 0.02).toFixed(3)})`)
  g.addColorStop(0.42,`rgba(${ink},${(a * 0.11).toFixed(3)})`)
  g.addColorStop(0.62,`rgba(${ink},${(a * 0.05).toFixed(3)})`)
  g.addColorStop(1,   `rgba(${ink},${(a * 0.015).toFixed(3)})`)
  ctx.fillStyle = g; ctx.fill()

  // the rim: bright along the lit side, gone along the other
  ctx.beginPath(); ctx.ellipse(cx, cy, rx, ry, 0, Math.PI * 0.75, Math.PI * 1.85)
  ctx.strokeStyle = `rgba(${ink},${(a * (hot ? 0.5 : 0.26)).toFixed(3)})`
  ctx.lineWidth = hot ? 1.5 : 1
  ctx.stroke()

  ctx.beginPath(); ctx.ellipse(cx, cy, rx, ry, 0, Math.PI * 1.9, Math.PI * 2.6)
  ctx.strokeStyle = `rgba(${ink},${(a * 0.08).toFixed(3)})`
  ctx.lineWidth = 1; ctx.stroke()
  ctx.restore()
}

export function drawBeatArt(ctx, kind, b, alpha, t, ink){
  if (alpha <= 0.008) return
  const bw = b.x1 - b.x0, bh = b.y1 - b.y0
  const cx = b.x0 + bw * 0.52, cy = b.y0 + bh * 0.48
  const S = Math.min(bw, bh)
  const a = alpha
  const drift = Math.sin(t * 0.22) * 0.5 + Math.sin(t * 0.13) * 0.5   // very slow

  ctx.save()

  if (kind === 'stack'){
    // three discs, held apart. Funding does not sit in one place; it stacks.
    const rx = S * 0.40, ry = rx * 0.30
    for (let i = 0; i < 3; i++){
      const y = cy + (i - 1) * S * 0.20 + drift * 5 * (i - 1)
      disc(ctx, cx, y, rx * (1 - i * 0.06), ry * (1 - i * 0.06), ink, a, i === 1)
    }
    // the light between them
    const g = ctx.createRadialGradient(cx, cy, 0, cx, cy, S * 0.42)
    g.addColorStop(0, `rgba(${ink},${(a * 0.07).toFixed(3)})`)
    g.addColorStop(1, `rgba(${ink},0)`)
    ctx.fillStyle = g
    ctx.beginPath(); ctx.ellipse(cx, cy, S * 0.42, S * 0.24, 0, 0, TAU); ctx.fill()
  }

  else if (kind === 'bars'){
    // a span of years. Tall where the funding ran, thin where it did not.
    const n = 7, w = S * 0.052, gap = S * 0.105
    const x0 = cx - (n - 1) * gap / 2
    const hs = [.34, .52, .78, 1, .86, .58, .40]
    for (let i = 0; i < n; i++){
      const x = x0 + i * gap
      const h = S * 0.52 * hs[i] * (1 + drift * 0.02)
      const g = ctx.createLinearGradient(x, cy - h / 2, x, cy + h / 2)
      g.addColorStop(0,  `rgba(${ink},${(a * 0.02).toFixed(3)})`)
      g.addColorStop(.5, `rgba(${ink},${(a * 0.13).toFixed(3)})`)
      g.addColorStop(1,  `rgba(${ink},${(a * 0.02).toFixed(3)})`)
      ctx.fillStyle = g
      ctx.beginPath()
      if (ctx.roundRect) ctx.roundRect(x - w / 2, cy - h / 2, w, h, w / 2)
      else ctx.rect(x - w / 2, cy - h / 2, w, h)
      ctx.fill()
      ctx.strokeStyle = `rgba(${ink},${(a * (i === 3 ? 0.34 : 0.14)).toFixed(3)})`
      ctx.lineWidth = 1; ctx.stroke()
      // the wick, the way a range is drawn
      ctx.beginPath()
      ctx.moveTo(x, cy - h / 2 - S * 0.05); ctx.lineTo(x, cy + h / 2 + S * 0.05)
      ctx.strokeStyle = `rgba(${ink},${(a * 0.10).toFixed(3)})`
      ctx.stroke()
    }
  }

  else if (kind === 'sphere'){
    // the world as rings of latitude, turning slowly
    const R = S * 0.36
    for (let i = -4; i <= 4; i++){
      const f = i / 4.6
      const rx = R * Math.sqrt(Math.max(0.02, 1 - f * f))
      const ry = rx * (0.16 + Math.abs(f) * 0.05)
      const y = cy + f * R
      ctx.beginPath(); ctx.ellipse(cx, y, rx, ry, 0, 0, TAU)
      ctx.strokeStyle = `rgba(${ink},${(a * (0.07 + 0.13 * (1 - Math.abs(f)))).toFixed(3)})`
      ctx.lineWidth = 1; ctx.stroke()
    }
    for (let i = 0; i < 6; i++){
      const ph = (i / 6) * Math.PI + t * 0.05
      const rx = Math.abs(Math.cos(ph)) * R
      ctx.beginPath(); ctx.ellipse(cx, cy, Math.max(1, rx), R, 0, 0, TAU)
      ctx.strokeStyle = `rgba(${ink},${(a * 0.07).toFixed(3)})`
      ctx.lineWidth = 1; ctx.stroke()
    }
    ctx.beginPath(); ctx.arc(cx, cy, R, 0, TAU)
    ctx.strokeStyle = `rgba(${ink},${(a * 0.30).toFixed(3)})`
    ctx.lineWidth = 1.2; ctx.stroke()
  }

  else if (kind === 'rings'){
    // circles of people. Unequal, overlapping, one much larger than the rest.
    const sizes = [1, .62, .5, .46, .4, .3, .18]
    const R = S * 0.30
    for (let i = 0; i < sizes.length; i++){
      const ang = (i / sizes.length) * TAU + t * 0.03
      const d = i === 0 ? 0 : R * 0.62
      const x = cx + Math.cos(ang) * d, y = cy + Math.sin(ang) * d * 0.6
      const r = R * sizes[i]
      const g = ctx.createRadialGradient(x - r * .3, y - r * .3, r * .1, x, y, r)
      g.addColorStop(0, `rgba(${ink},${(a * 0.055).toFixed(3)})`)
      g.addColorStop(1, `rgba(${ink},0)`)
      ctx.beginPath(); ctx.arc(x, y, r, 0, TAU)
      ctx.fillStyle = g; ctx.fill()
      ctx.strokeStyle = `rgba(${ink},${(a * (i === 0 ? 0.26 : 0.13)).toFixed(3)})`
      ctx.lineWidth = 1; ctx.stroke()
    }
  }

  else if (kind === 'plates'){
    // a literature, seen edge-on: thin sheets, the top one lit
    const n = 9, rx = S * 0.34, ry = rx * 0.17
    for (let i = n - 1; i >= 0; i--){
      const y = cy + (i - n / 2) * S * 0.045 + drift * 3
      const k = 1 - i / n
      ctx.beginPath(); ctx.ellipse(cx, y, rx * (0.72 + k * 0.28), ry, 0, 0, TAU)
      ctx.strokeStyle = `rgba(${ink},${(a * (0.06 + k * 0.22)).toFixed(3)})`
      ctx.lineWidth = i === 0 ? 1.4 : 1
      ctx.stroke()
    }
  }

  else if (kind === 'lattice'){
    // everything joined to everything, thinning as it goes out
    const R = S * 0.40, pts = []
    for (let i = 0; i < 22; i++){
      const ang = (i / 22) * TAU + t * 0.02
      const rr = R * (0.30 + ((i * 37) % 11) / 11 * 0.7)
      pts.push([cx + Math.cos(ang) * rr, cy + Math.sin(ang) * rr * 0.74])
    }
    for (let i = 0; i < pts.length; i++)
      for (let j = i + 1; j < pts.length; j++){
        const d = Math.hypot(pts[i][0] - pts[j][0], pts[i][1] - pts[j][1])
        if (d > R * 0.62) continue
        ctx.beginPath(); ctx.moveTo(pts[i][0], pts[i][1]); ctx.lineTo(pts[j][0], pts[j][1])
        ctx.strokeStyle = `rgba(${ink},${(a * 0.09 * (1 - d / (R * 0.62))).toFixed(3)})`
        ctx.lineWidth = 1; ctx.stroke()
      }
    for (const p of pts){
      ctx.beginPath(); ctx.arc(p[0], p[1], 2.2, 0, TAU)
      ctx.fillStyle = `rgba(${ink},${(a * 0.20).toFixed(3)})`; ctx.fill()
    }
  }

  ctx.restore()
}
