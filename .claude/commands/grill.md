---
description: Closed-book quiz on a chapter, escalating through four tiers
argument-hint: <chapter number>
---

Grill Deandre on **chapter $1**. This is closed-book — say so at the start, and
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
Use their real code — read it before asking.

## Rules

- One question per message. Never stack them.
- When an answer is wrong, do not correct it immediately — ask a narrower
  question that exposes the error to them. Correct only after the second miss.
- When correcting, cite the chapter and section.
- Do not accept fluent-sounding answers that dodge the mechanism. "It uses
  consensus to stay consistent" is a dodge. Push: "which mechanism, and what
  does it cost you when a node is slow rather than dead?"

## After

Append every miss to `review/queue.md` as a retrieval item — the prompt they
failed, the chapter, and `due: next cycle`. Then give a short, honest read:
what's solid, what's shaky, and the single concept to re-read before moving on.
