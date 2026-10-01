# LinkedIn skills for recruiting, personal brands and company content

Thirty Claude skills for LinkedIn. Free, MIT, no signup, no API key, nothing to
connect. Built on [Jake Schincariol's LinkedIn agent skill](https://github.com/Jakeschincariol/linkedin-agent-skill)
(eleven skills for posts, comments, replies, profile, planning, DMs and a
humanizer) and extended with nineteen more for the people who run LinkedIn for
a living: recruiters, personal-brand builders and company marketing teams.

**These skills write. You post.** Nothing is published, sent or scheduled for
you, and none of them automate LinkedIn. That is the design: automation breaks
[LinkedIn's User Agreement](https://www.linkedin.com/legal/user-agreement) and
gets accounts restricted.

## Install

```bash
git clone https://github.com/SriniGundelli/linkedin-talent-brand-skills.git
cd linkedin-talent-brand-skills
./scripts/install.sh                 # all 30 skills into ~/.claude/skills
./scripts/install.sh --pack recruiting   # or: brand | company
./scripts/install.sh --project           # into ./.claude/skills of this project
```

Or as a plugin in Claude Code: `/plugin marketplace add SriniGundelli/linkedin-talent-brand-skills`.
No Claude Code? Paste any `SKILL.md` at the top of a chat and it runs as a mode
(the Python tools need a shell; the rest works).

Then run `/li-voice` (or `/li-positioning` if you are starting from zero) so
every skill writes like you. Fill the **House rules** section of `voice.md`:
spelling, banned words, who approves.

## The thirty

**Recruitment marketing** (new)

| command | what it does |
| --- | --- |
| `/li-job-post` | Role brief into a job post plus the feed post. Lints for missing pay, requirement walls, gendered and age-coded wording |
| `/li-employer-brand` | EVP in three sentences, five pillars, four-week calendar of proof-backed posts, consent checklist |
| `/li-candidate-outreach` | Note, first message, two follow-ups and objection replies for passive candidates, with a linter and a compliance checklist |
| `/li-referral-campaign` | Referral push: who-to-think-of card, five distinct share angles so posts are not copies, DM script, tracker |
| `/li-hiring-announcement` | New-hire, promotion and milestone posts with a consent gate |
| `/li-recruiter-brand` | Market-intel post series and a two-hour weekly rhythm so candidates come to you |

**Personal branding** (new)

| command | what it does |
| --- | --- |
| `/li-positioning` | Audience, positioning sentence, three to five positions with evidence, content pillars; writes `voice.md` |
| `/li-voice` | Measures your own posts (rhythm, contractions, openers, repeated phrases) and builds `voice.md` from evidence |
| `/li-story-bank` | Interviews you for real stories, files them with consent flags, turns one into a post |
| `/li-newsletter` | Series promise, issue outline, long-form draft, and the feed posts that send people to it |
| `/li-brand-sprint` | A 90-day plan with baseline, three goals, weekly rhythm and reviews at weeks 4, 8 and 12 |

**Company content** (new)

| command | what it does |
| --- | --- |
| `/li-company-page` | Pillars, a monthly calendar, and the split between what the page posts and what people post |
| `/li-case-study` | Client results into a post or carousel, with a consent and anonymity gate first |
| `/li-launch` | Product, funding or partnership launch as a coordinated set: founder post, page post, team copy, follow-ups |
| `/li-founder-ghost` | Ghostwriting workflow for executives: interview, drafts, per-post approval, hard limits |
| `/li-advocacy-kit` | Weekly employee share kit: five angles, blanks for their own detail, a stagger schedule |
| `/li-event-promo` | Webinar or event promotion, seven posts from T-14 to the recap |

**Quality and measurement** (new)

| command | what it does |
| --- | --- |
| `/li-postlint` | Lints a post: hook truncation, links, hashtags, bait, tells. Scored, local |
| `/li-metrics` | Analyses an analytics CSV against your own median: what to repeat, what to stop |

**The inherited core** (from Jake Schincariol's repo, with small additions)

`/li-post` (21 hook formulas) · `/li-comment` · `/li-reply` · `/li-profile` (12-part, 100-point rubric) · `/li-plan` · `/li-human` (the humanizer) · `/li-carousel` · `/li-repurpose` · `/li-dm` · `/li-inbox` · `/li-audit`

## The tools that actually run

All standard-library Python 3, on your machine, nothing uploaded.

| script | skill | what it does |
| --- | --- | --- |
| `humanize.py`, `detect.py` | `li-human` | Strip invisible characters, em dashes and a 113-word slop lexicon; five-check score. New: `--extra` merges add-on lexicons |
| `postlint.py` | `li-postlint` | Post linter |
| `jobpost_lint.py` | `li-job-post` | Pay, location, requirement bloat, gender- and age-coded wording, jargon |
| `outreach_lint.py` | `li-candidate-outreach` | Note limit, filler, early links, missing ask |
| `voiceprint.py` | `li-voice` | Measures your voice from your posts |
| `analyze.py` | `li-metrics` | Ranks posts against your own median |

## How this compares to the repo it came from

Honest version. Jake's repo is the better choice if you only need to run your
own personal account, because it is smaller and there is less to learn. This
one is for you if you hire, if you market a company, or if you are building a
personal brand on a plan rather than post by post.

| | Jake's original | This repo |
| --- | --- | --- |
| Skills | 11 | 30 (the same 11, plus 19) |
| Audience | An individual posting for themselves | Individuals, recruiters, in-house talent teams, company marketers, executive ghostwriters |
| Recruiting | `/li-dm`, `/li-inbox` | Job posts, employer brand, candidate outreach, referrals, announcements, recruiter brand |
| Company content | None | Page system, case studies, launches, advocacy, events, ghostwriting |
| Personal brand | Profile score, plan | Plus positioning, measured voice, story bank, newsletter, 90-day sprint |
| Runnable tools | 2 (humanizer, detector) | 7 |
| Add-on lexicons | No | Yes: `--extra` for UK spelling, recruitment jargon, your own banned words |
| Compliance prompts | A "never" list | Plus consent gates (hires, clients, employees) and a recruiter data-protection checklist |
| Tests and CI | No | 14 unit tests, a validator, GitHub Actions |
| Install | Copy folders | `install.sh` with packs, `--project`, `--force` |
| Simplicity | Higher | Lower: thirty skills is a lot. Use a pack |

What we did not change: the approval gate, the hooks, the rubric and the
humanizer logic. Those are Jake's, and they are good.

## Status and limits

- The Python tools and the repo validator are covered by unit tests and CI.
- The `SKILL.md` flows are prompts. They are not tested by CI, because their
  behaviour depends on the model. Treat the first run as a trial and tell us
  what broke, with an issue.
- The linters are drafting aids, not legal advice. Pay-transparency,
  data-protection and anti-discrimination rules differ by country and state.
- The detector is a set of local heuristics, not a third-party AI detector, and
  does not promise any verdict. See the original README for the long version.
- LinkedIn changes its analytics export and its limits. `analyze.py` matches
  column names loosely; if yours differ, rename a column to `impressions`.

## Fork it and make it yours

See [FORKING.md](FORKING.md). In short: fork, edit `templates/voice.md` and a
lexicon, rename the plugin, run `python3 scripts/validate.py`, and open a pull
request upstream if you built something others would want.

## Credit

The eleven core skills, the hook formulas, the profile rubric and the
humanizer are by [Jake Schincariol](https://opusjake.ai) (MIT,
[original repo](https://github.com/Jakeschincariol/linkedin-agent-skill)). The
additions are by BalanceX.ai and contributors. See [NOTICE](NOTICE) and
[LICENSE](LICENSE).

## License

MIT. Take it, change it, ship it. Keep the notices.
