# Work Instructions — the build, routed

The build, written down the way a factory would route it: numbered work
instructions (WIs), each a sequence of operations with the tools, parts, and
checks it needs. Follow them in order. Each WI ends in a verifiable state, so a
session can stop at the end of any WI without leaving the aircraft in an
unknown condition.

Every WI is written as a **slide deck** — one slide per step, one photo, one
check — so the build can be walked through the same way it was done. It exists
in two forms:

- **The markdown WIs** (`WI-NN-*.md`) — the written procedure, readable right
  here on GitHub.
- **[Project-One-Build-Walkthrough.pptx](Project-One-Build-Walkthrough.pptx)** —
  one slide deck covering every WI, edited in Google Slides. This is the
  presentation; the markdown is the reference.

## Index

| WI | Title | Steps | Needs | Status |
|---|---|---|---|---|
| [WI-01](WI-01-bench-setup-and-frame.md) | Bench setup, frame assembly, motor mounting | 11 | No FC | **Complete — 2026-09-20** |
| [WI-02](WI-02-esc-soldering.md) | ESC soldering — motors, XT60, capacitor | 11 | No FC | **In progress** — started 2026-09-21 |
| WI-03 | FC install, pinout verification, first power-up | — | **FC** | Blocked on delivery (ETA Sep 22–25) |
| WI-04 | Betaflight setup → bench-alive | — | FC | Not started |

## How a slide is built

```markdown
## Slide 5: Bottom plate, arms, standoffs

*Op 30 · 30 min*

<img src="images/wi-01/05-frame-assembled.jpg" width="480" alt="What the photo shows">

**Do**

1. ...

**Check:** the one observation that proves the step is done.

<sub>[◀ Prev](#slide-4-...) · [Deck](#deck) · [Next ▶](#slide-6-...)</sub>
```

- **Heading** is `Slide N: title`. The deck table at the top of the WI links
  to every slide by that heading.
- **Photo** sits directly under the heading, before the words. Until a photo
  exists the slot is an HTML comment naming the file it's waiting for, so
  nothing looks broken.
- **Do** is the action; **Check** is the observation. A slide without a check
  isn't a slide, it's a caption.
- **Safety lines are bold and come before the step they protect.**

## Adding photos — the workflow

1. **Drop phone originals into `Pictures/`** with a plain-English filename
   (`Loctite on screw.jpeg`). That folder is git-ignored: it's the inbox, and
   5 MB originals never enter the repository.
2. **Import each one** into the WI it belongs to. This applies the phone's
   rotation, strips every bit of metadata (phone photos carry GPS — this repo
   is public), and resizes to 1600 px / ~300 KB:

   ```
   python tools/import-photo.py "Pictures/Loctite on screw.jpeg" images/wi-01/08c-loctite-on-screw.jpg
   ```

   Names are `SS-short-description.jpg` — `SS` is the slide number, with a
   letter suffix (`08a`, `08b`) when a slide has more than one photo.
3. **Wire it into the markdown** — replace the `<!-- photo: … -->` comment with
   an image tag:

   ```markdown
   <img src="images/wi-01/08c-loctite-on-screw.jpg" width="480" alt="What the photo shows">
   ```
4. **Drop it into the slide deck.** Every slide that is still waiting for a
   photo has a labelled `PHOTO` slot; the tool fills it in place and keeps the
   deck's own layout:

   ```
   python tools/deck-add-photo.py --list                     # which slots are still empty
   python tools/deck-add-photo.py 5 images/wi-01/02-iron-at-temperature.jpg
   ```

   Then re-upload the `.pptx` to Google Drive to see it in Slides.

## The slide deck and Google Slides

The deck is edited in Google Slides and lives here as the downloaded `.pptx`.
The round trip:

- **Slides → repo:** File → Download → Microsoft PowerPoint (.pptx), save it
  over `Project-One-Build-Walkthrough.pptx`, commit.
- **Repo → Slides:** upload the `.pptx` to Drive, open, File → Save as Google
  Slides (replace the old copy).

Nothing regenerates this file from the markdown — the two are kept in step by
hand, and the deck wins on layout while the markdown wins on wording.

## Rules for writing a WI

1. **One WI = one sitting.** If it can't be done in an evening, split it.
2. Slide 1 is always **tools & parts on the bench** — nothing mid-deck should
   send you hunting.
3. Every slide that can be verified gets a **Check**. A WI is done when every
   check passed, not when the steps were attempted.
4. Write down what actually happened, including mistakes — this is also the
   raw material for the [build log](../../build-log/) and the [blog](../../blog/).
