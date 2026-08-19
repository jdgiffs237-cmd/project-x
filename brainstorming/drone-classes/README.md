# Drone Classes — DoD UAS Group Survey

A survey of unmanned aircraft organized by the **US Department of Defense UAS Group classification** (Groups 1–5), which sorts systems by maximum gross takeoff weight, normal operating altitude, and airspeed.

**Purpose:** understand the full scale of what "drone" covers, learn where a personal build actually sits, and see why the size thresholds land where they do.

---

## The five Groups

| Group | Weight | Altitude | Speed | Example | Buildable by you? |
|---|---|---|---|---|---|
| **[1](01-group-1/)** | < 20 lb | < 1,200 ft AGL | < 100 kt | RQ-11 Raven | **Yes** |
| **[2](02-group-2/)** | 21–55 lb | < 3,500 ft AGL | < 250 kt | ScanEagle | No |
| **[3](03-group-3/)** | 55–1,320 lb | < 18,000 ft MSL | < 250 kt | RQ-7 Shadow | No |
| **[4](04-group-4/)** | > 1,320 lb | < 18,000 ft MSL | Any | MQ-1 Predator | No |
| **[5](05-group-5/)** | > 1,320 lb | > 18,000 ft MSL | Any | MQ-9 Reaper | No |

---

## Files

| Path | Contents |
|---|---|
| [00-overview.md](00-overview.md) | **Start here.** What the Group system measures, what it deliberately ignores, why the thresholds sit where they do, and how it maps to FAA rules. |
| [01-group-1/](01-group-1/) | **The deep one.** Small UAS — the only group you can build in. Includes the airframe configuration comparison (multirotor, fixed-wing, VTOL, helicopter) that the DoD taxonomy doesn't cover. |
| [02-group-2/](02-group-2/) | Medium UAS. Where launch and recovery infrastructure becomes mandatory. |
| [03-group-3/](03-group-3/) | Large UAS. Past the 55 lb Part 107 ceiling. |
| [04-group-4/](04-group-4/) | Larger UAS. Aircraft-scale, below the flight levels. |
| [05-group-5/](05-group-5/) | Largest UAS. Strategic aircraft in Class A airspace. |
| [99-comparison.md](99-comparison.md) | **The payoff.** All five Groups side by side, the Group 1 configuration comparison, a straight recommendation, and the traps to avoid. |

Every group file opens with an **"In general"** section — a plain-language description of what that class of aircraft actually is, before any of the technical detail.

### Layout of a group folder

Each group folder is self-contained and follows the same shape:

```
0N-group-N/
├── README.md        ← the writeup for this group
├── images/          ← reference images for this group only
└── zz-CREDITS.md    ← source URL, author, and license for each image
```

The credits file is named `zz-` so it always sorts to the bottom of the folder, out of the way of the content.

---

## Two things to know before reading

**1. The Group system classifies operational envelope, not aircraft configuration.** It says nothing about whether something is a quadcopter, a fixed-wing, or a helicopter. Group 1 alone covers a 33-gram nano-helicopter and a 19-pound quadplane. Configuration is an orthogonal axis — and inside Group 1, it's the axis that actually matters for your build. That's why [01-group-1/](01-group-1/) and [99-comparison.md](99-comparison.md) cover it directly.

**2. The DoD Groups have no legal force over a civilian.** Your obligations come from the FAA. The two systems coincide at 55 lb (the Part 107 ceiling) and nowhere else. In particular, the FAA's **250 g** registration and Remote ID threshold — the number that will actually shape your build — has no DoD equivalent. See [../07-regulatory-checklist.md](../07-regulatory-checklist.md).

---

## Reading order

1. [00-overview.md](00-overview.md) — the framework
2. [01-group-1/](01-group-1/) — your group, in depth
3. [02-group-2/](02-group-2/) → [05-group-5/](05-group-5/) — scale calibration
4. [99-comparison.md](99-comparison.md) — comparison and recommendation

If you're short on time: read [00-overview.md](00-overview.md), then [01-group-1/](01-group-1/), then [99-comparison.md](99-comparison.md). Groups 2–5 are context, not decisions.

---

## Image licensing

All images are local copies downloaded from Wikimedia Commons, downsampled to ~1200px on the long edge. Every license was verified on its Commons file page before use — public domain (mostly US Government works), CC0, CC BY, or CC BY-SA. **No non-commercial or no-derivatives material, and nothing hotlinked.** Per-image attribution lives in the `zz-CREDITS.md` inside each group folder, alongside the `images/` directory it documents.
