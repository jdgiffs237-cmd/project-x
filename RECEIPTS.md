# Receipts — Money Actually Spent

**Last updated:** 2026-08-29 · **Budget ceiling:** $10,000 ([04-budget.md](brainstorming/04-budget.md))

> Records what was **actually paid**; the budget file records what was *planned*. When they disagree, this file is right.
> **This repo is public** — log order numbers and vendors, never card numbers, addresses, or logins.

## Totals

| | |
|---|---|
| **Spent to date** | **$797.97** |
| Refunds received | −$0.00 |
| **Remaining against ceiling** | **$9,202.03** |

| Bucket | Spent | Planned |
|---|---|---|
| Aircraft | $317.28 | — |
| Tools & consumables | $422.24 | $300 (**−$122 over**) |
| Shipping & tax | $58.45 | — |
| Ground equip / crash fund / software | $0.00 | $1,000 / $2,000 / — |

> **⚠ All spend so far is Project One (Betaflight 5" quad), which has no line in the stage budget.** Decide whether it comes from Stage 1's $700 or the $2,930 unallocated before the next order.

## Orders

One row per order, newest first. `Order #` blank = fill from confirmation email.

| Date | Vendor | Items | Subtotal | Ship + tax | **Total** | Order # | Status |
|---|---|---|---|---|---|---|---|
| 08-29 | MEPS King | Matek H743-Slim V4 FC ×1 | $125.99 | free / — | **$125.99** | | ordered |
| 08-29 | RaceDayQuads | Skystars KO60II 60A AM32 4-in-1 ESC ×1 ($58.49); HOTA D6 Pro 325W charger ×1 ($149.99) | $208.48 | free / $12.51 | **$220.99** | PNQ25YZPH | ordered, ETA 09-03 |
| 08-29 | Amazon | AiXun T3A 200W soldering station, **T12 handle** + 3 tips ×1 | $128.00 | free / $7.68 | **$135.68** | 112-5817558-1657853 | ordered, ETA 09-10–17 |
| 08-29 | Amazon | Consumables & tools bundle, 13 items (cap, XT60 pigtail, heat shrink, threadlocker, zip ties, M3 screws, LiPo bag, solder, flux, wick, smoke stopper, multimeter, hex drivers, safety glasses) | $144.25 (after $1.50 coupon) | free / $8.66 | **$152.91** | 112-0737547-2133806 | ordered |
| 08-29 | RMRC | TBS Source One **V6** 5" frame kit ×1 | $35.85 | $6.68 / not quoted | **$42.53** + tax? | | ordered |
| 08-29 | RaceDayQuads | GNB 6S 1530 mAh 160C LiPo, XT60 ×1 | $44.99 | $10.60 / $3.33 | **$58.92** | | ordered |
| 08-26 | EMAX USA | ECO II 2207 1900KV motor ×4 @ $12.99 | $51.96 | $8.99 / $0 | **$60.95** | | ordered (Shop Pay) |

**Phase 1 purchasing is complete** — every part needed for bench-alive is ordered.

## On-arrival checks

- **Soldering station (Sep 10–17) is the schedule-critical item.** It's the T12 handle, not the T245 the list specified — use a large chisel tip and run ~380–400 °C for the ESC battery pads and 12 AWG XT60 leads.
- **Motor screw length vs. the frame's 6 mm arms:** ~arm thickness + 5 mm. Too long kills the motor; too short loses one in flight. The M3×10/12/14 in the frame kit are standoff hardware, not motor screws.
- **FC ↔ ESC pinout:** different brands; 8-pin JST-SH pin *order* is not standard. Compare diagrams, continuity-check, first power-up through the smoke stopper.
- **ESC box may include a capacitor and XT60 lead** — duplicates of the Amazon ones; keep as spares.
- **Battery:** don't charge until the charger and LiPo bag arrive; store in the bag from the first charge.
- **MEPS King** didn't state shipping origin — watch for a customs charge on delivery; add it here if billed.
- **RMRC** tax not quoted at checkout — update the total from the email.
- **Flash Betaflight first** on the H743 for a known-good baseline before ArduPilot/INAV.

## Returns, refunds & warranty

| Date | Item | Vendor | Order # | Amount | Reason | Resolved? |
|---|---|---|---|---|---|---|
| | | | | | | |

## Recurring costs

| Item | Cost | Frequency | Next due |
|---|---|---|---|
| FAA recreational registration | $5 | every 3 years | |

## How to log a purchase

1. Add one row to **Orders** with the order number.
2. Update **Totals**.
3. Mark `arrived` when the box is opened and checked, not when tracking says delivered.
4. Keep the vendor email — this file is the index, the email is the proof for warranty claims.
