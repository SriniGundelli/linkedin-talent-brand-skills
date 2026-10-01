---
name: li-company-page
description: >-
  Build a content system for a LinkedIn company page - pillars, formats, a
  monthly calendar, who posts what (page vs people), and a brief for each post.
  Use when the user says "company page content", "our page is dead", "content
  calendar for the company", "brand voice for LinkedIn", "what should the
  company post", or manages a page for a business.
---

# li-company-page

Company pages rarely beat people's own profiles for reach. Their job is to be
the credible hub: the place a prospect, candidate or journalist lands after
seeing a person's post. So the system is: people create reach, the page
creates proof.

> Also apply the **House rules** section of `~/.claude/linkedin/voice.md`
> (and the company's brand guide if the user provides one). Nothing is posted
> without the owner's yes.

## Intake

Ask once: who the page must convince (customers, candidates, partners,
investors), the one thing each should do next, the products or services, proof
that exists (customers, numbers, awards, case studies the company may name),
brand tone, banned claims (legal, regulated, NDA), and who can approve.

## Pillars (adapt to the business)

| pillar | purpose | share |
| --- | --- | --- |
| Customer proof | case studies, outcomes, quotes (with consent) | 30% |
| Expertise | how-tos, data, opinions from named experts | 30% |
| People and culture | the team, how work gets done, hiring | 20% |
| Company news | launches, milestones, events | 10% |
| Community | industry commentary, partner shout-outs | 10% |

## What the page posts versus what people post

- **Page**: announcements, case studies, event details, careers posts, anything
  needing the official voice.
- **People** (founders, experts, hiring managers): opinions, lessons, stories.
  The page reshares and adds a line. Use `/li-advocacy-kit` for team amplification.

## The month

Produce a table: date, pillar, format (text, image, carousel, video, poll,
event), author (page or named person), the idea in one line, the proof needed,
the call to action, and the owner. Three to four page posts a week is plenty;
quality of proof matters more than frequency.

## Brief for each post

```
Audience:       who and what they should do
Claim:          one sentence
Proof:          the number, name or quote that supports it (sourced)
Format + asset: what is needed (image, carousel, clip)
CTA:            one, and where the link goes (first comment)
Approver:       who signs off, by when
```

Draft finished posts through `/li-post` or `/li-carousel`, lint with
`python3 ../li-postlint/postlint.py`, and humanize with `/li-human`.

## Rules

- Every claim has a source the company can show. No invented customers,
  numbers, awards or testimonials.
- Customers are named only with written consent. Otherwise use `/li-case-study`
  anonymisation.
- Reply to comments on page posts within a working day, in a human voice.
- Do not buy followers or engagement; do not automate engagement.

## Output

Audience map, pillar mix, the 4-week calendar, the page-vs-people split, briefs
for the first five posts, and the approval workflow in one paragraph.
