# Progress

Tracker for the DDIA learning plan. Design: `plan/2026-09-13-ddia-learning-plan.md`

**Current cycle:** not started — chapter 1 begins Sep 14, 2026

## Cycles

| Ch | Title | Dates | Build | Design problem | Status |
|----|-------|-------|-------|----------------|--------|
| 1 | Reliable, Scalable, Maintainable | Sep 14 – 23, 2026 | Latency histogram harness | — | ☐ not started |
| 2 | Data Models & Query Languages | Sep 24 – Oct 3, 2026 | One domain, three models | URL shortener | ☐ not started |
| 3 | Storage & Retrieval | Oct 4 – 13, 2026 | LSM-tree (spine) | — | ☐ not started |
| 4 | Encoding & Evolution | Oct 14 – 23, 2026 | Wire format + compat tests (spine) | News feed | ☐ not started |
| 5 | Replication | Oct 24 – Nov 2, 2026 | Single-leader replication (spine) | — | ☐ not started |
| 6 | Partitioning | Nov 3 – 12, 2026 | Consistent hashing + rebalance (spine) | Sharded rate limiter | ☐ not started |
| 7 | Transactions | Nov 13 – 22, 2026 | MVCC snapshot isolation (spine) | — | ☐ not started |
| 8 | The Trouble with Distributed Systems | Nov 23 – Dec 2, 2026 | Fault injector (spine) | Job scheduler | ☐ not started |
| 9 | Consistency & Consensus | Dec 3 – 12, 2026 | Raft (spine, anchor) | — | ☐ not started |
| 10 | Batch Processing | Dec 13 – 22, 2026 | MapReduce + joins | Metrics system | ☐ not started |
| 11 | Stream Processing | Jan 4 – 13, 2027 | Toy Kafka + windowing | — | ☐ not started |
| 12 | The Future of Data Systems | Jan 14 – 23, 2027 | CDC pipeline (spine tie-off) | Payment ledger | ☐ not started |
| — | *Holiday pause / slack* | Dec 23, 2026 – Jan 3, 2027 | — | — | — |
| — | **Interview block** | Jan 25 – Feb 21, 2027 | 8 timed mocks | — | ☐ not started |

## Phase checklist per cycle

Copy this block under the chapter heading below as each cycle starts.

```
- [ ] 1. Read (3.0h)           — first pass clean, second pass on marks only
- [ ] 2. Distill (1.5h)        — CLOSED BOOK, then 'what I got wrong'
- [ ] 3. Build (3.0h / 2.25h)  — hard timebox, NOTES.md on where I got stuck
- [ ] 4. Explain (1.0h)        — no undefined jargon
- [ ] 5. Grill (0.75h)         — /grill N
- [ ] 6. Review (0.5h)         — /review
- [ ] Design problem (0.75h)   — only on even chapters
- [ ] git tag chNN-complete    — spine chapters only (3–9, 12)
```

## Rubric scores

Tracked to make grading drift visible. Explainer dimensions: mechanism /
tradeoffs / jargon / failures / connections.

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

## Design problem scores

Dimensions: requirements / data model / failure modes / tradeoffs / estimation.

| Problem | Reqs | Model | Failures | Tradeoffs | Estimation | Mean |
|---------|------|-------|----------|-----------|------------|------|
| URL shortener (ch 2) | | | | | | |
| News feed (ch 4) | | | | | | |
| Sharded rate limiter (ch 6) | | | | | | |
| Job scheduler (ch 8) | | | | | | |
| Metrics system (ch 10) | | | | | | |
| Payment ledger (ch 12) | | | | | | |

## Log

Running notes — slips, decisions, anything that changes the plan.

- **2026-09-13** — Plan designed and approved. Repo scaffolded.
