# Delta-wing VTOL Quadplane

- **Captured:** 2026-08-16
- **Status:** EXPLORING
- **Applies to:** not v1 — see [Verdict](#verdict)
- **Budget context:** $10,000 general project budget

---

## The idea

Build a delta-wing (or twin-boom) VTOL quadplane in the style of the [DeltaQuad](../drone-classes/01-group-1/images/deltaquad-vtol-quadplane.jpg): a fixed-wing aircraft with four upward-facing lift motors on booms, plus a separate forward-flight motor. Takes off vertically from anywhere, transitions to wing-borne flight, cruises efficiently for an hour-plus, then transitions back to hover to land.

## Why I want it

The configuration genuinely does dominate on capability: no runway needed, and 45–90 min endurance instead of a multirotor's 6–8. It looks superb. And unlike most "best of both worlds" claims, this one is real — it's why commercial mapping and delivery operators actually buy them.

---

## Cost analysis

**Headline finding: at a $10k budget, money is not your constraint.** Skill sequencing is. The numbers below are why.

### Option A — Buy a commercial DeltaQuad

| Item | Cost |
|---|---|
| DeltaQuad Pro (base configuration) | **$15,000–30,000** |

**Verdict: out of budget, and would consume it entirely even if it weren't.** These are commercial survey aircraft sold to businesses with a mapping contract to service. You'd also be buying an appliance rather than learning anything — which defeats the stated point of the project.

**Ruled out on price.**

### Option B — Build one yourself

This is the real option, and it's dramatically cheaper than most people expect.

| Component | Rough cost | Notes |
|---|---|---|
| Airframe (Skywalker X8 delta, ~2 m span) | **$150–250** | The classic quadplane conversion platform. Foam, cheap, replaceable. |
| — or MFE Believer / twin-boom kit | $400–500 | Roomier fuselage, easier to mount lift booms |
| Autopilot (Pixhawk 6C or Cube Orange) | **$200–900** | Cube Orange for serious autonomy; 6C is plenty to start |
| GPS / compass (M9N) | **$80–150** | |
| — RTK GPS, *only if* survey-grade mapping | +$500–1,500 | Skip unless the mission demands centimetre accuracy |
| **Airspeed sensor** | **$30–60** | **Not optional.** A quadplane must know its airspeed to transition safely. |
| Lift motors ×4 | **$150–250** | |
| Lift ESCs ×4 | **$100–160** | |
| Forward motor + ESC | **$80–150** | |
| Propellers (lift + forward, plus spares) | **$80–150** | |
| Carbon booms, mounts, hardware | **$100–200** | Often custom — this is the structural work |
| Batteries (6S 16–22 Ah × 3) | **$450–750** | The single biggest consumable line |
| Charger (quality, e.g. iCharger/ISDT) | **$150–300** | Needed for packs this size |
| Telemetry radio (RFD900x) | **$60–300** | SiK radio at the low end; RFD900x for real range |
| RC transmitter (ELRS, e.g. TX16S) | **$200** | Buy once, outlives every aircraft |
| RC receiver | **$30** | |
| Power module / wiring / connectors | **$100–150** | |
| Tools & consumables | **$200–300** | If not already owned |
| **Realistic total** | **$2,200–4,000** | Comfortably inside $10,000 |

### Option C — The staged path, fully funded

| Stage | Aircraft | Cost | What it teaches |
|---|---|---|---|
| 0 | Sub-250 g whoop (bought) | **$150** | How to fly, with zero build risk |
| 0 | Simulator | **$20** | Whether you enjoy this at all |
| 1 | 5" quad (kit build) | **$500** | Soldering, multirotor tuning, failure modes |
| 2 | Foam fixed-wing + ArduPilot | **$400** | CG, launching, landing, mission planning |
| 3 | **Delta quadplane** | **$2,500** | Integration — and it feels like integration, not mystery |
| — | Ground gear (radio, goggles, charger, tools) | **$1,000** | Reusable across all of the above |
| | **Total** | **~$4,570** | Leaves **>$5,000** buffer |

**Your $10k funds the entire path, three aircraft, all the ground gear, and a large crash reserve — with half the budget untouched.**

---

## Pros — on price specifically

| | |
|---|---|
| **DIY is ~6–12× cheaper than commercial** | $2.2–4k vs. $15–30k for comparable capability |
| **Well inside budget** | ~25–40% of $10k, leaving a genuine reserve |
| **Ground gear is reusable** | The radio, charger, and tools carry across every future build — spending well here is an investment, not a cost |
| **Foam airframes are cheap to replace** | An X8 wing is $150–250; a crash isn't project-ending |
| **No time pressure** | The budget doesn't force you to rush stages or skip a trainer |
| **Room for RTK later** | +$500–1,500 is affordable *if* mapping turns out to be the mission |

## Cons — on price specifically

| | |
|---|---|
| **Crash cost is 10–50× a quad's** | A quad crash costs $3–20 in props. A quadplane transition failure costs **$500–1,500** and often the whole airframe. |
| **Transition failures are typically total** | You can't bench-test a transition. Failures happen at altitude, and the aircraft usually doesn't come back in one piece. |
| **Batteries dominate running costs** | 6S 22 Ah packs are $150–250 each, wear out, and are ruined by over-discharge. Budget for replacement, not just purchase. |
| **Custom structural parts aren't off-the-shelf** | Boom mounts are often bespoke — CAD, printing, iteration, and re-buying when v1 flexes |
| **Very little is reusable after a hard crash** | Unlike a quad, where motors and the stack usually survive |
| **Debugging costs money, not just time** | With no known-good reference, diagnosis is "replace the part and try again," and each attempt is a flight |
| **Sunk-cost risk** | An expensive aircraft you're afraid to fly is the worst outcome — and it's a real one at this price |

### Crash economics — the number that matters

With $10k, a **$1,000 crash is survivable but not casual.** You can absorb perhaps three to five catastrophic losses before the project is in trouble.

The problem is that a quadplane built as a *first* aircraft has a high probability of at least one such crash, because the failure modes cluster exactly where you have no experience: transition, CG under a new weight distribution, and hover tuning on an airframe never designed for it. Built as a *third* aircraft, that probability drops sharply — you'll have already made the cheap mistakes on cheap aircraft.

**The staged path isn't slower. It's the cheaper route to a flying quadplane**, because it front-loads your mistakes onto $20 airframes instead of $2,500 ones.

---

## What it would take

- **Cost:** $2,200–4,000 (DIY) — see above
- **New skills needed:** ArduPilot configuration, fixed-wing CG and trim, multirotor tuning, basic structural fabrication, mission planning
- **New parts needed:** essentially everything — no overlap with a multirotor build except the radio and charger
- **Added weight:** N/A (separate aircraft, not a modification)
- **Rough effort:** 3–6 months as a third project; 6–12 months and probably a destroyed airframe as a first

## What it would cost me

Not money — **sequence**. Building this first means learning multirotor tuning, fixed-wing aerodynamics, autopilot configuration, and transition tuning simultaneously, with no way to isolate which one is causing a given problem. That ambiguity is where projects stall, and it's expensive here in a way it isn't on a $400 quad.

## Prerequisites

- [ ] A large open field for launch and recovery — VTOL removes the *launch* requirement, not the landing-space or line-of-sight one
- [ ] **Built and flown a multirotor** (hover tuning, failure modes, prop/motor direction) ← **the largest gap**
- [ ] **Built and flown a fixed-wing** — *not* covered by Altius experience. Production familiarity with one airframe ≠ setting up and flying an unfamiliar one. Teaches CG, stall, and landing without hover.
- [ ] Comfortable with ArduPilot / Mission Planner on a simpler airframe first
- [ ] Some stick time — currently zero
- [ ] FAA path settled — this will be **well over 250 g**, so registration and Remote ID both apply → [../07-regulatory-checklist.md](../07-regulatory-checklist.md)
- [ ] Mission defined → [../01-mission-and-use-case.md](../01-mission-and-use-case.md). If it doesn't need hover *and* endurance, a plain fixed-wing is cheaper, simpler, and better.

## Open questions

- Does the mission actually require VTOL, or just endurance? *(If there's a field to land in, a plain fixed-wing does this for a fifth the cost and a fraction the risk.)* → copy to [../05-open-questions.md](../05-open-questions.md)
- Delta wing (X8) or twin-boom (Believer)? Twin-boom is easier to mount lift booms to; delta is cheaper and more crash-tolerant.
- Is survey-grade mapping the goal? Only that justifies RTK.
- Is there a local ArduPilot/VTOL community within reach? This is a configuration where one experienced person saves months.

---

## Revised for an Altius production background

*Added 2026-08-16. Corrected same day: **production team, not engineering.** That distinction matters and changes the plan.*

### What the Altius experience actually transfers

| Skill | Covered? | Notes |
|---|---|---|
| Airframe assembly, fasteners, torque, thread lock | **Yes** | Real, and genuinely valuable |
| Wiring harnesses, connectors, soldering | **Likely** | The exact skills a first build needs |
| Composite / airframe handling | **Yes** | |
| Build discipline and process rigour | **Yes** | **The underrated advantage — see below** |
| How a UAS works operationally | **Yes** | Good intuition for the whole system |
| — | — | — |
| CG determination on a *new* airframe | **No** | Knowing Altius's CG ≠ finding one on an X8 |
| Aerodynamics, stall behaviour, trim | **No** | |
| Autopilot config (ArduPilot / Mission Planner) | **No** | |
| PID tuning, hover or forward flight | **No** | |
| Stick time — actually flying anything | **No** | Zero |

> **The honest framing: he knows how an Altius is *built*. He has never had to make one *fly*.** Those are different skills, and the second one is the whole project.

### The real advantage, which is not the one you'd expect

Production experience won't let you skip a stage. What it *will* do is eliminate an entire category of first-build failure.

Most beginner builds don't fail on design — they fail on **workmanship**. Cold solder joints, unsecured wiring that chafes through, fasteners without thread lock backing out under vibration, connectors that aren't fully seated, a battery strap that lets the pack shift in flight. These are the actual causes of most "it just fell out of the sky" posts, and they are exactly what a production floor trains out of you.

You'll likely build cleaner than 90% of first-timers. That's worth real money on a $2,500 airframe — but it's a *build* advantage, not a *design or flying* advantage, and this project's difficulty is concentrated in the latter two.

### So: keep the fixed-wing stage

The earlier version of this file dropped it. That was wrong — it assumed engineering-level fixed-wing knowledge rather than production familiarity with one specific airframe.

Keep it. At **$400 against a $10,000 budget and a $2,500 target airframe, it's the cheapest insurance available**, and it teaches three things Altius doesn't: how to find and set CG on an unfamiliar airframe, what a stall feels like before it bites you during a transition, and how to land something that can't hover.

The multirotor stage stays too, and remains the largest single gap.

### Why "two things > one thing" is the wrong frame

Difficulty here isn't additive, it's **multiplicative in ambiguity**. With two coupled subsystems and no prior experience of either, a failure gives you no way to localise the cause: bad hover tune, wrong transition airspeed, CG shifted by the lift booms, a structural flex, or a configuration error all look identical from the ground. That ambiguity — not the aircraft's complexity — is what stalls builds.

Doing the multirotor first doesn't reduce the challenge. It makes the challenge *diagnosable*.

### Don't make the quad a boring stepping stone

The real objection to staging is that a beginner quad sounds tedious. Fix that by building the right kind of quad:

**Build the multirotor on ArduPilot with GPS — not a Betaflight freestyle quad.**

- Same autopilot, same Mission Planner, same GPS, same failsafe logic, same telemetry the quadplane will use
- Autonomous waypoint missions, return-to-home, position hold — genuinely interesting work
- Roughly 80% of the quadplane's software and configuration stack, on an airframe where mistakes cost $20
- Directly reusable: the flight controller, GPS, telemetry radio, and RC gear all move to the quadplane

That's not a toy stage. It's the quadplane's avionics stack, debugged in advance on cheap hardware.

### Revised path

| Stage | Aircraft | Cost | What it closes |
|---|---|---|---|
| 0 | Whoop + simulator | **$170** | Stick time. Zero currently, and unrelated to Altius. |
| 1 | **ArduPilot quad + GPS** | **$700** | Hover tuning + the entire autopilot stack. The largest gap. |
| 2 | **Foam fixed-wing** | **$400** | CG on an unfamiliar airframe, stall behaviour, landing without hover. |
| 3 | **Delta VTOL quadplane** | **$2,500** | The goal — now an integration exercise rather than a mystery. |
| — | Ground gear + tools | **$1,300** | Reusable across all of it |
| | **Total** | **~$5,070** | Half the budget, four aircraft, everything de-risked |

Roughly **6–9 months**. The build phases will go faster than typical because of the production background; the flying and tuning phases will not, and those are the ones that gate progress.

> **Where the "two things > one thing" instinct is right:** the goal genuinely is the quadplane, and nothing here changes that. The staging isn't about lowering ambition — it's about arriving at the transition-tuning problem with a diagnosable aircraft instead of an ambiguous one.

---

## A note on working at Anduril

Low concern, mentioned once for completeness: invention-assignment clauses target *inventions*, and a production-team member building a widely-documented open-source airframe (X8 + ArduPilot) isn't in that territory. Nothing here derives from Altius.

Worth a glance at the employment agreement if you ever move toward original design work or anything you'd publish — not worth worrying about for this build.

---

## Verdict

**Do it — but build a multirotor first, and make that multirotor interesting.**

The finding that matters on price: **$10,000 is not the limiting factor.** A DIY delta quadplane costs $2,200–4,000, and the revised path to it costs ~$4,570 including two aircraft and all ground equipment.

Since money isn't the constraint, spend it on **de-risking**:

1. **Buy the good reusable gear now** — quality radio, proper charger, real tools. They carry across every build, and the flight controller, GPS, and telemetry from stage 1 move directly onto the quadplane.
2. **Drop the fixed-wing stage.** Altius covers it. This is the genuine saving from your background.
3. **Do not drop the multirotor stage** — it's the largest gap and the cheapest place to close it.
4. **Hold ~$2,000 as a crash reserve** for the quadplane phase. Knowing you can rebuild it is what lets you actually fly it.
5. **Don't buy the commercial DeltaQuad.** Out of budget, and it turns the project into a purchase.

**Decision:** approved as the project goal; preceded by one ArduPilot multirotor
**Date:** 2026-08-16
**Where it went:** promote to [../06-decision-log.md](../06-decision-log.md) once the multirotor has flown

---

*Related: [../drone-classes/01-group-1/](../drone-classes/01-group-1/) (VTOL hybrid section) · [../drone-classes/99-comparison.md](../drone-classes/99-comparison.md) (why this is the classic first-build trap) · [../04-budget.md](../04-budget.md)*
