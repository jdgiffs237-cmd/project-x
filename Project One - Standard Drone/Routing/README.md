# Routing — Work Instructions

The build, written down the way a factory would route it: numbered work
instructions (WIs), each one a sequence of operations with the tools,
parts, and checks it needs. Follow them in order; each WI ends in a
verifiable state, so a session can stop at the end of any WI without
leaving the aircraft in an unknown condition.

## Index

| WI | Title | Needs | Status |
|---|---|---|---|
| [WI-01](WI-01-bench-setup-and-frame.md) | Bench setup, frame assembly, motor mounting | No FC | in progress |
| [WI-02](WI-02-esc-soldering.md) | ESC soldering — motors, XT60, capacitor | No FC | not started |
| WI-03 | FC install, pinout verification, first power-up | **FC** | blocked on delivery |
| WI-04 | Betaflight setup → bench-alive | FC | not started |

## Rules for writing a WI

1. **One WI = one sitting.** If it can't be done in an evening, split it.
2. Start with a **tools & parts list** — nothing mid-step should send you hunting.
3. Every step that can be verified gets a **CHECK** line. A WI is done when
   every CHECK passed, not when the steps were attempted.
4. Write down what actually happened, including mistakes — this is also the
   raw material for the [blog](../../blog/).
5. Safety lines are bold and come **before** the step they protect.
