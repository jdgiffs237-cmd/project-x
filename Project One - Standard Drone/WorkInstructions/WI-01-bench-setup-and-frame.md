# WI-01 — Bench setup, frame assembly, motor mounting

| | |
|---|---|
| **Status** | **Complete — 2026-09-20** |
| **Needs** | Everything that has arrived. **Not** the flight controller. |
| **Battery** | Stays in the LiPo bag for the entire WI. Not needed, not used. |
| **Time** | ~2 h 15 min across five operations |

This WI is a slide deck: one slide per step, one photo, and the check that
proves the step is done. Walk it with the **Next ▶** link at the bottom of each
slide, or jump in from the deck list. PowerPoint / Google Slides version:
[WI-01-bench-setup-and-frame.pptx](WI-01-bench-setup-and-frame.pptx).

## Deck

| # | Slide | Op |
|---|---|---|
| 1 | [Tools & parts on the bench](#slide-1-tools--parts-on-the-bench) | — |
| 2 | [Prove the iron: heat, hold, tin](#slide-2-prove-the-iron-heat-hold-tin) | 10 |
| 3 | [Three practice joints on scrap](#slide-3-three-practice-joints-on-scrap) | 10 |
| 4 | [Inventory the open boxes](#slide-4-inventory-the-open-boxes) | 20 |
| 5 | [Battery storage-voltage check](#slide-5-battery-storage-voltage-check) | 20 |
| 6 | [Lay out the frame kit](#slide-6-lay-out-the-frame-kit) | 30 |
| 7 | [Bottom plate, arms, standoffs](#slide-7-bottom-plate-arms-standoffs) | 30 |
| 8 | [Frame check: flat and square](#slide-8-frame-check-flat-and-square) | 30 |
| 9 | [Motor screw length — do the math](#slide-9-motor-screw-length--do-the-math) | 40 |
| 10 | [Loctite: dab, dip, drive](#slide-10-loctite-dab-dip-drive) | 40 |
| 11 | [Seat the motor on the arm](#slide-11-seat-the-motor-on-the-arm) | 40 |
| 12 | [Drive the screws in a cross pattern](#slide-12-drive-the-screws-in-a-cross-pattern) | 40 |
| 13 | [Motor check: free spin, wires untrimmed](#slide-13-motor-check-free-spin-wires-untrimmed) | 40 |
| 14 | [Stage the ESC and route the wires](#slide-14-stage-the-esc-and-route-the-wires) | 50 |
| 15 | [End state](#slide-15-end-state) | — |

---

## Slide 1: Tools & parts on the bench

<img src="images/wi-01/01-tools-and-parts.jpg" width="480" alt="The tools and parts for WI-01 laid out on the bench before starting">

**On the bench before starting**

- Soldering station — YIHUA 939D+ (75 W) with the largest chisel tip
- Hex driver set, multimeter, calipers if you have them
- Safety glasses
- Loctite 243 (blue)
- Frame kit — TBS Source One V6, 5"
- Motors ×4 — EMAX ECO II 2207 1900KV
- M3 screw assortment
- ESC — Skystars KO60II 60A AM32
- Solder, flux, wick, scrap wire, heat shrink

**Check:** nothing on this list is still in a box you'd have to go find mid-step.

<sub>[Deck](#deck) · [Next ▶](#slide-2-prove-the-iron-heat-hold-tin)</sub>

---

## Slide 2: Prove the iron: heat, hold, tin

*Op 10 · 5 min*

<!-- photo: images/wi-01/02-iron-at-temperature.jpg -->

The AiXun sat in its box, turned out to be defective, and cost a week. The
first thing the new iron does is prove it works.

**Do**

1. Power on the YIHUA. Set **350 °C / 662 °F**.
2. Fit the **largest chisel tip**.
3. Tin it — touch solder to the hot tip.

**Check:** display reaches and *holds* temperature. Solder flows and coats the
tip instantly; if it balls up, the tip isn't hot or isn't clean.

<sub>[◀ Prev](#slide-1-tools--parts-on-the-bench) · [Deck](#deck) · [Next ▶](#slide-3-three-practice-joints-on-scrap)</sub>

---

## Slide 3: Three practice joints on scrap

*Op 10 · 10 min*

<!-- photo: images/wi-01/03-practice-joint.jpg -->

**Do** — three times, before any real joint:

1. Tin two scrap wire ends.
2. Join them.
3. Slide heat shrink over the joint and shrink it — iron barrel held near,
   rotate the wire. No heat gun needed.

**Check:** joint is shiny and solid, shrink is tight over it. Three in a row
that pass, or keep practicing.

<sub>[◀ Prev](#slide-2-prove-the-iron-heat-hold-tin) · [Deck](#deck) · [Next ▶](#slide-4-inventory-the-open-boxes)</sub>

---

## Slide 4: Inventory the open boxes

*Op 20 · 5 min*

<!-- photo: images/wi-01/04-inventory.jpg -->

**Do**

1. Amazon bundle — confirm the **M3 screw assortment** and the **safety
   glasses** are present.
2. ESC box — note whether a **capacitor** and/or **XT60 lead** is included.
   The better part goes on the aircraft; the other becomes the spare.

**Check:** both tracker flags cleared; ESC box contents written down.

<sub>[◀ Prev](#slide-3-three-practice-joints-on-scrap) · [Deck](#deck) · [Next ▶](#slide-5-battery-storage-voltage-check)</sub>

---

## Slide 5: Battery storage-voltage check

*Op 20 · 5 min*

<img src="images/wi-01/05a-battery-voltage-check.jpg" width="360" alt="Multimeter probes on the XT60 pins of the 6S pack, reading storage voltage">
<img src="images/wi-01/05b-battery-back-in-bag.jpg" width="360" alt="The GNB 6S pack back inside the open fireproof LiPo bag">

**Do**

1. Multimeter on DC volts.
2. Measure pack voltage at the XT60 — red probe to the + pin, black to −.
3. Straight back into the LiPo bag.

**Check:** **~22.2–22.8 V** for a 6S pack at storage charge (3.7–3.8 V per
cell). Anything far outside that range is a question for the charger, not the
bench.

<sub>[◀ Prev](#slide-4-inventory-the-open-boxes) · [Deck](#deck) · [Next ▶](#slide-6-lay-out-the-frame-kit)</sub>

---

## Slide 6: Lay out the frame kit

*Op 30 · 10 min*

<!-- photo: images/wi-01/06-frame-kit-layout.jpg -->

**Do**

1. Lay out every Source One V6 plate, arm, standoff, and bag of hardware
   against the kit sheet.
2. Sort the hardware by length. The kit's **M3×10 / 12 / 14 screws are
   standoff hardware — they are not motor screws.**

**Check:** everything on the kit sheet is present and sorted before a single
screw is driven.

<sub>[◀ Prev](#slide-5-battery-storage-voltage-check) · [Deck](#deck) · [Next ▶](#slide-7-bottom-plate-arms-standoffs)</sub>

---

## Slide 7: Bottom plate, arms, standoffs

*Op 30 · 30 min*

<img src="images/wi-01/07-frame-assembled.jpg" width="480" alt="The assembled Source One V6 frame — bottom plate, four arms, standoffs — on a paper towel, no motors yet">

**Do**

1. Bottom plate first, then the four arms, then the standoffs.
2. **One drop of blue Loctite** on each frame bolt.
3. **Snug, not gorilla-tight.** Carbon fibre crushes under an over-torqued bolt
   and there is no undoing it.

**Check:** every frame bolt has Loctite and is snug; no bolt bottomed out.

<sub>[◀ Prev](#slide-6-lay-out-the-frame-kit) · [Deck](#deck) · [Next ▶](#slide-8-frame-check-flat-and-square)</sub>

---

## Slide 8: Frame check: flat and square

*Op 30 · 5 min*

<!-- photo: images/wi-01/08-frame-flat-check.jpg -->

**Do**

1. Set the assembled frame on a flat surface and press each arm tip.
2. Sight down the stack holes.

**Check:** no rock on any arm. Stack holes line up on the **30 × 30 mm**
pattern — the FC and ESC both mount to it.

<sub>[◀ Prev](#slide-7-bottom-plate-arms-standoffs) · [Deck](#deck) · [Next ▶](#slide-9-motor-screw-length--do-the-math)</sub>

---

## Slide 9: Motor screw length — do the math

*Op 40 · 10 min*

<!-- photo: images/wi-01/09-screw-length-measure.jpg -->

**Wrong screw length is the #1 motor killer. A screw that reaches the windings
shorts the motor the first time it spins. Do the math before driving any screw.**

**Do**

1. Measure arm thickness — calipers, or the edge of the multimeter case (~6 mm).
2. Measure the motor's blind-hole depth.
3. Target thread into the motor = **arm + ~5 mm**. Pick screws from the
   assortment to match.

**Check:** test-fit a screw through the arm into a motor by hand — the tip sits
**at least 1 mm short** of the hole bottom.

<sub>[◀ Prev](#slide-8-frame-check-flat-and-square) · [Deck](#deck) · [Next ▶](#slide-10-loctite-dab-dip-drive)</sub>

---

## Slide 10: Loctite: dab, dip, drive

*Op 40 · 5 min*

<img src="images/wi-01/10a-loctite-dab-on-towel.jpg" width="240" alt="A drop of blue Loctite 243 squeezed onto a paper towel next to the motor screws">
<img src="images/wi-01/10b-loctite-dip-screw.jpg" width="240" alt="Screw tip being touched into the drop of Loctite">
<img src="images/wi-01/10c-loctite-on-screw.jpg" width="240" alt="Close-up of the blue Loctite coating the screw threads">

The bottle nozzle puts far too much on a screw this small. Dab, then dip.

**Do**

1. Squeeze **one drop** of blue Loctite 243 onto a paper towel.
2. Touch each screw's threads into the drop — a thin film, not a coating.
3. Drive it within a minute or two, before it starts to set.

**Check:** blue on the threads only, none on the screw head or the carbon.

<sub>[◀ Prev](#slide-9-motor-screw-length--do-the-math) · [Deck](#deck) · [Next ▶](#slide-11-seat-the-motor-on-the-arm)</sub>

---

## Slide 11: Seat the motor on the arm

*Op 40 · 10 min*

<img src="images/wi-01/11-motor-seated-on-arm.jpg" width="480" alt="EMAX ECO II motor held seated on the end of a carbon arm, wires trailing">

**Safety glasses on.**

**Do**

1. Set the motor on the arm end, bolt holes aligned with the arm's
   16 × 16 mm pattern.
2. Wires pointing **inboard**, toward the centre of the frame.
3. Hold it flat while the first screw goes in.

**Check:** motor base sits flush on the arm, all four holes visible through the
arm, wires headed toward the stack.

<sub>[◀ Prev](#slide-10-loctite-dab-dip-drive) · [Deck](#deck) · [Next ▶](#slide-12-drive-the-screws-in-a-cross-pattern)</sub>

---

## Slide 12: Drive the screws in a cross pattern

*Op 40 · 20 min*

<img src="images/wi-01/12-driving-motor-screws.jpg" width="480" alt="Hex driver driving a motor screw up through the arm into the motor base">

**Do**

1. Screws go up **through the arm, into the motor** — from underneath.
2. Drive them in a **cross pattern** — one corner, then the opposite corner,
   then the other pair — so the motor seats flat, not tilted.
3. Snug only. Same rule as the frame bolts.
4. Repeat for all four motors.

**Check:** all 16 screws in, all Loctited, no gap between motor base and arm on
any motor.

<sub>[◀ Prev](#slide-11-seat-the-motor-on-the-arm) · [Deck](#deck) · [Next ▶](#slide-13-motor-check-free-spin-wires-untrimmed)</sub>

---

## Slide 13: Motor check: free spin, wires untrimmed

*Op 40 · 5 min*

<img src="images/wi-01/13a-spin-check-left.jpg" width="360" alt="Motor bell being turned by hand, counter-clockwise">
<img src="images/wi-01/13b-spin-check-right.jpg" width="360" alt="Motor bell being turned by hand, clockwise">

**Do**

1. Spin each motor bell by hand — both directions.
2. Leave every motor wire at full length.

**Check:** each motor spins freely both ways — no scraping, no wobble, no tick.
A tick means a screw is touching the windings: **back it out now.** **Do not
trim motor wires yet;** final length depends on where the ESC sits.

<sub>[◀ Prev](#slide-12-drive-the-screws-in-a-cross-pattern) · [Deck](#deck) · [Next ▶](#slide-14-stage-the-esc-and-route-the-wires)</sub>

---

## Slide 14: Stage the ESC and route the wires

*Op 50 · 15 min*

<img src="images/wi-01/14-esc-staged-wires-routed.jpg" width="480" alt="Skystars KO60II ESC dry-fitted on the stack standoffs, motor wires from all four arms routed toward it">

**Do**

1. Dry-fit the ESC on the stack standoffs, **arrow / battery pads facing the
   rear** of the aircraft.
2. Route each motor's three wires to its ESC corner.
3. Mark the trim length on each wire with a scrap of tape.

**Check:** every wire reaches its pads with a little slack, and no wire crosses
a prop line.

<sub>[◀ Prev](#slide-13-motor-check-free-spin-wires-untrimmed) · [Deck](#deck) · [Next ▶](#slide-15-end-state)</sub>

---

## Slide 15: End state

<!-- photo: images/wi-01/15-end-state.jpg -->

**WI-01 is done when all of these are true:**

- Iron proven at temperature; three practice joints passed
- Inventory flags cleared; ESC box contents recorded
- Battery measured at storage voltage and back in the bag
- Frame assembled, Loctited, flat, stack holes on 30 × 30
- Four motors mounted with verified screw length; all spin free
- ESC staged; every motor wire routed and tape-marked, none trimmed

**Next:** [WI-02 — ESC soldering](WI-02-esc-soldering.md)

<sub>[◀ Prev](#slide-14-stage-the-esc-and-route-the-wires) · [Deck](#deck) · [Work instructions index](README.md)</sub>
