# DDIA Learning Plan — Design

**Date:** 2026-09-13 (remapped 2026-09-13 for the 2nd edition)
**Author:** deandrebaker (with Claude)
**Status:** Approved design, scaffolded
**Edition:** 2nd (Kleppmann & Riccomini, Feb 2026) — 14 chapters

## 1. Purpose

Build genuine system design skill by reading *Designing Data-Intensive
Applications*, 2nd edition (Kleppmann & Riccomini, February 2026), with a
structured practice loop around it.
Depth of understanding is the primary goal; interview performance is treated as
a *test* of that understanding rather than the target itself.

## 2. Learner context

- ~4 years of engineering experience (2 internship, 2 full-time), full-stack.
- Learns best by: reading, seeing visuals, explaining what was learned, and
  practicing problems. The plan's six-phase cycle maps directly onto these four.
- Available: 6–8 hours/week, sustained.
- Wants Claude actively in the loop each cycle — quizzing and grading, not
  just producing material.

## 3. Success criteria

By the end of the plan:

1. A working toy distributed key-value store in Go, built incrementally, with
   a git tag per chapter so its evolution is readable as a diff.
2. Fourteen closed-book chapter distillations, each with an explicit
   "what I got wrong" section.
3. Fourteen Feynman explainers graded against a rubric, with scores trending up.
4. Seven design problems plus eight timed mock interviews, each with written
   post-mortems.
5. A spaced-repetition queue that has been worked continuously, such that
   chapter 4 material is still retrievable cold in March.

The real test: given an unfamiliar system design problem, able to name the
failure modes *before* naming the components.

## 4. The chapter cycle

Each chapter is a ~10-day cycle totalling **9.75 hours** — which fits a 6–8
hour week across 10 days with room to spare. Every phase is a retrieval test of
the phase before it, not a restatement of it.

| # | Phase | Time | Output |
|---|-------|------|--------|
| 1 | **Read** | 3.0h | First pass straight through, margin marks only where confusing or surprising. Second pass over marks only. No note-taking during first pass — transcription feels productive and teaches little. |
| 2 | **Distill (closed-book)** | 1.5h | Book shut. Write `notes/chNN-*.md` from memory, draw the central mechanism from memory into `diagrams/chNN.md`. *Then* open the book and correct yourself in a separate "What I got wrong" section. |
| 3 | **Build (hard timebox)** | 3.0h | The chapter's Go exercise. Unpolished by design — the goal is to hit the wall the chapter describes. When the box expires, write `NOTES.md` on where you got stuck and move on. |
| 4 | **Explain** | 1.0h | `explainers/chNN.md`, aimed at a competent engineer who has not read DDIA. Constraint: no jargon you cannot define in the same document. |
| 5 | **Grill (with Claude)** | 0.75h | Closed-book quiz + cross-examination of the explainer. Misses are logged to the retrieval queue. |
| 6 | **Spaced review** | 0.5h | Work the due items in `review/queue.md` cold. |

On every other cycle a ~45-minute interview-style design problem is added, and
the build timebox drops from 3.0h to 2.25h to pay for it. The cycle total stays
at 9.75 hours either way.

**Known friction:** phase 2 will feel bad for the first several chapters.
Closed-book recall always does. That discomfort is the mechanism working.

## 5. The build spine

Chapters 4–10 and 13 compound into **one** system — a toy distributed key-value
store in **Go**, in `builds/kvstore/` as a single module. Chapters 1, 2, 3, 11
and 12 get standalone exercises; chapter 14 has no build. Go was chosen because
its concurrency primitives make replication and consensus work materially
clearer, and it is close to what real infrastructure is written in.

The 2nd edition preserves the *relative* order of the spine chapters from the
1st, so the compounding design carries over intact — only the numbering shifts
(+1 from chapter 4 onward), and two chapters are genuinely new.

