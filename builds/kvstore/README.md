# kvstore — the spine

One toy distributed key-value store, grown chapter by chapter. This is the
spine of the DDIA plan: chapters 3–9 and 12 each bolt on the mechanism they
teach, and every addition stress-tests the last one.

**This code is a teaching artifact.** Unpolished is correct. The goal is to hit
the walls the book describes, not to ship.

## Evolution

| Chapter | What gets added | Tag |
|---------|-----------------|-----|
| 3 — Storage & Retrieval | Append-only log + hash index (Bitcask-style), then memtable → SSTable → compaction. A mini LSM-tree. | `ch03-complete` |
| 4 — Encoding & Evolution | Length-prefixed binary wire format with field tags. Schema evolution proven by replaying old bytes against new code. | `ch04-complete` |
| 5 — Replication | Single-leader replication over that wire format. Lag injected; read-your-writes and monotonic-read violations reproduced, then fixed. | `ch05-complete` |
| 6 — Partitioning | Consistent hashing with virtual nodes, routing layer, rebalance. Hot shard manufactured with skewed keys. | `ch06-complete` |
| 7 — Transactions | MVCC snapshot isolation. A test that *produces* write skew, then prevents it. | `ch07-complete` |
| 8 — Distributed Trouble | Fault injector: partitions, reordering, delays, clock skew. Pointed at this cluster. Expect chapters 5–7 to break. | `ch08-complete` |
| 9 — Consistency & Consensus | Raft leader election + log replication, replacing the chapter 5 replication. Run under the chapter 8 fault injector. | `ch09-complete` |
| 12 — Future of Data Systems | CDC: tail the chapter 3 WAL → publish to the chapter 11 event log → materialize a derived read view. | `ch12-complete` |

## The payoff diff

```sh
git diff ch05-complete..ch09-complete -- builds/kvstore/
```

That diff is what consensus bought over naive leader-follower replication,
written in your own code. It's a better artifact than any note in this repo.

## Rules

- Standard library first. Add a dependency only when the thing it provides
  isn't the thing the chapter is teaching you to build.
- Each chapter's work is timeboxed. When the box expires, write down where you
  got stuck in `NOTES.md` and move on — an unfinished build with an honest
  post-mortem beats a finished one that ate the next chapter.
- Claude does not write this code. Review, critique, and fault-finding only.
