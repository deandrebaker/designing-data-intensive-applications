---
description: Work the spaced-repetition queue — quiz due items cold, or run the cumulative exam
argument-hint: [exam]
---

Run a spaced-repetition session from `review/queue.md`. Its header defines
cycles, intervals and the item format; follow it exactly. With `exam` as the
argument, run the cumulative exam instead (below).

1. Select every open item whose `due` is the current cycle or earlier. The
   current cycle is the current chapter number in `PROGRESS.md`, or 15–18 in
   the interview block. If more than 12 are due, take the 12 oldest — don't
   run a marathon.

2. Quiz them **one item at a time**, closed-book. Ask the prompt exactly as
   written. Wait for the answer.

3. Score each as hit or miss against the item's `key` — their own corrected
   understanding — not against your memory of the book. Be strict: a partial
   answer that misses the mechanism is a miss. Fluency is not knowledge. If an
   item has no key, have the learner write one after answering.

4. Update each item per the interval rules in the queue header. Hits at
   interval 4 move to Graduated.

5. Where an item is missed twice running, don't just requeue it. Point at its
   `ref` and the chapter's reference one-pager (linked in `PROGRESS.md`'s
   cycle log), and suggest they redraw that mechanism's diagram from memory —
   repeated misses usually mean the mental model is missing, not the fact.

6. For each item still tagged `verify`, remind the learner to check its key against
   the book at its `ref` once the session is over.

7. If this was the current cycle's phase-6 review, tick Review in
   `PROGRESS.md`.

Close with a one-line state of the queue: how many due, how many graduated,
which chapter is generating the most repeat misses.

## `/review exam`

The cumulative closed-book exam at the start of the interview block (plan §7),
and the test of success criterion 5.

- Draw about 20 items from Open and Graduated together: at least one per
  chapter, weighted toward the earliest chapters, since they've had longest
  to fade.
- Quiz and score them exactly as above. Hits leave intervals unchanged; misses
  go back into Open at interval 1, due next cycle.
- Record the result in the Cumulative exam table in `PROGRESS.md`: items,
  hits, and the weakest chapter.
