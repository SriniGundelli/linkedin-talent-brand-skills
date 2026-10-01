---
name: li-launch
description: >-
  Plan and write a launch on LinkedIn - product, feature, funding, partnership
  or milestone - as a coordinated set: the founder post, the company-page post,
  employee share copy, the first comment and a seven-day follow-up. Use when the
  user says "launch post", "announce our product", "funding announcement",
  "partnership post", "we just shipped", or "launch week content".
---

# li-launch

One post from the company page is not a launch. A launch is a sequence in which
the person closest to the story speaks first, the page backs them, the team
amplifies, and the days after answer the questions people ask.

> Also apply the **House rules** section of `~/.claude/linkedin/voice.md`.
> Nothing is posted without the owner's yes. Check embargoes, legal and
> investor communication rules before any funding or financial news.

## Intake

Ask once: what is launching and for whom; the one problem it solves; one real
proof point (customer, number, demo); the date and embargo; who the founder
voice is; what the call to action is; legal or investor constraints.

For funding: confirm the announcement is cleared with investors and counsel and
that figures are exactly the ones approved. Do not infer numbers.

## The set

**1. Founder post (T-0, morning).** Story first, news second.

```
Line 1   the problem or the number, not "excited to announce"
Body     why we built it (one honest paragraph), what it does (3 lines),
         who it is for, one proof point
Close    the ask: try it, tell us who needs it, reply with the hard question
```

**2. Company-page post (T-0, 1-2 hours later).** The factual version: what it
is, who it is for, link in the first comment, asset attached.

**3. Team share copy (T-0).** Five angles through `/li-advocacy-kit` so no two
posts match.

**4. First comment.** Link, a sentence of context, and a question to start a
thread.

**5. Day 2-7 sequence.** Day 2: the customer story or demo. Day 3: the hard
decision behind it. Day 5: answer the top three questions people asked. Day 7:
what we learned in the first week, with real numbers.

## Rules

- Lead with the user's problem, never the feature list.
- One proof point you can show beats five adjectives. No "revolutionary",
  "game-changing", "world-class".
- Do not claim customer logos, benchmarks, certifications or investor names
  without permission and a source.
- Reply to every comment the first day, in a human voice.
- Lint each draft with `python3 ../li-postlint/postlint.py` and humanize with
  `/li-human`.

## Output

The five-part set with send times, an asset checklist, the day 2-7 follow-ups,
and the list of things that must be confirmed before 'go' (legal, embargo,
customer consent, figures).
