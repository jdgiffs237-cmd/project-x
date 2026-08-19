# brainstorming/

**This is the active working area.** Thinking space for the drone project — messy, revisable, and contradictory by design. Nothing here is final.

Contrast with the rest of the project:
- **brainstorming/** — thinking. Revised constantly.
- **[../build-log/](../build-log/)** — history. Append-only, never revised.
- **[../docs/](../docs/)** — conclusions. Clean and current; things graduate here once they stop changing.

---

## Read and fill in this order

| # | File | What it's for | Status |
|---|---|---|---|
| 1 | [01-mission-and-use-case.md](01-mission-and-use-case.md) | What this drone is *for*. Nearly every later decision descends from it. | Empty — **start here** |
| 2 | [02-requirements-and-constraints.md](02-requirements-and-constraints.md) | Performance targets and hard limits, derived from the mission. | Empty |
| 3 | [03-component-research.md](03-component-research.md) | What each part does, candidate parts, and the compatibility checklist. | Empty |
| 4 | [04-budget.md](04-budget.md) | Four-bucket budget: aircraft, ground equipment, tools, crash fund. | Empty |
| 5 | [05-open-questions.md](05-open-questions.md) | Everything unresolved, flagged by what it blocks. | Seeded with starter questions |
| 6 | [06-decision-log.md](06-decision-log.md) | Append-only record of every real decision and *why*. | One entry |
| 7 | [07-regulatory-checklist.md](07-regulatory-checklist.md) | FAA obligations — registration, Remote ID, TRUST vs. Part 107. | Checklist ready |
| — | **[drone-classes/](drone-classes/)** | **Survey of drone types by DoD UAS Group (1–5).** Reference reading to figure out what to build. | **Complete** |
| — | [ideas/](ideas/) | Things you might want to do, one file per idea. No obligation attached. Where scope creep is supposed to live. | Empty — add as they come |

---

## Current active work

**[drone-classes/](drone-classes/)** — a survey of unmanned aircraft organized by the US DoD's UAS Group classification, written to answer "what kind of drone do I even want to build?"

Start with [drone-classes/00-overview.md](drone-classes/00-overview.md), then [drone-classes/01-group-1/](drone-classes/01-group-1/) (the only group a personal build lands in), then [drone-classes/99-comparison.md](drone-classes/99-comparison.md) for the recommendation.

---

## How to use these files

- **Fill in order.** The numbering is a dependency chain, not a preference. Requirements that don't descend from a mission are guesses.
- **Record decisions as you make them** in [06-decision-log.md](06-decision-log.md), including the ones you later reverse. Six months from now you'll be holding a part with no memory of why you chose it.
- **Move resolved items** out of [05-open-questions.md](05-open-questions.md) and into the decision log, so the questions file stays a working list rather than an archive.
- **Park stray ideas in [ideas/](ideas/)** rather than letting them into the build. If it blocks progress it's an open question; if you've committed to it it's a decision; if it's "wouldn't it be cool if…" it's an idea. **Keep v1 boring.**
- **Don't buy anything** until files 02 and 04 are filled in.
- **State units explicitly, every time.** Mixing grams and ounces is the most common source of ordering mistakes in this hobby.
- **Dates as `YYYY-MM-DD`.**
