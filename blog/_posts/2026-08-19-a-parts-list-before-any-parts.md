---
layout: post
title: "A parts list before any parts"
stage: "Design · Entry 03"
date: 2026-08-19
summary: >-
  Writing the bill of materials before buying anything surfaced four things I'd
  have got wrong: the stack, the battery count, the smoke stopper, and the fact
  that the most important purchase isn't hardware at all.
---

I wrote a full bill of materials for a 5" FPV quad this week. Nothing is
ordered, no brands are chosen, and the airframe isn't formally locked — the
point wasn't to shop. It was to find out what I don't know yet, while finding
out is still free.

Four things surfaced that I would have got wrong by ordering first.

## 1. The flight controller and ESC are one purchase, not two

Buy them together as a matched **stack**. Bought separately, the interconnect
between them isn't guaranteed to fit — mounting pattern, connector, and pinout
all have to line up, and "both are 30×30" is not sufficient.

This is the category of mistake that doesn't announce itself until two boxes
have arrived and neither can be returned. It's also exactly the kind of
compatibility research that pre-built kits have already solved, which is a real
argument for a kit on a first build even at a price premium.

## 2. One battery is not a quantity

The naive plan is: buy the aircraft, buy a battery, go fly.

A 5" quad gets **5–8 minutes** of flight per pack. So one pack means five
minutes of flying and an hour of charging. Three to four packs is the difference
between a session and a demonstration.

That reframes the budget in a way I didn't expect. Batteries aren't an
accessory line item — they're a substantial fraction of the build, and they're
consumable. Props too: buy more sets than feels reasonable, because they're the
thing crashes actually cost.

## 3. Two safety items I'd have skipped

**A LiPo-safe charging bag.** Non-negotiable. Lithium polymer packs fail
energetically, and they fail while charging, unattended, indoors.

**A smoke stopper.** This one I genuinely didn't know about. It's an inline
current limiter between the battery and the aircraft on first power-up. If
you've made a wiring mistake — reversed polarity, a solder bridge across the
battery pads — it limits the current instead of letting the mistake destroy the
board. It turns a dead flight controller into a shrug.

For a first hand-wired build, where the probability of a wiring mistake is not
low, that's the highest-value cheap tool on the list. Continuity-check with a
multimeter before every first power-up, then power up through the smoke stopper.

Add a temperature-controlled soldering iron to the same category. A bad iron
destroys boards — either it can't deliver enough heat into a ground plane, so
you sit on the joint and cook the pad off, or it has no regulation and runs hot
enough to lift traces.

## 4. The most important purchase isn't hardware

It's an **FPV simulator**, about $20.

Two arguments for it. The first is that it decouples learning to fly from
learning to build, and those are genuinely separate skills that a first-timer
usually tries to acquire simultaneously on the same fragile object. Stick time
in a simulator is the item most likely to decide whether the quad survives its
first month.

The second is cheaper still: two hours in a simulator tells you whether you
actually enjoy this, before any money is committed to hardware. Highest-return
spend in the project by a wide margin, and it's the one thing on the list I can
buy today.

## The legal line, which is a design constraint

One item on the BOM exists purely because of the airframe choice: a **Remote ID
broadcast module**. A 5" quad is well over 250 g, so it requires FAA
registration and Remote ID compliance.

This is the FAA threshold I flagged in the last entry — the one the DoD Group
system has no equivalent for. It's worth being precise that this isn't
paperwork you handle after the build. It's a design input: it adds weight, it
adds cost, and choosing a sub-250 g airframe instead removes the entire
requirement. That choice has to be made before ordering, not after.

Also required and not purchasable: recreational registration, and a visual
observer present for FPV flight.

## What the exercise actually produced

A parts list, yes. But mostly a list of decisions I hadn't realised were
decisions — stack compatibility, pack count, the 250 g question, whether to buy
a kit or hand-wire.

Writing the BOM before shopping cost an evening and caught four errors. That's a
good trade, and it's the same reason the decision log exists: the expensive
mistakes in this hobby are made at the ordering stage, silently, and don't
surface for two weeks.

## Next

Mission and use case — the document everything else falls out of, and the one
that will settle the 250 g question. Then the budget. Nothing gets ordered until
both are filled in.

**Status:** Design stage · $0 spent · 0 flights · BOM drafted, nothing ordered
