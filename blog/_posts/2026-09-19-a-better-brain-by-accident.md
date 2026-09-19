---
layout: post
title: "A better brain, by accident"
stage: "Build · Entry 08"
date: 2026-09-19
summary: >-
  The Matek flight controller never showed up and its vendor went silent, so
  I cancelled it — and found a board from the same company as my ESC, with
  every firmware door still open, for $45 less.
---

The flight controller was supposed to be the easy part of the last three
weeks. Instead the Matek H743 sat somewhere between MEPS King's warehouse and
my door for over two weeks, and every message to their customer service
vanished into the same void the board did. On day one I'd written a note to
watch for a customs charge on delivery; I never got far enough to pay one.

So I cancelled it and went shopping with one non-negotiable requirement
unchanged: **I want to write my own firmware.** That means an STM32H743 with
2 MB of flash — the hard floor for ArduPilot Lua scripting — and official,
maintained firmware targets, not "compatible with" claims on a no-name board.

## The replacement found me

The board that checked every box turned out to be the **SkyStars H743 HD** —
same company that made the ESC already sitting on my bench. Skystars sells
this exact flight controller factory-stacked on the KO60, the sibling of my
KO60II, which means the scariest step of this whole build — the 8-pin
cable between two brands that never agreed on a pin order — becomes a
same-family handshake. I'll still verify it pin by pin, but I expect the
diagrams to match for once.

The rest of the checklist:

- **STM32H743, 2 MB flash** — Lua scripting and custom firmware fully intact.
- **Official targets in all three firmwares**: ArduPilot (`SkystarsH7HD`,
  with its own page in the ArduPilot docs), Betaflight, and INAV.
- **30×30 mount**, BMI270 gyro, BMP280 barometer — all mainline-supported
  parts.
- **$80.99, sold by GetFPV through Amazon** — a real US shop with real
  customer service, Prime shipping, and a 30-day return window. Arrives
  early next week.

That's **$45 less than the Matek**, and the only thing genuinely lost is
Matek's famously thorough documentation. The ArduPilot hardware definition
file documents the pin mapping anyway, which is the part that matters when
you're writing code against the board.

## The scoreboard after a messy week

Gross spend is now **$936.19**, but $261.67 of refunds are in flight — the
defective AiXun iron and the cancelled Matek — so the real number is heading
to about **$675**, comfortably under where it stood two weeks ago. Two boxes
remain: this flight controller and the YIHUA iron, both due within days of
each other. If the week cooperates, the next entry is written next to a
frame with motors soldered to it.

Two lessons for the log. First: **the vendor is part of the part.** A
perfect board you can't get, from a company that won't answer, is worse
than a good board from a shop that picks up the phone. Second, a repeat
offender: **test everything the day it arrives.** The new FC gets powered
on before the packing tape hits the floor.
