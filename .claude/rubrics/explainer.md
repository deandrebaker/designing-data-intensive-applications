# Explainer rubric

For grading `explainers/chNN.md`. Five dimensions, 1–5 each. **Every score
needs a quoted sentence from the explainer as evidence.**

Audience assumption: a competent engineer who has *not* read DDIA.

---

## 1. Mechanism accuracy

Is the mechanism described actually how it works?

- **1** — Describes it wrongly, or describes only what it achieves, never how.
- **3** — Broadly right, with a hand-wave at the hard part ("then it syncs").
- **5** — Correct, and the hard part is the part explained in most detail.

## 2. Tradeoff articulation

Is the cost named, not just the benefit?

- **1** — Presented as a free win. No cost mentioned.
- **3** — A cost is named but not quantified or situated ("it's slower").
- **5** — Names what you give up, under which workload it hurts, and who
  should therefore *not* use it.

## 3. Jargon discipline

Is every term used also defined in the same document?

- **1** — Leans on terms like "quorum", "linearizable", "idempotent" as if
  they were self-explanatory.
- **3** — Most terms defined; one or two load-bearing ones assumed.
- **5** — Every term earns its place and is defined on first use. Nothing is
  pattern-matched.

*This dimension catches the most self-deception. Undefined jargon is usually
where understanding stops.*

## 4. Failure-mode awareness

What breaks, and under what conditions?

- **1** — Happy path only.
- **3** — Failures acknowledged generically ("if a node goes down").
- **5** — Specific failure modes with their triggering conditions, including
  the partial ones — slow nodes, not just dead ones; stale reads, not just
  lost writes.

## 5. Connection to prior chapters

Does it link to what came before?

- **1** — Freestanding; could have been written without the preceding chapters.
- **3** — Mentions a prior concept in passing.
- **5** — Explicitly builds on or *corrects* an earlier chapter's model,
  including their own earlier builds.

---

## Grading notes

- Lead with the lowest score, not the highest.
- For any score below 4, write the sentence a 5 would have contained.
- Score 3 is the honest default for competent-but-incomplete work. Resist
  drifting upward across cycles — check the last two chapters' scores in
  `PROGRESS.md` before finalizing.
