# DDIA Learning Plan — Design

**Date:** 2026-09-13 (remapped 2026-09-13 for the 2nd edition; revised 2026-09-26 after review)
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
- No hard deadline. Given the choice, slow down and finish every phase rather
  than skip one to hold a date (§8).
- Wants Claude actively in the loop each cycle — quizzing and grading, not
  just producing material.

## 3. Success criteria

By the end of the plan:

1. A working toy distributed key-value store in Go, built incrementally, with
   a git tag per chapter so its evolution is readable as a diff.
2. Fourteen closed-book chapter distillations, each with an explicit
   "what I got wrong" section.
3. Fourteen Feynman explainers graded against a rubric, ending on three
   chapters in a row with no dimension scored 2 or below.
4. Seven design problems plus eight timed mock interviews, at least two of the
   mocks with a human interviewer, each with a written post-mortem.
5. A spaced-repetition queue that has been worked continuously, and a
   cumulative closed-book exam at the start of the interview block (§7) showing
   chapter 4 material still retrievable cold months later.

The real test: given an unfamiliar system design problem, able to name the
failure modes *before* naming the components.

## 4. The chapter cycle

Each chapter budgets **9.75 hours**: about 11–12 days at 6h/week, or 8–9 days
at 8h/week. Every phase is a retrieval test of the phase before it, not a
restatement of it.

The budgets are first guesses. `/close` records actual hours per phase in
`PROGRESS.md`, and after chapter 3 the budgets are re-set from three chapters
of real numbers.

| # | Phase | Budget | Output |
|---|-------|--------|--------|
| 1 | **Read** | 3.0h | First pass straight through, margin marks only where confusing or surprising. Second pass over marks only. No note-taking during first pass — transcription feels productive and teaches little. |
| 2 | **Distill (closed-book)** | 1.5h | Book shut. Write `notes/chNN-*.md` from memory, draw the central mechanism from memory into `diagrams/chNN.md`. *Then* open the book and correct yourself in a separate "What I got wrong" section. |
| 3 | **Build (timeboxed)** | 3.0h | The chapter's Go exercise. Unpolished by design — the goal is to hit the wall the chapter describes. When the 3h box expires, stop and write in `NOTES.md` where you got stuck and what's left, then keep going until the build's MVP is done (§5). The timebox is a checkpoint, not a cutoff. |
| 4 | **Explain** | 1.0h | `explainers/chNN.md`, aimed at a competent engineer who has not read DDIA. Constraint: no jargon you cannot define in the same document. |
| 5 | **Grill (with Claude)** | 0.75h | Closed-book quiz + cross-examination of the explainer. Misses, plus 3–5 core items for the chapter, go into the retrieval queue. |
| 6 | **Spaced review** | 0.5h | Work the due items in `review/queue.md` cold. |

The seven cycles listed in §6 also carry a design problem: 45 minutes timed,
plus about 30 minutes for grading and the post-mortem. Those cycles run about
1.25h longer; the build keeps its full scope.

A cycle ends with `/close N`, which checks every phase is done, records hours,
and hands off to the next chapter.

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
| 13 — A Philosophy of Streaming Systems | spine (tie-off) | CDC pipeline: tail a log from the spine (which one is an open question below) → publish to the chapter 12 event log → materialize a derived read-optimized view. The whole spine in one dataflow. |
| 14 — Doing the Right Thing | standalone | **No build.** The freed time goes to a written critique of a real system's data practices plus this cycle's design problem. |

**Git tags:** `ch04-complete` … `ch13-complete`, set by `/close`. Tags cover
the whole repo, so scope the diff to the spine:
`git diff ch06-complete..ch10-complete -- builds/kvstore` is itself a
deliverable. It shows, in your own code, what consensus bought over naive
leader-follower replication.

### Scope notes

Before writing code for a spine chapter, open that chapter's section of
`builds/kvstore/NOTES.md` with three lines:

