# Receipts — Money Actually Spent

**Last updated:** 2026-08-19
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
| **Total spent to date** | **$0.00** |
| Refunds / returns received | −$0.00 |
| **Net spent** | **$0.00** |
| Remaining against ceiling | **$10,000.00** |

---

## Spend by bucket

Buckets match [04-budget.md](brainstorming/04-budget.md) so the two files can be compared directly.

| Bucket | Planned | Spent | Remaining |
|---|---|---|---|
| Aircraft | — | $0.00 | — |
| Ground equipment | $1,000 | $0.00 | $1,000.00 |
| Tools & consumables | $300 | $0.00 | $300.00 |
| Crash fund & regulatory | $2,000 | $0.00 | $2,000.00 |
| Software & subscriptions | — | $0.00 | — |
| Shipping & tax | — | $0.00 | — |
| **TOTAL** | **$10,000** | **$0.00** | **$10,000.00** |

## Spend by stage

| Stage | Allocated | Spent | Remaining |
|---|---|---|---|
| Stage 0 — whoop + simulator | $170 | $0.00 | $170.00 |
| Stage 1 — ArduPilot quad + GPS | $700 | $0.00 | $700.00 |
| Stage 2 — foam fixed-wing | $400 | $0.00 | $400.00 |
| Stage 3 — delta VTOL quadplane | $2,500 | $0.00 | $2,500.00 |
| Unallocated | $2,930 | $0.00 | $2,930.00 |

---

## Receipt log

One row per line item. Split a multi-item order into one row per item, sharing an order number.

**Bucket codes:** `AIR` aircraft · `GND` ground equipment · `TOOL` tools & consumables · `CRASH` crash fund & regulatory · `SW` software · `SHIP` shipping & tax
**Status:** `ordered` · `shipped` · `arrived` · `returned` · `refunded`

| Date | Item | Vendor | Bucket | Stage | Qty | Unit | Total | Order # | Status | Notes |
|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | |

---

## Orders

One block per order — the receipt as it arrived, before it was split into line items above.
Newest first. Delete the example once the first real order lands.

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
