---
description: Score an explainer, design problem or mock interview against its rubric
argument-hint: explainer <N> | problem <N> | mock <N>
---

Grade `$ARGUMENTS`.

- `explainer N` → grade `explainers/chNN.md` against `.claude/rubrics/explainer.md`
- `problem N` → grade `problems/chNN-<slug>.md`, chapter N's design problem,
  against `.claude/rubrics/design-problem.md`
- `mock N` → grade `problems/mockNN-<slug>.md` against
  `.claude/rubrics/design-problem.md`

## How to grade

Score all five rubric dimensions 1–5. **Every score requires quoted evidence
from their text.** A score without a quote attached is not a score, it's a
vibe — go back and find the sentence that earned it.

Lead with the weakest dimension, not the strongest. Open with the honest
headline ("This is a 2 on failure modes — the word 'partition' doesn't appear
anywhere"), then the evidence, then what a 5 would have said instead.

Be specific about the fix. Not "expand on tradeoffs" but "you said quorum reads
give you consistency; say what they cost — every read now waits on the slowest
of r nodes, so your p99 is a tail-latency problem you didn't have before."

Where they're wrong about a mechanism, cite per `CLAUDE.md` rule 4.

## After

- Record the five scores in `PROGRESS.md`, in the explainer, design problem or
  mock interview table.
- Append anything they got materially wrong to `review/queue.md`, in the
  format defined there, due the next cycle. The learner writes the `key`; tag it
  `verify` when it rests on your correction.
- Name the single highest-leverage thing to fix. One thing, not a list.
- For a problem or mock, ask the learner to write the post-mortem — the single
  biggest gap, in their own words — at the bottom of the answer file.
- For an explainer or chapter problem, tick Explain or Design problem in the
  current cycle's checklist.

Do not soften. An inflated score here costs them a real interview later.
