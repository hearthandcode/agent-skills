---
name: rust-development
description: Rust development skill — bounded implementation language approach, with explicit refusal boundaries (not a proof assistant).
revision: public-safe-redraft-2026-09-10
status: candidate
verified: false
public_safe: true
omitted_reference_classes: [TCCP, EKRP, MINC, SIGIL, ESS]
---

# Rust Development Skill — Public-Safe Projection

## When to use

Use this skill for Rust implementation, review, diagnosis, and validation work
where the goal is bounded engineering evidence rather than proof of correctness
across untested boundaries. Applies to workspace selection, type construction,
ownership design, state modeling, traits, FFI/unsafe review, serialization,
persistence, async/task ownership, concurrency, performance, error design,
procedural/declarative macros, build and security checks, test selection,
compiler feedback loops, and application delivery.

This is a public-safe projection of the canonical skill at the Hub root.
The canonical source retains the full 32 reference cases (including TCCP,
EKRP, MINC, Sigil, ESS references); those 5 governance classes are omitted
from this projection per the owner's release (Effect B). All content here
is drawn from the 27 public-safe reference files and the skill contract.

## Design thesis (public-safe, preserved)

Rust is a bounded implementation language with compile-time ownership,
borrowing, lifetime, and type guarantees — not a proof assistant, not a
total-correctness framework, and not a substitute for formal verification
where the obligation requires it. Each reference defines a specific
engineering decision (types, ownership, concurrency, macros, serialization,
security, testing) and names its refusal boundaries explicitly.

## Reference structure (27 public-safe cards)

The package contains 27 public-safe reference files (0001–0010, 0019–0032;
0011–0018 — ESS/TCCP/EKRP/MINC/Sigil/Exocore governance references — omitted).
Each reference maps to 8 card sections: Purpose · Source Posture · Practice · Boundary · Contract · Cross-Reference · Validation · Review/Handoff.
The projection is rendered at `dist/index.html` with Prism CDN syntax highlighting;
the source of each card section is the reference `.md` file, not boilerplate.

## What this skill does NOT claim

- It does not establish universal correctness, termination, or arbitrary
  arithmetic proof for Rust programs.
- It does not claim memory-safety proofs across FFI boundaries, async
  cancellation, or unverified build scripts.
- It does not substitute for a formal proof assistant (Lean, Agda, Isabelle)
  when the obligation requires named definitions, assumptions, and a
  verified theorem environment.
- It does not authorize external publication, provider activation, secret
  exposure, or deployment.
- It does not claim verified status; `verified: false` is preserved.

## Source links (27 reference routes)

- 0001 Rust engineering orientation — workspace, compiler, lockfile, baseline
- 0002 Rust language and type system — types, newtypes, TryFrom, boundaries
- 0003 Algebraic data types and pattern matching — ADTs, patterns, transitions
- 0004 Traits, generics, GATs and associated types — abstraction, coherence
- 0005 Ownership, borrowing, lifetimes, drop — owner design, borrow rules
- 0006 Typestate, capabilities, proof witnesses — stronger static guarantees
- 0007 Const generics, refinement, type-level limits — fixed-shape contracts
- 0008 Haskell, Lean, Idris orientation and non-equivalence — formal-language
  comparison (orientation only, not equivalence claim)
- 0009 Procedural macro architecture — macro design, parsing, emission
- 0010 Declarative macros and hygiene — macro repetition, hygiene, testing
- 0019 Crate, module, workspace architecture — packaging, dependency direction
- 0020 API design, semver, feature policy — facade, deprecation, compatibility
- 0021 Error taxonomy and diagnostics — error classification, mapping
- 0022 Testing, property, fuzz, model checking — test layers, oracles
- 0023 Concurrency, async, cancellation, backpressure — task ownership, queues
- 0024 Performance profiling and benchmarking — measurement, comparison
- 0025 Unsafe, FFI, trusted computing base — unsafe blocks, invariants, ABI
- 0026 Serde, schema versioning, migrations — serialization admission, version
- 0027 Security, supply chain, secret boundaries — dependency, input, build
- 0028 Observability, receipts, recovery — receipts, recovery, restart
- 0029 Agentic Rust compiler feedback workflow — diagnostic loop, correction
- 0030 Code review, refactoring, maintenance — review discipline, preservation
- 0031 Game, desktop, harness, general application patterns — adapter, CLI
- 0032 Rust application delivery checklists — checklist, verification, handoff

## Projection details

- Build source: `src/generate_site.py` (reads source `.md` files; no boilerplate)
- Output: `dist/index.html` (27 cards), `dist/landing.html` (product-ad page)
- Syntax highlighting: Prism CDN (`prismjs` + autoloader)
- Public-safe filter: excludes filenames containing TCCP, EKRP, MINC, SIGIL, ESS
- Verification state: `verified: false` (preserved honestly — not Scott's seal)
- No credentials, secrets, or private paths in output
- No installation, activation, or deployment authorization granted

## License / release posture

Local-candidate only. Public release is authorized by Scott's direct
instruction (session-20260910T041024Z-virgil-soul-pcc-rewrite, Q36/amd 62).
`verified: true` is Scott's personal seal — separate, not set here.
Copyright (c) 2026 Scott Rallya & Hearth & Code. MIT-licensed public projection.
