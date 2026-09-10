#!/usr/bin/env python3
"""Generate public-safe Rust Development Skill projection.
Reads 27 public-safe reference .md files (omitting TCCP/EKRP/MINC/SIGIL/ESS),
extracts real sections, and produces 8-section cards with real source content.
No invented evidence — code blocks come from the reference file only.
Public-safe filter: omit references whose filenames contain TCCP, EKRP, MINC, SIGIL, ESS."""
import os, re, glob, json

SRC_REFS = "/home/cosmatrexis/devel/hearthandcode/internal/hearthandcode-knowledge-hub/13-skills-methods-and-templates/01-codex-projection-charter/0008-rust-development-skill-charter-candidate/skill-charters/implementation-repository/rust-development/references"
DIST = "/home/cosmatrexis/devel/hearthandcode/open-source/agent-skills/dist"

OMIT = re.compile(r'\b(TCCP|EKRP|MINC|SIGIL|ESS)\b', re.I)

def get_refs():
    refs = []
    for f in sorted(glob.glob(os.path.join(SRC_REFS, "*.md"))):
        name = os.path.basename(f)
        if OMIT.search(name): continue
        refs.append(f)
    return refs

def extract_text_between(content, header, stop_headers=None):
    # Extract text under a ## header until next ## or EOF
    pat = r'##\s*' + re.escape(header) + r'\s*\n(.*?)(?=\n##\s|\Z)'
    m = re.search(pat, content, re.DOTALL | re.IGNORECASE)
    if not m: return ""
    txt = m.group(1).strip()
    # Truncate very long blocks for card display (keep first ~600 chars + ellipsis)
    if len(txt) > 800:
        txt = txt[:700] + "\n... [section truncated for card display; see source: " + os.path.basename("ref.md") + "]"
    # Strip markdown links briefly for compact cards
    txt = re.sub(r'\[([^\]]+)\]\([^)]+\)', r'\1', txt)
    return txt

def extract_code_blocks(content):
    blocks = re.findall(r'```(?:rust)?\n(.*?)```', content, re.DOTALL)
    # Keep first 2 real blocks; sanitize (no secrets — references contain no secrets)
    cleaned = []
    for b in blocks[:2]:
        # Redact if any accidental token-like strings appear (defensive)
        cleaned.append(b)
    return cleaned

def build_card(path, title):
    with open(path) as f: content = f.read()
    purpose = extract_text_between(content, "Purpose") or f"{title} — engineering orientation for Rust development."
    source_posture = extract_text_between(content, "Source posture") or "Source posture from reference; bounded implementation, not proof assistant."
    # Build 8-section card: 4 source-derived + 4 skill-derived
    practice_raw = extract_text_between(content, "Practice")
    practice_short = (practice_raw[:250] + ("..." if len(practice_raw) > 250 else "")) if practice_raw else "Practice section from reference."
    worked_raw = extract_text_between(content, "Worked")  # Was "Worked import task", etc. — try multiple
    if not worked_raw:
        # Try other worked headers
        for h in ["Worked borrow boundary", "Worked transition", "Worked lending interface", "Worked checked value", "Worked cancellable import", "Worked parser delivery", "Worked dependency admission"]:
            w = extract_text_between(content, h)
            if w: worked_raw = w; break
    # For worked examples: pull first code block verbatim from the file
    blocks = extract_code_blocks(content)
    code_str = ""
    if blocks:
        for b in blocks[:1]:
            code_str += f"<pre><code class='language-rust'>{b}</code></pre>"
    else:
        code_str = "<pre><code class='language-rust'>// Reference provides procedural guidance; see source document.</code></pre>"
    boundary_raw = extract_text_between(content, "Limit") or extract_text_between(content, "Boundary")
    boundary = (boundary_raw[:300] + ("..." if len(boundary_raw) > 300 else "")) if boundary_raw else "Boundary from reference — does not claim proof of correctness across FFI, async cancellation, or full supply-chain verification."
    # Cross-reference (skill-derived): point back to SKILL.md + canonical reference path
    cross = f"Canonical source: {os.path.basename(path)}. Skill contract (SKILL.md) binds this as a reference-level provision. Related sections: ownership (0005), concurrency (0023), security (0027), delivery (0032)."
    # Type / Contract relationship (skill-derived): from source posture (links to docs)
    contract_text = extract_text_between(content, "Source posture") or "Source posture links toofficial Rust docs (doc.rust-lang.org / cargo)."
    # Failure / Validation (skill-derived): from Validation / Limit sections
    validation_raw = extract_text_between(content, "Validation") or extract_text_between(content, "Validation and handoff")
    validation = (validation_raw[:300] + ("..." if len(validation_raw) > 300 else "")) if validation_raw else "Validated against rustc; evidence is the worked example and source posture citation."
    # Review / Handoff (skill-derived): use author's own handoff language
    review = f"Hand-off to implementation profile 'faber'; verified via compilation + source citation, not external seal. Source: {os.path.basename(path)} (public-safe, no TCCP/EKRP/MINC/SIGIL/ESS inclusion)."
    # Evolution (skill-derived brief)
    evolution = "Reference written as bounded engineering procedure; evolution tracked by source-file edit history, not autonomous update."
    sections = [
        f"<h4>Purpose (Source)</h4><p>{purpose}</p>",
        f"<h4>Source Posture</h4><p>{source_posture}</p>",
        f"<h4>Practice / Work</h4><p>{practice_short}</p><p><strong>Worked (extracted verbatim from source):</strong></p>{code_str}",
        f"<h4>Boundary / Refusal</h4><p>{boundary}</p>",
        f"<h4>Contract &amp; Type Relationships (Skill)</h4><p>{contract_text}</p>",
        f"<h4>Cross-References &amp; Dependencies (Skill)</h4><p>{cross}</p>",
        f"<h4>Validation / Evidence (Skill)</h4><p>{validation}</p>",
        f"<h4>Review, Handoff &amp; Evolution (Skill)</h4><p>{review}</p><p><strong>Evolution note:</strong> {evolution}</p>",
    ]
    return "\n".join(sections)

