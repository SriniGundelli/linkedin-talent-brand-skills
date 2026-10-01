---
name: li-voice
description: >-
  Build or refresh the user's voice.md from their own writing, using measured
  evidence (sentence rhythm, contractions, emoji, openers, words they lean on)
  instead of guesses. Use when the user says "write my voice file", "learn my
  voice", "make it sound like me", "my posts sound generic", "build voice.md", or
  after they paste three or more of their own posts.
---

# li-voice

Every other skill reads `~/.claude/linkedin/voice.md`. If it is a guess, every
draft is a guess. This one measures first.

## Get the samples

Ask for **8-10 of the user's own best posts or messages**, written by them, not
by an assistant. Three is the minimum and gives a sketch. Separate posts with a
line of `---` in one file. Also ask which two they think sound most like them.

## Measure

```bash
python3 voiceprint.py my-posts.txt
```

The script reports: sentence length and spread, share of short and long
sentences, contractions and first-person use per 100 words, emoji, hashtags,
em dashes, how posts open and close, words they lean on, and phrases they
repeat. It prints a draft "What I sound like" block for `voice.md`.

Read the numbers back to the user in plain words: "Your sentences average 9
words and you start four out of ten posts with 'I'. Is that how you want to
sound?" The numbers describe what they do, not what they should do.

## Fill the rest of voice.md

Use `templates/voice.md`. From the samples and a short conversation fill:
who they are and write for; words they use and never use; humour and swearing
rules; positions; off-limits topics; proof they can use. Ask only what the
samples cannot answer.

## Test it

Write one 120-word post on a topic from their samples in the voice you derived.
Ask: "Would you post this unedited? What would you change?" Each change is a
rule; add it to voice.md. Repeat once.

## Maintain it

Re-run on fresh posts every quarter. Add a "Changes" line with the date. If
the user's role or audience changed, run `/li-positioning` first.

## Never

- Never include text the user did not write. Ghost-written or AI-generated
  samples teach the wrong voice.
- Never save voice.md without the user seeing it.
- Never copy a stranger's voice. Say so if the user asks to sound like a
  public figure; borrow structure, not identity.

## Output

The measurements in plain words, the completed `voice.md` for approval, and
one test post with the user's corrections folded back in.
