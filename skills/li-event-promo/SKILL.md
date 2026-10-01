---
name: li-event-promo
description: >-
  Promote a webinar, meetup, panel, talk or conference appearance on LinkedIn -
  the announcement, speaker posts, a countdown, the day-of and the follow-up that
  turns attendees into conversations. Use when the user says "promote our
  webinar", "event post", "I'm speaking at", "meetup announcement", "panel
  promotion", "recap post", or "get people to register".
---

# li-event-promo

An event post that only says "join us" gets ignored. People register for a
reason that is specific to them: a question answered, a person to meet, a
thing they will leave with. Lead with that.

> Also apply the **House rules** section of `~/.claude/linkedin/voice.md`.
> Nothing is posted without the owner's yes.

## Intake

Ask once: what it is, date/time with time zone, where (link or venue),
cost, who it is for, the three things attendees will leave with, speakers and
their agreement to be named, the registration link, and the capacity.

## The sequence

| when | post | goal |
| --- | --- | --- |
| T-14 | The problem the event addresses, with one provocative fact. Soft ask to register | awareness |
| T-10 | Speaker spotlight: who they are and one thing they will say (their words, approved) | credibility |
| T-7 | "Three questions we will answer", each a question the audience has | relevance |
| T-3 | Low seats or the one reason to register now (true scarcity only) | urgency |
| T-0 | Day-of: "starting in an hour", link | attendance |
| T+1 | Recap: three takeaways and the slide or recording | value |
| T+3 | The best question asked and its answer | conversation |

Each post follows `/li-post` rules: strong first line, short paragraphs, one
instruction. Link in the first comment where possible; use the LinkedIn event
object for the registration page when the user has it.

## Speaker kit

For each speaker, a 60-word post they can share in their own words with
blanks for their own detail, a headshot request, and the exact session title.
Do not post for them. See `/li-advocacy-kit`.

## Follow-up that matters

After the event, draft a message for attendees who engaged (replied, asked a
question, shared): reference what they said, offer one resource, and ask one
small question. Send by hand, one at a time, only to people who attended or
opted in; use `/li-dm` for the note.

## Rules

- State the time zone and the format (live, recorded, hybrid) clearly.
- Do not use "last chance" unless it is true. Do not claim attendee numbers or
  speakers that are not confirmed.
- Get permission before naming attendees or sharing photos of them.
- Accessibility: say if captions or recordings will exist.
- Lint each draft with `python3 ../li-postlint/postlint.py`.

## Output

The seven-post sequence with dates and first-comment text, the speaker kit,
the recap drafts, and the attendee follow-up message.
