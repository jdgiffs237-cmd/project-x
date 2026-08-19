# 06 — Decision Log

> Append-only. One entry per real decision. **Never delete an entry** — if you change your mind, add a new entry that supersedes the old one and mark the old one `SUPERSEDED BY DL-##`.
>
> The value of this file is six months from now, when you're staring at a part and asking "why on earth did I pick this?"

**Last updated:** _(YYYY-MM-DD)_

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

<!-- Add new entries below. Newest at the bottom, numbered sequentially. -->
