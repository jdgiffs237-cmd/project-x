# 02 — Requirements & Constraints

> Requirements come *from* the mission in [01](01-mission-and-use-case.md). Don't fill this in first.
>
> Mark each requirement **MUST** (project fails without it) or **WANT** (nice to have). Be ruthless — first builds fail from too many MUSTs.

**Last updated:** _(YYYY-MM-DD)_

---

## Performance requirements

| # | Requirement | MUST / WANT | Target value | Source (why?) |
|---|---|---|---|---|
| P1 | Flight time | | ___ min | |
| P2 | Range from pilot | | ___ m/km | |
| P3 | Payload capacity | | ___ g | |
| P4 | Max takeoff weight | | ___ g | |
| P5 | Top speed | | ___ km/h | |
| P6 | Wind tolerance | | ___ km/h | |
| P7 | Video/telemetry link range | | ___ | |

> **The 250 g line matters more than any other number here.** Under 250 g total takeoff weight, flown recreationally, means no FAA registration and no Remote ID. Over it, both apply. See [07-regulatory-checklist.md](07-regulatory-checklist.md). Decide deliberately which side you're on — don't drift over it by accident.

## Hard constraints

| Constraint | Value | Notes |
|---|---|---|
| Total budget (all-in, incl. tools & spares) | $______ | See [04-budget.md](04-budget.md) |
| Deadline | ______ | |
| Workspace available | ______ | Soldering needs ventilation and a surface you don't mind damaging |
| Tools I already own | ______ | |
| Skills I already have (soldering, CAD, coding, RC) | ______ | |
| Storage / transport (car? backpack?) | ______ | A 7" quad does not fit in a backpack |
| Local flying sites | ______ | |
| Noise tolerance of where I'll fly | ______ | Drones are loud; this ends more builds than you'd think |

## Derived requirements

> Fill in once the above is settled. These follow logically and are what you actually shop against.

- **Frame class:** ______ (see [03-component-research.md](03-component-research.md))
- **Number of motors:** ______ (4 is the default; 6/8 for redundancy and lift, at cost/complexity)
- **Battery chemistry & size:** ______
- **Flight controller firmware family:** ______ (Betaflight = sport/FPV; ArduPilot/PX4 = autonomy)
- **Radio protocol:** ______
- **Video system:** ______ (analog, digital, or none)

## Assumptions I'm making

> Write these down. Assumptions that stay unexamined are where budget overruns come from.

1. ______
2. ______
3. ______

## Known risks

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| I damage components while soldering | | | Practice on scrap first; buy one spare of the cheap fragile parts |
| First flight ends in a crash | High | | Budget for spare props + one spare arm/frame |
| Parts turn out incompatible | | | Verify voltage + connector + protocol for every pair before ordering |
| Long shipping times on key parts | | | |
| | | | |

---

## Guiding questions

- Which single requirement is doing the most damage to the rest of the design? Can it be relaxed?
- Flight time is the most commonly over-specified requirement. 10–15 minutes is normal for a build like this. 30+ minutes is a fundamentally different (and more expensive) aircraft.
- What's my *actual* skill floor? Have I ever soldered? Flown anything? Be honest — it changes the recommendation.
- If I halved the budget, what would the build look like? If that version still satisfies the mission, build it.
