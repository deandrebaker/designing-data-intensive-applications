# Retrieval queue

Spaced-repetition items, worked by `/review`. They come from three places:

- `/grill` misses
- 3–5 core items per chapter, added at the end of `/grill` whether they were
  hit or missed — otherwise a clean chapter is never asked again
- each chapter's "What I got wrong" section, moved in by `/close`

## Cycles

A cycle is a chapter number: cycle 4 is the chapter 4 cycle. The interview
block's four weeks are cycles 15–18. Breaks don't advance the counter, so
nothing comes due during one.

## Intervals

- **New item:** `interval: 1`, due next cycle.
- **Miss:** back to `interval: 1`, due next cycle, `misses` +1.
- **Hit:** interval 1 → 2 → 4, due that many cycles ahead. A hit at interval 4
  graduates the item: move it to Graduated at the bottom.

Graduated items leave the rotation but stay in the file. `/review exam` draws
on them for the cumulative exam at the start of the interview block.

## Format

Every command that writes here uses exactly this:

```
- [ch04] What does compaction actually reclaim, and what does it cost while running?
  ref: ch04 "<heading copied from plan/toc.md>"
  key: <one line, in the learner's own words>
  due: 5 | interval: 1 | misses: 1
```

- `ref` — the chapter and a heading from `plan/toc.md`. Append ` verify` when
  the key rests on a correction Claude made without the book open. The learner
  checks it against the book and drops the tag; if the book disagrees, the
  book wins and the key is rewritten.
- `key` — the learner's words, quoted from their notes or dictated, never Claude's
  paraphrase. It's what `/review` scores against.
- `due` — a cycle number, never "next cycle".

Keep open items flat and sorted by `due`. When they exceed ~40, that's a
signal to slow down, not to prune.

---

## Open

*(empty — first items arrive with chapter 1's `/grill` and `/close`)*

## Graduated

*(empty)*
