# Progress

Tracker for the DDIA learning plan, **2nd edition** (Kleppmann & Riccomini,
Feb 2026 — 14 chapters). Design: `plan/2026-09-13-ddia-learning-plan.md`

**Current cycle:** Chapter 1 — Trade-Offs in Data Systems Architecture, Sep 14 – 23, 2026

## Cycles

`◆` marks a spine chapter — one that builds on `builds/kvstore/`.

| Ch | Title | Dates | Build | Design problem | Status |
|----|-------|-------|-------|----------------|--------|
| 1 | Trade-Offs in Data Systems Architecture | Sep 14 – 23, 2026 | Row store vs column store | — | ◐ in progress |
| 2 | Defining Nonfunctional Requirements | Sep 24 – Oct 3, 2026 | Latency histogram harness | — | ☐ not started |
| 3 | Data Models and Query Languages | Oct 4 – 13, 2026 | One domain, three models | URL shortener | ☐ not started |
| ◆ 4 | Storage and Retrieval | Oct 14 – 23, 2026 | LSM-tree | — | ☐ not started |
| ◆ 5 | Encoding and Evolution | Oct 24 – Nov 2, 2026 | Wire format + compat tests | News feed fan-out | ☐ not started |
| ◆ 6 | Replication | Nov 3 – 12, 2026 | Single-leader replication | — | ☐ not started |
| ◆ 7 | Sharding | Nov 13 – 22, 2026 | Consistent hashing + rebalance | Sharded rate limiter | ☐ not started |
| ◆ 8 | Transactions | Nov 23 – Dec 2, 2026 | MVCC snapshot isolation | — | ☐ not started |
| ◆ 9 | The Trouble with Distributed Systems | Dec 3 – 12, 2026 | Fault injector | Job scheduler | ☐ not started |
| ◆ 10 | Consistency and Consensus | Dec 13 – 22, 2026 | Raft (anchor build) | — | ☐ not started |
| — | *Holiday pause / slack — the overrun reserve* | Dec 23 – Jan 3 | — | — | — |
| 11 | Batch Processing | Jan 4 – 13, 2027 | MapReduce + joins | Metrics system | ☐ not started |
| 12 | Stream Processing | Jan 14 – 23, 2027 | Toy Kafka + windowing | — | ☐ not started |
| ◆ 13 | A Philosophy of Streaming Systems | Jan 24 – Feb 2, 2027 | CDC pipeline (tie-off) | Payment ledger | ☐ not started |
| 14 | Doing the Right Thing | Feb 3 – 12, 2027 | — (no build) | Deletion & consent pipeline | ☐ not started |
| — | **Interview block** | Feb 14 – Mar 13, 2027 | 8 timed mocks | — | ☐ not started |

## Phase checklist per cycle

Copy this block under the chapter heading in the log as each cycle starts.

```
- [ ] 1. Read (3.0h)           — first pass clean, second pass on marks only
- [ ] 2. Distill (1.5h)        — CLOSED BOOK, then 'what I got wrong'
- [ ] 3. Build (3.0h / 2.25h)  — hard timebox, NOTES.md on where I got stuck
- [ ] 4. Explain (1.0h)        — no undefined jargon
- [ ] 5. Grill (0.75h)         — /grill N
- [ ] 6. Review (0.5h)         — /review
- [ ] Design problem (0.75h)   — ch 3, 5, 7, 9, 11, 13, 14 only
- [ ] git tag chNN-complete    — spine chapters only (4–10, 13)
```

## Explainer scores

Tracked to make grading drift visible across all fourteen chapters.

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

| Problem | Reqs | Model | Failures | Tradeoffs | Estimation | Mean |
|---------|------|-------|----------|-----------|------------|------|
| URL shortener (ch 3) | | | | | | |
| News feed fan-out (ch 5) | | | | | | |
| Sharded rate limiter (ch 7) | | | | | | |
| Job scheduler (ch 9) | | | | | | |
| Metrics system (ch 11) | | | | | | |
| Payment ledger (ch 13) | | | | | | |
| Deletion & consent pipeline (ch 14) | | | | | | |

## Cycle log

### Ch 1 — Trade-Offs in Data Systems Architecture (Sep 14 – 23, 2026)

- [ ] 1. Read (3.0h)           — first pass clean, second pass on marks only
- [ ] 2. Distill (1.5h)        — CLOSED BOOK, then 'what I got wrong'
- [ ] 3. Build (3.0h)          — hard timebox, NOTES.md on where I got stuck
- [ ] 4. Explain (1.0h)        — no undefined jargon
- [ ] 5. Grill (0.75h)         — /grill 1
- [ ] 6. Review (0.5h)         — /review
- [ ] Design problem           — n/a this cycle
- [ ] git tag                  — n/a, standalone build

## Log

Running notes — slips, decisions, anything that changes the plan.

- **2026-09-13** — Plan designed and approved. Repo scaffolded.
- **2026-09-13** — Remapped to the 2nd edition: 14 chapters, spine shifts to
  ch 4–10 + 13, two new chapters (13 *A Philosophy of Streaming Systems*,
  14 *Doing the Right Thing*). End date moves Feb 21 → **Mar 13, 2027**.
- **2026-09-14** — Cycle 1 started. Stubs created for notes, explainer,
  diagram, and the row-vs-column build.
