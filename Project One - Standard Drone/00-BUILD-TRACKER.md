# Project One — Build Tracker

*Updated 2026-10-11*

## Where things stand

| | |
|---|---|
| Build | **Day 3 — the FC is here and alive.** Flashed with **Betaflight 2026.6.2**; with the battery on the stack, Betaflight reads **24.49 V, 6S detected**. [WI-01](WorkInstructions/WI-01-bench-setup-and-frame.md) complete; [WI-02](WorkInstructions/WI-02-esc-soldering.md) audit to finish, then WI-04. See [Day 03](../build-log/2026-10-11-day-03.md). |
| Parts bought | **20 / 20 — done** |
| Arrived | **Everything** — the FC landed 2026-10-11 |
| Waiting on | Nothing for Phase 1 · helping-hands arrival not logged *(confirm)* |
| Spent | **~$956.19** across 10 orders · $261.67 in refunds pending (AiXun + Matek) → ~$695 net |
| Software | Betaflight Configurator, ImpulseRC Driver Fixer, Zadig installed; esc-configurator.com bookmarked — **done Sep 20** |

## What's where

| Item | Status |
|---|---|
| Frame, motors ×4, battery, tools bundle | Arrived Sep 3 — **frame built, motors mounted Sep 19–20** |
| ESC + charger | Arrived — ESC staged on the stack; charger used for the first (supervised, in-bag) charge Sep 20 |
| Soldering iron (YIHUA 939D+, 75 W) | Arrived Sep 19 — tested at temperature the same day |
| Helping-hands station with magnifier | Ordered Sep 21 (~$20) — arrives Sep 22 |
| Flight controller (SkyStars H743 HD, single gyro) | **Arrived Oct 11** ($80.99, Amazon/GetFPV) — shipped on Betaflight 4.5.3, flashed to 2026.6.2 (CRSF · digital OSD · DShot) the same day |
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

## The FC landed — Oct 11

Powered on the day it arrived, as promised.

- [x] USB power-on, Configurator connects (factory Betaflight 4.5.3)
- [x] Flashed **Betaflight 2026.6.2** — the first try hung in DFU, see [Day 03](../build-log/2026-10-11-day-03.md)
- [x] Battery on the stack: 24.49 V, 6S detected
- [ ] Accelerometer calibrated · `diff all` saved to `hardware/`
- [ ] Power tab: capacity 1530 mAh, current scale from the KO60II manual
- [ ] Continuity audit complete (motor pads included)
- [ ] Spin motors from Betaflight, props off. **That's bench-alive.**

## Then: two flight tests

Flight test 1 flies **standard Betaflight**. Flight test 2 flies **firmware
written from scratch** for this same H743, after a bench-then-rig firmware
track. Steps, gates and wiring diagrams are on the
[build roadmap](https://claude.ai/artifact/TSb7eo9mAvQgAtfM15WNNo); the plan
for the code is in [code/README.md](../code/README.md).

## Open questions

- Tools budget is $122 over (the charger is counted in it).
- Project One isn't in the stage budget plan yet — see [RECEIPTS.md](../RECEIPTS.md).

---
Daily record: [build-log/](../build-log/) · Money: [RECEIPTS.md](../RECEIPTS.md) ·
Quick list: [PARTS-BOUGHT.md](PARTS-BOUGHT.md) ·
Live pages: [build roadmap](https://claude.ai/artifact/TSb7eo9mAvQgAtfM15WNNo) · [interactive tracker](https://claude.ai/artifact/7uWwutntfPKyU8hupoE4K8) · [Build Day 1 checklist](https://claude.ai/artifact/4GPMzLcXZW3vpemujTUTYw)
