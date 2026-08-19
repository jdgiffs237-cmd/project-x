# build-log/

**Append-only history of what actually happened.** One file per session: `YYYY-MM-DD-short-description.md`.

This is deliberately separate from [brainstorming/](../brainstorming/). Brainstorming is a plan and gets revised. This is a record and doesn't. When something stops working, the build log is the only artifact that can tell you what changed since it last worked.

## Why bother

- **Debugging.** "It worked yesterday" is only useful if you know what you did yesterday.
- **Asking for help.** Forums and Discords give dramatically better answers to someone who can say exactly what they did, in what order, with photos.
- **Not repeating mistakes.** You will make the same soldering mistake twice unless you wrote it down the first time.

## Entry template

```markdown
# YYYY-MM-DD — <what this session was about>

**Time spent:** ___
**Goal for this session:** ___

## What I did
-

## What went wrong
-

## What I learned
-

## Photos
- `2026-08-16-esc-solder-joints.jpg`

## Parts consumed / damaged
-

## Next session
-
```

## Rules

- Write the entry **the same day**, while it's fresh. A vague entry beats no entry.
- Record failures in more detail than successes — they're worth more later.
- Photograph anything before you cover it up or glue it down.
- If you fixed something, write down *what the fix was*, not just that it's fixed.
- Never edit a past entry to make it look better. Append a correction instead.
