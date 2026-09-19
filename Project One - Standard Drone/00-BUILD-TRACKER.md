# Project One — Build Tracker

**Live page:** https://claude.ai/code/artifact/37ebf69d-c8ca-4cd8-bf25-904359ae8ecf

*Updated 2026-09-19*

## Where things stand

| | |
|---|---|
| Parts bought | **20 / 20 — done** |
| Arrived | Everything except the FC and the replacement iron |
| Spent | **$936.19** (9 orders; $261.67 in refunds pending — AiXun + Matek) |
| Waiting on | **SkyStars H743 HD FC** (ETA Sep 22–25) + **YIHUA 939D+ iron** |

## What's where

| Item | Status |
|---|---|
| Frame, motors ×4, battery, tools bundle | Arrived Sep 3 |
| ESC + charger | **Arrived** |
| ~~Soldering iron (AiXun T3A)~~ | **Defective — being returned** ($135.68 refund pending) |
| Soldering iron (YIHUA 939D+, 75W) | **Ordered Sep 11**, $57.23 |
| ~~Flight controller (Matek H743)~~ | **Cancelled Sep 19** — stuck in transit, vendor unresponsive; $125.99 refund pending |
| Flight controller (SkyStars H743 HD, single gyro) | **Ordered Sep 19**, $80.99, Amazon/GetFPV — ETA Sep 22–25 |
| M3 screws + safety glasses | Still unconfirmed in the Amazon bundle box |

## Soldering queue — ready the moment the YIHUA lands

The FC connects to the ESC by a plug-in cable, so none of these joints wait on it:

1. **Motors → ESC pads** (4 motors × 3 wires). Trim wire to arm length first.
2. **XT60 pigtail → ESC battery pads** — the fat 12 AWG joints. The YIHUA is 75W, so: **largest chisel tip, max temperature**, and give the joint time to heat.
3. **Capacitor across the battery pads** — read the can first: **1000 µF 35 V**, stripe = negative.
4. Heat shrink everything as you go. *No heat gun needed: the iron's barrel held near the tubing, or the lower half of a lighter flame kept moving, shrinks it fine.*

**Check the ESC box first** — if it includes its own capacitor and XT60 lead, use whichever is better and keep the spares.

## When the FC lands

**Power it on the day it arrives** — the AiXun taught that lesson.

1. **Compare the FC and ESC 8-pin pinout diagrams before plugging anything.** Both are now Skystars — the factory stacks this FC on the KO60 — so they should match, but the check costs two minutes and a mistake costs both boards.
2. Continuity-check every wire with the multimeter.
3. First power-up **through the smoke stopper**, no props.
4. Spin motors from Betaflight, props off. **That's bench-alive.**

Meanwhile: install **Betaflight Configurator** + **ImpulseRC Driver Fixer** if not done yet.

## Two open questions (your call)

- Tools budget is $122 over (the charger is counted in it).
- Project One isn't in the budget plan yet.

---
Money detail: [RECEIPTS.md](../RECEIPTS.md) · Quick list: [PARTS-BOUGHT.md](PARTS-BOUGHT.md)
