---
name: li-brand-sprint
description: >-
  Run a 90-day personal brand sprint on LinkedIn - baseline, weekly goals,
  posting and engagement targets, a month-by-month plan, and a review that
  decides what to keep. Use when the user says "90 day plan", "personal brand
  plan", "I want to grow on LinkedIn", "get known in my field", "start from
  zero", or wants a structured programme rather than one post.
---

# li-brand-sprint

Brand building fails from a missing plan and missing review, not from missing
talent. This sprint gives it 90 days, three goals and a weekly rhythm small
enough to keep.

> Also apply the **House rules** section of `~/.claude/linkedin/voice.md`.
> Nothing is posted or sent without the user's yes.

## Day 0: baseline

Collect, or ask the user to paste:

- Followers, connections, average views on the last 10 posts, comments per post.
- Profile score from `/li-profile` (out of 100).
- Posts per week now, and time available per week (be honest: 2, 4 or 6 hours).
- Their goal, in business terms: inbound leads, a job, speaking, hires, deals.
- The audience (from `/li-positioning`). If missing, run it first.

Do not set targets without a baseline. A number with no starting point is a wish.

## Three goals, no more

One **outcome** goal (e.g. five inbound conversations a month), one **reach**
goal (e.g. median impressions up 50%), one **habit** goal (e.g. three posts and
ten comments a week for 12 weeks). The habit goal is the one fully in the
user's control.

## The plan

| phase | weeks | focus |
| --- | --- | --- |
| Foundation | 1-2 | Fix profile (`/li-profile`), write `voice.md` (`/li-voice`), build the story bank (`/li-story-bank`), make a list of 25 people to engage with |
| Consistency | 3-6 | Three posts a week, ten comments a day on the 25, one DM conversation a week |
| Proof | 7-10 | Case posts, one carousel, one longer piece, ask for two recommendations |
| Compound | 11-13 | Double down on formats that worked, retire what did not, plan the next 90 days |

Fill in the weekly calendar with `/li-plan` for the first two weeks; the rest
is planned at each review.

## Weekly rhythm (the whole thing)

```
Mon  plan the week, draft two posts (30 min)
Daily  10 minutes: comment on 5 posts from the engagement list
Wed/Fri  publish, reply to every comment within the first hour
Fri  5-minute review: what got a reaction, what got silence
```

## Review at weeks 4, 8 and 12

Export analytics and run `python3 ../li-metrics/analyze.py posts.csv`. Decide
three things each time: what to repeat, what to stop, one thing to try. At week
12 compare to the Day 0 baseline and set the next 90 days.

## Rules

- Never promise a result or follower count; reach depends on things nobody
  controls. Promise the habit and measure the rest.
- Do not buy followers, pods or engagement. Do not use automation tools.
- If time drops, cut posts first, comments last: conversation compounds.

## Output

The baseline table, the three goals, the 13-week plan, the first two weeks'
calendar, and review dates written into the user's calendar format.
