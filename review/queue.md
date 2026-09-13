# Retrieval queue

Spaced-repetition items. Worked by `/review` each cycle; added by `/grill`
from misses, and from the "What I got wrong" sections of each chapter's notes.

**Interval rule (Leitner):** a miss resets to `due: next cycle` with
`interval: 1`. A hit doubles the interval — 2 cycles, then 4, then 8. An item
that survives an 8-cycle gap graduates and is deleted.

Format:

```
- [ch04] What does compaction actually reclaim, and what does it cost while running?
  due: 5 | interval: 2 | misses: 1
```

Keep it flat and sorted by `due`. When it exceeds ~40 open items, that's a
signal to slow down, not to prune.

---

*(empty — first items arrive after chapter 1's `/grill`)*
