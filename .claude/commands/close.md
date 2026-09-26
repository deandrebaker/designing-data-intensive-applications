---
description: Close a chapter's cycle — verify every phase, record hours, feed the queue, hand off
argument-hint: <chapter number>
---

Close the cycle for **chapter $1**. Closing is bookkeeping and a hand-off; it
never shortens a cycle.

1. **Confirm every phase is done.** Check chapter $1's checklist in
   `PROGRESS.md` against the files:
   - Distill — `notes/chNN-*.md` has both the distillation and "What I got
     wrong"; `diagrams/chNN.md` has a from-memory diagram.
   - Build — the build's `NOTES.md` says where they got stuck. Spine chapters:
     the scope note exists, and the learner confirms its MVP is done.
   - Explain — `explainers/chNN.md` is written and its scores are in
     `PROGRESS.md`.
   - Design problem (plan §6 cycles only) — graded, with a post-mortem.
   - Read, Grill, Review — ticked; ask if unsure.

   Tick any box the evidence shows is done. If anything is unfinished, list
   what's left and stop. The plan slows down rather than skips (plan §8), so
   the cycle stays open until it's done.

2. **Record hours.** Ask the learner for actual hours per phase — rough is fine —
   and fill chapter $1's row in the Actual hours table, with calendar days from
   start to today. After closing chapter 3, compare the three rows with the
   budget and propose revised per-phase budgets for plan §4; the learner decides
   whether to adopt them.

3. **Feed the queue.** Each correction in the notes' "What I got wrong" section
   becomes an item in `review/queue.md`, in the format defined there, due cycle
   $1 + 1 at interval 1. Skip any `/grill` already added. The `ref` is the
   heading they cited; the `key` is their correction, quoted. If it won't fit
   on one line, ask them to compress it. These were written with the book
   open, so they don't take `verify`.

4. **Log the slip.** If today is past chapter $1's baseline end (plan §8), add
   a line to the Log in `PROGRESS.md`: baseline end, actual close, days over,
   and the phase that ran longest. Slipping is the policy; the line is data
   for the re-budget, not a judgement.

5. **Tag spine chapters** (4–10, 13). The tag must point at their finished
   chapter, so `git status --short -- builds/kvstore` has to be clean; if it
   isn't, ask them to commit first. Then create the tag, zero-padded:
   `ch04-complete`.

6. **Publish the reference one-pager** (plan §10): the chapter's mechanism
   drawn properly, its failure modes, a tradeoff table. Build it only from
   `notes/chNN-*.md` as corrected by "What I got wrong" and the Reference half
   of `diagrams/chNN.md`. Anything not in their files stays out — filling gaps
   from your memory of the book would put your errors into their review
   material. Publish it as an artifact and add its link to the chapter's cycle
   log entry.

7. **Close and hand off.** In `PROGRESS.md`: status ✓ closed, Actual end date,
   Closed ticked. Then tell the learner, briefly, what the next cycle inherits:
   - open questions from the notes that the book didn't settle
   - Stretch items and known defects from the build's `NOTES.md`
   - queue items still tagged `verify`