| Chapter | Type | Build |
|---------|------|-------|
| 1 — Trade-Offs in Data Systems Architecture | standalone | Same dataset, two architectures: run one analytical query workload against a row store (SQLite) and a column store (DuckDB). Measure the gap. Instruments the chapter's operational-vs-analytical divide directly. |
| 2 — Defining Nonfunctional Requirements | standalone | Load generator + latency histogram. Demonstrate that mean latency lies, and that p99 amplifies across a fan-out. |
| 3 — Data Models and Query Languages | standalone | Model one domain three ways (relational, document, graph); run the same three queries against each. Feel join pain and schema-on-read pain directly. |
| 4 — Storage and Retrieval | **spine** | Append-only log + hash index (Bitcask-style), then memtable → SSTable flush → compaction: a mini LSM-tree. Benchmark against SQLite's B-tree. |
| 5 — Encoding and Evolution | spine | The store's wire format: length-prefixed binary with field tags. Evolve the schema; prove backward/forward compatibility by replaying old bytes against new code. |
| 6 — Replication | spine | Single-leader replication over that wire format. Inject lag; *reproduce* read-your-writes and monotonic-read violations; then fix them. |
| 7 — Sharding | spine | Consistent hashing with virtual nodes, a routing layer, a rebalance operation. Manufacture a hot shard with skewed keys. |
| 8 — Transactions | spine | MVCC snapshot isolation over the storage engine. Write a test that *produces* write skew, then prevent it. |
| 9 — The Trouble with Distributed Systems | spine | A fault injector: network partitions, message reordering, delays, clock skew. Point it at your own cluster. This is the cycle where chapters 6–8 are revealed to be wrong. |
| 10 — Consistency and Consensus | spine (anchor) | Raft leader election + log replication, replacing the hand-rolled chapter 6 replication. Run it under the chapter 9 fault injector. |
| 11 — Batch Processing | standalone | MapReduce from scratch (map, shuffle/sort, reduce). Implement both a reduce-side join and a broadcast hash join; measure the gap. |
| 12 — Stream Processing | standalone | A toy Kafka: partitioned append-only log with consumer offsets. Then windowed aggregation, event-time vs processing-time, late arrivals. |
| 13 — A Philosophy of Streaming Systems | spine (tie-off) | CDC pipeline: tail the chapter 4 write-ahead log → publish to the chapter 12 event log → materialize a derived read-optimized view. The whole spine in one dataflow. |
| 14 — Doing the Right Thing | standalone | **No build.** The freed time goes to a written critique of a real system's data practices plus this cycle's design problem. |

**Git tags:** `ch04-complete` … `ch13-complete` on `builds/kvstore/`. The diff
`ch06-complete..ch10-complete` is itself a deliverable: it shows, in your own
code, what consensus bought over naive leader-follower replication.

## 6. Design problems

Seven, sited so the chapter just finished is what unlocks each one. They are no
longer on a fixed odd/even rhythm — placement follows the material.

| After | Problem | Focus it forces |
|-------|---------|-----------------|
| Ch 3 | URL shortener | Data model, access patterns, read/write ratio |
| Ch 5 | News feed / activity stream | Fan-out on write vs read; schema evolution across a rollout |
| Ch 7 | Sharded rate limiter + counter at scale | Partitioning, hot keys, approximate vs exact |
| Ch 9 | Distributed job scheduler | Failure detection, at-least-once vs exactly-once |
| Ch 11 | Metrics / observability system | Time-series storage, rollups, batch pipelines |
| Ch 13 | Payment ledger | Event sourcing, derived views, auditability, idempotence |
| Ch 14 | User data deletion & consent pipeline | Deletion across derived data and backups, consent propagation, retention |

The chapter 14 problem is the one with no 1st-edition equivalent. It is also the
hardest to fake: deletion is trivial to promise and genuinely difficult to
implement once data has been replicated, cached, and derived into three other
places — which is exactly what the preceding thirteen chapters built.

## 7. Interview block

Four weeks, Feb 14 – Mar 13, 2027. Two timed 45-minute mock designs per week,
eight total, drawn from the standard question bank. Each is graded against the
design-problem rubric and followed by a written post-mortem naming the single
biggest gap in the answer.

## 8. Schedule

| Cycle | Dates |
|-------|-------|
| Ch 1 — Trade-Offs in Data Systems Architecture | Sep 14 – 23, 2026 |
| Ch 2 — Defining Nonfunctional Requirements | Sep 24 – Oct 3, 2026 |
| Ch 3 — Data Models and Query Languages | Oct 4 – 13, 2026 |
| Ch 4 — Storage and Retrieval | Oct 14 – 23, 2026 |
| Ch 5 — Encoding and Evolution | Oct 24 – Nov 2, 2026 |
| Ch 6 — Replication | Nov 3 – 12, 2026 |
| Ch 7 — Sharding | Nov 13 – 22, 2026 |
| Ch 8 — Transactions | Nov 23 – Dec 2, 2026 |
| Ch 9 — The Trouble with Distributed Systems | Dec 3 – 12, 2026 |
| Ch 10 — Consistency and Consensus | Dec 13 – 22, 2026 |
| *Holiday pause / slack* | Dec 23, 2026 – Jan 3, 2027 |
| Ch 11 — Batch Processing | Jan 4 – 13, 2027 |
| Ch 12 — Stream Processing | Jan 14 – 23, 2027 |
| Ch 13 — A Philosophy of Streaming Systems | Jan 24 – Feb 2, 2027 |
| Ch 14 — Doing the Right Thing | Feb 3 – 12, 2027 |
| Interview block | Feb 14 – Mar 13, 2027 |

The Raft anchor build (ch 10) now lands immediately before the holiday pause,
which is a better arrangement than the 1st-edition mapping produced: the cycle
most likely to overrun is backed directly onto the reserve.

**Overrun policy:** chapter 10's Raft build is the most likely to overrun. If it
does, take the time from the holiday pause rather than cutting the build.
Consensus pays back the most in real architecture work. If any other cycle
slips, cut the build's polish, never the closed-book distillation — phase 2 is
the phase with the highest learning-per-hour and the strongest temptation to skip.

## 9. Repository structure

