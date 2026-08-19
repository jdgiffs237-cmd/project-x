# ideas/

**Anything you might want to do, with no obligation to do it.** One file per idea.

This is the low-pressure end of the project. Nothing here is committed to, costed, or scheduled. The point is to get an idea out of your head and onto disk so it stops taking up room, and so it's still there in six months when it might actually be feasible.

---

## How this differs from its neighbours

The distinction matters, or everything ends up in the wrong file:

| Folder / file | Holds | Nature |
|---|---|---|
| **ideas/** | Things you *might* want to do | Optional. No obligation. |
| [../05-open-questions.md](../05-open-questions.md) | Things you don't *know* yet | Blocking. Needs an answer. |
| [../06-decision-log.md](../06-decision-log.md) | Things you've *decided* | Committed. Append-only. |
| [../01-mission-and-use-case.md](../01-mission-and-use-case.md) | What the drone is *for* | The constraint everything else answers to. |

Rule of thumb: **if it blocks progress, it's an open question. If you've committed to it, it's a decision. If it's "wouldn't it be cool if…", it lives here.**

---

## How to use it

- **One idea per file**, named `short-kebab-case-title.md`. Copy [_template.md](_template.md).
- **Write it down badly rather than not at all.** A two-line stub beats a lost thought.
- **Date every idea.** Feasibility changes fast — parts get cheaper, your skills improve, and an idea that was absurd in month one may be obvious in month eight.
- **Don't delete ideas you reject.** Mark them `REJECTED` with a one-line reason. The reasoning is the valuable part, and rejected ideas have a habit of becoming good ones when a constraint changes.
- **When an idea graduates**, move it: into [../06-decision-log.md](../06-decision-log.md) if you commit to it, or into [../02-requirements-and-constraints.md](../02-requirements-and-constraints.md) if it becomes a requirement. Leave a stub here pointing at where it went.

---

## Status values

Put one at the top of each idea file:

- `RAW` — just captured, not thought about
- `EXPLORING` — actively researching feasibility
- `PARKED` — good idea, wrong time (say what would unblock it)
- `PROMOTED` — became a decision or requirement; note where it went
- `REJECTED` — decided against; note why

---

## A note on scope creep

This folder is where scope creep is *supposed* to live. That's its job — a holding pen, so that "what if it had a thermal camera" doesn't quietly become part of build v1.

Ideas are free. Ideas that leak into an unfinished first build are not. **Keep v1 boring.** The single most common way a first drone project dies is by growing features until it's never finished.

Check any idea against the non-goals in [../01-mission-and-use-case.md](../01-mission-and-use-case.md) before promoting it.

---

## Index

_(Add a line per idea as you create it — title, status, one-line hook.)_

| Idea | Status | Hook |
|---|---|---|
| [delta-vtol-quadplane.md](delta-vtol-quadplane.md) | EXPLORING | **The project goal.** DIY ~$2.2–4k vs. $15–30k commercial. Reached via a 4-stage path (~$5,070) — Altius production experience transfers build skill, not flying or tuning skill. |
