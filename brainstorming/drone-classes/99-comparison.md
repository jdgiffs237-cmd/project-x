# 99 — Comparison and Recommendation

All five DoD Groups side by side, what the framework does and doesn't decide for you, and a straight recommendation for your build.

---

## The five Groups at a glance

| | **Group 1** | **Group 2** | **Group 3** | **Group 4** | **Group 5** |
|---|---|---|---|---|---|
| **Max weight** | < 20 lb | 21–55 lb | 55–1,320 lb | > 1,320 lb | > 1,320 lb |
| **Altitude** | < 1,200 ft AGL | < 3,500 ft AGL | < 18,000 ft MSL | < 18,000 ft MSL | > 18,000 ft MSL |
| **Speed** | < 100 kt | < 250 kt | < 250 kt | Any | Any |
| **Launch** | Hand / VTOL | Catapult / rail | Catapult / runway | Runway | Runway |
| **Recovery** | Land anywhere | Net / hook | Net / arrested | Runway | Runway |
| **Propulsion** | Battery-electric | Electric or piston | Piston / turboprop | Turboprop / piston | Turbofan / turboprop |
| **Endurance** | 5 min – 2 hr | 10–24 hr | 10–24 hr | 20–30 hr | 24–40+ hr |
| **Crew** | 1 person | 2–4 | 4–10 | 10+ shifts | 10+ shifts |
| **Control link** | Line of sight | LOS / limited BLOS | LOS / BLOS | Satellite | Satellite |
| **Cost per aircraft** | $150 – $60k | $100k – $250k | $500k – $2M | $4M – $20M | $15M – $180M |
| **Example** | RQ-11 Raven | ScanEagle | RQ-7 Shadow | MQ-1 Predator | MQ-9 Reaper |
| **Civilian-operable?** | **Yes** (Part 107 / §44809) | **Yes** (Part 107) | Exemption only | No | No |
| **Buildable by you?** | **Yes** | No | No | No | No |

---

## What this framework does and doesn't tell you

**What it's genuinely good for:**

- **Scale calibration.** The taxonomy spans a factor of ~440,000 in mass, from a 33 g Black Hornet to a 32,000 lb Global Hawk. Knowing that range is the fastest cure for thinking "drone" is a meaningful description on its own.
- **Understanding why thresholds exist.** Each boundary marks a change in what the aircraft demands of the people around it — portability at 20 lb, civil certifiability at 55 lb, collision energy at 1,320 lb, airspace class at 18,000 ft.
- **Reading defense and industry material.** "Group 3 UAS" is used constantly in procurement, doctrine, and trade press. Now it parses.
- **Locating yourself.** You're in Group 1, at roughly 3–7% of its weight ceiling.

**What it cannot tell you:**

- **What configuration to build.** Group 1 contains nano-helicopters, racing quads, foam gliders, and quadplanes. The taxonomy is silent on which you want.
- **Anything about cost or sophistication.** Group 1 spans $150 to $60,000. A hobby quad and a Black Hornet are the same Group.
- **Your legal obligations.** Those come from the FAA, and the two systems agree only at 55 lb. The FAA's 250 g threshold — the one that will actually shape your build — has no DoD equivalent.

> **The one-line summary:** the Group system classifies the *operational envelope*. Your build decision is about *configuration*. They're orthogonal, and only one of them is yours to choose.

---

## Inside Group 1: the decision that actually matters

Since every viable option is Group 1, here is that group's internal comparison — ranked on what matters to a first-time builder rather than on capability.