- **MVP:** the chapter's build as specified in the table above, listing first
  what the next spine chapter depends on. Build that part first. The cycle
  doesn't close until the MVP is done.
- **Stretch:** anything beyond the spec that tempts you. Optional — log what
  you left, rather than carrying it as debt.
- **Ignored:** interactions deliberately left out, e.g. "single node only".

Three chapters need their scope settled before they start:

- **Ch 4** packs a hash-indexed log, an LSM-tree and a SQLite benchmark into
  one build. Expect it to run well past 3h.
- **Ch 8:** does MVCC run on a single node or across the chapter 7 shards?
  Decide in the scope note.
- **Ch 10:** Raft is the biggest build in the plan — similar in scope to MIT
  6.5840's Raft labs, which take students many times 3h. Write its MVP and
  Ignored lines before the chapter starts, and expect the cycle to run long.

### Open questions — yours to answer

Two design questions this plan deliberately leaves open. They're yours to work
out: Claude won't answer them before you've committed to your own
(`CLAUDE.md` rule 1), and `/cycle` restates each one, without hints, when it's
raised and again before it's due. Write your answer into the named chapter's
scope note.

| Raised at | Answer before | Question |
|-----------|---------------|----------|
| `/cycle 6` | the ch 6 build | In chapter 9 you'll need to partition, delay and reorder messages between the nodes you connect in chapter 6. How will you do that? |
| `/cycle 10` | the ch 13 build | After chapter 10, which log should the chapter 13 CDC pipeline tail, and why? |

Think about the first one during chapter 6, not chapter 9. Claude won't raise
it in a chapter 6 review — `CLAUDE.md`'s conventions steer reviews away from
suggesting abstraction layers — so this table is the only reminder.

## 6. Design problems

Seven, sited so the chapter just finished is what unlocks each one.

Each runs through `/interview N`: Claude plays the interviewer and holds the
requirements back until you ask for them, since the rubric's first dimension
scores whether you did. Talk it through out loud as you type. The answer goes
in `problems/chNN-<slug>.md`, followed by `/grade problem N` and a written
post-mortem.

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

Four weeks, starting once chapter 14 closes (baseline Feb 14 – Mar 13, 2027).
For the review queue they count as cycles 15–18.

- **Cumulative exam first.** Week 1 opens with `/review exam`: a closed-book
  exam drawn from every chapter's items, graduated ones included. It is the
  real test of success criterion 5.
- **Eight mocks.** Two timed 45-minute mock designs per week, drawn from the
  standard question bank, run through `/interview mock N` and done out loud.
  At least two with a human interviewer: real interviews are a spoken
  conversation with someone who pushes back, which a solo written answer can't
  rehearse.
- **Graded and post-mortemed.** Each is graded against the design-problem
  rubric and followed by a written post-mortem naming the single biggest gap in
  the answer. Files: `problems/mockNN-<slug>.md`.

## 8. Schedule

These are **baseline** dates from the original plan, not deadlines. Each cycle
starts when the previous one closes, and `PROGRESS.md` records actual dates
beside the baseline so drift stays visible.

| Cycle | Baseline dates |
|-------|----------------|
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
| *Holiday pause* | Dec 23, 2026 – Jan 3, 2027 |
| Ch 11 — Batch Processing | Jan 4 – 13, 2027 |
| Ch 12 — Stream Processing | Jan 14 – 23, 2027 |
| Ch 13 — A Philosophy of Streaming Systems | Jan 24 – Feb 2, 2027 |
| Ch 14 — Doing the Right Thing | Feb 3 – 12, 2027 |
| Interview block | Feb 14 – Mar 13, 2027 |

**Overrun policy: slow down, never skip.** There is no hard deadline. When a
cycle runs long, the schedule slides — every later date moves, the interview
block included. No phase is cut to catch up: not the build's MVP, and above
all not the closed-book distillation (phase 2), which has the highest
learning-per-hour and the strongest temptation to skip. Slips are logged in
`PROGRESS.md`, so the re-budget after chapter 3 has real data.

