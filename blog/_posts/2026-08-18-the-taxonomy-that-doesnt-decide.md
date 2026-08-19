---
layout: post
title: "The taxonomy everyone quotes, and what it can't tell you"
stage: "Design · Entry 02"
date: 2026-08-18
summary: >-
  I surveyed all five DoD UAS Groups to figure out what to build. The survey was
  worth doing and the framework was the wrong tool — it classifies operational
  envelope, and a build decision is about configuration.
---

The obvious first question is "what kind of drone am I building?" The obvious
place to start is the DoD's UAS Group system, because it's the taxonomy that
gets quoted everywhere in defense and trade press.

I worked through all five Groups properly — writeups, reference aircraft, the
lot. Here's the short version of what they are:

| Group | Max gross takeoff weight | Operating altitude | Airspeed |
|---|---|---|---|
| **1** | < 20 lb (9 kg) | < 1,200 ft AGL | < 100 kt |
| **2** | 21–55 lb (9–25 kg) | < 3,500 ft AGL | < 250 kt |
| **3** | 55–1,320 lb (25–600 kg) | < 18,000 ft MSL | < 250 kt |
| **4** | > 1,320 lb (600 kg) | < 18,000 ft MSL | Any |
| **5** | > 1,320 lb (600 kg) | > 18,000 ft MSL | Any |

Two details trip people up. A system lands in the **highest** Group it triggers —
exceed any one threshold and you move up, so a 30 lb aircraft cruising at 300 kt
is not Group 2. And the reference changes from AGL to MSL at Group 3, because
Groups 1–2 are tactical and locally launched while 3–5 share airspace structure
with crewed aviation.

## The thresholds are better than they look

The numbers aren't arbitrary. Each boundary marks a change in what the aircraft
**demands of the people around it**:

- **20 lb** — roughly where a hand-launched, one-person-portable aircraft stops
  being practical.
- **55 lb** — the most consequential line for a civilian, because it's also the
  FAA Part 107 ceiling. Shared deliberately.
- **1,320 lb** — approximately where a UAS becomes comparable in mass and
  kinetic energy to a light crewed aircraft.
- **18,000 ft MSL** — Flight Level 180, the floor of Class A airspace. Above it,
  everything flies IFR under positive ATC control.

Portability, civil certifiability, collision energy, airspace integration. Read
that way, the system is genuinely well-designed.

## And it does not answer my question

Here's the thing I actually took away, and it's the reason this entry exists:

> The Group system classifies the **operational envelope**, not the **aircraft
> configuration**.

It says nothing about whether an aircraft is a quadcopter, a fixed-wing, a
helicopter, or a hybrid. Group 1 covers a 33-gram nano-helicopter and a
19-pound quadplane equally. It spans $150 to $60,000. The taxonomy exists to
answer logistics and doctrine questions — who's authorized to operate it, what
airspace coordination it needs, what echelon owns it — not engineering ones.

That's a feature. But it means the Groups do not tell you what to build, and I
spent a while treating them as though they would.

**Where I actually sit:** Group 1, and not near the top of it.

| | |
|---|---|
| Group 1 ceiling | 20 lb / 9,072 g |
| A typical 5" FPV quad | ~1.4 lb / 650 g |
| A sub-250 g build | 0.55 lb / 250 g |

A hobby build is **3–7% of the Group 1 weight limit**. Two orders of magnitude
of headroom before the next boundary is even visible. Groups 2 through 5 are
reference material, not options.

## So was the survey wasted?

No — but not for the reason I started it.

The value turned out to be **calibration**. The taxonomy spans a factor of
roughly 440,000 in mass, from a 33 g Black Hornet to a 32,000 lb Global Hawk.
Once you know that a ScanEagle is a 48 lb aircraft that needs a pneumatic
catapult and a net recovery system, the constraints on a 650 g quad stop feeling
arbitrary and start feeling like the cheap end of a continuum. And once you
understand why the 55 lb line exists, the regulatory checklist stops reading as
bureaucracy.

There's also a trap worth naming. The DoD Groups have **no legal force over a
civilian**. My obligations come from the FAA. The two systems agree on 55 lb and
nowhere else — and in particular, the FAA's **250 g** registration and Remote ID
threshold has no DoD equivalent at all. That's the boundary that will actually
shape this build, and the framework everyone quotes doesn't contain it.

## The real decision, which is orthogonal

Since everything viable is Group 1, the actual choice lives inside Group 1, on
an axis the taxonomy is silent about. Ranked on what matters to a first-time
builder rather than on capability:

| | Multirotor | Fixed-wing (foam) | VTOL quadplane | Helicopter |
|---|---|---|---|---|
| **Build difficulty** | 2/5 | 2/5 | 4/5 | 5/5 |
| **All-in cost** | $300–600 | $200–400 | $600–1,500 | $300–600 + consumables |
| **Crash cost** | $3–20 (props) | ~$0 (hot glue) | $100s | $50–150 routinely |
| **Tuning burden** | Low | Low | Very high | Very high |
| **Flight time** | 5–8 min | 30–90 min | 45–90 min | 6–12 min |
| **Failure mode** | Falls | **Glides** | Falls in hover | Autorotation |
| **Community size** | Enormous | Large | Small | Shrinking |
| **Time to first flight** | 2–4 weeks | 2–3 weeks | 3–6 months | 2–6 months |

Two are worth serious consideration. A **5" multirotor** is the default and
probably the right answer: ~20 solder joints, no precision mechanics, the best
parts ecosystem in the hobby, crashes that cost props rather than airframes, and
firmware defaults that fly acceptably without understanding control theory. It
also hovers, which gives you thinking time in the air — a real safety margin on
flight one that fixed-wing doesn't offer.

A **foam fixed-wing** is the underrated one: under $250 flying, ten times the
endurance, fails gracefully into a glide, repairs indefinitely with hot glue,
and actually teaches aerodynamics — CG, stall, trim — in a way a multirotor
never will, because the flight controller hides all of it. The hard gate is that
it needs a large open field, for landing more than takeoff. That's a
check-before-anything-else item.

Notably, the thing I want to build — the quadplane — is the seductive trap I
already knew it was, and the survey only made that clearer.

## Next

The mission definition, which is the document every later decision falls out of,
and the 250 g question — which is a design constraint, not paperwork. I've also
sketched a first bill of materials, which is the next entry.

**Status:** Design stage · $0 spent · 0 flights · survey complete, airframe not locked

---

*Sources for the Group definitions: [CRS Defense Primer on UAS categories](https://www.congress.gov/crs-product/IF12797),
the [USAF sUAS Identification and Reporting Guide](https://media.defense.gov/2022/Mar/14/2002969679/-1/-1/1/SUAS%20IDENTIFICATION%20AND%20REPORTING%20GUIDE.PDF),
and [FAA AIM Chapter 11](https://www.faa.gov/air_traffic/publications/atpubs/aim_html/chap11_section_3.html).
Per-aircraft figures are approximate and drawn from public sources.*
