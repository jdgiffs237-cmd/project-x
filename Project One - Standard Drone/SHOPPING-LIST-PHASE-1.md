# Phase 1 Shopping List — Bench Alive

**Status: everything bought — 2026-08-29.** $797.97 across 7 orders.
Live tracker: [00-BUILD-TRACKER.md](00-BUILD-TRACKER.md)

**Goal:** motors spin on command, props off, frame clamped to the bench.

## What was bought

| Part | Pick | Paid | Where |
|---|---|---|---|
| Frame | TBS Source One V6, 5" | $42.53 | RMRC |
| Motors ×4 | EMAX ECO II 2207 1900KV | $60.95 | EMAX USA |
| Flight controller | ~~Matek H743-Slim V4~~ → **SkyStars H743 HD** (see below) | ~~$125.99~~ $80.99 | ~~MEPS King~~ Amazon / GetFPV |
| ESC | Skystars KO60II 60A AM32 | $58.49 | RaceDayQuads |
| Battery | GNB 6S 1530 mAh 160C | $58.92 | RaceDayQuads |
| Charger | HOTA D6 Pro 325W | $149.99 | RaceDayQuads |
| Soldering station | ~~AiXun T3A 200W~~ → **YIHUA 939D+ 75W** (see below) | ~~$135.68~~ $57.23 | Amazon |
| 13 tools + consumables | cap, XT60, solder, flux, wick, smoke stopper, multimeter, hex drivers, screws, shrink, Loctite, LiPo bag, glasses | $152.91 | Amazon |

Shipping and tax are included above. Order numbers: [RECEIPTS.md](../RECEIPTS.md).

## Two parts were swapped after the order

- **Soldering station:** the AiXun T3A was defective on arrival (Sep 11) and
  went back. Replaced with a YIHUA 939D+ — 75 W, less than half the price,
  enough for the job with the largest chisel tip at max temperature.
- **Flight controller:** the Matek H743 sat stuck in transit with an
  unresponsive vendor and was cancelled (Sep 19). Replaced with a SkyStars H743
  HD — same STM32H743 with 2 MB flash, so ArduPilot scripting is unaffected,
  and the same brand as the ESC, so the 8-pin harness should match.

Both refunds are pending; the current picture is in [PARTS-BOUGHT.md](PARTS-BOUGHT.md).

## Free software

- Betaflight Configurator
- ImpulseRC Driver Fixer — **install before first flash** (Windows driver trap)
- ESC Configurator (in Edge/Chrome) — for AM32

## Why the list changed from the original

- **Stack split:** SpeedyBee stack discontinued + closed ESC firmware → separate FC + AM32 ESC.
- **Matek FC:** only board that can run ArduPilot scripting (needs 2 MB flash). +$59.
- **Battery:** Tattu 75C was 40% short on current → GNB 160C.
- **Charger:** real price $150, not $65.

## Four things that will bite you

1. **Smoke stopper = first power-up only.** It trips if you spin motors through it.
2. **Motor screws:** arms are 6 mm. Too long shorts the motor. Aim for arm + 5 mm.
3. **Pinout:** Matek FC + Skystars ESC are different brands. Compare 8-pin diagrams, continuity check, then power.
4. **Capacitor must be 35 V.** 25 V ones blow on 6S.

## Not needed for Phase 1

Radio, receiver, props, GPS, goggles, camera, FAA stuff. See [BOM.md](BOM.md).
