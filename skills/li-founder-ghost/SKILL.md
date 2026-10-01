---
name: li-founder-ghost
description: >-
  Run an executive or founder LinkedIn ghostwriting workflow - the 30-minute
  interview, drafts in the leader's real voice, an approval loop that works for
  busy people, and rules for what an exec must never be made to say. Use when
  the user says "ghostwrite for our CEO", "founder content", "write posts for my
  boss", "executive thought leadership", or manages a leader's LinkedIn.
---

# li-founder-ghost

The best executive content is the leader's own thinking, written down. A
ghostwriter's job is to extract it, shape it and protect the leader from saying
something they cannot stand behind.

> This skill reads the leader's own `voice.md` (one per person, e.g.
> `~/.claude/linkedin/voices/jane-doe.md`) plus the House rules in it. Nothing
> is posted without the leader's explicit yes.

## Set up once per leader

1. **Voice.** Gather 8-10 of the leader's real writing samples (posts, emails,
   talk transcripts, podcast transcripts). Run `/li-voice` on them. Transcripts
   of how they speak often beat their old posts.
2. **Positioning.** Run `/li-positioning` with them for 20 minutes.
3. **Off-limits.** Record: topics, people and companies not to mention,
   regulated statements, quiet periods, litigation, investor communications.
4. **Approver and channel.** Who approves (the leader, not an assistant), how
   they approve (reply "yes" in one thread), and the turnaround.

## The weekly 30-minute interview

Do not ask them to "think of a topic". Ask three questions and record:

1. What did you decide, argue about or change your mind on this week?
2. What did a customer, candidate or team member say that stuck?
3. What is something people in your industry believe that you think is wrong?

Take their words verbatim. The best sentence in any post is usually something
the leader said off the cuff. Store each answer as a story block in their
`stories.md` (`/li-story-bank`).

## Drafting

Draft four posts from one interview: two opinion or story posts, one how-to,
one reaction to industry news. Use `/li-post`; keep the leader's own phrases.
Each draft carries: the source (interview date and quote), claims that need
checking, and `{{needs leader's input}}` wherever a fact is missing.

## The approval loop

Send the leader a message per post, not a document:

```
Post 1 of 4: [opening line]
Reply YES to post as written, or send me what to change. I will not post
anything you have not said yes to.
```

Track status (draft, sent, approved, changes, posted) in a table. A post that
is not approved within 48 hours is dropped, not nudged into posting.

## Never

- Never put words in an executive's mouth about people, performance, deals,
  numbers, politics or legal matters they have not stated.
- Never post from their account without explicit approval for each post.
- Never share their login. If scheduling is needed, use LinkedIn's own tools
  under their control.
- Never present ghost-written content as unaided if the leader or their
  company policy requires disclosure.

## Output

Per leader: the voice file, the interview notes, four drafts with sources and
open questions, the approval messages, and the status table.
