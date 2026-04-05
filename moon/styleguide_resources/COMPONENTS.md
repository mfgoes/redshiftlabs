# UI Components Reference

Bootstrap-style component library for Project Moon UI Style Guide examples.

## Overview

This system provides reusable, semantic CSS classes and HTML snippets organized like Bootstrap. Each component handles a specific UI element (buttons, cards, panels, viewports) and can be composed into larger layouts.

## Stylesheets

- **`style.css`** — Base typography, colors (CSS custom properties), and global component styles (buttons, toggles, sliders, etc.)
- **`components.css`** — Reusable layout components (demo viewport, tab bar, panels, grids, etc.)

Link in your HTML `<head>`:

```html
<link rel="stylesheet" href="styleguide_resources/style.css">
<link rel="stylesheet" href="styleguide_resources/components.css">
<link rel="stylesheet" href="styleguide_resources/mission-log.css">
<script src="styleguide_resources/tabs.js"></script>
<script src="styleguide_resources/mission-log.js"></script>
```

## Component Types

### Viewports

**`.demo-viewport`** — Interactive demo container with game-world background

```html
<div class="demo-viewport">
  <div class="demo-viewport-label">game viewport</div>
  <!-- Your interactive content here -->
</div>
```

### Tab Bars

**`.tab-bar`** — Pill bar with toggle buttons, anchored to bottom of viewport

```html
<div id="my-tabbar" class="tab-bar" data-tabbar>
  <button class="tab-button active" data-panel="panel-build">
    <svg>...</svg>
    Build
  </button>
  <button class="tab-button" data-panel="panel-colonists">
    <svg>...</svg>
    Colonists
  </button>
</div>
```

**Attributes:**
- `data-tabbar` — Marks this container for auto-initialization
- `data-panel="panel-id"` — Links button to its panel element by ID

**`.tab-button.active`** — Automatically managed by `TabBar` class. Don't set manually.

### Tab Behavior (tabs.js)

Import `tabs.js` to enable automatic tab switching:

```html
<script src="styleguide_resources/tabs.js"></script>
```

**Auto-initialization:**
Any `[data-tabbar]` element automatically creates a `TabBar` instance on page load.

**Manual initialization:**
```javascript
const myTabs = new TabBar('my-tabbar-id');
myTabs.select('panel-build');   // Open panel
myTabs.deselect();              // Close all panels
myTabs.toggle('panel-build');   // Toggle state
```

**Behavior:**
- Clicking a button toggles its panel (click again to close)
- Only one panel visible at a time
- Panel visibility managed via `.visible` class on `.panel-floating`

### Floating Panels

**`.panel-floating`** — Slides up from tab bar, sits flush on top

```html
<div class="panel-floating visible">
  <div class="panel-title">Build</div>
  <!-- Grid or list content -->
</div>
```

Use `.visible` class to show/hide with CSS instead of inline styles.

### Building Grid

**`.building-grid`** — 3-column responsive grid for building/structure cards

```html
<div class="building-grid">
  <div class="building-card">
    <div class="building-card-icon">⚙</div>
    <div class="building-card-name">Refiner</div>
    <div class="building-card-cost">80 Al</div>
  </div>
  <!-- More cards... -->
</div>
```

### Colonist List

**`.colonist-list`** + **`.colonist-item`** — Vertical list of colonist status items

```html
<div class="colonist-list">
  <div class="colonist-item">
    <div class="colonist-avatar">👤</div>
    <div class="colonist-info">
      <div class="colonist-name">Boris</div>
      <div class="colonist-status">Working · Refiner Alpha</div>
    </div>
    <div class="colonist-state active">● Active</div>
  </div>
  <!-- More items... -->
</div>
```

