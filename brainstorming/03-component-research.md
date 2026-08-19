# 03 — Component Research

> A place to learn what each part *is*, then record candidates. Don't order anything until the compatibility checklist at the bottom passes for every pair.

**Last updated:** _(YYYY-MM-DD)_

---

## The subsystems

A multirotor is roughly ten interacting parts. Understand what each does before shopping.

### Frame
Carbon fiber (usually) skeleton. Sized by **motor-to-motor diagonal in mm** or by **propeller size in inches**.

| Class | Prop size | Typical use | Notes |
|---|---|---|---|
| Tiny whoop | 1–2" | Indoor, ducted | Very safe, very cheap, limited outdoors |
| Micro / sub-250g | 2.5–3.5" | Legal-light flying, parks | Dodges registration + Remote ID if under 250 g |
| 5" | 5" | The default FPV/freestyle size | Huge parts ecosystem, most tutorials assume it |
| 7" | 7" | Long range, efficiency | Heavier, more dangerous, more expensive |
| 10"+ / heavy lift | 10"+ | Camera payloads, mapping | Serious money and serious risk |

**Candidates:**

| Frame | Size | Weight | Price | Pros | Cons |
|---|---|---|---|---|---|
| | | | | | |

---

### Motors
Brushless. Labeled like `2207 1750KV`. First four digits = stator size (`22`mm wide × `07`mm tall); **KV** = RPM per volt unloaded. Higher KV = faster spin, less torque; lower KV = swings bigger props efficiently.

**Rule of thumb:** total thrust of all motors should be **at least 2×** the all-up weight; 3–4× for sport flying.

**Candidates:**

| Motor | Size/KV | Thrust @ prop/voltage | Price ea. | Notes |
|---|---|---|---|---|
| | | | | |

---

### ESCs (Electronic Speed Controllers)
Translate flight controller commands into motor phase current. Rated in **amps** — pick above your motors' peak draw, with margin. A **4-in-1 ESC** stacks with the flight controller and is much easier for a first build than four individual ESCs.

**Candidates:**

| ESC | Amp rating | 4-in-1? | Voltage (S) | Protocol (DShot?) | Price |
|---|---|---|---|---|---|
| | | | | | |

---

### Flight Controller (FC)
The brain: IMU + processor running firmware. The firmware choice is a **fork in the road** for the whole project.

| Firmware | Best for | Trade-off |
|---|---|---|
| **Betaflight** | FPV, racing, freestyle, manual flight | Minimal autonomy; not built for waypoints |
| **INAV** | GPS-assisted fixed-wing/multirotor, return-to-home, simple missions | Middle ground; smaller community than either neighbor |
| **ArduPilot** | Autonomy, missions, research, heavy lift | Steep learning curve, huge capability |
| **PX4** | Autonomy, robotics/ROS integration, academic | Steepest curve, most "software project" |

**Choice & why:** ______

**Candidates:**

| FC | MCU | Firmware support | Mounting (30.5×30.5? 20×20?) | Price |
|---|---|---|---|---|
| | | | | |

---

### Propellers
Sized `diameter × pitch × blades`, e.g. `5×4.3×3`. Cheap, consumable, and the part you will destroy most often. **Buy many spares.** They are also the part that injures people — treat them as the sharp edge of the machine.

---

### Battery (LiPo)
Labeled like `4S 1500mAh 100C`. **S** = cells in series (voltage: 1S ≈ 3.7 V nominal); **mAh** = capacity; **C** = discharge rate.

> **Safety, non-negotiable:** LiPo batteries are a genuine fire hazard. Charge on a non-flammable surface, in a LiPo bag or ammo can, never unattended, never overnight. Never charge a puffed, dented, or crashed pack. Store at ~3.8 V/cell, not full. Dispose of damaged packs properly (many hobby shops take them).

**Candidates:**

| Battery | S | mAh | C | Weight | Connector (XT30/XT60?) | Price |
|---|---|---|---|---|---|---|
| | | | | | | |

---

### Radio link (control)
Transmitter (the thing in your hands) + receiver (on the drone). Protocols: **ELRS** (current default — cheap, long range, open), **Crossfire/TBS**, **FrSky**, **DJI**. TX and RX must match protocol.

> The radio transmitter outlives every drone you build. Buy a decent one once.

**Candidates:** ______

---

### Video link (only if FPV)
- **Analog** — cheap, low latency, mature, low resolution.
- **Digital (DJI / HDZero / Walksnail)** — much better image, more money, ecosystem lock-in.
- **None** — if flying line-of-sight or autonomously.

**Candidates:** ______

---

### GPS / compass, telemetry, extras
Needed for position hold, return-to-home, and any autonomy. Skip for pure sport builds.

**Candidates:** ______

---

### Tools & consumables (budget for these — first-timers forget)
- [ ] Temperature-controlled soldering iron (a bad iron ruins boards)
- [ ] Solder (leaded 63/37 is easier), flux, wick
- [ ] Helping hands / vise
- [ ] Hex drivers (metric, quality — cam-out strips frame screws)
- [ ] Multimeter
- [ ] Smoke stopper (limits current on first power-up — cheap insurance)
- [ ] LiPo charger + charging bag
- [ ] Battery voltage checker
- [ ] Zip ties, heat shrink, thread locker, double-sided foam tape
- [ ] Safety glasses (props at full throttle are dangerous)
- [ ] Spare props (many)

---

## Compatibility checklist — verify EVERY pair before ordering

- [ ] Battery cell count (S) is within the ESC's rated voltage range
- [ ] Battery cell count is within the motors' rated voltage range
- [ ] ESC amp rating exceeds motors' max continuous draw, with margin
- [ ] Motor mounting hole pattern matches the frame's arms
- [ ] Prop size fits the frame without overlap
- [ ] FC mounting pattern matches the stack/frame (30.5×30.5 mm vs 20×20 mm)
- [ ] FC and ESC connect with the same plug/pinout (or you plan to solder)
- [ ] FC firmware supports every peripheral you're buying
- [ ] Receiver protocol matches the transmitter
- [ ] Receiver voltage input matches what the FC supplies (5 V vs 3.3 V — this kills receivers)
- [ ] Connectors match end to end (XT30 vs XT60 vs solder pads)
- [ ] Camera voltage matches FC/VTX output
- [ ] All-up weight is under the frame's and motors' sensible limits
- [ ] All-up weight lands on the intended side of 250 g (if that's a requirement)

---

## Guiding questions

- For each part: **why this one instead of the obvious cheaper one?** If there's no answer, buy the cheaper one.
- Is this part well-supported and current, or a dead-end I found in a 6-year-old video? Drone parts turn over fast.
- Can I get it from one vendor to save shipping and simplify returns?
- What's the failure mode if this part dies mid-flight? Which single failure destroys the aircraft?
