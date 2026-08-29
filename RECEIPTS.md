# Receipts — Money Actually Spent

**Last updated:** 2026-08-26
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
| **Total spent to date** | **$60.95** |
| Refunds / returns received | −$0.00 |
| **Net spent** | **$60.95** |
| Remaining against ceiling | **$9,939.05** |

---

## Spend by bucket

Buckets match [04-budget.md](brainstorming/04-budget.md) so the two files can be compared directly.

| Bucket | Planned | Spent | Remaining |
|---|---|---|---|
| Aircraft | — | $51.96 | — |
| Ground equipment | $1,000 | $0.00 | $1,000.00 |
| Tools & consumables | $300 | $0.00 | $300.00 |
| Crash fund & regulatory | $2,000 | $0.00 | $2,000.00 |
| Software & subscriptions | — | $0.00 | — |
| Shipping & tax | — | $8.99 | — |
| **TOTAL** | **$10,000** | **$60.95** | **$9,939.05** |

## Spend by stage

| Stage | Allocated | Spent | Remaining |
|---|---|---|---|
| Stage 0 — whoop + simulator | $170 | $0.00 | $170.00 |
| **Project One — 5" freestyle quad** | *unbudgeted* | **$60.95** | — |
| Stage 1 — ArduPilot quad + GPS | $700 | $0.00 | $700.00 |
| Stage 2 — foam fixed-wing | $400 | $0.00 | $400.00 |
| Stage 3 — delta VTOL quadplane | $2,500 | $0.00 | $2,500.00 |
| Unallocated | $2,930 | $0.00 | $2,930.00 |

> **⚠ Project One is not in the stage plan.** [04-budget.md](brainstorming/04-budget.md)
> allocates Stages 0–3, where Stage 1 is an *ArduPilot* quad with GPS. Project One
> is a Betaflight 5" freestyle quad — a different aircraft, and it has no
> allocation. Its own docs use **Phases** 1–3, a separate axis from these Stages.
> Its Phase 1 shopping list runs **~$625–655**, which has to come from somewhere:
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

---

## Orders

One block per order — the receipt as it arrived, before it was split into line items above.
Newest first.

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
