# WI-02 — ESC soldering: motors, XT60, capacitor

**Needs:** WI-01 complete. **Does not need:** the flight controller.
**No battery in this WI. First power-up is WI-03, through the smoke stopper, after the pinout check.**

## Tools & parts

Iron with **largest chisel tip**, solder (63/37), flux, wick, side cutters,
heat shrink, ESC, XT60 pigtail (or the one from the ESC box), capacitor
(**read the can: 1000 µF 35 V** — the stripe side is negative), safety glasses.

## Operations

### Op 10 — Motor wires → ESC pads (12 joints, ~1.5 h)

1. Trim each motor wire at the tape mark from WI-01 Op 50. Strip ~2 mm, tin.
2. Tin all 12 ESC motor pads: flux, 350–370 °C, small blob per pad.
3. Solder each wire: iron on pad+wire, feed a little solder, hold still 2 s.
   Wire order per corner doesn't matter — motor direction is fixed in software.
4. CHECK each joint: shiny cone, no ball, no bridge to the neighbor. Tug test.

### Op 20 — XT60 + capacitor on the battery pads (~45 min)

**These are the two big joints. Max temperature (480 °C), largest tip, patience —
let the pad fully wet before feeding solder. 75W needs a few extra seconds, not force.**

1. Slide heat shrink onto the XT60 leads BEFORE soldering (it can't go on after).
2. Tin the big pads generously. Solder XT60: **red → +, black → −.** Triple-check
   before the iron touches — reversed polarity destroys the ESC instantly.
3. Solder the capacitor across the same pads, legs short: **stripe to −.**
4. Shrink all shrink. CHECK: no exposed copper anywhere on the battery side.

### Op 30 — Continuity audit (~20 min)

Multimeter on continuity, **no battery anywhere near the bench**:

1. CHECK: XT60 + to − reads OPEN (a brief cap charging blip is fine; a solid
   beep means a short — STOP and find it).
2. CHECK: each motor wire beeps to its own pad, and not to any neighbor pad.
3. CHECK: + pad does not beep to any motor pad or the frame; − likewise
   (except intended grounds).

**End state:** powertrain fully soldered and audited, still never powered.
WI-03 (FC install + smoke-stopper first power) unblocks when the SkyStars lands.
