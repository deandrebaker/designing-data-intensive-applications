---
description: Work the spaced-repetition queue — quiz due items cold
---

Run a spaced-repetition session from `review/queue.md`.

1. Read the queue and select every item whose `due` cycle is the current cycle
   or earlier (current cycle is in `PROGRESS.md`). If more than 12 are due, take
   the 12 oldest — don't run a marathon.

2. Quiz them **one item at a time**, closed-book. Ask the prompt exactly as
   written. Wait for the answer.

3. Score each as hit or miss. Be strict: a partial answer that misses the
   mechanism is a miss. Fluency is not knowledge.

4. Update each item's interval, Leitner-style:
   - **miss** → `due: next cycle`, and reset its interval to 1
   - **hit** → push out by its current interval doubled: 2 cycles, then 4,
     then 8. An item that survives 8 cycles graduates — delete it.

5. Where an item is missed twice running, don't just requeue it. Point at the
   chapter and section, and suggest they redraw that mechanism's diagram from
   memory — repeated misses usually mean the mental model is missing, not the
   fact.

Close with a one-line state of the queue: how many due, how many graduated,
which chapter is generating the most repeat misses.
