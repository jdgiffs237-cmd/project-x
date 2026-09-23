# Project X — Drone Build

Designing, building, and flying a custom drone from scratch — with every
decision, purchase, mistake, and reversal written down as it happens.

**Public build log:** https://jdgiffs237-cmd.github.io/project-x/

---

## Project One — 5" quadcopter · build in progress

The first aircraft: a bare-frame, hand-wired 5" quad running Betaflight, built
to a factory-style routing of numbered work instructions, each one a photo
walkthrough with a check at every step.

| | |
|---|---|
| **Status** | **At the bench — Day 2.** Frame assembled, four motors mounted, ESC soldering under way. Flight controller in transit (ETA Sep 22–25). |
| **Airframe** | TBS Source One V6 · EMAX ECO II 2207 1900KV ×4 · Skystars KO60II 60A AM32 ESC · SkyStars H743 HD FC · GNB 6S 1530 mAh |
| **Milestone in sight** | *Bench alive* — motors spin on command, props off, before a single flight |
| **Spent** | ~$956 across 10 orders · ~$695 net once two refunds land (a defective iron, a stuck-in-transit FC) |

**Start here →** [`Project One - Standard Drone/`](Project%20One%20-%20Standard%20Drone/)

| Document | What it is |
|---|---|
| [00-BUILD-TRACKER.md](Project%20One%20-%20Standard%20Drone/00-BUILD-TRACKER.md) | Where the build stands right now — what's arrived, what's next, what's waiting |
| [WorkInstructions/](Project%20One%20-%20Standard%20Drone/WorkInstructions/) | **The work instructions.** WI-01 bench & frame, WI-02 ESC soldering — each a slide-by-slide photo walkthrough with checks, readable on GitHub — plus one Google Slides deck of the whole build |
| [BOM.md](Project%20One%20-%20Standard%20Drone/BOM.md) | The phased bill of materials — bench-alive, then flight, then FPV — and why it's phased that way |
| [SHOPPING-LIST-PHASE-1.md](Project%20One%20-%20Standard%20Drone/SHOPPING-LIST-PHASE-1.md) | The Phase 1 buy as it was placed, with the four things most likely to bite |
| [PARTS-BOUGHT.md](Project%20One%20-%20Standard%20Drone/PARTS-BOUGHT.md) | Every part, date, price, and vendor — including the two that went back |
| [build-log/](build-log/) | Same-day, append-only record of each bench session |

---

## Repository structure

```
Project X/
├── Project One - Standard Drone/   ← THE BUILD — start here
│   ├── 00-BUILD-TRACKER.md         ← live status
│   ├── WorkInstructions/           ← the procedure: markdown per WI + one slide deck
│   │   ├── README.md
│   │   ├── WI-01-bench-setup-and-frame.md
│   │   ├── WI-02-esc-soldering.md
│   │   ├── images/wi-NN/           ← photos, one folder per WI
│   │   ├── Project-One-Build-Walkthrough.pptx  ← the slide deck (Google Slides)
│   │   └── tools/                  ← photo import helpers
│   ├── BOM.md                      ← phased bill of materials
│   ├── SHOPPING-LIST-PHASE-1.md
│   └── PARTS-BOUGHT.md
├── build-log/                      ← dated bench sessions, append-only
├── blog/                           ← public build log (GitHub Pages, Jekyll)
│   ├── _posts/
│   ├── _layouts/
│   └── assets/css/
├── brainstorming/                  ← how the project got to Project One
│   ├── 01-mission-and-use-case.md … 07-regulatory-checklist.md
│   ├── 06-decision-log.md          ← every real decision, with reasoning
│   ├── drone-classes/              ← survey by DoD UAS Group (1–5), with images
│   └── ideas/
├── RECEIPTS.md                     ← actual spend: receipts, orders, returns
├── 00-BLOG-LINK.md                 ← the live blog URL and how publishing works
├── hardware/{cad,datasheets,wiring}/
├── flight-logs/{telemetry}/
├── reference/
├── docs/
└── code/
```

| Folder | What lives here | Active now? |
|---|---|---|
| [Project One - Standard Drone/](Project%20One%20-%20Standard%20Drone/) | The aircraft being built: tracker, work instructions, BOM, purchase record. | **Yes — the build** |
| [build-log/](build-log/) | Dated entries of what was actually done, what broke, what was learned. Written the same day, never edited after. | **Yes — daily** |
| [blog/](blog/) | Public-facing build log, published to GitHub Pages on every push. The edited, readable version of `build-log/` and `brainstorming/`. | **Yes — live** |
| [RECEIPTS.md](RECEIPTS.md) | Every purchase actually made — receipts, order numbers, returns, running total against the $10,000 ceiling. | **Yes — live** |
| [brainstorming/](brainstorming/) | The thinking that led here — mission, requirements, component research, budget, open questions, decision log, regulatory checklist, and a survey of drone types by DoD UAS Group. | Reference |
| [hardware/](hardware/) | CAD models, wiring diagrams, datasheets. | Later |
| [flight-logs/](flight-logs/) | Per-flight records and telemetry captures. | After first flight |
| [reference/](reference/) | Third-party material: manuals, spec sheets, saved articles, regulations. | Ongoing |
| [docs/](docs/) | Polished output — final design doc, assembly guide, pre-flight checklist. | Later |
| [code/](code/) | Flight controller config, ground station, custom firmware. | Much later |

## How the repo is organised, and why

- **`build-log/` is separate from `brainstorming/`** because brainstorming is *forward-looking and revisable* while a build log is *append-only history*. Editing your plan is normal; editing your history is not. When something goes wrong, the build log is the only thing that tells you what actually changed.
- **`blog/` is separate from `build-log/`** because they have different readers. The build log is written for *me*, same-day, raw, optimised for debugging. The blog is written for *someone else*, edited, and optimised for being worth reading. Conflating them makes the build log performative — which destroys the one property that makes it useful.
- **`WorkInstructions/` is written like a factory routing** — numbered work instructions, each ending in a verifiable state — so a session can stop at the end of any WI without leaving the aircraft in an unknown condition, and so the next build (or the next person) gets a procedure instead of a memory.
- **`hardware/` is separate from `code/`** because the artifacts are completely different in kind (STLs, PDFs, diagrams vs. text files) and change on different schedules.
- **`flight-logs/` is separate from `build-log/`** because flight data is periodic, structured, and often machine-generated (`.bin`/`.ulg` telemetry). It will outgrow the build log quickly.
- **`reference/` is separate from `docs/`** because one is *other people's material I collected* and the other is *my material I produced*. Keeping them apart avoids confusion about what is authoritative and what has licensing implications.

## Reading order

1. [Project One — Build Tracker](Project%20One%20-%20Standard%20Drone/00-BUILD-TRACKER.md) — where things stand today.
2. [WorkInstructions/](Project%20One%20-%20Standard%20Drone/WorkInstructions/) — how the aircraft is actually being put together.
3. [build-log/](build-log/) — what each session at the bench produced.
4. [brainstorming/06-decision-log.md](brainstorming/06-decision-log.md) — why the project is shaped the way it is, including the decisions that were reversed.
5. [The blog](https://jdgiffs237-cmd.github.io/project-x/) — the whole story, in order, written to be read.

## Conventions

- Markdown for everything writable.
- Dates as `YYYY-MM-DD`.
- Units stated explicitly, every time. Mixing grams and ounces, or mm and inches, is the single most common source of ordering mistakes in this hobby.
- Money: planned spend lives in [brainstorming/04-budget.md](brainstorming/04-budget.md); actual spend lives in [RECEIPTS.md](RECEIPTS.md). They are never the same file.
