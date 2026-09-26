# Design Notes — UCS 2026 Mockup

## Rationale

Public adjusting sells **trust under stress**. The bar: premium 2026 marketing site — generous whitespace, refined type, soft glass/shadows, cinematic heroes — without playful startup candy or “insurance blue boxes.”

## Palette

| Token | Value | Role |
|-------|-------|------|
| Navy 950/900 | `#0a1628` / `#0f1f35` | Authority, heroes, footer |
| Teal 500 | `#0d9488` | Confident accent / primary CTA |
| Amber 500 | `#d97706` | Optional highlight (sparingly) |
| Cream / slate | `#f8fafc` / slate scale | Surfaces, muted text |

Derived as a refined evolution of typical PA-industry navy, not purple SaaS.

## Typography

- Stack: `Inter, ui-sans-serif, system-ui, …` (system fonts only — no paid font deps; Inter used if installed)
- Display scale: clamp-based `--text-5xl` → `--text-xs`
- Tight tracking on headlines (`-0.02em` / `-0.035em`)
- Body at comfortable ~1.6–1.75 line-height; blog prose larger for magazine reading

## Components

- **Header:** sticky, frosted glass (`backdrop-filter`), top utility bar with phone/email
- **Buttons:** pill radius, gradient primary + glow shadow, secondary glass on dark
- **Cards:** soft border, hover lift (`translateY(-3px)`), icon tile
- **Forms:** muted fill fields → white on focus with teal ring
- **Hero:** radial teal/amber washes + subtle grid mask over navy gradient
- **Trust strip:** licenses, multi-state, no-fee-unless-paid, free inspection
- **Footer:** 4-column clean layout (live footer had script junk in fetch)

## Accessibility

- Skip link; `:focus-visible` rings on interactive controls
- Semantic landmarks (`header` / `main` / `footer` / `nav`)
- Contrast: navy/white and teal-on-light checked for WCAG-minded pairs
- `prefers-reduced-motion` disables transitions/animations
- Mobile nav: `aria-expanded`, Escape to close

## Mobile (375px+)

- Hamburger + accordion mega sections under 1100px
- Sticky bottom Call / Free Inspection bar
- Hero stacks; form full-width; card grids collapse 1→2→3/4

## Conversion improvements (chrome only — copy unchanged)

1. Persistent primary CTA in header + mobile bar → `insurance-claim-help`
2. Trust strip immediately under heroes
3. Claim-help: large phone (855-917-2449) + premium form side-by-side
4. Every page ends with CTA band (Free Inspection + Call)
5. Blog articles: pullquote + related posts + CTA band to claim-help
6. Clear Inspect → Respond → Recover step cards

## Micro-interactions (CSS only)

- Hero children staggered `fade-up`
- Card/blog hover lift + shadow
- Button press scale; chevron rotate on nav hover
- No JS beyond mobile menu


## Color family lock (2026-09-26 Joe)
Live UCS lime `#99cc02` / `#99cc00` + charcoal `#2e2e2e` + soft greys. Mockup keeps that family; shading/tone/gradients may change. Do not drift to unrelated navy/teal.
