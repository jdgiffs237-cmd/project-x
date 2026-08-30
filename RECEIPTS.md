# Receipts — Money Actually Spent

**Last updated:** 2026-08-29
**Budget ceiling:** $10,000 → see [brainstorming/04-budget.md](brainstorming/04-budget.md)

> This file records **what was actually paid**. The budget file records what was *planned*.
> When the two disagree, this file is right.
>
> **This repo is public.** Record order numbers and vendors — never card numbers,
> billing addresses, or account logins.

---

## Running total

Update these three numbers every time you add a receipt. Everything else is detail.

| | Amount |
|---|---|
| **Total spent to date** | **$797.97** |
| Refunds / returns received | −$0.00 |
| **Net spent** | **$797.97** |
| Remaining against ceiling | **$9,202.03** |

---

## Spend by bucket

Buckets match [04-budget.md](brainstorming/04-budget.md) so the two files can be compared directly.

| Bucket | Planned | Spent | Remaining |
|---|---|---|---|
| Aircraft | — | $317.28 | — |
| Ground equipment | $1,000 | $0.00 | $1,000.00 |
| Tools & consumables | $300 | **$422.24** | **−$122.24 OVER** |
| Crash fund & regulatory | $2,000 | $0.00 | $2,000.00 |
| Software & subscriptions | — | $0.00 | — |
| Shipping & tax | — | $58.45 | — |
| **TOTAL** | **$10,000** | **$797.97** | **$9,202.03** |

## Spend by stage

| Stage | Allocated | Spent | Remaining |
|---|---|---|---|
| Stage 0 — whoop + simulator | $170 | $0.00 | $170.00 |
| **Project One — 5" freestyle quad** | *unbudgeted* | **$797.97** | — |
| Stage 1 — ArduPilot quad + GPS | $700 | $0.00 | $700.00 |
| Stage 2 — foam fixed-wing | $400 | $0.00 | $400.00 |
| Stage 3 — delta VTOL quadplane | $2,500 | $0.00 | $2,500.00 |
| Unallocated | $2,930 | $0.00 | $2,930.00 |

> **⚠ Project One is not in the stage plan.** [04-budget.md](brainstorming/04-budget.md)
> allocates Stages 0–3, where Stage 1 is an *ArduPilot* quad with GPS. Project One
> is a Betaflight 5" freestyle quad — a different aircraft, and it has no
> allocation. Its own docs use **Phases** 1–3, a separate axis from these Stages.
> Its Phase 1 shopping list runs **~$661**, which has to come from somewhere:
> either Stage 1's $700, the $2,930 unallocated, or a new line. **Unresolved —
> decide before the next order.**

---

## Receipt log

One row per line item. Split a multi-item order into one row per item, sharing an order number.

**Bucket codes:** `AIR` aircraft · `GND` ground equipment · `TOOL` tools & consumables · `CRASH` crash fund & regulatory · `SW` software · `SHIP` shipping & tax
**Status:** `ordered` · `shipped` · `arrived` · `returned` · `refunded`

