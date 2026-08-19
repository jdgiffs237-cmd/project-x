# 06 — Decision Log

> Append-only. One entry per real decision. **Never delete an entry** — if you change your mind, add a new entry that supersedes the old one and mark the old one `SUPERSEDED BY DL-##`.
>
> The value of this file is six months from now, when you're staring at a part and asking "why on earth did I pick this?"

**Last updated:** 2026-08-19

---

## Entry template — copy this

```markdown
### DL-00 — <short title>

- **Date:** YYYY-MM-DD
- **Status:** ACCEPTED | SUPERSEDED BY DL-## | REVERSED
- **Decision:** <what was decided, in one sentence>
- **Context:** <what forced the decision; what was true at the time>
- **Options considered:**
  1. <option> — pros / cons
  2. <option> — pros / cons
- **Why this one:** <the actual reason>
- **Consequences:** <what this now commits you to, and what it rules out>
- **Cost impact:** $___
- **Reversible?** <cheaply / expensively / not>
- **Related:** Q# from [05](05-open-questions.md)
```

---

## Decisions

### DL-01 — Use a structured project scaffold for this build

- **Date:** 2026-08-16
- **Status:** ACCEPTED
- **Decision:** Track the build in a folder structure with a brainstorming space, decision log, and build log rather than ad-hoc notes.
- **Context:** Starting from zero experience; many interdependent decisions ahead, made over months.
- **Options considered:**
  1. Ad-hoc notes / memory — zero overhead, but decisions and their reasons get lost
  2. Structured markdown project — small upkeep cost, preserves reasoning and history
- **Why this one:** With no prior experience, the reasoning behind each choice is the thing most worth preserving; it's also what makes it possible to ask for help intelligently later.
- **Consequences:** Requires the discipline of writing entries as decisions get made.
- **Cost impact:** $0
- **Reversible?** Cheaply
- **Related:** —

---

### DL-02 — Phase the build around "bench alive" before flight

- **Date:** 2026-08-19
- **Status:** ACCEPTED
- **Decision:** Split the Project One purchase into three phases — Phase 1 buys only what is needed to get motors spinning on command with props off; Phase 2 adds the radio, props and batteries for line-of-sight flight; Phase 3 adds FPV.
- **Context:** Stated priority is building the aircraft, not flying it yet ("I really just want to build it so it can move"). The original BOM was a single undifferentiated list in which FPV gear — the largest cost block — read as a prerequisite to assembly. It is not.
- **Options considered:**
  1. Buy the whole BOM at once — one shipping event, but ~$700 of goggles/camera/VTX sits unused for months and the build stalls on decisions (video system, goggle compatibility) that assembly doesn't depend on
  2. Phase by milestone — more orders and more shipping waits, but each purchase is unblocked by the previous milestone actually working
  3. Buy a ready-to-fly quad instead — fastest to flight, but discards the build, which is the stated point of the project
- **Why this one:** Every Phase 1 item is either soldered into the aircraft or is the tool doing the soldering, so nothing in it can be deferred and nothing in it is speculative. Everything else can wait for evidence that the stack works. It also front-loads the failure mode that actually matters on a first build — bad solder joints — while the aircraft is still cheap.
- **Consequences:** Commits to bench-testing with props off as the Phase 1 completion criterion. Defers FAA registration and Remote ID until Phase 2, since neither attaches to an indoor propless bench. Leaves a skill gap at the end of Phase 1 — a flyable aircraft and no stick time — mitigated by a whoop + simulator (~$120) bought during Phase 1, per [04-budget.md](04-budget.md) Stage 0.
- **Cost impact:** $0 net; re-sequences roughly $400–700 of FPV spend to later
- **Reversible?** Cheaply — phases can be collapsed by placing one order
- **Related:** [Project One BOM](../Project%20One%20-%20Standard%20Drone/BOM%20Claude.md), Stage 0 in [04-budget.md](04-budget.md)

---

<!-- Add new entries below. Newest at the bottom, numbered sequentially. -->
