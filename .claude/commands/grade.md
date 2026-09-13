---
description: Score an explainer or design problem against its rubric
argument-hint: explainer <N> | problem <N>
---

Grade `$ARGUMENTS`.

- `explainer N` → grade `explainers/chNN.md` against `.claude/rubrics/explainer.md`
- `problem N` → grade the file in `problems/` for chapter N against
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

Where they're wrong about a mechanism, cite the chapter and section.

## After

- Record the five scores in `PROGRESS.md` so drift is visible over time.
- Append anything they got materially wrong to `review/queue.md`.
- Name the single highest-leverage thing to fix. One thing, not a list.

Do not soften. An inflated score here costs them a real interview later.