| Date | Item | Vendor | Bucket | Stage | Qty | Unit | Total | Order # | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| 2026-08-26 | EMAX ECO II 2207 1900KV motor | EMAX USA | AIR | P1 | 4 | $12.99 | $51.96 | *(fill from email)* | ordered | Direct; beat Pyrodrone $15.99 and RDQ $19.49 |
| 2026-08-26 | Shipping | EMAX USA | SHIP | P1 | — | — | $8.99 | *(same order)* | ordered | |
| 2026-08-29 | Gaoneng GNB 6S 1530 mAh 160C LiPo, XT60 | RaceDayQuads | AIR | P1 | 1 | $44.99 | $44.99 | *(fill from email)* | ordered | 245 A. Bought ahead of the 2026-09-03 tariff date |
| 2026-08-29 | Shipping | RaceDayQuads | SHIP | P1 | — | — | $10.60 | *(same order)* | ordered | |
| 2026-08-29 | Estimated tax | RaceDayQuads | SHIP | P1 | — | — | $3.33 | *(same order)* | ordered | |
| 2026-08-29 | TBS Source One V6 frame, 5" kit | RMRC | AIR | P1 | 1 | $35.85 | $35.85 | *(fill from email)* | ordered | V6, not V5 — RMRC URL still says v5 |
| 2026-08-29 | Shipping | RMRC | SHIP | P1 | — | — | $6.68 | *(same order)* | ordered | Tax not yet confirmed |
| 2026-08-29 | Consumables & tools bundle (13 items) | Amazon | TOOL | P1 | 13 | — | $144.25 | 112-0737547-2133806 | ordered | Net of $1.50 coupon. Per-item prices not itemised — includes ~$16 of AIR parts (capacitor, XT60 pigtail) |
| 2026-08-29 | Estimated tax | Amazon | SHIP | P1 | — | — | $8.66 | *(same order)* | ordered | Free shipping |
| 2026-08-29 | AiXun T3A 200W soldering station, T12 handle + 3 tips | Amazon | TOOL | P1 | 1 | $128.00 | $128.00 | 112-5817558-1657853 | ordered | **T12 handle, not the T245 the list specified.** Arriving Sep 10–17 |
| 2026-08-29 | Estimated tax | Amazon | SHIP | P1 | — | — | $7.68 | *(same order)* | ordered | Free shipping |
| 2026-08-29 | Skystars KO60II 60A 3-6S AM32 4-in-1 ESC, 30×30 | RaceDayQuads | AIR | P1 | 1 | $58.49 | $58.49 | PNQ25YZPH | ordered | Open-source AM32 firmware |
| 2026-08-29 | HOTA D6 Pro 325W AC/DC charger, gray | RaceDayQuads | TOOL | P1 | 1 | $149.99 | $149.99 | *(same order)* | ordered | |
| 2026-08-29 | Estimated tax | RaceDayQuads | SHIP | P1 | — | — | $12.51 | *(same order)* | ordered | Free USA shipping — consolidating saved a second charge |
| 2026-08-29 | Matek H743-Slim V4 flight controller, 30×30 | MEPS King | AIR | P1 | 1 | $125.99 | $125.99 | *(fill from email)* | ordered | H7, 2 MB flash. Official ArduPilot + INAV + Betaflight targets. Free shipping over $79 |

---

## Orders

One block per order — the receipt as it arrived, before it was split into line items above.
Newest first.

### 2026-08-29 — MEPS King — $125.99

| | |
|---|---|
| **Order #** | *(fill from confirmation email)* |
| **Paid with** | *(fill in)* |
| **Ship date** | *(quoted: within 3 days of order)* |
| **Arrived** | |
| **Tracking** | |
| **Return window closes** | *(check MEPS King policy — fill in)* |

| Item | Qty | Unit | Total |
|---|---|---|---|
| Matek H743-Slim V4 flight controller — 30×30 | 1 | $125.99 | $125.99 |
| Subtotal | | | $125.99 |
| Shipping | | | $0.00 (free over $79) |
| Tax | | | *(none stated)* |
| **Total** | | | **$125.99** |

**Notes:**
- **This completes Phase 1 purchasing.** Every item needed to reach bench-alive is
  now bought.
- Chosen over the SpeedyBee F405 V5 FC ($66.59) to keep autonomy and onboard
  scripting possible. ArduPilot Lua needs 2 MB of flash and is unavailable on F4
  autopilots; the H743 has 2 MB plus a microSD slot. Official `MATEKH743` targets
  for ArduPilot, INAV **and** Betaflight.
- **Watch for a customs charge on delivery.** MEPS King did not state a shipping
  origin. If this ships from China and crosses after 2026-09-03, duties may be
  billed on arrival. Add a SHIP row here if that happens.
- **Flash Betaflight first.** Reach bench-alive on the simple firmware before
  reflashing to ArduPilot or INAV, so there is a known-good baseline to return to.
- **Pinout check before first power-up.** Matek FC and Skystars ESC are different
  brands; 8-pin JST-SH is physically standard but pin *order* is not.

### 2026-08-29 — RaceDayQuads — $220.99

| | |
|---|---|
| **Order #** | PNQ25YZPH |
| **Paid with** | *(fill in)* |
| **Ship date** | |
| **Arrived** | |
| **Tracking** | *(track via Shop)* |
| **Estimated delivery** | **Thu 2026-09-03** (2–4 business days) |
| **Return window closes** | *(check RDQ policy — fill in)* |

| Item | Qty | Unit | Total |
|---|---|---|---|
| Skystars KO60II 60A 3-6S AM32 4-in-1 ESC — 30×30 | 1 | $58.49 | $58.49 |
| HOTA D6 Pro 325W 15A 1-6S AC/DC charger — gray | 1 | $149.99 | $149.99 |
| Subtotal | | | $208.48 |
| Shipping | | | **FREE** |
| Estimated tax | | | $12.51 |
| **Total** | | | **$220.99** |

