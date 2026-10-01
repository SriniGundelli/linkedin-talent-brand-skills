---
name: li-hiring-announcement
description: >-
  Write the people-news posts that go wrong most often - a new-hire welcome, a
  promotion, a "we're hiring" push, a milestone or anniversary, a team
  expansion - with a consent check built in. Use when the user says "announce a
  new hire", "welcome post", "promotion post", "we're hiring post", "work
  anniversary", "congratulate our team", or "team update post".
---

# li-hiring-announcement

People-news posts are the easiest posts to write badly: "thrilled to announce"
with no information. A good one tells the reader what the person will do, why
it matters, and one true thing about them.

> Also apply the **House rules** section of `~/.claude/linkedin/voice.md`.
> Nothing is posted without the owner's yes.

## Consent first (non-negotiable)

Before drafting anything about a named person, confirm and record:

- They have agreed to be named, and to this wording and any photo.
- The start date is confirmed and the current employer has been told, if the
  post mentions where they are coming from. Never out someone's job move early.
- For a promotion, the person and their manager have seen the post.
- For departures or sensitive news, stop and ask the owner. Do not draft it as
  a celebration.

If consent is not confirmed, the draft carries `{{consent not confirmed}}` and
a flag at the top.

## Shapes

**New-hire welcome**

```
Line 1   who they are and what they will own, not "please welcome"
Body     the problem they will work on, why we picked them (a true detail they
         approved), one thing they will change
Close    how to say hello, or what they are hiring for next
```

**Promotion.** What they did that earned it (one specific outcome), what they
will own now, and a line in their own words if they offered one.

**"We're hiring".** Do not post a pasted ad. Use `/li-job-post` for the feed
version; this skill handles the surrounding announcement and who posts it.

**Milestone or anniversary.** One number and one story. "Two years" tells
nobody anything; "two years, 40 customers, and the thing we got wrong in
month three" does.

**Team expansion.** What the new headcount lets the company do that it could
not do before.

## Rules

- Lead with the work, not the adjective. Cut "thrilled", "humbled", "rockstar".
- Tag people only if they have asked to be tagged or are plainly expecting it.
- Never state pay, equity, performance ratings or reasons for leaving.
- Offer the employee a version to post from their own profile in their own
  words, rather than only a company-page post.
- Run the draft through `python3 ../li-postlint/postlint.py` and `/li-human`.

## Output

The consent checklist with its status, the draft, a short version for the
person to post themselves, and the alt text for any photo.
