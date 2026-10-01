---
name: li-job-post
description: >-
  Turn a role brief into a job post people actually apply to, plus the LinkedIn
  feed post that promotes it, and lint it for missing pay, bloated requirements,
  gendered or age-coded wording and jargon. Use when the user says "write a job
  post", "job description", "we're hiring", "promote this role", "why is nobody
  applying", or pastes a role brief or an existing job ad.
---

# li-job-post

A job post is a sales page for a decision the candidate makes in under a
minute. Most fail on the same five things: no pay, no location, a wall of
requirements, a company-centred voice, and jargon in place of facts.

> Also apply the **House rules** section of `~/.claude/linkedin/voice.md`
> (spelling, banned words, approval). Nothing is posted without the user's yes.

## Before writing, get the facts

Ask once, batched. Do not invent any of it.

1. **The outcome.** What does this person own and what is different in 12
   months because they did it well? Not a task list.
2. **The pay range**, location and work model, level, and employment type.
3. **Day-one requirements**: the 4-6 things they cannot do the job without.
   Everything else is "helpful".
4. **The honest hard part.** What is difficult about this role? Candidates
   trust a post that says it.
5. **Why someone good would leave where they are.** One real reason: the
   problem, the scope, the people, the stage.
6. **Process.** Steps, who they meet, how long it takes.

If pay is not decided, say so and stop. A post without a range is a worse post
and, in a growing number of jurisdictions, an unlawful one.

## The job post

```
Title        what a candidate would search for. No "Ninja", no internal levels.
Hook (2 ln)  the outcome and the reason it matters, written to "you".
The role     what you will own, in 3-4 sentences, then 4-5 bullets of real work.
You have     4-6 bullets, each a thing they can show. Mark the rest "helpful".
The hard part  one paragraph. What is difficult here.
Pay + terms  range, equity or bonus, location/work model, benefits that matter.
Process      steps and timeline. "Hear back in 5 working days" is a promise: keep it.
Inclusion    the equal-opportunity or accommodation line your jurisdiction needs.
```

Aim for 300-600 words. Write to "you", not "the successful candidate".

## The feed post

A short post that sends the right people to the role, not a pasted job ad:

```
Line 1   the problem this hire solves, or the number that makes it interesting
Body     3-5 short lines: what they will own, one hard thing, the range
Close    one instruction: who should apply, who should send it to someone
```

Put the link in the first comment, not the body. Offer a version the hiring
manager can post from their own profile; those outperform a company-page post.

## Lint it

Run the linter before showing the draft:

```bash
python3 jobpost_lint.py role.txt
```

It flags: missing pay or location, requirement walls, `10+ years`-style
inflation, masculine-coded and age-coded words, exclusionary terms, filler
jargon, "we" outnumbering "you", and a missing inclusion line. Fix every ERROR.
Decide on every WARN and say why if you keep it.

Optionally run the wording through the humanizer with the recruitment add-on:

```bash
python3 ../li-human/humanize.py role.txt --extra ../li-human/lexicons/recruitment.json --report
```

## Never

- Never invent pay, benefits, team size, funding or growth numbers.
- Never write "native speaker", an age band, or anything tied to a protected
  characteristic. Describe the skill needed, not the person.
- Never promise a process speed the company cannot hold.
- This is a drafting aid, not legal advice. Pay-transparency and
  anti-discrimination law differs by country and state; the user checks theirs.

## Output

The job post, the feed post (plus a hiring-manager variant), the lint result
with each finding resolved or consciously kept, and the first-comment text.
