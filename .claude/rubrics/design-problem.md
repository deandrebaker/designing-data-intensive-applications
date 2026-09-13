# Design problem rubric

For grading `problems/*.md` and the timed mock interviews. Five dimensions,
1–5 each. **Every score needs quoted evidence.**

---

## 1. Requirements clarification

Were constraints and scale established *before* designing?

- **1** — Jumped straight to components. No numbers, no constraints.
- **3** — Asked about scale, then designed without using the answer.
- **5** — Established read/write ratio, scale, latency budget, and consistency
  needs — and the design visibly follows from them.

## 2. Data model & access patterns

Driven by the actual reads and writes, or by habit?

- **1** — Reached for a familiar database and shaped the problem to fit it.
- **3** — Reasonable model, but the access patterns were assumed not stated.
- **5** — Access patterns enumerated first; the storage choice is justified by
  them, and an alternative is explicitly rejected with a reason.

## 3. Failure modes

Named *before* components, or bolted on after?

- **1** — Not discussed, or only "we'll add retries".
- **3** — Failures addressed after the design was complete.
- **5** — Failure modes shaped the design as it was drawn. Partial failures
  covered: slow nodes, network partitions, duplicate delivery, clock skew.

## 4. Tradeoff reasoning

Alternatives considered and rejected with reasons?

- **1** — One design presented as the answer.
- **3** — Alternatives mentioned, dismissed without argument.
- **5** — At least one real fork in the road, both branches argued, the choice
  justified against *this problem's* constraints.

## 5. Estimation

Are the numbers sane and stated explicitly?

- **1** — No numbers at all.
- **3** — Numbers present but unexamined; no sense of what they imply.
- **5** — Back-of-envelope QPS, storage growth, and bandwidth, carried through
  to a conclusion ("that's 40 TB/year, so we shard by time, not by user").

---

## Grading notes

- Failure modes (dimension 3) is the one that most separates real system design
  ability from rehearsed interview patter. Weight it heaviest in the summary.
- For the timed mocks, note the clock: what was still unaddressed at 45 minutes
  matters as much as what was covered.
- Finish with one sentence: the single biggest gap in this answer.
