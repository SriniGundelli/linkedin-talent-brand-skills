---
name: li-candidate-outreach
description: >-
  Write recruiter outreach to passive candidates on LinkedIn - the 200-character
  connection note, the first message built on a specific reason, two follow-ups,
  and replies to the usual objections - then lint it. Use when the user says
  "reach out to this candidate", "recruiter message", "InMail", "passive
  candidate", "sourcing outreach", "they didn't reply", or pastes a candidate
  profile and a role.
---

# li-candidate-outreach

For recruiters, headhunters and hiring managers. `/li-dm` is the general
version; this one knows the candidate has a job, a reason not to reply, and an
inbox full of the same message.

> Also apply the **House rules** section of `~/.claude/linkedin/voice.md`.
> The user sends every message by hand.

## What you need first

1. **The profile evidence.** Paste the candidate's public profile or the
   relevant posts. Do not guess at their history. If nothing specific to them
   is available, say so: a message with no reason to be about them is spam.
2. **The role, honestly.** Title, scope, level, pay range, location, why it is
   open, what is hard about it. If pay is unknown, say so before drafting.
3. **The hook.** One true reason this person, not "your background is
   impressive": a project, a post, a number, a team they built, a move they
   made.
4. **Why they might care.** What the role offers that their current seat
   probably does not. If you cannot name one, do not message.

## The sequence

**Connection note (200 chars; 300 on Premium).** A reference to them and one
line on who you are. No role, no ask, no link. The accept should be obvious.

**First message (after they accept, wait a day; 50-110 words).**

```
1  the specific thing about them (their reason, not flattery)
2  the role in one sentence: what they would own, and the range
3  why it is open or why now
4  one small ask: "Worth a 15 minutes this week?" Not a calendar link.
```

**Follow-up 1 (+4 days).** Add one new fact: a detail about the team, a
number, a reference. If you have nothing new, do not send it.

**Follow-up 2 (+10 days).** Close the loop. Say you will stop, leave the door
open, and mean it. Then stop.

## Objections, with honest replies

| they say | do |
| --- | --- |
| "Happy where I am" | Thank them, ask nothing, offer to stay in touch, and ask whether they know someone. |
| "What's the pay?" | Give the range. If you cannot, say when you can. Never dodge. |
| "Not looking" | Respect it. Ask permission to message in six months. |
| "Who's the client?" | If confidential, say so and offer an NDA-level intro on a call; never invent details. |
| "Is it remote?" | Answer exactly, including the days in office. |

Draft replies in the user's voice; never argue someone out of "no".

## Lint it

```bash
python3 outreach_lint.py messages.txt --kinds note,first,followup1,followup2
```

Blocks separated by a line of `---`. It checks the 200-char limit, links in the
note, filler phrases, a missing specific, a missing ask, early calendar links,
and follow-ups that only chase. Fix every ERROR; resolve each WARN.

## Rules that protect the candidate and the account

- Never run automated connection or message sequences. Automation violates the
  LinkedIn User Agreement and gets accounts restricted.
- Never send more than ~20 invites a day, or message people who have said no.
- Never use a candidate's data outside the purpose they would expect, and
  honour deletion or "do not contact" requests. Check GDPR/UK GDPR/CCPA in your
  region; see `compliance.md` in this folder.
- Never fabricate a mutual connection, a client, a salary or a deadline.
- Never name a confidential client or a candidate to a third party without
  consent.

## Output

For each candidate: the note with its character count, the first message, both
follow-ups with send days, objection replies, and the lint result. All
humanized through `/li-human` before the user sees them.
