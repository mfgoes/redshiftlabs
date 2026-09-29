# Redshift Labs style guide

The visual system behind the Redshift Labs site: dark and editorial, with one warm accent and a technical second voice. It is written so it can be lifted into another project, such as a personal UX portfolio. The site's source of truth is the "Studio site layer" section at the end of [`css/kosmograd.css`](css/kosmograd.css). Its behaviour lives in [`js/site.js`](js/site.js).

---

## 1. Principles

1. **One accent, used sparingly.** Red marks what matters: the primary action, the active state, a rule that fills on hover. If everything is red, nothing is.
2. **Two voices.** A humanist sans (Onest) says things. A mono (JetBrains Mono) *labels* things: dates, tags, roles, counters. Never swap their jobs.
3. **Hairlines, not boxes.** Structure comes from 1px rules and spacing. Filled, bordered cards are kept for things you can click.
4. **Texture over flatness.** Film grain, a vignette and a faint glow stop large dark areas from looking like a default template.
5. **Motion confirms, it doesn't perform.** Hover states grow, nudge or fill. Nothing bounces or loops for attention, except one small "live" detail per page.
6. **Respect reduced motion.** Every animation is off under `prefers-reduced-motion`, and content never depends on JS to be visible.

---

## 2. Colour

### Surfaces (darkest to lightest)
| Token | Value | Use |
|---|---|---|
| `--void` | `#0a0d10` | Page background, default sections, footer |
| `--void-raised` | `#12171c` | Alternating sections |
| `--panel` | `#171d23` | Cards, trailer slot |

Alternate `void` and `void-raised` between sections. Don't put two raised sections next to each other.

### Lines
| Value | Use |
|---|---|
| `#1a2025` | Section dividers |
| `#232a30` (`--line`) | Card borders, footer and nav hairlines |
| `#2e363c` | Open-column top rules (USPs, team) |
| `#3a4248` | Tag outlines, card border on hover |
| `#4a5157` | Secondary button border |

### Text
| Value | Use |
|---|---|
| `#ffffff` | Hero titles, button text |
| `#f2f3f3` | Headings |
| `#aab3b8` (`--text`) | Body copy, ledes |
| `#97a3a9` | Card body copy |
| `#8f9aa0` | Nav links, notes, footer links |
| `#7f8b91` | Metadata |
| `#5d686e` | Faintest (copyright) |

### Accent and signal
| Value | Use |
|---|---|
| `#c6312f` (`--accent`) | Primary buttons, rules, active dot, selection. Taken from the logo |
| `#e5544f` (`--accent-bright`) | Accent **text** and icons on dark (better contrast than the base red) |
| `#a92826` | Primary button hover |
| `#7fb8e6` | Secondary strand: research and writing, anything that is *not* the main product |
| `#6fcf8e` | "Live / nominal" status dot only |

The secondary blue exists to say "this is a different kind of thing". It separates research from the game devlog. In a portfolio, use it the same way: case studies get the accent, side writing or experiments get the secondary colour.

---

## 3. Typography

```html
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500&family=Onest:wght@400;500;600;700;800&display=swap" rel="stylesheet">
```

| Role | Font | Size | Weight | Tracking | Line height |
|---|---|---|---|---|---|
| Display (product name) | Onest, UPPERCASE | `clamp(3rem, 10vw, 6.5rem)` | 800 | `.02em` | `.95` |
| Page title (h1) | Onest | `clamp(2.6rem, 7.5vw, 5rem)` | 800 | `-.02em` | `1.02` |
| Section title (h2) | Onest | `clamp(1.7rem, 3.6vw, 2.5rem)` | 700 | `-.02em` | `1.15` |
| Card title (h3) | Onest | `1.2–1.35rem` | 700 | `-.02em` | default |
| Lede | Onest | `1.15rem` | 400 | 0 | `1.6` |
| Body | Onest | `1rem` | 400 | 0 | `1.7` |
| Label / eyebrow | JetBrains Mono, UPPERCASE | `.68–.75rem` | 500 | `.1–.14em` | default |

Rules:
- Big headings are tight (negative tracking). Small mono labels are loose (wide tracking). That contrast is most of the "designed" feel.
- Keep ledes to 40rem wide at most, and footer sign-offs to 16ch.
- One word in a big heading can take the accent (`Small games about big, <span>hostile places.</span>`), but only once per page.
- Use `font-variant-numeric: tabular-nums` for anything that ticks or counts.