```
├── CLAUDE.md              # tutor rules: withhold explanation until attempt
├── PROGRESS.md            # cycle tracker, phase checkboxes, dates
├── plan/                  # this design doc
├── notes/chNN-slug.md     # closed-book distillation + "what I got wrong"
├── explainers/chNN.md     # Feynman write-ups
├── diagrams/chNN.md       # from-memory mermaid, then reference version
├── builds/
│   ├── ch01-row-vs-column/
│   ├── ch02-latency-harness/
│   ├── ch03-three-models/
│   ├── kvstore/           # THE SPINE — one Go module, ch4–10 + 13
│   ├── ch11-mapreduce/
│   └── ch12-eventlog/
├── problems/              # design problem answers + graded feedback
├── review/queue.md        # spaced-repetition retrieval queue
└── .claude/
    ├── commands/          # /cycle /grill /grade /review
    └── rubrics/           # explainer + design-problem rubrics
```

## 10. Tooling

### Slash commands

| Command | Behaviour |
|---------|-----------|
| `/cycle N` | Scaffold chapter N: create note/explainer/diagram/build stubs, update `PROGRESS.md`, state the build goal and timebox. |
| `/grill N` | Closed-book quiz in four escalating tiers: **recall** the mechanism → **apply** it to a scenario → **argue** the tradeoff → **adversarial** (e.g. "your chapter 6 replication drops writes under this partition; why, and what did the book tell you that you ignored?"). Every miss is appended to `review/queue.md`. |
| `/grade explainer N` / `/grade problem N` | Score against the relevant rubric, with specific textual evidence for every score. |
| `/review` | Pull due items from the retrieval queue and quiz them cold; update intervals. |

### Rubrics

**Explainer rubric** — five dimensions, scored 1–5, evidence required per score:

1. **Mechanism accuracy** — is the described mechanism actually how it works?
2. **Tradeoff articulation** — is the cost named, not just the benefit?
3. **Jargon discipline** — is every term used also defined in the document?
4. **Failure-mode awareness** — what breaks, and under what conditions?
5. **Connection to prior chapters** — does it link to what came before?

**Design-problem rubric** — five dimensions, scored 1–5:

1. **Requirements clarification** — were constraints and scale established first?
2. **Data model & access patterns** — driven by reads/writes, not by habit?
3. **Failure modes** — named before components, not after?
4. **Tradeoff reasoning** — alternatives considered and rejected with reasons?
5. **Estimation** — are the numbers sane and stated explicitly?

### Spaced repetition

`review/queue.md` holds retrieval items, each with a chapter, a prompt, and a
next-due cycle. Leitner-style intervals: a miss returns next cycle; a hit is
pushed out 2 cycles, then 4, then 8. Items are added by `/grill` from misses
and from the "What I got wrong" sections.

### Visuals

Two distinct uses, not to be conflated:

- **From-memory diagrams (phase 2)** are the *learning tool*. Drawn in mermaid,
  closed-book, then corrected. Their value is in the act of drawing.
- **Reference one-pagers** are the *review tool*. Claude publishes a visual
  one-pager per chapter as a shareable artifact — mechanism drawn properly,
  failure modes, tradeoff table — consulted during `/review`, never before the
  from-memory attempt.

## 11. Claude's role (`CLAUDE.md`)

The load-bearing configuration. Without it, Claude defaults to explaining
things immediately, which substantially reduces learning. It must instruct:

- **Withhold.** When asked "how does X work?", ask the learner first, require
  an attempt, and only then fill the gap.
- **Grade honestly**, not encouragingly. A 3 that is called a 3 is worth more
  than a 4 that was really a 3.
- **Never write spine code unprompted.** Review it, break it, question it —
  but the learner writes it.
- **Cite the book.** When correcting, point to the section, so the correction
  is verifiable rather than taken on faith.

## 12. Risks

| Risk | Mitigation |
|------|------------|
| Build debt compounds — a skipped chapter-6 build blocks chapter 7 | Standalone chapters (1, 2, 3, 11, 12) and build-free chapter 14 act as catch-up slack; holiday pause is the larger reserve |
| Closed-book distillation gets quietly skipped because it is uncomfortable | It is phase 2, before the fun part (the build); `/grill` is explicitly closed-book, so skipping it shows up immediately as a bad session |
| Chapter 10 (Raft) overruns badly | Budgeted as the anchor build, and scheduled to end immediately before the holiday pause, which is the designated overflow |
| Grading drifts encouraging over time | Rubrics demand textual evidence per score; scores are tracked across all fourteen chapters in `PROGRESS.md` so drift is visible as a trend |
| Motivation decay around chapters 9–10, the hardest stretch | These are also the highest-payoff chapters; the compounding spine means quitting there leaves a visibly unfinished system |

## 13. Non-goals

- Production-quality code. Every build is a teaching artifact and should look like one.
- Supplementary papers on the first pass. Paper follow-ups (Raft, Dynamo,
  Bigtable, Spanner) are optional extensions after chapter 14.
- Covering system design topics DDIA does not cover (CDNs, API gateway design,
  mobile sync). Those are gaps to close after the book, not during it.
- Public writing. Explainers are for the learner and for grading, not publication.
