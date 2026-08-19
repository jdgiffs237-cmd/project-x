# reference/

**Other people's material.** Manuals, saved articles, tutorials, regulatory documents, forum threads worth keeping, thrust test data.

Kept separate from [docs/](../docs/) — that folder is for things *you* wrote. The distinction matters: reference material is not authoritative for your build (it may describe different parts, older firmware, or another country's rules), and it may carry licensing restrictions that make it inappropriate to redistribute.

## Suggested organization

| Subfolder | Contents |
|---|---|
| `regulations/` | FAA advisory circulars, Part 107 study material, saved rule pages. Date every capture — regulation changes. |
| `firmware/` | Betaflight / ArduPilot / PX4 documentation snapshots, wiring guides for your specific FC |
| `tutorials/` | Build guides, soldering references, video links with timestamps and a note on why it was useful |
| `datasheets/` | Only for parts you're *considering* — once purchased, the datasheet moves to [hardware/datasheets/](../hardware/datasheets/) |

## Rules

- **Record the source URL and the date you saved it** at the top of every saved document. A guide from 2019 may be actively wrong now.
- Note *why* you saved it. "Explains why my receiver needs 5 V not 3.3 V" beats an untitled PDF.
- Prefer official documentation over YouTube. Prefer recent over popular.
- Regulatory material especially: this is a snapshot, not the current rule. Re-verify at [faa.gov/uas](https://www.faa.gov/uas) before acting on it.

## Starting points worth collecting

- FAA UAS pages — see [brainstorming/07-regulatory-checklist.md](../brainstorming/07-regulatory-checklist.md)
- Official docs for whichever firmware you choose
- Manufacturer manuals for every part on your shortlist
- A thrust-data table for your candidate motor/prop/battery combinations