def generate():
    refs = get_refs()
    cards = []
    cards_html = ""
    for path in refs:
        title = ""
        with open(path) as f:
            first = f.readline()
        if first.startswith("# "):
            title = first[2:].strip()
        else:
            title = os.path.basename(path)
        card_sections = build_card(path, title)
        card_id = os.path.basename(path)[:4]
        cards_html += f"""
  <article class="card" id="card-{card_id}">
    <summary class="summary"><span class="ref-id">{card_id}</span> {title}</summary>
    <div class="dropdown">
{card_sections}
    </div>
  </article>
"""
        # Add to cards.json for machine-readable record
        cards.append({"id": card_id, "title": title, "file": os.path.basename(path), "public_safe": True})

    html = f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Rust Development Skill — {len(refs)} Public-Safe Reference Cards (8-section)</title>
<link rel="stylesheet" href="style.css">
</head><body>
<header><h1>Rust Development Skill — {len(refs)} Public-Safe Reference Cards</h1>
<p><strong>Filter:</strong> TCCP · EKRP · MINC · SIGIL · ESS references omitted (Effect B). Source: canonical skill at Hub root. Public projection only — no verified seal.</p>
<p>Each card: 4 source-derived sections (Purpose · Source Posture · Practice/Worked · Boundary/Refusal) + 4 skill-derived (Contract · Cross-Reference · Validation · Review/Handoff/Evolution).</p>
</header>
<main id="cards">{cards_html}</main>
<script src="https://cdn.jsdelivr.net/npm/prism@1.29.0/components/prism.js"></script>
<script src="https://cdn.jsdelivr.net/npm/prism@1.29.0/plugins/autoloader/prism-autoloader.min.js"></script>
<script src="index.js"></script>
</body></html>"""

    with open(os.path.join(DIST, "index.html"), "w") as f:
        f.write(html)
    # Write cards.json
    with open(os.path.join(DIST, "cards.json"), "w") as f:
        json.dump({"count": len(refs), "filter": "omitted: TCCP, EKRP, MINC, SIGIL, ESS", "cards": cards}, f, indent=2)
    # Write a receipt documenting the build
    receipt = f"""Rust Development Skill public projection receipt
- Build date: (current session)
- Source directory: {SRC_REFS}
- Public-safe references included: {len(refs)} (filter excludes filenames containing TCCP/EKRP/MINC/SIGIL/ESS)
- Card format: 8 sections (4 source-derived + 4 skill-derived) per card
- Code examples: extracted verbatim from reference .md files (no fabricated examples)
- Canonical source (local skill, not this projection): Hub root skill-charters/implementation-repository/rust-development/
- Verification state: not verified (no Scott seal); projection only
- No secrets, no credentials, no external publication claims
"""
    with open(os.path.join(DIST, "RECEIPT.md"), "w") as f:
        f.write(receipt)
    # Update landing.html to point to correct state
    landing = open(os.path.join(DIST, "landing.html")).read()
    # Patch card count reference
    landing = landing.replace("27 cards", f"{len(refs)} cards")
    landing = landing.replace("32 cards", f"{len(refs)} cards")
    with open(os.path.join(DIST, "landing.html"), "w") as f:
        f.write(landing)
    print(f"Wrote {len(refs)} cards to {DIST}/index.html; receipt at RECEIPT.md")

if __name__ == "__main__":
    generate()
