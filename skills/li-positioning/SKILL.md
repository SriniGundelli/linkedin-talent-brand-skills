---
name: li-positioning
description: >-
  Work out who the user is for on LinkedIn - the audience, the one-sentence
  positioning, three to five positions they hold that others do not, and the
  content pillars - then write it into voice.md. Use when the user says "personal
  brand", "positioning", "what should I be known for", "who is my audience",
  "find my niche", "I post but nothing sticks", or has no voice.md yet.
---

# li-positioning

Posting more does not fix a blurry position. This skill makes the position
sharp first, then everything else (`/li-post`, `/li-plan`, `/li-profile`) has
something to aim at.

> Also apply the **House rules** section of `~/.claude/linkedin/voice.md` if
> it exists. This skill creates or updates that file.

## Interview (one batched round, then follow up once)

1. Who do you want to notice you, in one specific job title and company type?
   ("Heads of talent at 50-300 person tech companies", not "HR professionals".)
2. What do you want them to do after they notice: hire you, buy, refer, work
   with you, invite you to speak?
3. What do you know, from doing it, that your audience gets wrong or does not
   know? Give me three.
4. What have you done that you can prove: numbers, names you may use, results?
5. What is an opinion you hold that colleagues in your field would push back on?
6. What will you never post about (employer rules, NDAs, family, politics)?

If answers are vague, ask for an example. "I help companies hire better" needs
"for example, last quarter I did X and Y happened".

## The positioning sentence

```
I help {specific audience} {achieve a specific result} by {the distinctive
way you do it}. Proof: {one real number or result}.
```

Test it: could a competitor say the same sentence? If yes, it is not a
position. Offer three versions, say which is strongest and why.

## Positions (the raw material of good posts)

List three to five beliefs, each as a claim a smart peer could disagree with,
with the evidence the user has:

```
Claim:      Most structured interviews measure rehearsal, not ability.
Evidence:   Ran 60 interviews with and without take-home work; ...
Pushback:   "Take-homes exclude people with caring duties."
Your answer: ...
```

A position with no evidence goes on a "to research" list, not into a post.

## Pillars

Three to four recurring themes, each tied to the audience's problem, with a
named post format for each (story, how-to, opinion, case). Share of the feed:
roughly 40% teach, 30% opinion or story, 20% proof, 10% personal.

## Write it down

Create or update `~/.claude/linkedin/voice.md` using `templates/voice.md`: who
you are, who you write for, your positions, off-limits topics, proof you can
use. Show the user the file and ask them to correct it before saving.

## Never

- Never invent credentials, numbers or clients. Missing proof stays
  `{{your number}}`.
- Never make the position wider to feel safer. "Everyone" is no one.
- Never copy someone else's positioning sentence.

## Output

The positioning sentence (three options, one recommended), three to five
positions with evidence status, the pillars, the posting mix, and the updated
`voice.md` for approval.