**Notes:**
- **Consolidated deliberately.** Both items in one order, and RDQ's free-shipping
  threshold was met — versus $10.60 shipping on the battery order alone. Ordering
  these separately would have cost a shipping charge for nothing.
- **On arrival, check the ESC box for a capacitor and an XT60 lead.** Many 4-in-1
  ESCs include both, and both were bought separately in the Amazon order. If they
  are in the box, the spares are still useful — XT60s are easy to ruin while
  learning to solder 12 AWG.
- **Do not charge the battery until the LiPo-safe bag is to hand.** Bag is in the
  Amazon order.
- **Pinout check before first power-up.** This ESC and whichever FC is chosen are
  different brands. 8-pin JST-SH is physically standard but pin *order* is not.
  Compare both diagrams, continuity-check every wire, first power-up through the
  smoke stopper.

### 2026-08-29 — Amazon — $135.68

| | |
|---|---|
| **Order #** | 112-5817558-1657853 |
| **Paid with** | Visa ending 0595 |
| **Ship date** | |
| **Arrived** | |
| **Tracking** | |
| **Return window closes** | *(check — Amazon is usually 30 days from delivery)* |

| Item | Qty | Unit | Total |
|---|---|---|---|
| AiXun T3A 200W soldering station, **T12 handle** + 3 tips | 1 | $128.00 | $128.00 |
| Subtotal | | | $128.00 |
| Shipping | | | $0.00 |
| Tax | | | $7.68 |
| **Total** | | | **$135.68** |

**Notes:**
- **Arriving September 10–17** — the longest lead time of anything ordered. No
  soldering can start before it lands, so this is the schedule-critical item now,
  not the tariff date.
- **This is the T12 handle, not the T245 the shopping list specified.** T12 is a
  smaller cartridge with less thermal grunt. It will do the job, but the fat
  battery pads on the ESC and the 12 AWG XT60 leads are the joints where it will
  feel slow. Use a **large chisel tip**, not a fine conical, and run hotter
  (~380–400 °C) for those specific joints.
- Price was **$128.00 against a ~$70 estimate** — the estimate was wrong, not the
  purchase.

### 2026-08-29 — Amazon — $152.91

| | |
|---|---|
| **Order #** | 112-0737547-2133806 |
| **Paid with** | Visa ending 0595 |
| **Ship date** | |
| **Arrived** | |
| **Tracking** | |
| **Return window closes** | *(check — Amazon is usually 30 days from delivery)* |

| Item | Qty | Unit | Total |
|---|---|---|---|
| Consumables & tools bundle — 13 items | 13 | — | $145.75 |
| Coupon savings | | | −$1.50 |
| Subtotal after coupon | | | $144.25 |
| Shipping | | | $0.00 |
| Tax | | | $8.66 |
| **Total** | | | **$152.91** |

**Notes:**
- Covers the capacitor, XT60 pigtail, heat shrink, thread locker + zip ties, M3
  screw assortment, LiPo-safe bag, solder, flux, solder wick, smoke stopper,
  multimeter, hex drivers and safety glasses.
- **Per-item prices are not recorded** — the receipt shows only a subtotal. Logged
  as one bundle row. Itemise later from the Amazon order detail page if the
  per-part breakdown is ever needed.
- Bucketed to TOOL, though roughly $16 of it (capacitor + XT60 pigtail) is
  properly AIR.
- Came in **~$28 under** the list estimate for these 13 items.

### 2026-08-29 — RMRC — $42.53

| | |
|---|---|
| **Order #** | *(fill from confirmation email)* |
| **Paid with** | *(fill in)* |
| **Ship date** | |
| **Arrived** | |
| **Tracking** | |
| **Return window closes** | *(check RMRC policy — fill in)* |

| Item | Qty | Unit | Total |
|---|---|---|---|
| TBS Source One V6 frame, 5" kit | 1 | $35.85 | $35.85 |
| Subtotal | | | $35.85 |
| Shipping | | | $6.68 |
| Tax | | | *(not stated — confirm from email)* |
| **Total** | | | **$42.53 + any tax** |

**Notes:**
- The **V6**, despite RMRC's URL still reading "v5". The V5 is discontinued.
- **Check on arrival:** the arms are **6 mm thick**. Motor screws must be about
  arm thickness + 5 mm. Too long bottoms into the stator windings and kills the
  motor; too short and a motor departs in flight. The M3×10/12/14 screws in the
  frame kit are standoff hardware, **not** motor screws.
