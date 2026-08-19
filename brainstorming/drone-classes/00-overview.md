# 00 — Overview: The DoD UAS Group System

> **Read this first.** It explains what the Group system measures, what it deliberately ignores, and where a project like yours actually sits.

---

## What the system is

The US Department of Defense sorts unmanned aircraft systems into **five Groups**, defined by three parameters:

| Group | Max gross takeoff weight | Normal operating altitude | Airspeed |
|---|---|---|---|
| **Group 1** | < 20 lb (9 kg) | < 1,200 ft AGL | < 100 kt |
| **Group 2** | 21–55 lb (9–25 kg) | < 3,500 ft AGL | < 250 kt |
| **Group 3** | 55–1,320 lb (25–600 kg) | < 18,000 ft MSL | < 250 kt |
| **Group 4** | > 1,320 lb (600 kg) | < 18,000 ft MSL | Any airspeed |
| **Group 5** | > 1,320 lb (600 kg) | > 18,000 ft MSL | Any airspeed |

Two details that trip people up:

1. **A system lands in the highest Group it triggers.** Exceed *any one* threshold and you move up. A 30 lb aircraft that cruises at 300 kt is not Group 2.
2. **"AGL" becomes "MSL" at Group 3.** Groups 1–2 are defined relative to the ground (they're tactical, launched and recovered locally). Groups 3–5 are defined relative to sea level, because they operate in the same airspace structure as crewed aviation.

Note also that Groups 4 and 5 share a weight threshold and are separated **only by altitude**. The distinction is not size — it's whether the aircraft operates in the high-altitude structure above Flight Level 180.

---

## What it measures, and what it deliberately ignores

This is the single most important thing to understand about the taxonomy:

> **The Group system classifies the *operational envelope*, not the *aircraft configuration*.**

It says nothing about whether an aircraft is a quadcopter, a fixed-wing, a helicopter, or a hybrid. A Group 1 designation covers a 33-gram nano-helicopter and a 19-pound quadplane equally. The system exists to answer logistics and doctrine questions — who is authorized to operate it, what airspace coordination it needs, what echelon owns it, what launch and recovery infrastructure it requires — not engineering questions.

That's a feature, not a flaw. But it means **the Groups do not tell you what to build.** Configuration is an orthogonal axis, and within Group 1 it's the axis that matters most. See [99-comparison.md](99-comparison.md), which treats it directly.

---

## Why the thresholds sit where they do

The numbers aren't arbitrary. Each boundary marks a change in what the aircraft *demands of the people around it*.

**20 lb (Group 1 → 2).** Roughly where a hand-launched, one-person-portable aircraft stops being practical. Below this, an individual carries, launches, and recovers the system alone.

**55 lb (Group 2 → 3).** The most consequential line for a civilian, because it is also the **FAA Part 107 ceiling**. Below 55 lb you're in the regime civilians can operate under ordinary certification. Above it, you need special authorization. This threshold is shared deliberately.

**1,320 lb / 600 kg (Group 3 → 4).** Approximately where a UAS becomes comparable in mass and kinetic energy to a light crewed aircraft, with the collision consequences that implies.

**18,000 ft MSL (Group 4 → 5).** This is **Flight Level 180**, the floor of Class A airspace in the US. Above it, everything flies on instruments under positive ATC control. An aircraft operating there must integrate with the crewed air traffic system as a peer.

So the Group boundaries are really **thresholds of operational consequence** — portability, civil certifiability, collision energy, and airspace integration.

---

## Where your project sits

Bluntly: **Group 1, and not near the top of it.**

| | |
|---|---|
| Group 1 ceiling | 20 lb / 9,072 g |
| A typical 5" FPV quad | ~1.4 lb / 650 g |
| A sub-250 g build | 0.55 lb / 250 g |

A hobby build is typically **3–7% of the Group 1 weight limit.** You have roughly two orders of magnitude of headroom before the next boundary matters.

This has a practical consequence worth internalizing: **Groups 2 through 5 are reference material for you, not options.** Group 2 begins at 21 lb — a 10 kg aircraft, well beyond a first build and past the point where crashes stop being a props-and-a-lesson matter. Group 3 starts at systems like the RQ-7 Shadow: 467 lb, pneumatic catapult launch, a ground crew.

The value in reading Groups 2–5 is **calibration**. When you understand that a ScanEagle is a 48 lb aircraft that needs a catapult and a recovery system, the design constraints on your 650 g quad stop feeling arbitrary. And when you understand why the 55 lb line exists, [../07-regulatory-checklist.md](../07-regulatory-checklist.md) stops feeling like bureaucracy.

---

## How this maps to civilian regulation

The DoD Groups and the FAA's rules are separate systems that happen to align at one point.

| DoD | Weight | FAA treatment (civilian operator) |
|---|---|---|
| **Group 1** | < 20 lb | Part 107, or recreational under §44809. **Under 250 g flown recreationally: no registration, no Remote ID.** |
| **Group 2** | 21–55 lb | Still Part 107 — the 55 lb ceiling is the same number |
| **Group 3** | 55–1,320 lb | Beyond Part 107. Needs waiver, exemption, or public-aircraft status |
| **Group 4–5** | > 1,320 lb | Type certification or public-aircraft operations. Not a civilian path |

> **The DoD Group system has no legal force over you.** Your obligations come from the FAA. The two systems agree on 55 lb and nowhere else — in particular, the FAA's 250 g registration threshold has no DoD equivalent, and it's the boundary that will actually shape your build.

---

## Reading order

1. **[01-group-1/](01-group-1/)** — the only group you can build in. Treated in depth, including the configuration choices that live inside it.
2. [02-group-2/](02-group-2/) — where sUAS stops being portable
3. [03-group-3/](03-group-3/) — catapults, ground crews, and the far side of the Part 107 line
4. [04-group-4/](04-group-4/) — armed and heavy, below the flight levels
5. [05-group-5/](05-group-5/) — strategic aircraft in Class A airspace
6. **[99-comparison.md](99-comparison.md)** — all five side by side, plus what this framework does and doesn't decide for you

---

## Sources

- [Congressional Research Service — Defense Primer: Categories of Uncrewed Aircraft Systems](https://www.congress.gov/crs-product/IF12797)
- [USAF Small Unmanned Aircraft Systems Identification and Reporting Guide (PDF)](https://media.defense.gov/2022/Mar/14/2002969679/-1/-1/1/SUAS%20IDENTIFICATION%20AND%20REPORTING%20GUIDE.PDF)
- [FAA AIM Chapter 11 — Unmanned Aircraft Systems](https://www.faa.gov/air_traffic/publications/atpubs/aim_html/chap11_section_3.html)

*Weights and performance figures for individual aircraft in the group files are approximate and drawn from public sources; treat them as indicative rather than authoritative.*
