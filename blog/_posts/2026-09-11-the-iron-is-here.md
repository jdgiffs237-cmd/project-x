---
layout: post
title: "The iron is here"
stage: "Build · Entry 06"
date: 2026-09-11
summary: >-
  The soldering iron beat its own delivery window, the ESC and charger landed
  with it, and the answer to "do I need a heat gun for heat shrink" turns out
  to be no. Six of seven boxes are in — only the flight controller is still
  on a truck.
---

The AiXun soldering station was supposed to be the long pole — September 10 to
17, the thing every other part waited on. It showed up at the front of its own
window, and the ESC and charger arrived alongside it. That makes **six of
seven orders in hand**. The only box still moving is the flight controller,
coming from MEPS King, possibly with a customs charge attached when it knocks.

## No, you don't need a heat gun

I asked this twice, so it's earning its own heading. Heat shrink tubing needs
roughly 90 °C to shrink, and there are already two things on this bench that
get much hotter than that:

- **The soldering iron itself.** Hold the hot barrel *near* the tubing — not
  pressed against it — and rotate the wire. It shrinks in a few seconds.
- **A lighter.** Use the lower half of the flame and keep it moving. The
  tubing scorches if you park the flame in one spot, so don't.

A hot air gun does the job faster and more evenly, and if one ever shows up
in a future order it won't be wasted. But it is not a thing this build is
blocked on, and it never was.

## The surprise: soldering can start before the last box arrives

I assumed nothing could happen until every part was here. Wrong — the flight
controller connects to the ESC with a plug-in cable, no solder involved. Every
joint that actually needs the iron is between parts that are already on the
bench:

- Four motors onto the ESC's motor pads — twelve small joints.
- The XT60 battery lead onto the ESC's fat battery pads — the two big 12 AWG
  joints the T12 handle will feel slowest on. Large chisel tip, 380–400 °C.
- The capacitor across those same pads. The can must read **1000 µF 35 V** —
  and the stripe side is negative.

First, though: open the ESC box properly. A lot of 4-in-1 ESCs ship with
their own capacitor and XT60 lead, and I bought both separately. Whichever
pair is nicer goes on the aircraft; the other pair becomes spares for the
joints I ruin learning.

What still waits for the flight controller: the 8-pin pinout comparison
(Matek and Skystars don't have to agree on pin order, and a mismatch kills
both boards), the continuity check, and the first power-up through the smoke
stopper. That moment — motors spinning from the configurator, props off — is
the whole point of Phase 1, and it is now one delivery away.