State color modifiers for `.colonist-state`:
- `.active` — green (#7EEB92)
- `.sleeping` — light blue (#99CCFF)
- `.idle` — gray (#8A8A7A)

## HTML Snippets

Pre-built HTML template files for common components:

### `snippets-viewport.html`
Game world background label. Include as first child of `.demo-viewport`.

### `snippets-building-card.html`
Template + helper function for programmatically creating building cards.

```html
<script src="styleguide_resources/snippets-building-card.html"></script>
<script>
  const grid = document.querySelector('.building-grid');
  grid.appendChild(createBuildingCard('⚙', 'Refiner', '80 Al'));
</script>
```

### `snippets-colonist-item.html`
Template + helper function for programmatically creating colonist items.

```html
<script src="styleguide_resources/snippets-colonist-item.html"></script>
<script>
  const list = document.querySelector('.colonist-list');
  list.appendChild(createColonistItem('Boris', 'Working · Refiner Alpha', 'active'));
</script>
```

## Example: Complete Bottom Tab Bar

See `UI_STYLE_GUIDE.html#ex-bottom-tab-bar` for a working example using all components together.

### Structure
```html
<div class="demo-viewport">
  <div class="demo-viewport-label">game viewport</div>
  
  <div id="sg-build-panel" class="panel-floating visible">
    <div class="panel-title">Build</div>
    <div class="building-grid"><!-- cards --></div>
  </div>
  
  <div id="sg-colonists-panel" class="panel-floating">
    <div class="panel-title">Colonists</div>
    <div class="colonist-list"><!-- items --></div>
  </div>
  
  <div id="sg-tabbar" class="tab-bar" data-tabbar>
    <button class="tab-button active" data-panel="sg-build-panel">Build</button>
    <button class="tab-button" data-panel="sg-colonists-panel">Colonists</button>
  </div>
</div>
```

### Behavior
- Tab buttons automatically toggle active state via `TabBar` class
- Panels automatically show/hide via `.visible` class
- All state management in `tabs.js`, no inline scripts needed

## CSS Custom Properties

Use semantic color tokens from `style.css`:

```css
/* Surfaces */
--surface-base           /* Void black background */
--surface-raised         /* Panel body */
--surface-inset          /* Card insets */
--surface-border         /* Borders */

/* Text */
--text-body              /* Cream foreground */
--text-dim               /* Dust shadow for secondary text */

/* Interactive */
--interactive            /* Arc cyan for active states */
--interactive-subtle     /* 10% opacity cyan for backgrounds */

/* Status */
--status-ok              /* Arc lime for active/working */
--status-caution         /* Arc yellow */
--status-warn            /* Arc orange */
--status-danger          /* Arc red */
```

## Mission Log Components

**`mission-log.css`** provides mission row states with semantic color coding and opacity progression:

```html
<div id="ml-container" class="mission-list" data-mission-log>
  <!-- DONE (Completed) -->
  <div class="ml-row ml-row--done">
    <div class="ml-row-header">
      <span class="ml-badge">DONE</span>
      <div class="ml-title">1. First Light</div>
      <span class="ml-chev">▸</span>
    </div>
    <div class="ml-row-body" hidden>
      <div class="ml-body-objective">Build 2 Generators...</div>
      <div class="ml-body-unlock">UNLOCKED &nbsp;<span class="ml-body-unlock-value">Battery Bank</span></div>
    </div>
  </div>

  <!-- ACTIVE (Current Mission) -->
  <div class="ml-row ml-row--active">
    <div class="ml-row-header">
      <span class="ml-badge">ACTIVE</span>
      <div class="ml-title">3. Mouths to Feed</div>
      <span class="ml-type">SURVIVAL</span>
    </div>
    <div class="ml-objective">Produce 30 Food...</div>
    <div class="progress-wrap"><!-- progress bar --></div>
    <div class="ml-unlocks">UNLOCKS &nbsp;<span class="ml-unlocks-value">Electronics Fab</span></div>
  </div>

  <!-- LOCKED (Next-in-line) -->
  <div class="ml-row ml-row--locked-next">
    <div class="ml-row-header">
      <span class="ml-lock-icon"><svg><!-- lock icon --></svg></span>
      <span class="ml-title">4. Unidentified Shipment</span>
      <span class="ml-type">SUPPLY</span>
    </div>
    <div class="ml-locked-msg" hidden>Complete <em>Mouths to Feed</em> to unlock.</div>
  </div>

  <!-- LOCKED (Far-off, opacity fades) -->
  <div class="ml-row ml-row--locked"><!-- ... --></div>
  
  <!-- DEEP-LOCKED (Very far future) -->
  <div class="ml-row ml-row--deep-locked">
    <div class="ml-row-header">
      <span class="ml-lock-icon"><svg><!-- lock icon --></svg></span>
      <span class="ml-deep-locked-text">3 further missions ···</span>
    </div>
  </div>
</div>
```

**`mission-log.js`** provides `MissionLog` controller for state management:

```html
<script src="styleguide_resources/mission-log.js"></script>
```

Add `data-mission-log` to the container for auto-initialization:

```javascript
const log = new MissionLog('ml-container-id');
// Handles:
// - Click .ml-row--done to expand/collapse body
// - Click .ml-row--locked-next to show/hide prerequisite
// - Chevron direction updates automatically
```

**State colors via CSS variables:**
- `.ml-row--done` — Plasma Purple (#A855F7)
- `.ml-row--active` — Arc Lime (#7EEB92)
- `.ml-row--locked-next` — 75% opacity
- `.ml-row--locked` — Progressive fade: 55%, 45%, 35%
- `.ml-row--deep-locked` — 25% opacity

No hard-coded rgba values in HTML — all managed via CSS variables and semantic class names.

## Adding New Components

1. **Define CSS** in `components.css` (or feature-specific file) using semantic class names
2. **Create HTML snippet** in `snippets-{name}.html` if reusable
3. **Add controller** to relevant `.js` file (tabs.js, mission-log.js, etc.)
4. **Document** in this file with usage examples
5. **Test** in `UI_STYLE_GUIDE.html` examples

Keep component CSS self-contained (no dependencies on other components). Composition happens in HTML/JS, not CSS nesting. Use CSS variables and semantic tokens to minimize duplication.
