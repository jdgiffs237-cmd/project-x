# Phase 1 Shopping List — Bench Alive

**Created:** 2026-08-19
**Goal:** motors spinning on command, props off, frame clamped to the bench
**Est. total:** ~$530 · **Log actual spend in [RECEIPTS.md](../RECEIPTS.md)**

> Links are Amazon where a genuine listing exists. Prices approximate, unverified
> at time of writing — confirm at checkout.
>
> **⚠ Clone warning.** Amazon is full of listings titled *"Compatible For
> SpeedyBee…"* / *"Compatible With TBS…"*. Those are third-party copies, not the
> real part. Every link below is the genuine article — check the brand name is
> the *first* word of the title, not preceded by "Compatible" or "For".
>
> **💰 Amazon is not the cheapest source** for the frame, stack, and motors —
> GetFPV, RaceDayQuads, and Pyrodrone typically run 20–40% lower on those three
> and are the primary distributors. Amazon wins on tools and charging gear.

---

## The aircraft — ~$230

| Part | Description | Link |
|---|---|---|
| **Frame** | Team BlackSheep TBS Source One V5, 5" kit. ~$35 | https://www.amazon.com/Team-Blacksheep-TBS-Source-Frame/dp/B0BJKTB3XK |
| **Motors** | iFlight XING2 2207 1855KV 6S, **4-pack**. ~$90 | https://www.amazon.com/iFlight-XING2-1855KV-Unibell-Titanium/dp/B09249RZLV |
| **FC + ESC stack** | SpeedyBee F405 V4 + 55A 4-in-1, 30×30, Bluetooth. ~$75 | https://www.amazon.com/SpeedyBee-F405-Flight-Controller-Stack/dp/B0CL3YLY6J |
| **Capacitor** | 1000 µF 35 V low-ESR, across the battery pads. ~$8 | https://www.amazon.com/s?k=1000uf+35v+low+esr+capacitor+fpv |
| **XT60 pigtail** | 12 AWG, male. ~$8 | https://www.amazon.com/s?k=XT60+male+pigtail+12awg+silicone |
| **Heat shrink kit** | Assorted, incl. large sizes for the pigtail. ~$10 | https://www.amazon.com/s?k=heat+shrink+tubing+assortment+kit |
| **Zip ties + thread locker** | Blue (removable) Loctite 243, not red. ~$12 | https://www.amazon.com/s?k=blue+threadlocker+243 |

## Power — ~$115

| Part | Description | Link |
|---|---|---|
| **Battery** | Tattu 6S 1300 mAh 75C, XT60. **One is enough for Phase 1.** ~$35 | https://www.amazon.com/TATTU-1300mah-Battery-Lumenier-Raceblade/dp/B07D4JF6L9 |
| *(alt)* | CNHL 6S 1300 mAh 130C, 2-pack — better value if buying two anyway | https://www.amazon.com/CNHL-1300mAh-Quadcopter-Helicopter-Airplane/dp/B0DN1P32DM |
| **Charger** | HOTA D6 Pro. **AC-capable** — no separate power brick needed. ~$65 | https://www.amazon.com/HOTA-D6-Pro-Balance-Charger/dp/B0BCJRDSRG |
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

## Two things that will bite you

**The smoke stopper caps at ~1 A.** It is for the *first power-up smoke test
only* — plug it in, confirm no short, confirm the FC boots. You **cannot spin
motors through it**; it will trip instantly. Motor spin-up happens on the bare
battery, after the smoke test passes.

**The stack is the clone minefield.** Search results are dominated by
"Compatible For Speedybee F405 V4" listings. Genuine SpeedyBee boards are the
only ones the SpeedyBee app and its Bluetooth config will reliably talk to —
which is the specific reason this stack was chosen.

---

## Not on this list, on purpose

Radio transmitter, receiver, propellers, FAA registration, Remote ID, goggles,
camera, VTX. None are needed to reach bench-alive. See
[BOM Claude.md](BOM%20Claude.md) for Phases 2 and 3.
