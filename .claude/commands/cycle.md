---
description: Start a chapter's cycle — scaffold its files, set the build goal and timebox
argument-hint: <chapter number>
---

Start the cycle for **chapter $1** of DDIA.

1. Read `plan/2026-09-13-ddia-learning-plan.md` — specifically the build spine
   table (§5), the schedule (§8), and whether chapter $1 is a design-problem
   cycle (§6).

2. Create these files if they don't exist. Each gets a stub with headings only
   — no content, since the content must come from memory:

   - `notes/chNN-<slug>.md` — headings: `## Distillation (closed-book)` and
     `## What I got wrong`
   - `explainers/chNN.md` — heading: `## <chapter title>, explained` plus a
     reminder of the constraint: no jargon undefined in the same document
   - `diagrams/chNN.md` — headings: `## From memory` (empty mermaid block) and
     `## Reference` (left empty until after the from-memory attempt)
   - the build directory named in the spine table, with a `NOTES.md` stub for
     recording where they got stuck

3. Update `PROGRESS.md`: mark chapter $1 as in progress, fill in its dates.

4. Then tell them, briefly:
   - the chapter's title and its date window
   - the build goal in one or two sentences, and its hard timebox
     (3.0h normally, 2.25h on design-problem cycles)
   - whether a design problem lands this cycle, and which one
   - which items are due in `review/queue.md` this cycle

Do **not** summarize the chapter, preview its concepts, or explain what they're
about to read. The first pass should be unspoiled.