- Tax was not quoted at checkout — running totals count $42.53. Update if the
  confirmation email shows tax.
- **The FC is also an RMRC item** ($66.59). Ordering it separately means paying
  RMRC shipping twice.

### 2026-08-29 — RaceDayQuads — $58.92

| | |
|---|---|
| **Order #** | *(fill from confirmation email)* |
| **Paid with** | *(fill in)* |
| **Ship date** | |
| **Arrived** | |
| **Tracking** | |
| **Return window closes** | *(check RDQ policy — fill in)* |

| Item | Qty | Unit | Total |
|---|---|---|---|
| Gaoneng GNB 6S 1530 mAh 160C LiPo, XT60 | 1 | $44.99 | $44.99 |
| Subtotal | | | $44.99 |
| Shipping | | | $10.60 |
| Tax | | | $3.33 |
| **Total** | | | **$58.92** |

**Notes:**
- 245 A continuous against an estimated ~160 A full-throttle draw — genuine
  headroom. The rejected Tattu 75C pack managed only 97.5 A.
- **One pack is enough for Phase 1.** More packs are a Phase 2 purchase.
- Ordered ahead of the 2026-09-03 tariff date.
- Shipping $10.60 + estimated tax $3.33 = **$13.93 on top of the $44.99 pack**,
  a 31% uplift. Worth remembering when comparing single-item orders across
  vendors — consolidating the remaining RDQ items into one order avoids paying
  this twice.
- **Store it in the LiPo-safe bag from the very first charge.** That bag is still
  unbought — see [00-BUILD-TRACKER.md](Project%20One%20-%20Standard%20Drone/00-BUILD-TRACKER.md).
- **Do not charge it until the charger arrives.** Also unbought.

### 2026-08-26 — EMAX USA — $60.95

| | |
|---|---|
| **Order #** | *(fill from confirmation email)* |
| **Paid with** | Shop Pay |
| **Ship date** | |
| **Arrived** | |
| **Tracking** | |
| **Return window closes** | *(check EMAX policy — fill in)* |

| Item | Qty | Unit | Total |
|---|---|---|---|
| ECO II 2207 Brushless Motor — 1900KV | 4 | $12.99 | $51.96 |
| Subtotal | | | $51.96 |
| Shipping | | | $8.99 |
| Tax | | | $0.00 |
| **Total** | | | **$60.95** |

**Notes:**
- Bought manufacturer-direct. $12.99/motor vs $15.99 at Pyrodrone and $19.49 at
  RDQ — 19–33% under retail. Worth checking manufacturer stores for future parts.
- Ordered ahead of the 2026-09-03 tariff date.
- **Check on arrival:** motor screw length against the frame's 6 mm arms. Too
  long bottoms into the windings and kills the motor. See the compatibility
  check in [SHOPPING-LIST-PHASE-1.md](Project%20One%20-%20Standard%20Drone/SHOPPING-LIST-PHASE-1.md).

<!--
### YYYY-MM-DD — Vendor name — $0.00

| | |
|---|---|
| **Order #** | |
| **Paid with** | *(e.g. "personal card" — never the number)* |
| **Ship date** | |
| **Arrived** | |
| **Tracking** | |
| **Return window closes** | |

| Item | Qty | Unit | Total |
|---|---|---|---|
| | | | |
| Subtotal | | | $0.00 |
| Shipping | | | $0.00 |
| Tax | | | $0.00 |
| **Total** | | | **$0.00** |

**Notes:**
-->

---

## Returns, refunds & warranty claims

| Date | Item | Vendor | Order # | Amount | Reason | Resolved? |
|---|---|---|---|---|---|---|
| | | | | | | |

---

## Recurring costs

Subscriptions and renewals — the spend that doesn't show up as a one-time receipt.

| Item | Cost | Frequency | Started | Next due | Notes |
|---|---|---|---|---|---|
| FAA recreational registration | $5 | Every 3 years | | | Per operator |
| | | | | | |

---

## How to log a purchase

1. Add one row per item to the **receipt log**, with the order number.
2. Paste the full order into **Orders** if it has shipping, tax, or multiple items worth keeping together.
3. Update **running total** and the two rollup tables.
4. Mark `arrived` when the box is opened and the contents are checked — not when the tracking says delivered.
5. Note the **return window** for anything you're unsure about. It closes quietly.

> **Keep the vendor email too.** This file is the index; the emailed receipt is the
> proof for warranty claims. Don't rely on the vendor keeping order history forever.
