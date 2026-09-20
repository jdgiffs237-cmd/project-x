# WI-01 — Bench setup, frame assembly, motor mounting

**Needs:** everything that has arrived. **Does not need:** the flight controller.
**Battery stays in the LiPo bag for this entire WI. It is not needed and not used.**

## Tools & parts

Iron (YIHUA 939D+), hex drivers, multimeter, safety glasses, Loctite 243 (blue),
frame kit, 4 motors, M3 screw assortment, ESC, solder/flux/wick, scrap wire.

## Operations

### Op 10 — Prove the new iron works (15 min)

The AiXun sat in its box and cost a week. Not this time.

1. Power on the YIHUA. Set 350 °C / 662 °F. CHECK: display reaches and holds temperature.
2. Fit the **largest chisel tip**. Tin it: touch solder to the hot tip — it should
   flow and coat instantly, not ball up.
3. **Practice on scrap:** tin two scrap wire ends, join them, shrink a piece of
   heat shrink over the joint (iron barrel held near, rotate). CHECK: joint is
   shiny and solid, shrink is tight. Do this three times before Op 50.

### Op 20 — Inventory the open boxes (10 min)

1. Amazon bundle: CHECK: M3 screw assortment present. CHECK: safety glasses present.
   (Both still unconfirmed in the tracker — clear the flags.)
2. ESC box: CHECK: note whether a capacitor and/or XT60 lead is included. Better
   part goes on the aircraft, other becomes the spare.
3. Battery: with the multimeter, measure pack voltage at the XT60.
   CHECK: ~22.2–22.8 V (storage charge). Back in the bag.
   **PASSED 2026-09-20 — 22.80 V, cells within 13 mV.** Charging procedure is
   [WI-02.5](WI-02.5-first-charge-and-battery-handling.md).

### Op 30 — Assemble the frame (45 min)

1. Lay out the Source One V6 plates and hardware per the kit sheet.
2. Assemble bottom plate + arms + standoffs. Frame kit M3×10/12/14 screws are
   the standoff hardware — **they are not motor screws.**
3. One drop of **blue** Loctite on each frame bolt. Snug, not gorilla-tight —
   carbon crushes.
4. CHECK: arms sit flat, no rock on a flat surface; stack holes line up 30×30.

### Op 40 — Motor screw length, then mount motors (45 min)

**Wrong screw length is the #1 motor killer. Do the math before driving any screw.**

1. Measure arm thickness with calipers or the multimeter case edge (~6 mm).
2. Target thread into the motor = **arm + ~5 mm**. Measure the motor's blind
   hole depth. Pick screws from the assortment. CHECK: screw tip sits at least
   1 mm short of the hole bottom when test-fitted through the arm.
3. Safety glasses on. Mount all 4 motors, blue Loctite, cross-pattern snug.
   Dab the Loctite onto a paper towel and **dip the screw threads** rather than
   squeezing it into the motor's blind hole — it can't wick down onto the
   windings that way, and the excess stays off the bell.
4. CHECK: each motor spins by hand freely, no scraping, no wobble.
5. Do **not** trim motor wires yet — final length depends on ESC placement (WI-02).

**Photos:** [threadlocker dip](images/wi01-threadlocker-dip.jpg) ·
motor mounted on the arm [1](images/wi01-motor-mounted-01.jpg)
[2](images/wi01-motor-mounted-02.jpg)
[3](images/wi01-motor-mounted-03.jpg)
[4](images/wi01-motor-mounted-04.jpg)

### Op 50 — Stage the ESC (15 min)

1. Dry-fit the ESC on the stack standoffs, arrow/battery pads facing rear.
2. Route each motor's 3 wires to its ESC corner. Mark trim length with tape.
3. CHECK: wires reach their pads with a little slack, no wire crosses a prop line.

**End state:** frame assembled, motors mounted and verified, ESC staged, iron
proven, all inventory flags cleared. Next: [WI-02 — ESC soldering](WI-02-esc-soldering.md).
