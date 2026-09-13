# Designing Data-Intensive Applications

A structured read of Kleppmann's *Designing Data-Intensive Applications*, with
notes, builds, and practice problems. Depth first; interview practice is how
the depth gets tested, not the goal.

**Runs Sep 14, 2026 → Feb 21, 2027.** Full design:
[`plan/2026-09-13-ddia-learning-plan.md`](plan/2026-09-13-ddia-learning-plan.md).
Live status: [`PROGRESS.md`](PROGRESS.md).

## The cycle

Each chapter is a ~10-day, 9.75-hour cycle. Every phase is a retrieval test of
the one before it:

1. **Read** (3.0h) — clean first pass, margin marks only
2. **Distill** (1.5h) — *closed book*, then correct yourself
3. **Build** (3.0h) — hard timebox, deliberately unpolished
4. **Explain** (1.0h) — Feynman write-up, no undefined jargon
5. **Grill** (0.75h) — closed-book quiz with Claude
6. **Review** (0.5h) — spaced repetition

## The spine

Chapters 3–9 and 12 compound into one Go toy distributed key-value store in
[`builds/kvstore/`](builds/kvstore/) — storage engine, wire format,
replication, partitioning, transactions, fault injection, Raft, CDC. Each
chapter stress-tests the last. Chapters 1, 2, 10 and 11 get standalone builds.

## Commands

| | |
|---|---|
| `/cycle N` | Scaffold chapter N — files, build goal, timebox |
| `/grill N` | Closed-book quiz, four escalating tiers |
| `/grade explainer N` · `/grade problem N` | Score against the rubric |
| `/review` | Work the spaced-repetition queue |

## Layout

```
plan/         the design doc
notes/        closed-book distillations + "what I got wrong"
explainers/   Feynman write-ups
diagrams/     from-memory mermaid, then reference
builds/       code — kvstore/ is the spine
problems/     design problems + graded feedback
review/       spaced-repetition queue
```
