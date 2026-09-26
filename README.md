# Designing Data-Intensive Applications

A structured read of *Designing Data-Intensive Applications*, 2nd edition
(Kleppmann & Riccomini, Feb 2026 — 14 chapters), with notes, builds, and
practice problems. Depth first; interview practice is how the depth gets
tested, not the goal.

**Started Sep 14, 2026; baseline end Mar 13, 2027.** No hard deadline — the
schedule slides rather than anything getting cut. Full design:
[`plan/2026-09-13-ddia-learning-plan.md`](plan/2026-09-13-ddia-learning-plan.md).
Live status: [`PROGRESS.md`](PROGRESS.md).

## The cycle

Each chapter budgets 9.75 hours. Every phase is a retrieval test of the one
before it:

1. **Read** (3.0h) — clean first pass, margin marks only
2. **Distill** (1.5h) — *closed book*, then correct yourself
3. **Build** (3.0h checkpoint) — deliberately unpolished; MVP before moving on
4. **Explain** (1.0h) — Feynman write-up, no undefined jargon
5. **Grill** (0.75h) — closed-book quiz with Claude
6. **Review** (0.5h) — spaced repetition

## The spine

Chapters 4–10 and 13 compound into one Go toy distributed key-value store in
[`builds/kvstore/`](builds/kvstore/) — storage engine, wire format,
replication, sharding, transactions, fault injection, Raft, CDC. Each chapter
stress-tests the last. Chapters 1, 2, 3, 11 and 12 get standalone builds;
chapter 14 has no build and trades it for an essay and a design problem.

## Commands

| | |
|---|---|
| `/cycle N` | Scaffold chapter N — files, build goal, timebox |
| `/grill N` | Closed-book quiz, four escalating tiers |
| `/grade explainer N` · `problem N` · `mock N` | Score against the rubric |
| `/review` · `/review exam` | Work the spaced-repetition queue · cumulative exam |
| `/interview N` · `/interview mock N` | Design problem or mock, Claude as interviewer |
| `/close N` | Verify phases, record hours, feed the queue, hand off |

## Layout

```
plan/         the design doc + toc.md (the book's headings)
notes/        closed-book distillations + "what I got wrong"
explainers/   Feynman write-ups
diagrams/     from-memory mermaid, then reference
builds/       code — kvstore/ is the spine; Claude never writes here
harness/      Claude-written scaffolding around builds, if any
problems/     design problems + mocks, with graded feedback
review/       spaced-repetition queue
```
