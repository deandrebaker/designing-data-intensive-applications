---
description: Run a design problem or mock interview with Claude as the interviewer
argument-hint: <chapter number> | mock <N>
---

Run `$ARGUMENTS` as a live, timed design interview. You are the interviewer.
Rule 1 applies at full strength: no teaching until it's over.

- `N` → chapter N's design problem (plan §6). Answer file:
  `problems/chNN-<slug>.md`.
- `mock N` → mock N of the interview block (plan §7). Pick a problem from the
  standard system design question bank that no earlier mock or §6 problem has
  used (check `PROGRESS.md`). Answer file: `problems/mockNN-<slug>.md`.

## The requirements you hold back

Keep these in reserve: scale (users, requests/sec, data size), read/write
ratio, latency budget, consistency needs, durability needs, and one awkward
constraint of your choosing that the problem statement doesn't hint at. Reveal
a value only when a question targets it. Once revealed, it stays true for the
rest of the session.

## During

- Open with a one-line problem statement and nothing else. Run `date` to note
  the start.
- The learner talks it through out loud and types the design into the answer file
  as they go. The spoken version is the rehearsal; the file is the record.
- Answer only what was asked. A vague question gets a vague answer ("a lot of
  users") — make them ask for numbers.
- Push like an interviewer: on a hand-waved component, on "what happens when
  this node is slow, not dead?". Save hints and corrections for the debrief.
- Check `date` as you go. At 45 minutes, call time; whatever's unaddressed
  stays unaddressed.

## After

- Append an `## Interviewer log` to the answer file: every question they asked
  with your answer, the values of the requirements they never asked about, and
  the constraint you held back. `/grade` scores rubric dimension 1 from it.
- Hand off to `/grade problem N` or `/grade mock N`.

For a mock with a human interviewer, none of this runs: the learner writes the
answer file and the interviewer's notes, then runs `/grade mock N`.
