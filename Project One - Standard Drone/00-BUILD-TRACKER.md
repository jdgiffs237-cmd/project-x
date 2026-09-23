# Project One — Build Tracker

*Updated 2026-09-22*

## Where things stand

| | |
|---|---|
| Build | **Day 2 at the bench.** Frame assembled, four motors mounted, ESC staged — [WI-01](WorkInstructions/WI-01-bench-setup-and-frame.md) complete. [WI-02](WorkInstructions/WI-02-esc-soldering.md) (ESC soldering) in progress. |
| Parts bought | **20 / 20 — done** |
| Arrived | Everything except the FC |
| Waiting on | **SkyStars H743 HD FC** — ETA Sep 22–25 · helping-hands station — arrives Sep 22 |
| Spent | **~$956.19** across 10 orders · $261.67 in refunds pending (AiXun + Matek) → ~$695 net |
| Software | Betaflight Configurator, ImpulseRC Driver Fixer, Zadig installed; esc-configurator.com bookmarked — **done Sep 20** |

## What's where

| Item | Status |
|---|---|
| Frame, motors ×4, battery, tools bundle | Arrived Sep 3 — **frame built, motors mounted Sep 19–20** |
| ESC + charger | Arrived — ESC staged on the stack; charger used for the first (supervised, in-bag) charge Sep 20 |
| Soldering iron (YIHUA 939D+, 75 W) | Arrived Sep 19 — tested at temperature the same day |
| Helping-hands station with magnifier | Ordered Sep 21 (~$20) — arrives Sep 22 |
| Flight controller (SkyStars H743 HD, single gyro) | Ordered Sep 19, $80.99, Amazon/GetFPV — **ETA Sep 22–25** |
| ~~Soldering iron (AiXun T3A)~~ | Defective on arrival — returned, $135.68 refund pending |
| ~~Flight controller (Matek H743)~~ | Cancelled Sep 19 — stuck in transit, vendor unresponsive; $125.99 refund pending |

## Now: WI-02 — ESC soldering

Fourteen joints, no flight controller needed, **no battery on the bench.**
The full slide-by-slide procedure is [WorkInstructions/WI-02](WorkInstructions/WI-02-esc-soldering.md);
the short version:

1. **Motors → ESC pads** — 4 motors × 3 wires, trimmed at the WI-01 tape marks.
2. **XT60 → battery pads** — the fat 12 AWG joints. 75 W means **largest chisel
   tip, max temperature**, and time for the pad to wet. Red → +, black → −.
3. **Capacitor across the battery pads** — **1000 µF 35 V**, stripe = negative.
4. **Continuity audit** before anything else happens.

Heat shrink as you go — the iron's barrel held near, or the lower half of a
lighter flame kept moving, shrinks it fine.

## When the FC lands

**Power it on the day it arrives** — the AiXun taught that lesson.

1. **Compare the FC and ESC 8-pin pinout diagrams before plugging anything.**
   Both are Skystars — the factory stacks this FC on the KO60 — so they should
   match, but the check costs two minutes and a mistake costs both boards.
2. Continuity-check every wire with the multimeter.
3. First power-up **through the smoke stopper**, no props.
4. Spin motors from Betaflight, props off. **That's bench-alive.**

## Open questions

- Tools budget is $122 over (the charger is counted in it).
- Project One isn't in the stage budget plan yet — see [RECEIPTS.md](../RECEIPTS.md).

---
Daily record: [build-log/](../build-log/) · Money: [RECEIPTS.md](../RECEIPTS.md) ·
Quick list: [PARTS-BOUGHT.md](PARTS-BOUGHT.md) ·
Live pages: [interactive tracker](https://claude.ai/artifact/7uWwutntfPKyU8hupoE4K8) · [Build Day 1 checklist](https://claude.ai/artifact/4GPMzLcXZW3vpemujTUTYw)
