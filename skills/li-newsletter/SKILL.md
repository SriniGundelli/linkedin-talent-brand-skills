---
name: li-newsletter
description: >-
  Plan and write a LinkedIn newsletter or long-form article - the series
  promise, issue outline, search-friendly title, the opening that earns the
  second paragraph, and the feed post that sends people to it. Use when the user
  says "LinkedIn newsletter", "write an article", "long-form post", "start a
  series", "turn this into an article", or has material too big for one post.
---

# li-newsletter

A feed post gets a day. A newsletter or article keeps compounding: it is indexed,
it builds a subscriber list the algorithm cannot take away, and it gives the
feed posts something to point to.

> Also apply the **House rules** section of `~/.claude/linkedin/voice.md`.
> Nothing is published without the user's yes.

## Decide if it should be a newsletter

Use a newsletter when there is a repeatable promise ("every other Thursday: one
hiring decision, taken apart"). Use a one-off article when the idea is
substantial and will not repeat. If it is under ~500 words, it is a post;
send it to `/li-post`.

## The series promise (newsletter)

Write it in one sentence and test it:

```
Every {cadence}, {who it is for} gets {one specific thing} in {read time}.
```

Then: a title that says what it is, a one-line description under 140 characters,
the first six issue titles, and a cadence the user can keep for six months.
Under-promise the cadence.

## Issue outline

```
Title          the problem or promise, with the words someone would search
Opening        two sentences: the claim, and why the reader should care now
The point      one idea, stated plainly in the first 150 words
Body           3-5 sections, each with a heading that reads as a claim
Evidence       real numbers, a real story, one example per section
What to do     3 concrete steps the reader can take this week
Close          one question or one next step; link to the next issue
```

Target 800-1,500 words. Write headings as claims ("Interviews measure
rehearsal"), not topics ("Interviews").

## The opening

The first 40 words decide whether anyone reads on and they also become the
preview. Lead with the surprising fact, the cost, or the scene. Cut any
sentence that starts with "In today's".

## The feed post that sends people to it

A separate short post (use `/li-post`): the sharpest claim from the piece, one
specific proof, and an instruction. Put the link in the first comment. Plan a
second post a few days later with a different angle on the same issue.

## Rules

- Evidence comes from the user. Missing evidence becomes `{{your example}}`.
- Do not republish another person's work. Quote briefly with attribution.
- Run the draft through `/li-human`.

## Output

The series promise and first six titles (or the single article outline), the
full draft, the feed post and the follow-up post, and the publish checklist:
title, cover image alt text, subscriber note, first comment.
