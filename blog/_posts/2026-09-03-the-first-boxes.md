---
layout: post
title: "The first boxes arrive"
stage: "Build · Entry 05"
date: 2026-09-03
summary: >-
  Four of the seven orders landed today: the frame, the motors, the battery,
  and the big Amazon box of tools. Nothing can be soldered yet, but there is
  finally hardware on the bench instead of tracking numbers.
---

Five days after the ordering spree, the doorbell started paying off. Four of
the seven orders arrived today:

- **The frame** — TBS Source One V6, still flat-packed carbon plates.
- **The motors** — four EMAX ECO II 2207s, satisfyingly heavy for their size.
- **The battery** — the GNB 6S pack. It went straight into the fireproof
  LiPo bag, which conveniently arrived in the same delivery wave.
- **The Amazon tools box** — thread locker, multimeter, hex drivers, solder,
  flux, solder wick, heat shrink, the XT60 pigtail, the capacitor, and the
  smoke stopper — the little connector whose whole job is to blow a fuse-like
  bulb instead of letting a wiring mistake burn out the electronics on first
  power-up.

Still in transit: the ESC and charger (due today, so probably tomorrow), the
flight controller, and — critically — the soldering iron, which doesn't land
until September 10–17. That iron is the real schedule. Every part in these
boxes is inert until it exists.

## Things I learned unboxing

**You don't need a heat gun for heat shrink.** I stared at the bag of heat
shrink tubing for a while wondering what tool I'd forgotten to buy. Answer:
none. The barrel of the soldering iron held near (not on) the tubing shrinks
it, and so does the lower half of a lighter flame if you keep it moving. Since
heat shrink only goes on *after* soldering, the iron will already be on the
bench when I need it.

**The battery is not a toy.** It can't even be charged yet — the charger is
still in transit — so the safest thing it can do is sit in the fireproof bag,
which is where it now lives.

**Checklist for the week:** measure the motor screws against the frame's 6 mm
arms (too long shorts the motor windings, too short loses a motor in flight),
confirm the M3 screw assortment and safety glasses actually made it into the
Amazon box, and read the capacitor's can to confirm it says 1000 µF **35 V**
— a 25 V part on a 6S battery is a small bomb.

Until the iron arrives: software. Betaflight Configurator and the Windows
driver fixer go on the laptop this week, and the Matek and Skystars pinout
diagrams get printed and compared line by line.