| | **Multirotor (quad)** | **Fixed-wing (foam)** | **VTOL quadplane** | **Helicopter** |
|---|---|---|---|---|
| **Build difficulty** | **2/5** | **2/5** | 4/5 | 5/5 |
| **Typical all-in cost** | $300–600 | $200–400 | $600–1,500 | $300–600 + consumables |
| **Part availability** | Excellent | Good | Limited | Model-specific |
| **Crash cost** | $3–20 (props) | ~$0 (hot glue) | $100s | $50–150 routinely |
| **Tuning burden** | Low — flies on defaults | Low — mechanical setup | **Very high** | Very high |
| **Flight time** | 5–8 min (5"), 20–30 (cine) | 30–90 min | 45–90 min | 6–12 min |
| **Skill to fly** | Low with GPS assist | Moderate | Moderate | **Brutal** |
| **Space needed** | A park | **A large field** | A large field | A park |
| **Failure mode** | Falls | **Glides** | Falls in hover | Autorotation |
| **Community size** | **Enormous** | Large | Small | Shrinking |
| **Time to first flight** | **2–4 weeks** | 2–3 weeks | 3–6 months | 2–6 months |

---

## Recommendation: the two to seriously consider

### 1. A 5" multirotor, or a sub-250 g micro quad — **the default, and the right one for most people**

**Why:**
- Lowest realistic barrier from zero experience to a flying aircraft you built. Roughly 20 solder joints and no precision mechanics.
- The parts ecosystem is the best in the hobby. Standardized mounting patterns, dozens of interoperable vendors, and every tutorial assumes this size.
- Crashes cost props, not airframes. That matters enormously when you're learning, because you will crash.
- Modern firmware defaults fly acceptably. You don't need to understand control theory to hover.
- Any problem you hit has been hit and documented by thousands of people. This is worth more than any technical advantage.
- It hovers, so you get thinking time in the air — a genuine safety margin that fixed-wing does not offer on flight one.

**Pick sub-250 g if:** you want to skip FAA registration and Remote ID entirely, fly in more places, and crash more cheaply. **Pick 5" if:** you want the maximum ecosystem and don't mind registering.

### 2. A foam fixed-wing — **the underrated choice, and better if you have a field**

**Why:**
- Cheapest complete aircraft. Under $250 flying, sometimes well under.
- **10× the flight time** of a comparable multirotor. 30–90 minutes instead of 6.
- Fails gracefully. Power loss makes it a glider, and foam plus hot glue repairs indefinitely.
- Less soldering than a quad — one ESC, one motor, a few servos.
- Modern trainers include self-leveling that will recover the aircraft if you panic.
- Teaches you actual aerodynamics — CG, stall, trim — in a way multirotors never do, because the flight controller hides it.

**The hard gate:** you need a large open field, and you need it for landing more than takeoff. If you don't have one within a reasonable drive, this option is off the table regardless of its merits. Check this before anything else.

### Honourable mention: buy a ducted sub-250 g whoop to learn on

Under $150, indoor-safe, props fully enclosed so it can't injure anyone, no registration, no Remote ID. It won't teach you to *build* — most come assembled — but it **decouples learning to fly from learning to build**, which is the single highest-leverage move a first-timer can make. Crash it a hundred times while your real build comes together.

---

## The traps — appealing options that will frustrate you

### ⚠️ VTOL quadplane — the most seductive trap in the hobby

"Hovers like a quad, cruises like a plane" sounds like it dominates both options. It doesn't. You're building **two aircraft that share a fuselage**, plus the transition between them — and the transition can only be tested in the air, on a real aircraft, with no way to bench-test it first.

You must tune hover, tune forward flight, *and* tune the transition. You need to already be competent at both multirotor and fixed-wing setup. And mounting lift booms to a wing so they survive hover loads is genuine structural engineering, where getting it wrong means an in-flight failure.

**If VTOL is truly your requirement:** build a quad, then a fixed-wing, then a quadplane. That path costs about what one crashed VTOL costs, and you end up with three aircraft and the ability to fix them.

### ⚠️ Collective-pitch helicopter — magnificent, and not a first build

Hundreds of parts assembled to tolerance. Blade tracking, linkage geometry, gear mesh. Every crash is $50–150 and an evening rebuilding. Realistically 10–30 hours in a simulator before your first real hover attempt, or you destroy it immediately.

It's a genuinely wonderful hobby if mechanical systems are what draw you. Just build a quad first so you have something flying while you learn.

### ⚠️ Designing your own airframe from scratch

Tempting if you have CAD skills, and it looks like the "real engineering" option. But it removes the thing that makes a first build tractable: **a known-good reference.** When your custom aircraft won't fly, you can't tell whether it's the design, the build, the tune, or the pilot — and that ambiguity is where projects die.

Build a proven design first. Then modify it. Then design your own, with the judgment you earned.

### ⚠️ Anything with a tiny community

Tricopters, tailsitters, monocopters, ornithopters. Difficulty in this hobby is dominated by **ecosystem support**, not intrinsic complexity. An unusual airframe means no parts, no firmware support, and nobody to ask at 11pm — regardless of how simple the concept looks on paper.

When a configuration has obvious advantages and still isn't popular, there's a hidden cost. Find out what it is before committing.

---

## Suggested path

1. **Check you have somewhere legal to fly.** B4UFLY app, your actual neighbourhood. This can invalidate the whole project and costs nothing to check. → [../05-open-questions.md](../05-open-questions.md) Q2
2. **Fly a simulator** (~$20). Tells you in two hours whether you enjoy this. Highest-return spend in the project.
3. **Fill in the mission** → [../01-mission-and-use-case.md](../01-mission-and-use-case.md). If it needs endurance or distance, that's fixed-wing and the decision is made for you.
4. **Decide the 250 g question** → [../07-regulatory-checklist.md](../07-regulatory-checklist.md). It's a design constraint, not paperwork.
5. **Buy a cheap whoop** and learn to fly while you plan.
6. **Build a 5" quad from a kit** — kits pre-solve the compatibility research, which is where first builds actually fail.
7. **Log the decision** → [../06-decision-log.md](../06-decision-log.md), including why you rejected the alternatives.

---

*Back to: [00-overview.md](00-overview.md) · [Group 1](01-group-1/) · [Group 2](02-group-2/) · [Group 3](03-group-3/) · [Group 4](04-group-4/) · [Group 5](05-group-5/)*
