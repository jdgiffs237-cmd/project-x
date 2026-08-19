# 05 — Open Questions

> Anything you don't know yet. Move items to [06-decision-log.md](06-decision-log.md) when they're resolved — this file should stay a *working* list, not an archive.

**Last updated:** _(YYYY-MM-DD)_

---

## How to use this

Each question gets: a **status**, a **blocker flag**, and a note on **how you'd answer it**. Questions that block purchasing get resolved first.

**Status values:** `OPEN` · `RESEARCHING` · `ANSWERED → see DL-##` · `PARKED`

---

## Blocking questions (must resolve before spending money)

| # | Question | Status | Blocks | How I'd find out |
|---|---|---|---|---|
| Q1 | What is this drone actually for? | OPEN | Everything | [01-mission-and-use-case.md](01-mission-and-use-case.md) |
| Q2 | Where can I legally and practically fly near me? | OPEN | Frame class, whether project is viable | B4UFLY app; FAA UAS Facility Maps; local parks dept.; AMA club finder |
| Q3 | What's my real budget ceiling? | OPEN | Every part choice | [04-budget.md](04-budget.md) |
| Q4 | Am I building sub-250 g or accepting registration + Remote ID? | OPEN | Frame, motors, battery, legal path | [07-regulatory-checklist.md](07-regulatory-checklist.md) |
| Q5 | Kit vs. build-from-parts? | OPEN | Ordering strategy | Compare a specific kit against a specific parts list |
| Q6 | Recreational (TRUST) or Part 107? | OPEN | Legal obligations, cost | FAA site; depends on whether any use is "for business" |
| Q7 | FPV or line-of-sight/autonomous? | OPEN | Goggles, VTX, camera, ~$400+ | |
| Q8 | Can I solder well enough, and if not, how do I get there? | OPEN | Kit vs. parts decision | Practice kit; solder scrap wire |

## Technical questions

| # | Question | Status | Notes |
|---|---|---|---|
| T1 | Which flight controller firmware? | OPEN | Betaflight / INAV / ArduPilot / PX4 — see [03](03-component-research.md) |
| T2 | 4S or 6S battery? | OPEN | Affects motor KV, ESC choice, cost |
| T3 | 4-in-1 ESC or individual ESCs? | OPEN | 4-in-1 is far easier for a first build |
| T4 | Do I need GPS? | OPEN | Required for position hold / return-to-home / any autonomy |
| T5 | Analog or digital video? | OPEN | Only if FPV |
| T6 | Do I need a Remote ID broadcast module, or a drone with it built in? | OPEN | Custom builds almost never have it built in |
| T7 | How do I test motors safely before the first flight? | OPEN | Props off, smoke stopper, bench test |

## Logistics & skills questions

| # | Question | Status | Notes |
|---|---|---|---|
| L1 | Where will I work on this? | OPEN | Ventilation for soldering; a surface you can damage |
| L2 | How will I store and charge LiPos safely? | OPEN | Fire-safe container, non-flammable surface |
| L3 | Should I fly a simulator first? | OPEN | Strongly yes if FPV — a sim costs ~$20 and saves a crashed drone |
| L4 | Should I buy a cheap ready-made trainer to learn on first? | OPEN | Common and effective; separates "learning to fly" from "learning to build" |
| L5 | Is there a local club / maker space with people who've done this? | OPEN | Cuts the learning curve more than any purchase |
| L6 | How do I transport this thing? | OPEN | |

## Parked / later

| # | Question | Notes |
|---|---|---|
| P1 | Custom CAD parts? | Only after v1 flies |
| P2 | Onboard compute for CV/autonomy? | Only after v1 flies |
| P3 | Do I need liability insurance? | Revisit before flying near anyone |

---

## Guiding questions

- Which open question, if answered, would collapse the most others? Answer that one.
- Which questions am I avoiding because I suspect the answer is inconvenient?
- Which of these can only be answered by *doing something* (soldering practice, visiting a field, trying a sim) rather than by more reading?
