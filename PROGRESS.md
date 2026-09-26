# Progress

Tracker for the DDIA learning plan, **2nd edition** (Kleppmann & Riccomini,
Feb 2026 — 14 chapters). Design: `plan/2026-09-13-ddia-learning-plan.md`

**Current cycle:** Chapter 1 — Trade-Offs in Data Systems Architecture
(started Sep 14, 2026; baseline end Sep 23)

The current phase is the first unchecked box in the current cycle's checklist
in the cycle log. Tick each box as its phase finishes — it's how Claude knows
when you're closed-book.

## Cycles

`◆` marks a spine chapter — one that builds on `builds/kvstore/`. Baseline
dates are the original plan's; Actual fills in as cycles start and close. The
schedule slides rather than cutting anything (plan §8).

| Ch | Title | Baseline | Actual | Build | Design problem | Status |
|----|-------|----------|--------|-------|----------------|--------|
| 1 | Trade-Offs in Data Systems Architecture | Sep 14 – 23, 2026 | Sep 14 – | Row store vs column store | — | ◐ in progress |
| 2 | Defining Nonfunctional Requirements | Sep 24 – Oct 3, 2026 | | Latency histogram harness | — | ☐ not started |
| 3 | Data Models and Query Languages | Oct 4 – 13, 2026 | | One domain, three models | URL shortener | ☐ not started |
| ◆ 4 | Storage and Retrieval | Oct 14 – 23, 2026 | | LSM-tree | — | ☐ not started |
| ◆ 5 | Encoding and Evolution | Oct 24 – Nov 2, 2026 | | Wire format + compat tests | News feed fan-out | ☐ not started |
| ◆ 6 | Replication | Nov 3 – 12, 2026 | | Single-leader replication | — | ☐ not started |
| ◆ 7 | Sharding | Nov 13 – 22, 2026 | | Consistent hashing + rebalance | Sharded rate limiter | ☐ not started |
| ◆ 8 | Transactions | Nov 23 – Dec 2, 2026 | | MVCC snapshot isolation | — | ☐ not started |
| ◆ 9 | The Trouble with Distributed Systems | Dec 3 – 12, 2026 | | Fault injector | Job scheduler | ☐ not started |
| ◆ 10 | Consistency and Consensus | Dec 13 – 22, 2026 | | Raft (anchor build) | — | ☐ not started |
| — | *Holiday pause* | Dec 23 – Jan 3 | | — | — | — |
| 11 | Batch Processing | Jan 4 – 13, 2027 | | MapReduce + joins | Metrics system | ☐ not started |
| 12 | Stream Processing | Jan 14 – 23, 2027 | | Toy Kafka + windowing | — | ☐ not started |
| ◆ 13 | A Philosophy of Streaming Systems | Jan 24 – Feb 2, 2027 | | CDC pipeline (tie-off) | Payment ledger | ☐ not started |
| 14 | Doing the Right Thing | Feb 3 – 12, 2027 | | — (no build) | Deletion & consent pipeline | ☐ not started |
| — | **Interview block** (cycles 15–18) | Feb 14 – Mar 13, 2027 | | Cumulative exam + 8 mocks | — | ☐ not started |

Status: ☐ not started · ◐ in progress · ✓ closed (set by `/close`)

## Phase checklist per cycle

`/cycle` copies this block under the chapter's heading in the cycle log. On
cycles without a design problem, the design-problem line is plain text
("- Design problem — n/a"), not a box.

```
- [ ] 1. Read (3.0h)           — first pass clean, second pass on marks only
- [ ] 2. Distill (1.5h)        — CLOSED BOOK, then 'what I got wrong'
- [ ] 3. Build (3.0h checkpoint) — NOTES.md on where I got stuck; spine: scope note first, MVP done
- [ ] 4. Explain (1.0h)        — no undefined jargon
- [ ] 5. Grill (0.75h)         — /grill N
- [ ] 6. Review (0.5h)         — /review
- [ ] Design problem (1.25h)   — /interview N, /grade problem N, post-mortem
- [ ] Closed                   — /close N (tags spine chapters 4–10, 13)
```

## Actual hours

Filled in by `/close`. After chapter 3, compare against the budget and re-set
it (plan §4).