**Eyebrow pattern:** a mono label with a short leading rule.
```css
.eyebrow { display: inline-flex; align-items: center; gap: .6rem;
  font: 500 .75rem/1 var(--mono); letter-spacing: .14em; text-transform: uppercase; color: var(--accent-bright); }
.eyebrow::before { content: ''; width: 1.5rem; height: 1px; background: currentColor; }
```

---

## 4. Space, shape, layout

- **Section padding:** `clamp(3.5rem, 8vw, 6rem)` top and bottom.
- **Container:** Bootstrap `.container` (max 1320px, 12px side gutter). Use `g-4 g-lg-5` on rows. A plain `g-5` causes horizontal scroll on phones.
- **Gaps:** cards `1.25rem`. Open columns `2rem 2.5rem`. Paired pillars `3rem 3.5rem`.
- **Radius:** `2px` everywhere. Almost square is the point, not pill-shaped.
- **Borders:** `1px` structure, and `2px` for accent rules.
- **Nav height:** `64px` (`--nav-h`). Sticky sub-navs sit at `top: var(--nav-h)`. Anchored sections use `scroll-margin-top: calc(var(--nav-h) + 3.5rem)`.
- **Grids:** 3 columns for cards and USPs, 2 columns for pillars, checklists and screenshots. Everything drops to 1 column below 768px.

---

## 5. Components

### Buttons
- **Primary:** accent fill, white text, and an arrow `→` that nudges 3px right on hover. **One per view.**
- **Secondary:** a translucent dark fill (`rgba(10,13,16,.35)`), `#4a5157` border and white text. On hover the border lightens to `#8a9299`.
- **Padding and weight:** `.75rem 1.4rem`, weight 600.
- **Never ship a disabled primary button** as a placeholder. Use a mono `.note` line under the buttons instead ("Steam page coming soon.").

### Clickable card
- Fill: `--panel` with a subtle top sheen (`linear-gradient(180deg, rgba(255,255,255,.025), transparent 60%)`).
- Border: `--line` at rest, `#3d464d` on hover. The card does **not** lift.
- On hover the title gets a 2px accent underline that grows from 0 to 100% (`background-size` transition, .35s), and a mono meta line that slides an arrow in from the left.
- **Wide image card:** image left, text right, and the image zooms 1.04× over 1.2s on hover.

### Open column (for features, team or principles; not clickable)
- No fill and no box. A 1px `#2e363c` top rule with a **2.5rem accent segment** that fills to 100% on hover (.5s).
- A mono counter in the top-right (`01`, `02`, `03`) via a CSS counter.
- Then an optional line icon (30px, 1.6 stroke, accent-bright), the heading and the body.

### Tags
Mono, uppercase, `.7rem`, a 1px `#3a4248` outline, and a faint dark fill so they sit over imagery.

### Numbered checklist
The same idea as open columns, as a list: a 1px top rule per item, a mono accent counter on the left, a bold title and a muted description.

### Live readout (the signature detail)
One small mono line of "live" state, with a status dot and a ticking value. It lives under the hero, separated by a 1px translucent rule. On the site it reads `● COLONISTS 3/3 · O₂ NOMINAL · DUST STORM IN 02:14`, and the storm clock counts down.
**For a portfolio:** keep the pattern and change the content, for example `● AVAILABLE FOR WORK · BASED IN HAARLEM · LOCAL TIME 14:02`, where the clock ticks.

### Navbar
- It is transparent over a hero and turns into `rgba(10,13,16,.82)` with a 12px backdrop blur and a hairline once the page scrolls past 40px.
- The active link gets a 4px accent dot below it, not an underline.
- The logo tilts `-8deg` on hover with a springy ease.
- Reserve the navbar's height so nothing jumps on load.

### Footer
A large sign-off line in 800 weight (one accent phrase), then a hairline row with the logo, links and a mono copyright.

### Hero
A full-bleed image behind three layers: a left-to-right darken for text legibility, a top-and-bottom fade, and a faint accent radial glow at the bottom edge. The image drifts slowly (`scale 1.02 → 1.1` over 40s, alternating). On phones, cut the image opacity to about 45%, since the side fade no longer protects the text.

### Lightbox
Use a native `<dialog>` with a blurred `rgba(5,7,9,.92)` backdrop and a mono caption. Clicking anywhere or pressing Esc closes it. Thumbnails use `cursor: zoom-in` and scale 1.03× on hover.

