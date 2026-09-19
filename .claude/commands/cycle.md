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

   - `notes/chNN-<slug>.md` — exactly this, with the chapter's own title:

     ```markdown
     # Ch N — <chapter title>

     ## Distillation (closed-book)

     <!-- Book shut. 45 minutes. Full sentences, not fragments — a fragment
          can't be wrong, which is how closed-book recall gets faked without
          you noticing. Mark every claim [sure] or [shaky]. -->

     ### The question this chapter answers

     <!-- One sentence. If you can't write it, you didn't get the chapter. -->

     ### Mechanisms

     <!-- For each: what it does / how it works / what it costs.
          The cost slot is mandatory. An empty one means you absorbed
          marketing, not engineering — and it's exactly what the explainer
          rubric scores in dimension 2. -->

     ### Trade-offs

     | Axis | One side | Other side | What decides |
     |------|----------|------------|--------------|
     |      |          |            |              |

     ### When this breaks

     <!-- Failure modes, and the conditions that trigger them. -->

     ### Connections

     <!-- What this changes about earlier chapters and about your own build. -->

     ### Open questions

     <!-- WRITE THESE BEFORE OPENING THE BOOK.
          Things you're unsure of. Highest-value section in the file. -->

     ## What I got wrong

     <!-- Only after the above is done. 45 minutes. Open the book and correct
          yourself here. Each correction cites a section.

          Watch for two kinds:
            - [shaky] that turned out right — you know more than you think
            - [sure] that turned out wrong — the dangerous kind; raw
              correctness hides these completely

          Every miss goes into review/queue.md. -->
     ```

     The sub-headings are deliberately *not* the chapter's own section
     headings — organizing by the book's structure lets them reproduce a
     table of contents without understanding anything.

     Where a section will predictably be thin or empty for this chapter, say
     so in its comment, so a short section doesn't read as bad recall.
     Connections is empty until roughly chapter 6.

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
