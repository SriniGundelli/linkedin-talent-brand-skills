---
name: li-metrics
description: >-
  Analyse a LinkedIn analytics export and say what to repeat and what to stop -
  engagement rate, reach and engagement multiples against the user's own
  median, best formats and weekdays. Use when the user says "analyse my
  LinkedIn stats", "what's working", "read my analytics", "which posts did
  best", "compare my posts", or pastes or attaches a CSV of post performance.
---

# li-metrics

`/li-audit` works from pasted posts and judgement. This works from a file and
arithmetic: it ranks every post against the user's own median so a post that
got 900 impressions can be a hit for a small account and a miss for a big one.

## Get the data

LinkedIn's own content analytics can be exported (the format changes, so
column names are matched loosely). Third-party scheduling tools also export
CSVs. A hand-made sheet works. Needed columns: impressions, plus any of:
date, text or title, reactions, comments, reposts, clicks, saves, sends,
format. Fewer than 8 posts is noise; the script refuses.

## Run it

```bash
python3 analyze.py posts.csv
python3 analyze.py posts.csv --json
```

## What it computes

- **Weighted engagement rate**: reactions + 3x comments + 4x reposts +
  saves/sends + clicks, over impressions. It weights what travels.
- **Reach multiple and ER multiple** for each post against the user's median.
- **Top five and bottom three**, by combined score.
- **By format** and **by weekday**, only for groups with two or more posts.

## How to read it back

1. Say the baseline first: "Your median post gets 1,650 impressions at 2.5%."
2. Name the top posts and what they share: topic, format, hook formula
   (`/li-post`'s `hooks.json`), length, day. Be careful: with 12 posts, this
   suggests, it does not prove.
3. Name what flopped, without judgement: usually the post was about the
   author, not the reader.
4. Give exactly three actions: one to repeat, one to stop, one to test.
5. Flag the caveats: small sample, one viral outlier skewing a format, a post
   boosted by a reshare, posting-time effects confounded with topic.

## Never

- Never compare the user's numbers with other people's or with industry
  "averages". Only their own median.
- Never call a single post a pattern. Look for three.
- Do not recommend buying engagement, pods or automation.
- Do not invent a column that is missing; say what is missing.

## Output

The baseline, the ranked posts with multiples, format and weekday tables, the
three actions, and the caveats. Feed the actions into `/li-plan`.
