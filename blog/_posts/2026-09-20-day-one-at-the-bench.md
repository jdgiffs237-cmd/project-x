---
layout: post
title: "Day one at the bench"
stage: "Build · Entry 09"
date: 2026-09-20
summary: >-
  Motors are on the frame, every tool is installed, and the battery took its
  first charge — but not one joint got soldered, on purpose. Day one was
  about knowing what I'm doing before the iron touches the ESC.
---

The build log officially opened today, and day one ended with an aircraft
shape sitting on the bench: frame assembled, **all four motors mounted**,
screw lengths measured against the 6 mm arms before a single screw went in.
I photographed every step of the motor mounting — those pictures become the
work instructions in the new `Routing/` folder, so the next build (or the
next person) gets a documented procedure instead of my memory.

## The software stack is ready before the hardware needs it

Everything the flight controller will want on arrival is now installed:
Betaflight Configurator, the browser-based ESC Configurator bookmarked, and
ImpulseRC Driver Fixer — the tool that fixes the Windows driver trap where a
flight controller connects fine and then vanishes the moment you try to
flash it.

One snag worth recording: ImpulseRC's own downloads page is a dead link now.
The tool actually lives on their GitHub, under Releases. Lesson repeated
from the flight controller saga: the official source moves, and a build log
that records *where things really are* earns its keep.

## First charge, and what "charging" even means

The battery took its first charge today — inside the fireproof bag,
supervised, on the HOTA charger. Instead of just pressing start, I dug into
what the charger is actually doing: **constant current** first, pushing a
fixed current in while cell voltage rises, then **constant voltage** as each
cell approaches 4.2 V, holding there while the current tapers toward zero.
The balance lead is the charger's window into each of the six cells
individually, nudging them even so no single cell ever gets overcharged.
Knowing why the charge takes as long as it does makes the "never walk away
from a charging LiPo" rule feel less like superstition and more like
engineering.

## The joint I didn't solder

The iron is tested and the ESC is staged — and I stopped there. The next
thing I solder will be a $58 four-in-one ESC, and my total soldering
experience is a few practice joints. So the plan between now and the flight
controller's arrival (due in the next few days) is: watch good soldering
technique videos, burn through some scrap wire until the joints come out
shiny on purpose rather than by luck, and only then run the 12 motor joints
and the two big battery-pad joints for real.

An aircraft you can't fly yet is fine. A powertrain soldered badly because
of impatience is a debugging season. Day two is practice, then commitment.
