# Project One — Bill of Materials

**Aircraft:** 5" quadcopter — bare frame, hand-wired, Betaflight
**Last updated:** 2026-08-19

> **Buy order is phased.** The goal of Phase 1 is *not* flight — it's a finished,
> wired aircraft whose motors spin on command with the props off. That is a real
> milestone, it is safe, and it needs roughly half this list.
>
> Generic descriptions, no brands.

---

## Phase map

| Phase | Milestone | What it proves | Roughly |
|---|---|---|---|
| **1 — Bench alive** | Motors spin on command, props off, frame clamped down | Your soldering is sound and the whole electrical stack talks to itself | **~$530** ($230 aircraft + $115 power + $185 tools) |
| **2 — It moves** | Lifts off and flies line-of-sight in an open field | You can command the aircraft | +$250–300 |
| **3 — FPV** | Flying from the camera | — | +$400–700 |

> Roughly **$185 of Phase 1 is tools, not aircraft** — a one-time cost that carries
> across every future build. Subtract whatever is already on the bench.
> Specific parts and prices: [03-component-research.md](../brainstorming/03-component-research.md).

Phase 3 is where the goggles, camera, and video transmitter live. Nothing in it
is needed to build the aircraft, and none of it is wasted by being bought later.

---

# PHASE 1 — BENCH ALIVE

Everything below is required. Nothing below can be deferred, because it's either
soldered into the aircraft or it's the tool that does the soldering.

## The aircraft

| Item | Qty | Notes |
|---|---|---|
| Frame kit | 1 | 5" prop class, replaceable arms |
| Brushless motors | 4 | Matched to frame size and battery cell count |
| Flight controller + 4-in-1 ESC **stack** | 1 | Buy as a matched pair — separately, the interconnect isn't guaranteed to fit |
| Capacitor | 1 | Across the battery pads |
| Battery connector pigtail | 1 | |
| Wire, heat shrink, zip ties, thread locker | — | |

> The ESC's current rating must sit above peak motor draw. This is the one spec
> on this page that quietly destroys hardware if you get it wrong.

## Power

| Item | Qty | Notes |
|---|---|---|
| Flight battery | 1–2 | More packs are a Phase 2 purchase — you only need one to prove the bench |
| Balance charger | 1 | |
| LiPo-safe bag | 1 | Non-negotiable, from the very first charge |

## Tools

| Item | Notes |
|---|---|
| Temperature-controlled soldering iron | A bad iron destroys boards. This is the single worst place to save money |
| Solder + flux + wick | Wick is for when you get it wrong, which you will |
| Multimeter | Continuity check before every first power-up |
| Smoke stopper | Turns a wiring mistake into a shrug instead of a fire |
| Hex driver set | Metric |
| Safety glasses | |

## Software for this phase

| Item | Cost | What it's for |
|---|---|---|
| Flight controller configurator | Free | Where you'll spin the motors from. Also ports, modes, failsafe |
| ESC configurator | Free | Motor direction and ESC settings |

> On macOS the ESC configurator is browser-based and needs a Chromium browser.
> The flight controller configurator has a native Mac build.

**Not needed in Phase 1:** radio transmitter, receiver, propellers, goggles,
camera, video transmitter, Remote ID, FAA registration. A quad on a bench with
no propellers is not an aircraft in flight, and nothing regulatory attaches to it.

---

# PHASE 2 — IT MOVES

Buy once Phase 1 is spinning. This is what turns a bench rig into something that
leaves the ground.

## Aircraft additions

| Item | Qty | Notes |
|---|---|---|
| Propellers | several sets | Consumable — buy more than feels reasonable |
| Radio receiver | 1 | Protocol must match the transmitter |
| Additional flight batteries | 2–3 | One pack means 5 minutes of flying and an hour of waiting |

## Ground equipment

| Item | Qty | Notes |
|---|---|---|
| Radio transmitter | 1 | Buy once, buy well — outlives every build |

## Software for this phase

| Item | Cost | What it's for |
|---|---|---|
| Radio link configurator | Free | Flashing and binding transmitter to receiver |
| Transmitter companion software | Free | Model setup and backups |
| Propulsion calculator | Paid, small | Sanity-check thrust and current draw |

## Required by law — from this phase onward

| Item | Notes |
|---|---|
| FAA recreational registration | This aircraft is well over 250 g |
| Remote ID broadcast module | Required for outdoor flight |
| TRUST certificate | Free online, takes 20 minutes |

> Both attach the moment you fly **outdoors**. Neither applies to the Phase 1 bench.

---

# PHASE 3 — FPV

Deferred by choice. Fly line-of-sight first.

| Item | Qty | Notes |
|---|---|---|
| FPV camera + video transmitter | 1 | One integrated air unit if going digital |
| Video antenna | 1 | |
| FPV goggles | 1 | Must match the video system above |
| FPV simulator | 1 | Paid, small. Stick time |
| Blackbox log viewer | Free | Tuning, once you're flying |

**Also required, not a purchase:** a visual observer present for FPV flight.

---

# THE GAP THIS PHASING LEAVES

Phasing the *purchase* doesn't phase the *skill*. Phase 1 ends with a working
aircraft you cannot yet fly, and the temptation at that point is to put props on
a 5" and find out. Don't — that's the version of this plan that ends in stitches
or a destroyed build.

The cheap fix, bought any time during Phase 1:

| Item | Cost | Why |
|---|---|---|
| Tiny whoop (sub-250 g, ducted, indoor) | ~$100 | Learns the sticks in a living room, breaks nothing, needs no registration |
| FPV simulator | ~$20 | The item most likely to decide whether the 5" survives its first month |

That's ~$120 against a $10,000 ceiling, and it's the difference between the 5"
being your *first* aircraft and being your first *good* one.

---

**Related:** [budget](../brainstorming/04-budget.md) ·
[regulatory checklist](../brainstorming/07-regulatory-checklist.md) ·
[decision log](../brainstorming/06-decision-log.md)
