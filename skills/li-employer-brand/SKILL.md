---
name: li-employer-brand
description: >-
  Build an employer brand content system for LinkedIn - the employee value
  proposition in plain words, five content pillars, a four-week calendar of
  posts that show what working there is really like, and the proof to back each
  claim. Use when the user says "employer brand", "EVP", "why work here",
  "culture content", "attract talent", "recruitment marketing", or "our careers
  page says nothing".
---

# li-employer-brand

Candidates do not believe "great culture". They believe specifics: a decision
the team made, a number, a person, a mistake. Employer brand on LinkedIn is
collecting those specifics and publishing them on a schedule.

> Also apply the **House rules** section of `~/.claude/linkedin/voice.md`.
> Nothing is posted without the user's yes.

## Step 1: find the real EVP

Ask for, in one batched question:

1. Why do people who have been there 2+ years stay? (Ask for three actual
   people's reasons, not a slogan.)
2. Why did the last three people leave, and what did the company learn?
3. What would a strong candidate give up to join, and what do they get back?
4. Which competitor do candidates compare you with, and where do you lose?

From the answers write the EVP in three sentences:

```
For {who}, we offer {the specific trade}. You will {get X}, you will {give up Y}.
That is not for everyone: {who it is not for}.
```

The last line is the one that makes it believable. An EVP with no "not for
everyone" is a brochure.

## Step 2: five pillars

Map the EVP onto content pillars. Defaults, change to fit:

| pillar | what it proves | example post |
| --- | --- | --- |
| The work | the problems are real and interesting | a hard decision and how it was made |
| The people | who you will sit next to | an employee's own story, in their words |
| How we run | process, pay, remote rules, meeting load | the actual compensation philosophy |
| Growth | what people became here | a promotion path, with the person's consent |
| The honest bit | what is hard or imperfect | a mistake and the fix |

Rule of thumb: a feed that is all celebration reads as recruiting spin. Keep
one "honest bit" post in every five.

## Step 3: four-week calendar

Produce a table: week, day, pillar, format (text, carousel, short video, poll),
who posts it (company page, hiring manager, employee), the one-line idea, and
the proof needed. Three posts a week is enough; consistency beats volume.

Rotate the author. Posts from named employees and hiring managers typically
travel further than the company page, and candidates trust them more. The page
posts the hub content; people post the stories.

## Step 4: draft the first week

Draft the first week's posts through `/li-post` (or `/li-carousel` for a list
post). Every post needs a specific, true detail the writer supplied. If it is
missing, the draft carries `{{your detail}}` and a flag.

## Never

- Never publish an employee's story, photo, pay, review or health details
  without their explicit, informed yes. Get consent in writing for each use.
- Never claim awards, ratings, diversity figures or growth numbers without a
  source the user can point to.
- Never write "family", "rockstar", "work hard play hard" or "passionate". Say
  what actually happens.

## Output

The three-sentence EVP, the pillar map, the four-week calendar, week-one drafts
with their proof requirements, and a consent checklist for every employee
featured.
