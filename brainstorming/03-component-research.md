# 03 — Component Research

> A place to learn what each part *is*, then record candidates. Don't order anything until the compatibility checklist at the bottom passes for every pair.

**Last updated:** 2026-08-19

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
| **TBS Source One V5** ← pick | 5" | ~110 g | ~$35 | Open source, unibody arms sold individually, the most-documented 5" frame there is | Heavier than premium frames; no warranty |
| ImpulseRC Apex Evo | 5" | ~95 g | ~$90 | Very crash-resistant, excellent build ergonomics | 2.5× the price to break |
| Armattan Badger | 5" | ~100 g | ~$95 | Lifetime warranty on carbon | Price; overkill for a first build |

**Choice & why:** Source One V5. The relevant property for a first build isn't strength, it's **cheap to replace** — a $35 frame with $8 arms means a broken arm is an annoyance, not an event. Revisit on build two.

---

### Motors
Brushless. Labeled like `2207 1750KV`. First four digits = stator size (`22`mm wide × `07`mm tall); **KV** = RPM per volt unloaded. Higher KV = faster spin, less torque; lower KV = swings bigger props efficiently.

**Rule of thumb:** total thrust of all motors should be **at least 2×** the all-up weight; 3–4× for sport flying.

**Candidates:**

| Motor | Size/KV | Thrust @ prop/voltage | Price ea. | Notes |
|---|---|---|---|---|
| **iFlight XING2 2207 1855KV** ← pick | 2207 / 1855KV | ~1.5 kg @ 5.1×4.3×3, 6S | ~$22 | 6S standard, widely stocked, well-documented |
| T-Motor Velox V3 2207 1950KV | 2207 / 1950KV | similar | ~$25 | Excellent, slightly pricier |
| Emax ECO II 2207 1900KV | 2207 / 1900KV | similar | ~$15 | Budget option; shorter life |

**Choice & why:** XING2 2207 1855KV, ×4. 2207 at ~1800–1950KV on 6S is the single most common 5" configuration in existence, which means every tuning guide and every troubleshooting thread already assumes it.

> **The 6S-vs-4S fork:** picking 6S here constrains battery, ESC, and motor KV together. 6S is the current default — lower current for the same power, so thinner wire and cooler ESCs. Chosen deliberately, not by drift.

---

### ESCs (Electronic Speed Controllers)
Translate flight controller commands into motor phase current. Rated in **amps** — pick above your motors' peak draw, with margin. A **4-in-1 ESC** stacks with the flight controller and is much easier for a first build than four individual ESCs.

**Candidates:**

| ESC | Amp rating | 4-in-1? | Voltage (S) | Protocol (DShot?) | Price |
|---|---|---|---|---|---|
| **SpeedyBee F405 V4 55A stack** ← pick | 55 A | Yes | 3–6S | DShot600 | ~$75 (with FC) |
| SpeedyBee F7 V3 + 55A | 55 A | Yes | 3–6S | DShot600 | ~$80 |

**Choice & why:** bought as a matched stack — see FC below. 55 A against a 2207/1855KV peak draw of ~30 A/motor is comfortable margin.

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
| **SpeedyBee F405 V4** ← pick | F405 | Betaflight, INAV | 30.5×30.5 | ~$75 as a stack with the 55 A ESC |

**Choice & why:** ships as a stack, so the FC↔ESC interconnect is guaranteed to fit — the specific mistake the BOM warns about. Onboard Bluetooth means Betaflight can be configured from a phone, which matters more than it sounds for a first build: it removes the USB-driver-on-macOS failure mode from the very first power-up.

**Firmware:** Betaflight — matches the Project One mission (manual sport flying). ArduPilot is Stage 1's problem, on different hardware.

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
| **6S 1300 mAh 100C** ← pick | 6S | 1300 | 100C | ~200 g | XT60 | ~$35 |

**Choice & why:** 6S 1300 mAh is the default pack for a 5" on 6S. **One** pack for Phase 1 — a bench test needs exactly one. Packs 2–4 are a Phase 2 purchase, and buying them later avoids storing charged LiPos for months while the build is in progress.

---

### Radio link (control)
Transmitter (the thing in your hands) + receiver (on the drone). Protocols: **ELRS** (current default — cheap, long range, open), **Crossfire/TBS**, **FrSky**, **DJI**. TX and RX must match protocol.

> The radio transmitter outlives every drone you build. Buy a decent one once.

**Candidates:**

| Item | Price | Notes |
|---|---|---|
| RadioMaster Pocket ELRS (TX) | ~$65 | Phase 2. Genuinely good, genuinely cheap |
| RadioMaster Boxer / TX16S (TX) | ~$150 / ~$200 | Phase 2. Buy-once-buy-well option |
| Any ELRS 2.4 GHz receiver (RX) | ~$15 | Phase 2 |

**Choice & why:** **ELRS** as the protocol — current default, open, cheap, long range. Specific transmitter deferred to Phase 2; the decision that matters now is only that it will be ELRS, so the receiver bought later matches.

---

### Video link (only if FPV)
- **Analog** — cheap, low latency, mature, low resolution.
- **Digital (DJI / HDZero / Walksnail)** — much better image, more money, ecosystem lock-in.
- **None** — if flying line-of-sight or autonomously.

**Candidates:** deferred to Phase 3 — see [BOM](../Project%20One%20-%20Standard%20Drone/BOM%20Claude.md). Deliberately undecided: analog vs. digital is the most expensive reversible-only-by-rebuying choice in the project, and nothing about building the airframe depends on it.

---

### GPS / compass, telemetry, extras
Needed for position hold, return-to-home, and any autonomy. Skip for pure sport builds.

**Candidates:** none — out of scope for Project One (Betaflight sport build). This is Stage 1's territory, on ArduPilot hardware.

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
