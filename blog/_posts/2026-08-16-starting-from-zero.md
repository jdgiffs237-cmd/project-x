---
layout: post
title: "Starting from zero, on purpose"
stage: "Design · Entry 01"
date: 2026-08-16
summary: >-
  I work on unmanned aircraft professionally and have never built one. This is
  the log of fixing that — and the first real decision was made before any
  hardware was chosen.
---

I work on fixed-wing unmanned aircraft for a living.

I have never built an aircraft with my own hands, and I have never flown
anything that hovers.

Both of those things are true at once, and the gap between them is the reason
this project exists. Professional exposure to UAS gives you a particular kind of
knowledge: airspace structure, why weight thresholds sit where they do, how to
read a spec sheet skeptically, what an operational envelope means. What it does
not give you is any of the tacit knowledge that comes from soldering a joint
badly, watching the magic smoke leave, and finding out why.

That's the knowledge I'm after. So: build a drone. From parts. Badly at first.

## The trap I'm trying to avoid

The failure mode for someone with domain knowledge and no hands-on experience is
predictable — you over-design. You reach for the interesting problem instead of
the tractable one, because the interesting problem is the one your professional
instincts recognise.

Concretely, I already know I want to build a VTOL quadplane. It's the
configuration closest to what I find genuinely interesting, and it is
categorically the wrong first build. You're building two aircraft that share a
fuselage plus the transition between them, and the transition can only be tested
in the air, on a real airframe, with no way to bench-test it first. You need to
already be competent at both multirotor and fixed-wing setup before that's a
sane thing to attempt.

So it goes in an ideas folder, unbuilt, where it can't leak into v1.

## The first decision was about process, not hardware

Before choosing a single component, the first real decision I logged was to
track this build in a structured repository rather than ad-hoc notes: a
brainstorming space that gets revised freely, a decision log that is append-only,
and a build log that is append-only and dated.

That split matters more than it sounds like it does.

**Brainstorming is forward-looking and revisable.** Plans should change; that's
what plans are for.

**A build log is history, and history doesn't get edited.** When something stops
working, the build log is the only artifact that can tell you what changed since
it last worked. The moment you start tidying it up to look competent, it stops
being able to do that job.

**A decision log preserves the reasoning, not just the outcome.** Six months from
now I will be holding a part and asking why on earth I picked it. "Because it
was cheaper and I accepted a 12% weight penalty for it" is a useful answer.
Silence is not.

With no prior experience, the reasoning behind each choice is the single thing
most worth preserving. It's also what makes it possible to ask for help
intelligently later — forums give dramatically better answers to someone who can
say exactly what they did, in what order.

## The rules

Four, and they're the whole discipline:

1. Write the entry the same day, while it's fresh. A vague entry beats no entry.
2. Record failures in more detail than successes.
3. Photograph anything before you cover it up or glue it down.
4. Never edit a past entry to make it look better. Append a correction instead.

That last one applies to this blog too. If I'm wrong about something here — and
on a first build I will be, repeatedly — the correction gets appended, not
retrofitted.

## Where this goes next

No hardware purchased. No airframe locked. The next entry is the survey work:
figuring out what class of aircraft this should even be, which turned out to be
a more interesting question than I expected, mostly because the obvious
framework for answering it doesn't answer it at all.

**Status:** Design stage · $0 spent · 0 flights