---

## 6. Texture

**Film grain:** a fixed overlay over every page at 5% opacity, pointer-events off.
```css
body::after {
  content: ''; position: fixed; inset: 0; z-index: 2000; pointer-events: none; opacity: .05;
  background-image: url("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='160' height='160'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='3' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E");
}
```
**Glow:** `radial-gradient(… rgba(198,49,47,.16–.22), transparent 60%)`, at the bottom of image heroes and the top-right of text-only heroes.

**Placeholder surfaces** (like the "trailer coming soon" slot): faint 135° diagonal hatching over `--panel`, with a mono label.

---

## 7. Motion

| What | Duration | Easing |
|---|---|---|
| Colour and border hovers | `.15–.2s` | `ease` |
| Title underline grow | `.35s` | `ease` |
| Accent rule fill | `.5s` | `cubic-bezier(.2,.8,.2,1)` |
| Scroll reveal (fade and 12px rise) | `.7s` | `cubic-bezier(.2,.8,.2,1)` |
| Image zoom on hover | `.8–1.2s` | `cubic-bezier(.2,.8,.2,1)` |
| Logo tilt | `.35s` | `cubic-bezier(.3,1.6,.5,1)` (spring) |
| Hero drift | `40s` alternate | `ease-in-out` |

- **Reveal:** items in a grid stagger by 60ms, up to 5 steps. Anything already on screen at load is not animated.
- **Hidden states are added by JS only,** so the page is complete without it.
- **Everything above is disabled** under `prefers-reduced-motion: reduce`, and smooth scrolling is only enabled when motion is allowed.

---

## 8. Details that add up
- `::selection` uses an accent background with white text.
- A thin dark scrollbar: `scrollbar-color: #2e363c var(--void)`.
- Focus ring: `outline: 2px solid var(--accent-bright); outline-offset: 3px`, on `:focus-visible` only.
- **A 404 page that stays in character** ("Lost on the Moon · ERROR 404 · SIGNAL LOST"), with two ways back.
- **A styled `console.log` greeting** with a genuine call to action (playtest, hire me).
- The favicon is the logo mark as SVG, with a `.ico` fallback.

---

## 9. Don'ts
- Pixel or novelty display fonts for UI text. The mono already carries the "technical" feel.
- Three identical bordered icon cards in a row. This is the most common template tell; use open columns.
- More than one primary button in a view, or a disabled button standing in for "coming soon".
- Cards that jump up on hover (`translateY`). Let the border and underline do the work.
- Pure black (`#000`) or pure grey backgrounds. The voids are slightly blue-green on purpose.
- Accent-coloured body text. The accent is for rules, labels and actions.
- Motion that runs without user intent, beyond the one live detail and the slow hero drift.

---

## 10. Portable token block

Drop this into a new project and swap `--accent` and `--accent-bright` for your own colour. Keep the bright variant about 15% lighter for text on dark.

```css
:root {
  /* Surfaces */
  --void: #0a0d10;
  --void-raised: #12171c;
  --panel: #171d23;
  /* Lines */
  --line: #232a30;
  --line-strong: #2e363c;
  /* Text */
  --heading: #f2f3f3;
  --text: #aab3b8;
  --muted: #7f8b91;
  /* Accent */
  --accent: #c6312f;
  --accent-bright: #e5544f;
  --accent-hover: #a92826;
  --secondary: #7fb8e6;
  /* Type */
  --sans: 'Onest', -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  --mono: 'JetBrains Mono', ui-monospace, SFMono-Regular, Menlo, monospace;
  /* Layout */
  --nav-h: 64px;
  --radius: 2px;
  --section-pad: clamp(3.5rem, 8vw, 6rem);
  /* Motion */
  --ease-out: cubic-bezier(.2, .8, .2, 1);
  --ease-spring: cubic-bezier(.3, 1.6, .5, 1);
}
```

**Mapping to this repo:** the site still uses its older token names. `--void` is `--kg-void`, `--void-raised` is `--kg-void-raised`, `--panel` is `--kg-panel`, `--accent` is `--rl-red`, `--accent-bright` is `--kg-accent`, `--sans` is `--rl-body` / `--kg-display`, `--mono` is `--rl-mono`, `--line` is `--rl-line`, and `--text` is `--rl-text`.
