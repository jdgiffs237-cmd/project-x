---
layout: post
title: "Everything is ordered"
stage: "Build · Entry 04"
date: 2026-08-29
summary: >-
  Ten days after writing the parts list, every Phase 1 part is bought: $797.97
  across seven orders. Half the list changed on the way, and the three
  decisions I made along the way matter more than the shopping.
---

Ten days ago I had a parts list and no parts. Today every Phase 1 part is
ordered — **$797.97 across seven orders** — and nothing can happen until the
soldering iron arrives in mid-September.

The list I wrote on the 19th did not survive contact with the shops. Three of
the four core parts were out of stock or discontinued, the charger was priced
at less than half its real cost, and a wave of US drone tariffs landing on
3 September was emptying every retailer's shelves. Most of what follows is
what I decided when the plan broke.

## Decision 1: split the stack

The plan was a SpeedyBee F405 V5 stack — flight controller and ESC as one
matched pair, because my own BOM said never to buy them separately.

Then SpeedyBee discontinued it. And when I looked closer, its ESC ran
**closed-source firmware** that can't be reflashed. I want to learn firmware on
this build, so that was a dead end regardless of stock.

So I split it: a separate flight controller and a **Skystars 60A ESC running
AM32**, which is open source and the firmware everything is moving to. Same
money as the dead stack, more current headroom, and an ESC I can actually
flash. The cost is one real risk — two brands means I have to check the 8-pin
pinout matches before the first power-up, or I kill both boards.

## Decision 2: buy the flight controller that can go autonomous

I asked myself whether I'd ever want this thing to fly itself. The answer was
yes. That killed the SpeedyBee flight controller too: it's an F4 board, and
ArduPilot's onboard scripting **needs 2 MB of flash and won't run on F4 at
all**. Not worse — absent.

The **Matek H743** was $59 more. It runs Betaflight, INAV and ArduPilot with
official support, has the 2 MB, and means I can flash Betaflight now, get the
motors spinning, and switch to ArduPilot later on the same board with nothing
re-bought. Every vendor was sold out; I found the last in-stock one at a
smaller shop.

## Decision 3: the battery I rejected

The original pick was a Tattu 75C pack. Working the numbers, four of these
motors at full throttle pull roughly 160 A and that pack manages 97.5 A — about
40% short. I went with a **GNB 160C** rated at 245 A. Eight dollars more, and
the difference between a battery that sags and runs hot and one with real
headroom.

## What I learned about shipping

Small orders from FPV shops cost $7–11 each in shipping. Once I noticed, I put
the ESC and charger in one RaceDayQuads order and got free shipping. Should
have done that with the frame and flight controller too. Consolidate.

## The number

Phase 1 was estimated at ~$530 on the 19th. It landed at **$797.97**. The
charger alone was $150 against a $65 guess, and the flight controller decision
added $59 on purpose. The tools — about $420 of it — carry over to every future
build.

## What's next

Boxes arrive over the next two weeks. The soldering iron is last, on the 10th
to 17th. Until then: install the configurator software, sort out the Windows
driver problem before I need it, and compare those two pinout diagrams very
carefully.

Then solder, continuity-check, smoke-test, and spin four motors with no props
on. That's bench-alive, and it's the whole point of Phase 1.
