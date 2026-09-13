# kvstore — the spine

One toy distributed key-value store, grown chapter by chapter. This is the
spine of the DDIA plan (2nd edition): chapters 4–10 and 13 each bolt on the
mechanism they teach, and every addition stress-tests the last one.

**This code is a teaching artifact.** Unpolished is correct. The goal is to hit
the walls the book describes, not to ship.

## Evolution

| Chapter | What gets added | Tag |
|---------|-----------------|-----|
| 4 — Storage and Retrieval | Append-only log + hash index (Bitcask-style), then memtable → SSTable → compaction. A mini LSM-tree. | `ch04-complete` |
| 5 — Encoding and Evolution | Length-prefixed binary wire format with field tags. Schema evolution proven by replaying old bytes against new code. | `ch05-complete` |
| 6 — Replication | Single-leader replication over that wire format. Lag injected; read-your-writes and monotonic-read violations reproduced, then fixed. | `ch06-complete` |
| 7 — Sharding | Consistent hashing with virtual nodes, routing layer, rebalance. Hot shard manufactured with skewed keys. | `ch07-complete` |
| 8 — Transactions | MVCC snapshot isolation. A test that *produces* write skew, then prevents it. | `ch08-complete` |
| 9 — The Trouble with Distributed Systems | Fault injector: partitions, reordering, delays, clock skew. Pointed at this cluster. Expect chapters 6–8 to break. | `ch09-complete` |
| 10 — Consistency and Consensus | Raft leader election + log replication, replacing the chapter 6 replication. Run under the chapter 9 fault injector. | `ch10-complete` |
| 13 — A Philosophy of Streaming Systems | CDC: tail the chapter 4 WAL → publish to the chapter 12 event log → materialize a derived read view. | `ch13-complete` |

## The payoff diff

```sh
git diff ch06-complete..ch10-complete -- builds/kvstore/
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