| Ch | Read | Distill | Build | Explain | Grill | Review | Problem | Total | Days |
|----|------|---------|-------|---------|-------|--------|---------|-------|------|
| *Budget* | 3.0 | 1.5 | 3.0 | 1.0 | 0.75 | 0.5 | 1.25 | 9.75 (+1.25) | — |
| 1 | | | | | | | | | |
| 2 | | | | | | | | | |
| 3 | | | | | | | | | |
| 4 | | | | | | | | | |
| 5 | | | | | | | | | |
| 6 | | | | | | | | | |
| 7 | | | | | | | | | |
| 8 | | | | | | | | | |
| 9 | | | | | | | | | |
| 10 | | | | | | | | | |
| 11 | | | | | | | | | |
| 12 | | | | | | | | | |
| 13 | | | | | | | | | |
| 14 | | | | | | | | | |

## Explainer scores

Scored by `/grade`, each explainer on its own text — read the column trends
yourself. For chapters 1–3, Connections is scored against systems you've
built, since there are no earlier chapters yet.

| Ch | Mechanism | Tradeoffs | Jargon | Failures | Connections | Mean |
|----|-----------|-----------|--------|----------|-------------|------|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |
| 6 | | | | | | |
| 7 | | | | | | |
| 8 | | | | | | |
| 9 | | | | | | |
| 10 | | | | | | |
| 11 | | | | | | |
| 12 | | | | | | |
| 13 | | | | | | |
| 14 | | | | | | |

## Design problem scores

Dimensions: requirements / data model / failure modes / tradeoffs / estimation.
Answers in `problems/chNN-<slug>.md`.

| Problem | Reqs | Model | Failures | Tradeoffs | Estimation | Mean |
|---------|------|-------|----------|-----------|------------|------|
| URL shortener (ch 3) | | | | | | |
| News feed fan-out (ch 5) | | | | | | |
| Sharded rate limiter (ch 7) | | | | | | |
| Job scheduler (ch 9) | | | | | | |
| Metrics system (ch 11) | | | | | | |
| Payment ledger (ch 13) | | | | | | |
| Deletion & consent pipeline (ch 14) | | | | | | |

## Mock interviews

Interview block, cycles 15–18 (plan §7). At least two with a human
interviewer. Answers in `problems/mockNN-<slug>.md`.

| # | Problem | Interviewer | Reqs | Model | Failures | Tradeoffs | Estimation | Mean | Biggest gap |
|---|---------|-------------|------|-------|----------|-----------|------------|------|-------------|
| 1 | | | | | | | | | |
| 2 | | | | | | | | | |
| 3 | | | | | | | | | |
| 4 | | | | | | | | | |
| 5 | | | | | | | | | |
| 6 | | | | | | | | | |
| 7 | | | | | | | | | |
| 8 | | | | | | | | | |

## Cumulative exam

`/review exam` at the start of the interview block — the test of success
criterion 5.

| Date | Items | Hits | Weakest chapter |
|------|-------|------|-----------------|
| | | | |

## Cycle log

### Ch 1 — Trade-Offs in Data Systems Architecture (started Sep 14, 2026)

- [x] 1. Read (3.0h)           — first pass clean, second pass on marks only
- [x] 2. Distill (1.5h)        — CLOSED BOOK, then 'what I got wrong'
- [ ] 3. Build (3.0h checkpoint) — NOTES.md on where I got stuck
- [ ] 4. Explain (1.0h)        — no undefined jargon
- [ ] 5. Grill (0.75h)         — /grill 1
- [ ] 6. Review (0.5h)         — /review
- Design problem — n/a this cycle
- [ ] Closed                   — /close 1 (no tag, standalone build)

## Log

Running notes — slips, decisions, anything that changes the plan.

- **2026-09-13** — Plan designed and approved. Repo scaffolded.
- **2026-09-13** — Remapped to the 2nd edition: 14 chapters, spine shifts to
  ch 4–10 + 13, two new chapters (13 *A Philosophy of Streaming Systems*,
  14 *Doing the Right Thing*). End date moves Feb 21 → **Mar 13, 2027**.
- **2026-09-14** — Cycle 1 started. Stubs created for notes, explainer,
  diagram, and the row-vs-column build.
- **2026-09-26** — Cycle 1 is past its Sep 23 baseline end. Read and Distill
  are done (distill committed Sep 20); Build onward is still open. No cuts to
  catch up — the schedule slides.
- **2026-09-26** — Plan and tooling revised after a review. The schedule slides
  instead of phases being cut, and the build timebox is now a checkpoint, with
  MVP / Stretch / Ignored scope notes for spine builds. Open design questions
  for ch 6 and ch 13 added (plan §5). The queue gains core items, an answer
  key, intervals capped at 4, and a cumulative exam. Citations now come only
  from `plan/toc.md`, and `builds/` is protected by a deny rule. New `/close`
  and `/interview` commands; actual-hours, mock-interview and exam tracking
  added here.
