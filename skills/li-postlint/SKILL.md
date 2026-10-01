---
name: li-postlint
description: >-
  Lint a LinkedIn post before it goes out - hook truncation, wall of text,
  links in the body, hashtag walls, engagement bait, cliche openers, em dashes,
  invisible characters - and get a score. Use whenever the user says "check this
  post", "is this ready", "lint my draft", "will this get cut off", "review
  before I post", or right after any drafting skill produces a post.
---

# li-postlint

A fast, local, deterministic check on the mechanical things that cost reach and
the tells that make a post read as automated. It does not judge whether the
idea is good. That is for the author.

## Run it

```bash
python3 postlint.py draft.txt
echo "..." | python3 postlint.py -
python3 postlint.py draft.txt --json
```

Exit code is 1 only if there is an ERROR (over the 3,000-character limit or
invisible characters present), so it can run in a pre-publish script.

## What it checks

| rule | why |
| --- | --- |
| `hook-truncates` | Mobile shows ~140 characters before "see more". The point has to land before that |
| `cliche-opener` | "Thrilled to announce..." says nothing; lead with the result or the problem |
| `wall-of-text` | Paragraphs over ~320 characters with no break read as homework |
| `link-in-body` | Links in the body tend to lower reach. Put it in the first comment |
| `hashtag-wall` / `mid-hashtags` | Three or fewer, at the end |
| `engagement-bait` | "Comment YES", "like if you agree", "tag someone" |
| `em-dash`, `invisible-chars`, `not-x-but-y` | Common automated-writing tells |
| `emoji-heavy`, `tag-spray` | Reads as an ad or as spam |
| `multiple-asks`, `no-close` | One clear ask converts better than two |
| `too-long` / `long` / `short` | Length against the working range |

Severity: ERROR must be fixed, WARN needs a decision, INFO is a prompt.

## How to use the result

1. Fix every ERROR.
2. For each WARN, either fix it or say in one line why the post is better
   with it. Do not silence rules to raise the score.
3. If the post fails `em-dash`, `invisible-chars` or `not-x-but-y`, run
   `/li-human` and then lint again.
4. Show the user the final score and anything you consciously kept.

The score is a checklist, not a quality rating. A 100 means no mechanical
problems, not that anyone will read it.
