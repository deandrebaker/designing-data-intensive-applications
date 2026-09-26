---
description: Start a chapter's cycle — scaffold its files, set the build goal and timebox
argument-hint: <chapter number>
---

Start the cycle for **chapter $1** of DDIA.

1. Check that the previous chapter is closed: its status in `PROGRESS.md` is
   ✓ closed. If it isn't, say so, point them at `/close` for that chapter, and
   stop. Scaffold anyway only if the learner explicitly says to. (Chapter 1 has no
   previous chapter.)

2. Read `plan/2026-09-13-ddia-learning-plan.md` — specifically the build spine
   table, scope notes and open questions (§5), and whether chapter $1 is a
   design-problem cycle (§6).

3. Create these files if they don't exist. Each gets a stub with headings only
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

     <!-- What this changes about earlier chapters, about your own builds,
          and about systems you've worked on. -->

     ### Open questions

     <!-- WRITE THESE BEFORE OPENING THE BOOK.
          Things you're unsure of. Highest-value section in the file. -->

     ## What I got wrong

     <!-- Only after the above is done. 45 minutes. Open the book and correct
          yourself here. Each correction cites the chapter and heading it
          came from. While the book is open, copy this chapter's headings
          into plan/toc.md.

          Watch for two kinds:
            - [shaky] that turned out right — you know more than you think
            - [sure] that turned out wrong — the dangerous kind; raw
              correctness hides these completely

          /close moves every correction into review/queue.md. -->
     ```

     The sub-headings are deliberately *not* the chapter's own section
     headings — organizing by the book's structure lets them reproduce a
     table of contents without understanding anything.

     Where a section will predictably be thin or empty for this chapter, say
     so in its comment, so a short section doesn't read as bad recall. For
     chapters 1–3, point Connections at systems they've built or run at work
     — there are no earlier chapters to connect to yet.

   - `explainers/chNN.md` — heading: `## <chapter title>, explained` plus a
     reminder of the constraint: no jargon undefined in the same document.
     For chapters 1–3, add that Connections is scored against systems they've
     built (rubric dimension 5).
   - `diagrams/chNN.md` — headings: `## From memory` (empty mermaid block) and
     `## Reference` (left empty until after the from-memory attempt)

   The build lives under `builds/`, which is the learner's; your edit tools are
   denied there. Tell them what to create instead: the build directory named
   in the spine table, with a `NOTES.md` for recording where they got stuck.
   For spine chapters, that's a new `## Ch $1` section in
   `builds/kvstore/NOTES.md`, opening with the scope note — MVP / Stretch /
   Ignored (plan §5) — written before any code.

4. Update `PROGRESS.md`: mark chapter $1 in progress, fill in its Actual start
   date (today), update the Current cycle line, and copy the phase checklist
   into the cycle log under a heading for this chapter. On cycles without a
   design problem, write that line as plain text, not a box; on non-spine
   chapters, note "no tag" on the Closed line.

5. Then tell them, briefly:
   - the chapter's title
   - the build goal in one or two sentences, and its 3.0h timebox — a
     checkpoint, not a cutoff (plan §4)
   - for spine chapters: write the scope note before any code
   - whether a design problem lands this cycle, and which one
   - which items are due in `review/queue.md` this cycle
   - any open question from plan §5 that's raised at this chapter or due
     before this chapter's build — quoted verbatim, with no hint toward an
     answer

Do **not** summarize the chapter, preview its concepts, or explain what they're
about to read. The first pass should be unspoiled.
