# Phase 1 Shopping List — Bench Alive

**Created:** 2026-08-19 · **Stock + prices re-verified: 2026-08-22**
**Goal:** motors spinning on command, props off, frame clamped to the bench
**Est. total:** ~$620 (was ~$530) · **Log actual spend in [RECEIPTS.md](../RECEIPTS.md)**

> **⚠ READ THIS FIRST — the original list is stale.** Three of the four core
> parts were out of stock or discontinued when re-checked on 2026-08-22, and the
> charger was priced at less than half its real cost. See
> [What changed and why](#what-changed-and-why) at the bottom. The tables below
> are the corrected version.
>
> **⚠ Clone warning.** Amazon is full of listings titled *"Compatible For
> SpeedyBee…"* / *"Compatible With TBS…"*. Those are third-party copies, not the
> real part. Check the brand name is the *first* word of the title, not preceded
> by "Compatible" or "For".
>
> **💰 Buy the aircraft parts from FPV specialists, not Amazon.** RMRC,
> Pyrodrone, GetFPV, and RaceDayQuads are the primary distributors and are the
> only places currently holding stock. Amazon wins on tools and consumables.

---

## The aircraft — ~$232

Stock status verified 2026-08-22 against live vendor inventory.

| Part | Description | Link |
|---|---|---|
| **Frame** | TBS Source One **V6**, 5" kit. $35.85 — ✅ in stock at RMRC | https://www.readymaderc.com/products/details/85715-tbs-source-one-v5-5-inch-kit |
| **Motors** | EMAX ECO II 2207 **1900KV**, ×4 @ $15.99 = $63.96 — ✅ in stock at Pyrodrone | https://pyrodrone.com/products/emax-eco-ii-2207-stator-motor-for-5-propeller-racing-and-freestyle-craft-1900kv |
| *(alt motors)* | iFlight XING2 **2306 1755KV**, ×4 @ $27.99 = $112 — ✅ in stock, nicer motor | https://pyrodrone.com/products/iflight-xing2-2306-1755kv-motor |
| **FC + ESC stack** | SpeedyBee F405 **V5** OX32 55A, 30×30, Bluetooth. ~$94 MSRP — ✅ in stock at RMRC. **Read the OX32 note below.** | https://www.readymaderc.com/products/details/86580-speedybee-f405-v5-ox32-55a-30x30-model-aircraft-fc-esc-stack |
| **Capacitor** | 1000 µF 35 V low-ESR, across the battery pads. ~$8 | https://www.amazon.com/s?k=1000uf+35v+low+esr+capacitor+fpv |
| **XT60 pigtail** | 12 AWG, male. ~$8 | https://www.amazon.com/s?k=XT60+male+pigtail+12awg+silicone |
| **Heat shrink kit** | Assorted, incl. large sizes for the pigtail. ~$10 | https://www.amazon.com/s?k=heat+shrink+tubing+assortment+kit |
| **Zip ties + thread locker** | Blue (removable) Loctite 243, not red. ~$12 | https://www.amazon.com/s?k=blue+threadlocker+243 |

## Power — ~$200

| Part | Description | Link |
|---|---|---|
| **Battery** | Tattu 6S 1300 mAh 75C, XT60. **One is enough for Phase 1.** ~$35 | https://www.amazon.com/TATTU-1300mah-Battery-Lumenier-Raceblade/dp/B07D4JF6L9 |
| *(alt)* | CNHL 6S 1300 mAh 130C, 2-pack — better value if buying two anyway | https://www.amazon.com/CNHL-1300mAh-Quadcopter-Helicopter-Airplane/dp/B0DN1P32DM |
| **Charger** | HOTA D6 Pro 325W. **AC-capable** — no separate power brick needed. **$149.99**, not $65 — the original estimate was wrong. ✅ in stock at RDQ, both colors | https://www.racedayquads.com/products/hota-d6-pro-dual-channel-325w-15a-ac-dc-battery-charger |
| **LiPo-safe bag** | COLCASE fireproof, large. ~$15 | https://www.amazon.com/COLCASE-Fireproof-Explosionproof-Charging-198x150x135mm/dp/B0719H46PF |

## Tools — ~$185

| Part | Description | Link |
|---|---|---|
| **Soldering station** | AiXun T3A 200W, T245 handle + 3 tips. ~$70 | https://www.amazon.com/AiXun-Temperature-Controlled-Soldering-Station/dp/B0FKRH7S2G |
| **Solder** | 63/37 **leaded**, rosin core, 0.8 mm. Not lead-free. ~$15 | https://www.amazon.com/s?k=63%2F37+rosin+core+solder+0.8mm |
| **Flux** | Rosin paste flux in a tub. ~$10 | https://www.amazon.com/s?k=rosin+paste+flux+soldering |
| **Solder wick** | For undoing mistakes. ~$6 | https://www.amazon.com/s?k=solder+wick+desoldering+braid |
| **Smoke stopper** | iFlight XT30/XT60 w/ buzzer. **Read the note below.** ~$15 | https://www.amazon.com/iFlight-Stopper-Short-Circuit-Protection-Inspecting/dp/B08MT4YKJY |
| **Multimeter** | Any with a continuity beep. ~$30 | https://www.amazon.com/s?k=digital+multimeter+continuity+beep |
| **Hex drivers** | Metric 1.5 / 2.0 / 2.5 mm, quality steel. ~$25 | https://www.amazon.com/s?k=metric+hex+driver+set+rc+1.5mm+2mm+2.5mm |
| **Safety glasses** | ~$10 | https://www.amazon.com/s?k=safety+glasses+ansi+z87 |

---

## Three things that will bite you

**The smoke stopper caps at ~1 A.** It is for the *first power-up smoke test
only* — plug it in, confirm no short, confirm the FC boots. You **cannot spin
motors through it**; it will trip instantly. Motor spin-up happens on the bare
battery, after the smoke test passes.

**The stack is the clone minefield.** Search results are dominated by
"Compatible For Speedybee F405 V4/V5" listings. Genuine SpeedyBee boards are the
only ones the SpeedyBee app and its Bluetooth config will reliably talk to —
which is the specific reason this stack was chosen.

**The V5 stack runs closed-source ESC firmware.** The V4's ESC ran BLHeli_S; the
V5's OX32 ESC runs SpeedyBee's own proprietary firmware instead, which was
unpopular enough to be the main complaint in every V5 review. For Phase 1 this
costs you nothing — the FC still runs Betaflight, Bluetooth config still works,
and you actually *gain* ESC RPM telemetry. It matters later only if you wanted
to flash Bluejay or AM32 yourself. If that bothers you, hunt a leftover V4 at
ProgressiveRC rather than buying a clone.

---

## What changed and why

Re-checked 2026-08-22 against live vendor inventory. The original list was
written 2026-08-19 with unverified prices, and most of it no longer holds.

**Verified out of stock or discontinued:**

| Part | What happened |
|---|---|
| TBS Source One **V5** frame | Superseded by V6. Zero inventory at RDQ ($49.99), Pyrodrone, and defianceRC (V5.1, $34.99). |
| iFlight XING2 2207 **1855KV** | Zero inventory at RDQ, Pyrodrone, and WREKD. iFlight's own store no longer lists 1855KV at all — only 1750 / 2050 / 2750KV. |
| SpeedyBee F405 **V4** stack | **Discontinued by SpeedyBee**, replaced by the V5. RMRC's V4 product page is dead. |
| HOTA D6 Pro | Out at Pyrodrone. Also **mispriced in the original list at ~$65 — it is ~$150.** |
| EMAX ECO II 2207 **1700KV** | The obvious 6S substitute for the XING2 — also out at both Pyrodrone and RDQ. |

**Why so much is gone at once.** New US tariffs on drones and drone components
(25–100%) were announced on 2026-08-14 and take effect **2026-09-03**, with
airframe parts and props hit at 25% from 2027-02-09. Retailers are being cleaned
out by pre-tariff buying and restocks will land at higher prices. SpeedyBee's
own store is already collecting a 54% prepaid tax on US orders.

**What this means for the build:** everything imported on this list gets more
expensive after 2026-09-03. If the Phase 1 budget is going to happen at all,
it should happen in the next ~10 days. The tools and consumables are the
flexible part — the frame, motors, stack, and charger are the ones to secure now.

**A note on the motors.** 1700KV is the textbook KV for a 6S 5-inch build, and
every 2207 at that KV is currently sold out. The substituted ECO II 2207
**1900KV** is rated 3–6S, so it is legitimate on 6S, just a little hotter than
ideal. For Phase 1 this is irrelevant — the props are off and the motors only
need to spin on command. If you would rather not compromise on the motor you
will fly, the in-stock iFlight XING2 **2306 1755KV** is the better motor at
$27.99 each, and 2306 is a fine stator for 5-inch 6S.

---

## Not on this list, on purpose

Radio transmitter, receiver, propellers, FAA registration, Remote ID, goggles,
camera, VTX. None are needed to reach bench-alive. See
[BOM Claude.md](BOM%20Claude.md) for Phases 2 and 3.
