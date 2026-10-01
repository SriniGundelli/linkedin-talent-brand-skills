---
name: li-story-bank
description: >-
  Mine the user's real career for postable stories - interview them with
  specific prompts, store each story with its facts, and turn any story into a
  post, carousel or comment. Use when the user says "I have nothing to post
  about", "find stories", "story bank", "turn this experience into a post",
  "what can I write about", or has run out of ideas.
---

# li-story-bank

People think they have nothing to post about because they are looking for
topics. The raw material is moments: a decision, a mistake, a number that
surprised them. This skill digs them out and files them so they are never
invented.

> Also apply the **House rules** section of `~/.claude/linkedin/voice.md`.
> Nothing is posted without the user's yes.

## The file

Stories live in `~/.claude/linkedin/stories.md`, one block each:

```
## {short title}
When / where:   {date range, role, setting. Anonymise if required}
What happened:  {3-6 plain sentences, in order}
The number:     {a real figure, or "none"}
The turn:       {the moment it changed or what they learned}
Cost / risk:    {what it cost, who could be identified}
Safe to share:  {yes / anonymise / no} - {who has agreed, if relevant}
Used in:        {post link or date, so it is not recycled blindly}
```

If the file exists, read it first and do not re-ask what is already there.

## Dig with prompts, three at a time

Ask three prompts, wait, follow up on the best answer, repeat.

1. The decision you were most wrong about, and what it cost.
2. A time you changed your mind because of one specific person or number.
3. The thing you do that colleagues think is odd, and why you do it.
4. The first month in a role, and what you wish someone had told you.
5. A client, candidate or customer who surprised you.
6. The moment you almost quit, and what stopped you.
7. Something you built that failed, and the one part that worked.
8. What you say no to now that you used to say yes to.

Follow-ups that pull the detail out: "What was the actual number?", "Who said
what?", "What did you do next?", "What would have happened if you had not?".
The detail makes the story; the adjectives do not.

## Turn a story into a post

Pick the post type by the shape of the story:

| story shape | post |
| --- | --- |
| mistake and fix | confession then lesson (hook: the cost) |
| surprise number | "I expected X. The data said Y." |
| change of mind | "I used to believe X. Here is what changed it." |
| odd habit | the habit, the reason, who it helps |
| process | a numbered carousel via `/li-carousel` |

Draft through `/li-post`. The story's facts come only from the file; anything
missing becomes `{{your detail}}`.

## Rules

- **Consent and safety.** If a story involves someone else, an employer, a
  client or health information, mark "anonymise" or "no" and respect it.
  Change identifying details and keep the lesson.
- **No invention.** Never fill gaps with plausible details. A true small story
  beats a polished fake one.
- **Rotate.** Do not reuse a story within 90 days without a new angle.

## Output

New or updated story blocks for the user's approval, and one draft post from
the strongest unused story.
