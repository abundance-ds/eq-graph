/*
  The landing page's window onto the graph.

  A real excerpt of the people lens (app/lib/graphTeaser.json, written by
  scripts/build-graph-scene.mjs) turned slowly on a 2-D canvas, drawn the way
  /graph draws: pencil hairlines multiplied onto paper, small colour discs
  with a paper rim, everything fading toward the paper with depth.
*/
import data from './graphTeaser.json'

const HUES = ['#0f7a6b', '#2f6db5', '#a8720d', '#b5567f', '#5c4fb3', '#3d8f5f', '#c9633a', '#5f6b78']
const NEUTRAL = '#9a9a92'
const PAPER = [252, 252, 251]
const PENCIL = [107, 107, 100]
const TURN = 0.11            // radians per second when left alone
const EYE = 150              // camera distance in layout units

const rgb = hexColour => [1, 3, 5].map(i => parseInt(hexColour.slice(i, i + 2), 16))
const clamp01 = v => Math.max(0, Math.min(1, v))
const mix = (a, b, t) => Math.round(a + (b - a) * t)

export function initGraphTeaser(canvas, options = {}) {
  const host = options.host || canvas.parentElement
  const ctx = canvas.getContext('2d')
  const reduced = typeof matchMedia === 'function' && matchMedia('(prefers-reduced-motion: reduce)').matches
  const nodes = data.nodes.map(n => ({
    x: n.p[0], y: n.p[1], z: n.p[2], s: n.s,
    colour: rgb(n.c == null || n.c >= HUES.length ? NEUTRAL : HUES[n.c]),
  }))
  const links = data.links
  const radius = nodes.reduce((max, n) => Math.max(max, Math.hypot(n.x, n.y, n.z)), 1)
  const projected = new Float32Array(nodes.length * 4)  // x, y, near (0 far … 1 near), scale
  const order = nodes.map((_, i) => i)

  let width = 0
  let height = 0
  let yaw = 0.7
  const pitch = -0.34
  let aimYaw = 0
  let aimPitch = 0
  let curYaw = 0
  let curPitch = 0
  let hoverAim = 0
  let hover = 0
  let visible = false
  let raf = 0
  let last = 0
  let destroyed = false

  function resize() {
    const rect = host.getBoundingClientRect()
    width = Math.round(rect.width)
    height = Math.round(rect.height)
    const dpr = Math.min(window.devicePixelRatio || 1, 2)
    canvas.width = Math.max(1, Math.round(width * dpr))
    canvas.height = Math.max(1, Math.round(height * dpr))
    ctx.setTransform(dpr, 0, 0, dpr, 0, 0)
    draw()
  }

  /* Rotate, then look at the cloud from a little way off so depth shows. */
  function project() {
    const cy = Math.cos(yaw + curYaw)
    const sy = Math.sin(yaw + curYaw)
    const cp = Math.cos(pitch + curPitch)
    const sp = Math.sin(pitch + curPitch)
    const unit = Math.min(width * 0.42, height * 0.8) / radius
    const cx = width * 0.62
    const cyPx = height * 0.5
    for (let i = 0; i < nodes.length; i++) {
      const n = nodes[i]
      const x1 = n.x * cy + n.z * sy
      const z1 = -n.x * sy + n.z * cy
      const y2 = n.y * cp - z1 * sp
      const z2 = n.y * sp + z1 * cp
      const f = EYE / (EYE - z2)
      const o = i * 4
      projected[o] = cx + x1 * unit * f
      projected[o + 1] = cyPx - y2 * unit * f
      projected[o + 2] = clamp01(0.5 + z2 / (radius * 1.6))
      projected[o + 3] = f
    }
    order.sort((a, b) => projected[a * 4 + 2] - projected[b * 4 + 2])
  }

  /* Soft edges, so the excerpt sits in the card instead of being cut by it. */
  function edgeFade(x, y) {
    const fx = clamp01(Math.min(x, width - x) / (width * 0.16))
    const fy = clamp01(Math.min(y, height - y) / (height * 0.24))
    return fx * fx * (3 - 2 * fx) * fy * fy * (3 - 2 * fy)
  }

  function draw() {
    if (!width || !height) return
    project()
    ctx.clearRect(0, 0, width, height)
    const lift = 1 + hover * 0.45

    ctx.globalCompositeOperation = 'multiply'
    ctx.lineCap = 'round'
    for (let i = 0; i < links.length; i++) {
      const a = links[i][0] * 4
      const b = links[i][1] * 4
      const near = (projected[a + 2] + projected[b + 2]) / 2
      const fade = Math.min(edgeFade(projected[a], projected[a + 1]), edgeFade(projected[b], projected[b + 1]))
      const alpha = (0.08 + 0.26 * near) * lift * fade
      if (alpha < 0.01) continue
      ctx.strokeStyle = `rgba(${PENCIL[0]},${PENCIL[1]},${PENCIL[2]},${alpha.toFixed(3)})`
      ctx.lineWidth = 0.5 + 0.5 * near
      ctx.beginPath()
      ctx.moveTo(projected[a], projected[a + 1])
      ctx.lineTo(projected[b], projected[b + 1])
      ctx.stroke()
    }

    ctx.globalCompositeOperation = 'source-over'
    for (let k = 0; k < order.length; k++) {
      const i = order[k]
      const o = i * 4
      const x = projected[o]
      const y = projected[o + 1]
      const near = projected[o + 2]
      const fade = edgeFade(x, y)
      if (fade < 0.02) continue
      const r = (0.9 + nodes[i].s * 3.4) * projected[o + 3]
      const fog = (1 - near) * 0.6
      const c = nodes[i].colour
      const alpha = (0.55 + 0.45 * near) * fade
      ctx.fillStyle = `rgba(${PAPER[0]},${PAPER[1]},${PAPER[2]},${(alpha * 0.9).toFixed(3)})`
      ctx.beginPath()
      ctx.arc(x, y, r + 1.1, 0, Math.PI * 2)
      ctx.fill()
      ctx.fillStyle = `rgba(${mix(c[0], PAPER[0], fog)},${mix(c[1], PAPER[1], fog)},${mix(c[2], PAPER[2], fog)},${alpha.toFixed(3)})`
      ctx.beginPath()
      ctx.arc(x, y, r, 0, Math.PI * 2)
      ctx.fill()
    }
  }

  function frame(now) {
    raf = 0
    if (destroyed || !visible) return
    const dt = Math.min(0.05, (now - (last || now)) / 1000)
    last = now
    const k = 1 - Math.exp(-dt * 4)
    curYaw += (aimYaw - curYaw) * k
    curPitch += (aimPitch - curPitch) * k
    hover += (hoverAim - hover) * k
    if (!reduced) yaw += TURN * dt * (1 + hover * 0.6)
    draw()
    const settled = reduced && Math.abs(aimYaw - curYaw) < 1e-3 && Math.abs(aimPitch - curPitch) < 1e-3 && Math.abs(hoverAim - hover) < 1e-3
    if (!settled) raf = requestAnimationFrame(frame)
  }

  function wake() {
    if (!raf && visible && !destroyed && !document.hidden) { last = 0; raf = requestAnimationFrame(frame) }
  }

  function onPointerMove(ev) {
    const rect = host.getBoundingClientRect()
    aimYaw = ((ev.clientX - rect.left) / Math.max(1, rect.width) - 0.5) * 0.5
    aimPitch = ((ev.clientY - rect.top) / Math.max(1, rect.height) - 0.5) * 0.28
    wake()
  }
  function onPointerEnter() { hoverAim = 1; wake() }
  function onPointerLeave() { hoverAim = 0; aimYaw = 0; aimPitch = 0; wake() }
  function onVisibility() { if (document.hidden) { cancelAnimationFrame(raf); raf = 0 } else wake() }

  const intersection = new IntersectionObserver(entries => {
    visible = entries.some(entry => entry.isIntersecting)
    if (visible) wake()
  }, { threshold: 0.05 })
  intersection.observe(host)
  const resizer = new ResizeObserver(resize)
  resizer.observe(host)
  host.addEventListener('pointermove', onPointerMove)
  host.addEventListener('pointerenter', onPointerEnter)
  host.addEventListener('pointerleave', onPointerLeave)
  document.addEventListener('visibilitychange', onVisibility)
  resize()

  return {
    destroy() {
      destroyed = true
      cancelAnimationFrame(raf)
      intersection.disconnect()
      resizer.disconnect()
      host.removeEventListener('pointermove', onPointerMove)
      host.removeEventListener('pointerenter', onPointerEnter)
      host.removeEventListener('pointerleave', onPointerLeave)
      document.removeEventListener('visibilitychange', onVisibility)
    },
  }
}
