# flight-logs/

Records of actual flights — one entry per flying session, plus any telemetry files pulled off the aircraft.

Separate from [build-log/](../build-log/) because this data is periodic, structured, and will eventually be mostly machine-generated (blackbox `.bfl`, ArduPilot `.bin`, PX4 `.ulg`). Mixing it into the build log would bury the build narrative.

## Layout

- `YYYY-MM-DD-session.md` — the human entry
- `telemetry/` — raw log files off the flight controller, named to match the session

## Session template

```markdown
# YYYY-MM-DD — Flight session

**Location:** ___
**Airspace check:** B4UFLY / LAANC status ___
**Weather:** temp ___, wind ___ from ___, visibility ___
**Aircraft config:** <firmware version, any changes since last flight>
**Batteries flown:** ___

## Pre-flight checklist
- [ ] Props tight and undamaged, correct rotation direction
- [ ] Battery charged, not puffed, securely strapped
- [ ] Control surfaces / motor directions verified
- [ ] Failsafe tested (throttle cut on signal loss)
- [ ] Return-to-home configured and tested (if applicable)
- [ ] Remote ID broadcasting (if required)
- [ ] Registration number visible on airframe
- [ ] Registration + TRUST/Part 107 proof on hand
- [ ] Bystanders clear, escape route identified
- [ ] Airspace clear of crewed aircraft

## Flights
| # | Duration | Pack used | What I tried | How it went |
|---|---|---|---|---|
| 1 | | | | |

## Issues observed
-

## Changes to make before next flight
-

## Log files
- `telemetry/2026-08-16-flight-01.bin`
```

## Notes

- Log the **first hover** in obsessive detail. It's the flight most likely to reveal a build error.
- Note battery voltage at landing — repeatedly flying packs below ~3.5 V/cell under load destroys them.
- Save telemetry even from boring flights. It's the baseline you compare against when something later goes wrong.
