# code/ — placeholder

**Nothing here yet, and nothing should be for a while.** Flying hardware comes first; software comes after there's hardware to run it on.

This file exists so future-you knows what the plan was.

## What will eventually live here

### `fc-config/` — Flight controller configuration
Not really "code," but it's text, it's versioned, and losing it means re-tuning from scratch after a firmware flash.

- Betaflight CLI dumps (`diff all` output), or
- ArduPilot/PX4 parameter files (`.param`)
- PID tuning history — one file per tuning session, dated, with a note on what changed and how it flew
- Rate profiles, failsafe settings, OSD layout

> Dump and commit the config **after every successful tuning session**. This is the single highest-value thing in this folder.

### `ground-station/` — Anything running on a laptop or phone
- Mission Planner / QGroundControl mission files, if going the autonomous route
- Scripts for parsing and plotting flight logs (`.bin` / `.ulg` / blackbox) from [flight-logs/](../flight-logs/)
- Telemetry dashboards or monitoring tools

### `firmware/` — Custom onboard code
Only if the project grows past off-the-shelf. Candidates:
- MAVLink scripts driving the flight controller from a companion computer (Raspberry Pi / Jetson)
- Custom sensor or peripheral integration
- Autonomy: waypoint logic, computer vision, tracking

> **Bench firmware track (added 2026-10-11):** writing your own code for the SkyStars H743 starts at Bench alive, on the bench, props off: blink an LED → USB "hello" → read the BMI270 → spin one motor with DShot. Betaflight goes back on after every rung. The steps are on the [roadmap](https://claude.ai/artifact/TSb7eo9mAvQgAtfM15WNNo#s8). Flight test 1 is on standard Betaflight. **Flight test 2 is on this firmware**, after five more rungs: read the radio, estimate attitude, PID and mixer, a safety layer, and props-on tuning on a single-axis rig.
>
> Realistically: don't write flight-critical firmware for a first build. Off-the-shelf firmware represents thousands of hours of debugging by people who crashed so you don't have to. The interesting custom work happens *on top of* it, usually on a companion computer talking MAVLink.

### `tools/` — Small utilities
- Thrust/weight and flight-time calculators
- Bill-of-materials generators from the parts tables
- Log-file converters

## Prerequisites before anything here matters

1. Hardware selected and purchased
2. Aircraft assembled and bench-tested
3. First successful hover
4. A reason to write code that off-the-shelf firmware doesn't already satisfy

See [../brainstorming/03-component-research.md](../brainstorming/03-component-research.md) — the firmware family choice (Betaflight vs. INAV vs. ArduPilot vs. PX4) determines almost everything about this folder, and it's a decision to make early even though the code comes late.
