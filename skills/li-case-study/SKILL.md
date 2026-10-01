---
name: li-case-study
description: >-
  Turn a client or customer result into a LinkedIn case study post or carousel
  - problem, what was done, the measured result - with a consent and anonymity
  check before anything is drafted. Use when the user says "case study", "client
  win", "customer story", "success story post", "show our results", or has a
  testimonial or outcome to publish.
---

# li-case-study

A case study sells because it shows a specific person with a specific problem
getting a measurable result. It is also the post most likely to leak
something it should not. Consent comes first.

> Also apply the **House rules** section of `~/.claude/linkedin/voice.md`.
> Nothing is posted without the owner's yes.

## Gate 1: can this be told?

Ask and record, for each client:

- Has the client **agreed in writing** to be named, and to these exact claims,
  figures and any logo or quote?
- If not named: what would let someone guess who they are (industry + size +
  location + a distinctive number)? Remove it.
- Any NDA, regulated-industry or confidentiality clause? (financial, legal,
  healthcare, government.) If unsure, stop and ask the owner to check.
- Are the figures real, measured and sourced? Over what period?

If consent is missing, offer the **anonymised** version: "a 200-person fintech",
rounded ranges, no logo, no quote. If neither is allowed, do not draft.

## The facts to collect

```
Situation   who they were, what was at stake, what they had tried
Problem     the specific thing that was breaking, in their words if possible
Action      what was actually done: 3-5 steps, including something that went wrong
Result      the measured outcome, the period, and how it was measured
Quote       one line from the client, verbatim, only if approved
Lesson      what other readers can take from it
```

Never fill a gap. `{{your number}}` stays until the user supplies it.

## The post shape

```
Line 1     the result as a plain sentence, with the number
Line 2     who it was for, or how long it took
Body       the problem (2 lines), what changed (3 lines), the surprise or the
           hard part (2 lines)
Proof      the number again, with the period and the method
Close      one instruction: who should talk to us, or one question
```

As a carousel (use `/li-carousel`): cover = the result; slide 2 = the
problem; 3-5 = the steps; 6 = the numbers; 7 = the lesson; last = the action.

## Rules

- Say what the client did, not only what you did. Clients are the heroes.
- Include one thing that did not go to plan. It is the credibility.
- Do not claim causation you cannot show ("revenue up 40%" needs "while we also
  changed pricing").
- Send the draft to the client before it goes out. Get a yes in writing.
- Lint with `python3 ../li-postlint/postlint.py` and humanize with `/li-human`.

## Output

The consent and anonymity checklist with its status, the facts table with gaps
flagged, the post and the carousel copy, and the client approval message.
