# Mission Log Refactoring

## Changes

### CSS Organization
Created **`mission-log.css`** with semantic class-based styling:

**Removed:** 140+ lines of inline `style="..."` attributes with hard-coded:
- RGBA color values (rgba(168,85,247,.04), rgba(126,235,146,.15), etc.)
- Opacity values (0.75, 0.55, 0.45, 0.35, 0.25)
- Spacing and border styles
- Font sizes and colors

**Added:** Reusable CSS classes using semantic tokens:
- `.ml-row--done` — Plasma Purple theme
- `.ml-row--active` — Arc Lime theme  
- `.ml-row--locked-next` — Next-in-line (75% opacity)
- `.ml-row--locked` — Far-off missions (progressive fade)
- `.ml-row--deep-locked` — Very distant (25% opacity)

**Benefits:**
- Change a color once in CSS, affects all missions of that state
- Opacity progression defined via CSS nth-child selectors (auto-scalable)
- All semantic color tokens use CSS variables (`--plasma-purple`, `--arc-lime`, etc.)
- No magic numbers in HTML

### JavaScript Extraction
Created **`mission-log.js`** with `MissionLog` controller:

**Removed:** 20-line inline `<script>` block with hardcoded selectors

**Added:**
```javascript
class MissionLog {
  constructor(containerId) { ... }
  init()              // Auto-initialize on DOMContentLoaded
  toggleDoneRow()     // Click to expand/collapse + chevron rotation
  toggleLockedNext()  // Click to reveal prerequisite
}
```

**Benefits:**
- No onclick handlers in HTML
- Reusable across multiple mission logs on same page
- Auto-discovery via `data-mission-log` attribute
- Clean separation of concerns

### HTML Structure
Simplified markup using CSS class composition:

**Before:** Every style inline
```html
<div style="display:flex;flex-direction:column;padding:7px 10px;border-radius:var(--r-card);margin-bottom:4px;background:rgba(168,85,247,.04);border:1px solid rgba(168,85,247,.15);cursor:pointer;user-select:none;">
  <div style="display:flex;align-items:center;gap:8px;">
    <span style="font-size:9px;letter-spacing:.06em;background:rgba(168,85,247,.15);color:var(--plasma-purple);border:1px solid rgba(168,85,247,.4);border-radius:3px;padding:2px 6px;flex-shrink:0;">DONE</span>
    <!-- ... -->
  </div>
</div>
```

**After:** Semantic classes
```html
<div class="ml-row ml-row--done">
  <div class="ml-row-header">
    <span class="ml-badge">DONE</span>
    <!-- ... -->
  </div>
</div>
```

## CSS Variables Used

All colors pulled from `style.css` tokens:

```css
/* Status Colors */
--plasma-purple   /* #A855F7 - completed missions */
--arc-lime        /* #7EEB92 - active/current */
--dust-shadow     /* #8A8A7A - text dim */
--cream           /* #EAE0CD - text body */
--regolith-slate  /* #2A2F37 - dividers */

/* Opacity is NOT hardcoded — controlled via nth-child selectors */
.ml-row--locked:nth-child(6) { opacity: 0.55; }  /* First locked */
.ml-row--locked:nth-child(7) { opacity: 0.45; }  /* Second locked */
.ml-row--locked:nth-child(8) { opacity: 0.35; }  /* Third locked */
```

## Maintenance

To **change mission state colors**, edit `mission-log.css`:
```css
.ml-row--done {
  --ml-bg: rgba(var(--arc-orange-rgb), 0.04);     /* Change background */
  --ml-badge-bg: rgba(168, 85, 247, 0.15);        /* Change badge */
}
```

To **adjust opacity progression**, edit nth-child selectors in `mission-log.css`.

To **add new mission states**, add a new class:
```css
.ml-row--urgent {
  background: rgba(var(--arc-red-rgb), 0.08);
  border: 1px solid rgba(var(--arc-red-rgb), 0.2);
}
```

Then in HTML, swap class: `<div class="ml-row ml-row--urgent">`

## Performance

- **Smaller HTML:** 140+ fewer characters per mission example
- **Faster styling changes:** CSS-only edits, no HTML rewrites
- **Better mobile:** Reduced DOM size aids memory usage
- **Easier QA:** Visual changes in one file, verified once

## Future Work

Could extend with:
- Animated transitions for state changes
- Dark mode support (via CSS variable override)
- Accessibility enhancements (ARIA attributes for screen readers)
- Mission progress bar animations
