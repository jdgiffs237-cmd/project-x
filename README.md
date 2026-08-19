# Project X — Drone Build

A personal project to design, build, and fly a custom drone from scratch.

**Status:** Brainstorming. No hardware purchased, no design locked.
**Current work:** surveying drone types by DoD UAS Group → [brainstorming/drone-classes/](brainstorming/drone-classes/)

---

## Repository structure

```
Project X/
├── 00-BLOG-LINK.md             ← the live blog URL, sorts first so it's findable
├── README.md
├── RECEIPTS.md                 ← actual spend: receipts, orders, returns
├── brainstorming/              ← active work
│   ├── README.md
│   ├── 01-mission-and-use-case.md
│   ├── 02-requirements-and-constraints.md
│   ├── 03-component-research.md
│   ├── 04-budget.md
│   ├── 05-open-questions.md
│   ├── 06-decision-log.md
│   ├── 07-regulatory-checklist.md
│   ├── ideas/                  ← one file per idea, no obligation
│   │   ├── README.md
│   │   └── _template.md
│   └── drone-classes/          ← DoD UAS Group survey (Groups 1–5)
│       ├── README.md
│       ├── 00-overview.md
│       ├── 01-group-1/
│       │   ├── README.md       ← writeup for this group
│       │   ├── images/         ← this group's images only
│       │   └── zz-CREDITS.md   ← image sources + licenses (sorts last)
│       ├── 02-group-2/         ← same shape
│       ├── 03-group-3/
│       ├── 04-group-4/
│       ├── 05-group-5/
│       └── 99-comparison.md
├── blog/                       ← public build log (GitHub Pages)
│   ├── _posts/                 ← one markdown file per published entry
│   ├── _layouts/
│   └── assets/css/
├── hardware/{cad,datasheets,wiring}/
├── code/                       ← stub only
├── build-log/
├── flight-logs/{telemetry}/
├── reference/
└── docs/
```

| Folder | What lives here | Active now? |
|---|---|---|
| [00-BLOG-LINK.md](00-BLOG-LINK.md) | The live blog URL and how publishing works. Sorts first on purpose — the link should never need hunting for. | **Yes — live** |
| [RECEIPTS.md](RECEIPTS.md) | Every purchase actually made — receipts, order numbers, returns, running total against the $10,000 ceiling. Planned spend lives in [04-budget.md](brainstorming/04-budget.md). | **Yes — live** |
| [brainstorming/](brainstorming/) | Thinking space — mission, requirements, component research, budget, open questions, decision log, regulatory checklist. | **Yes — start here** |
| [brainstorming/drone-classes/](brainstorming/drone-classes/) | Survey of unmanned aircraft by **DoD UAS Group (1–5)**, with reference images. Each group folder holds its own writeup, images, and image credits. | **Yes — current focus** |
| [brainstorming/ideas/](brainstorming/ideas/) | Optional ideas, one file per idea. A holding pen so feature creep doesn't leak into the v1 build. | As needed |
| [hardware/](hardware/) | Physical build: CAD models, wiring diagrams, datasheets, bill of materials. | Later |
| [code/](code/) | Flight controller config, ground station, custom firmware. | Much later |
| [build-log/](build-log/) | Dated entries of what was actually done, what broke, what was learned. | When parts arrive |
| [blog/](blog/) | Public-facing build log, published to GitHub Pages. The edited, readable version of the material in `build-log/` and `brainstorming/`. See [blog/README.md](blog/README.md) to write a post. | **Yes — live** |
| [flight-logs/](flight-logs/) | Per-flight records and telemetry captures. | After first flight |
| [reference/](reference/) | Third-party material: manuals, spec sheets, saved articles, regulations. | Ongoing |
| [docs/](docs/) | Polished output — final design doc, assembly guide, pre-flight checklist. | Later |

## Why these folders

- **`hardware/` is separate from `code/`** because the artifacts are completely different in kind (STLs, PDFs, diagrams vs. text files) and change on different schedules. Mixing them makes both harder to find.
- **`build-log/` is separate from `brainstorming/`** because brainstorming is *forward-looking and revisable* while a build log is *append-only history*. Editing your plan is normal; editing your history is not. When something goes wrong, the build log is the only thing that tells you what actually changed.
- **`flight-logs/` is separate from `build-log/`** because flight data is periodic, structured, and often machine-generated (`.bin`/`.ulg` telemetry files). It will outgrow the build log quickly.
- **`reference/` is separate from `docs/`** because one is *other people's material you collected* and the other is *your material you produced*. Keeping them apart avoids confusion about what is authoritative and what has licensing implications.
- **`docs/` exists even though it's empty** so there's an obvious destination for things that graduate out of brainstorming once they stop changing.
- **`blog/` is separate from `build-log/`** because they have different readers. The build log is written for *you*, same-day, raw, optimised for debugging. The blog is written for *someone else*, edited, and optimised for being worth reading. Conflating them makes the build log performative — which destroys the one property that makes it useful.

## Working order

0. Read [brainstorming/drone-classes/](brainstorming/drone-classes/) to figure out what kind of aircraft you're building — start with its [overview](brainstorming/drone-classes/00-overview.md), then [Group 1](brainstorming/drone-classes/01-group-1/), then the [comparison and recommendation](brainstorming/drone-classes/99-comparison.md).
1. Fill in [brainstorming/01-mission-and-use-case.md](brainstorming/01-mission-and-use-case.md) first. Nearly every later decision falls out of it.
2. Record every real choice in [brainstorming/06-decision-log.md](brainstorming/06-decision-log.md) — including the ones you reverse.
3. Do not buy anything until [brainstorming/02-requirements-and-constraints.md](brainstorming/02-requirements-and-constraints.md) and [brainstorming/04-budget.md](brainstorming/04-budget.md) are filled in.
4. Work through [brainstorming/07-regulatory-checklist.md](brainstorming/07-regulatory-checklist.md) before the first flight, not after.

## Conventions

- Markdown for everything writable.
- Dates as `YYYY-MM-DD`.
- Units: state them explicitly, every time. Mixing grams and ounces, or mm and inches, is the single most common source of ordering mistakes in this hobby.
