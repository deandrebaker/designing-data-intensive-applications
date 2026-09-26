---
description: Closed-book quiz on a chapter, escalating through four tiers
argument-hint: <chapter number>
---

Grill the learner on **chapter $1**. This is closed-book — say so at the start, and
hold the line if they try to look something up mid-session.

Read their `notes/chNN-*.md` (especially the "What I got wrong" section) and
`explainers/chNN.md` first, so your questions target their actual gaps rather
than generic chapter content. Also pull anything for chapter $1 sitting in
`review/queue.md`.

Work through four tiers, **one question at a time**. Wait for each answer before
moving on. Do not move up a tier until they've cleared the one below.

**Tier 1 — Recall.** Can they state the mechanism? "What actually happens on
disk when a write hits an LSM-tree?"

**Tier 2 — Apply.** Does it survive contact with a scenario? "You've got a
write-heavy workload with keys clustered in a narrow range. What happens to
compaction, and what do you feel first?"

**Tier 3 — Argue the tradeoff.** Can they name the cost, not just the benefit?
"Why would anyone still choose a B-tree here? Make the strongest case against
the thing you just described."

**Tier 4 — Adversarial.** Attack their own build. "Your chapter 6 replication
drops acknowledged writes under this specific partition. Walk me through why,
and tell me what the book already warned you about that you didn't implement."
Use their real code — read it before asking. Chapter 14 has no build: aim
tier 4 at the kvstore as a whole and at their chapter 14 critique.

## Rules

- One question per message. Never stack them.
- When an answer is wrong, do not correct it immediately — ask a narrower
  question that exposes the error to them. Correct only after the second miss.
- When correcting, cite per `CLAUDE.md` rule 4.
- Do not accept fluent-sounding answers that dodge the mechanism. "It uses
  consensus to stay consistent" is a dodge. Push: "which mechanism, and what
  does it cost you when a node is slow rather than dead?"

## After

1. Give a short, honest read: what's solid, what's shaky, and the single
   concept to re-read before moving on. The grill is over; the book can open.
2. Add items to `review/queue.md`, in the format defined there, due cycle
   $1 + 1 at interval 1:
   - every miss
   - 3–5 core items covering the chapter's central mechanisms, including ones
     they answered well
   The learner writes each `key`: ask for one line in their own words and record
   it verbatim. Tag `verify` on any item whose key rests on a correction you
   made — it came from you, not the book.
3. Tick Grill in chapter $1's checklist in `PROGRESS.md`.