The holiday pause stays on the calendar as a break. Whichever chapter is in
progress pauses with it, and nothing in the review queue comes due, since
cycles count chapters, not weeks (§10).

## 9. Repository structure

```
├── CLAUDE.md              # tutor rules: withhold explanation until attempt
├── PROGRESS.md            # cycle tracker, phase checkboxes, dates, hours
├── plan/
│   ├── (this design doc)
│   └── toc.md             # 2nd-edition headings, copied from the book
├── notes/chNN-slug.md     # closed-book distillation + "what I got wrong"
├── explainers/chNN.md     # Feynman write-ups
├── diagrams/chNN.md       # from-memory mermaid, then reference version
├── builds/                # all yours: Claude reviews, never writes
│   ├── ch01-row-vs-column/
│   ├── ch02-latency-harness/
│   ├── ch03-three-models/
│   ├── kvstore/           # THE SPINE — one Go module, ch4–10 + 13
│   ├── ch11-mapreduce/
│   └── ch12-eventlog/
├── harness/               # Claude-written scaffolding around builds, if any
├── problems/              # chNN-<slug>.md design problems, mockNN-<slug>.md mocks
├── review/queue.md        # spaced-repetition retrieval queue
└── .claude/
    ├── settings.json      # denies Claude's file edits under builds/
    ├── commands/          # /cycle /grill /grade /review /interview /close
    └── rubrics/           # explainer + design-problem rubrics
```

## 10. Tooling

### Slash commands

| Command | Behaviour |
|---------|-----------|
| `/cycle N` | Scaffold chapter N: create note/explainer/diagram stubs, update `PROGRESS.md`, state the build goal and timebox, restate any open question from §5. Stops if chapter N−1 isn't closed. |
| `/grill N` | Closed-book quiz in four escalating tiers: **recall** the mechanism → **apply** it to a scenario → **argue** the tradeoff → **adversarial** (e.g. "your chapter 6 replication drops writes under this partition; why, and what did the book tell you that you ignored?"). Every miss, plus 3–5 core items, goes into `review/queue.md`. |
| `/grade explainer N` / `problem N` / `mock N` | Score against the relevant rubric, with specific textual evidence for every score. |
| `/review` | Pull due items from the retrieval queue and quiz them cold; update intervals. `/review exam` runs the cumulative exam (§7). |
| `/interview N` / `/interview mock N` | Claude plays interviewer for a design problem or mock, revealing requirements only when asked. |
| `/close N` | Verify every phase is done, record actual hours, move "What I got wrong" into the queue, log any slip, tag spine chapters, publish the reference one-pager, hand off. |

### Rubrics

**Explainer rubric** — five dimensions, scored 1–5, evidence required per score:

1. **Mechanism accuracy** — is the described mechanism actually how it works?
2. **Tradeoff articulation** — is the cost named, not just the benefit?
3. **Jargon discipline** — is every term used also defined in the document?
4. **Failure-mode awareness** — what breaks, and under what conditions?
5. **Connection to prior chapters** — does it link to what came before? For
   chapters 1–3, connections to systems you've built count.

**Design-problem rubric** — five dimensions, scored 1–5:

1. **Requirements clarification** — were constraints and scale established first?
2. **Data model & access patterns** — driven by reads/writes, not by habit?
3. **Failure modes** — named before components, not after?
4. **Tradeoff reasoning** — alternatives considered and rejected with reasons?
5. **Estimation** — are the numbers sane and stated explicitly?

### Spaced repetition

`review/queue.md` holds retrieval items. Its header is the single source of
truth for the item format and interval rules. In short:

- **Sources:** `/grill` misses; 3–5 core items per chapter added by `/grill`
  whether hit or missed, so a clean chapter still gets reviewed; and each
  chapter's "What I got wrong" section, moved in by `/close`.
