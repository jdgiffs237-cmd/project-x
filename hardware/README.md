# hardware/

Everything physical about the aircraft.

## Layout

| Path | Contents |
|---|---|
| [cad/](cad/) | Source CAD files and exported STL/STEP for anything printed or machined — camera mounts, battery trays, antenna holders, landing gear. Keep the **source** file, not just the STL; you will want to change it. |
| [datasheets/](datasheets/) | Manufacturer PDFs and spec sheets for every part actually purchased. Vendor pages go dead and manuals disappear — download them at purchase time. |
| [wiring/](wiring/) | Wiring diagrams, connector pinouts, photos of the stack before it gets buried under other components. |

## Also belongs here

- **`bom.md`** — the real bill of materials, once parts are actually chosen. This is different from the candidate tables in [brainstorming/03-component-research.md](../brainstorming/03-component-research.md): that file is *shopping*, this one is *what's on the aircraft*, with serial numbers and purchase dates.
- **Weight budget** — a running table of every component's measured weight and the running total. Essential if targeting sub-250 g, useful regardless. Measure, don't trust listed specs.
- **Photos** — take pictures of every wiring step *before* covering it. Every experienced builder says this and every first-timer skips it.

## Conventions

- Name files so they sort usefully: `2026-08-16-motor-mount-v2.step`
- Never delete an old CAD revision; bump the version number
- Record measured values, not spec-sheet values, in the weight budget — they differ

## Not here

- Assembly instructions you wrote → [docs/](../docs/)
- Narrative of what you did on a given day → [build-log/](../build-log/)
- Parts you're still deciding between → [brainstorming/](../brainstorming/)
