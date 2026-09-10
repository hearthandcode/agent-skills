# agent-skills — public-safe skill projections

Public-safe projections of Hearth & Code skill charters, reference cases, and
rendered build artifacts.

## What's here

- **`skill-charters/`** — SKILL.md contract files (source-bound skill charters)
- **`references/`** — worked reference cases (source-derived, omitting TCCP, EKRP,
  MINC, Sigil, and ESS governance references)
- **`dist/`** — rendered static projections (HTML + Prism syntax highlighting)

## Public-safe filter

Per Scott's release, the following reference classes are **omitted** from this
public-safe projection:

- TCCP (Hearth & Code Threshold Dashboard)
- EKRP (Exocore Knowledge Representation Protocol)
- MINC (Minimal Notation Calculus)
- Sigil (Exocore Sigil Standard)
- ESS (Exocore Sigil Standard synthesis)

## Build

Static site served from `dist/index.html` — no build step required. Open
`dist/index.html` directly or serve with `python3 -m http.server` from `dist/`.

## License

Local-candidate. Public release pending Scott's separate authorization.