- **Answer key:** each item carries a `ref` (chapter + heading from
  `plan/toc.md`) and a one-line `key` in your own words, so `/review` scores
  against your corrected understanding rather than Claude's memory of the book.
- **Intervals:** a cycle is a chapter number; the interview weeks are cycles
  15–18. Leitner-style: a miss returns next cycle; a hit moves 1 → 2 → 4
  cycles out, and a hit at 4 graduates the item. Graduated items stay in the
  file for the cumulative exam.

### Citations

DDIA doesn't number its sections, and Claude's knowledge of the book is mostly
the 1st edition, whose chapter numbers and content differ. `plan/toc.md` holds
the 2nd edition's headings, copied from the book. Claude cites only a chapter
plus a heading from it, says so when it isn't sure where something is covered,
and yields to the book when they disagree.

### Visuals

Two distinct uses, not to be conflated:

- **From-memory diagrams (phase 2)** are the *learning tool*. Drawn in mermaid,
  closed-book, then corrected. Their value is in the act of drawing.
- **Reference one-pagers** are the *review tool*. `/close` publishes a visual
  one-pager per chapter as a shareable artifact — mechanism drawn properly,
  failure modes, tradeoff table — built only from your corrected notes and
  reference diagram, never from Claude's memory of the book, so review never
  drills Claude's errors. Consulted during `/review`, never before the
  from-memory attempt.

## 11. Claude's role (`CLAUDE.md`)

The load-bearing configuration. Without it, Claude defaults to explaining
things immediately, which substantially reduces learning. `CLAUDE.md` is the
authoritative text; in short, it instructs Claude to:

1. **Withhold** explanations until after an attempt, with a `hint` / `unstuck`
   ladder for when you're stuck mid-build.
2. **Grade honestly**, with quoted evidence, and hold scores under pushback.
3. **Never write build code** anywhere in `builds/`, backed by a permissions
   deny rule.
4. **Cite the book** as chapter + heading from `plan/toc.md`, and defer to the
   book over its own memory.
5. **Respect the closed-book phases.**
6. **Let the schedule slide** rather than cut a phase.

## 12. Risks

| Risk | Mitigation |
|------|------------|
| Build debt compounds — a skipped chapter-6 build blocks chapter 7 | Nothing is skipped: a spine cycle doesn't close until its MVP is done, and the scope note (§5) builds what the next chapter needs first. The schedule slides instead. |
| Open-ended slippage — with no deadline, the plan drifts indefinitely | Actual hours and slips are logged every cycle, and the budgets are re-set after chapter 3, so the projected end date stays honest |
| Closed-book distillation gets quietly skipped because it is uncomfortable | It is phase 2, before the fun part (the build); `/grill` is explicitly closed-book, so skipping it shows up immediately as a bad session; `/close` won't close a cycle without it |
| Chapter 10 (Raft) overruns badly | Scope settled in its scope note before the chapter starts; the schedule slides rather than the build shrinking |
| Grading drifts encouraging over time | Rubrics demand textual evidence per score; a score changes mid-session only when Claude misread text written before the grade; scores are tracked across all fourteen chapters in `PROGRESS.md` for you to read as a trend |
| Claude corrects toward the 1st edition, or invents a citation | Citations only from `plan/toc.md`; corrections made without the book open are tagged `verify`; the book outranks Claude |
| Motivation decay around chapters 9–10, the hardest stretch | These are also the highest-payoff chapters; the compounding spine means quitting there leaves a visibly unfinished system |

## 13. Non-goals

- Production-quality code. Every build is a teaching artifact and should look like one.
- Supplementary papers on the first pass. Paper follow-ups (Raft, Dynamo,
  Bigtable, Spanner) are optional extensions after chapter 14.
- Covering system design topics DDIA does not cover (CDNs, API gateway design,
  mobile sync). Those are gaps to close after the book, not during it.
- Public writing. Explainers are for the learner and for grading, not publication.
