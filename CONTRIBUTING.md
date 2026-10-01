# Contributing

Thanks for helping. Small, specific pull requests are easiest to merge.

## What fits

- A new skill for a real LinkedIn job: recruiting, personal brand, company
  content, sales, creator, executive comms.
- A better rule, lexicon entry or compliance note, with a source or a reason.
- A fix to a script, with a test.
- A translation or a regional variant (spelling lexicon, local pay-transparency
  notes).

## What does not

- Anything that automates LinkedIn actions, scrapes member data, runs pods or
  buys engagement. These breach LinkedIn's User Agreement and put users at risk.
- Fabricated statistics, testimonials or "guaranteed" outcomes.
- Client names, candidate data, credentials or personal paths.
- Skills that post, send or publish without the user's explicit yes.

## Skill standard

- Folder `skills/li-<name>/`, with `SKILL.md` whose frontmatter `name` equals
  the folder.
- `description` states what it does and when to use it ("Use when the user
  says ..."), under 1,024 characters.
- The body has: what you need first, the steps, the rules (a "Never" list),
  and the output. Match the tone of the existing skills: plain, specific,
  no hype.
- State what the skill never invents. Gaps become `{{placeholders}}`, not
  plausible fiction.
- Where people are named (employees, candidates, clients) include a consent step.
- Scripts: Python 3 standard library only, `--help` works, nothing leaves the
  machine, covered by a test in `tests/`.

## Before you open a PR

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests
```

Both must pass. CI runs the same.

## Reporting a problem

Open an issue with: the skill, what you asked, what you expected, what came
back. For anything involving privacy or a security concern, see
[SECURITY.md](SECURITY.md) rather than a public issue.
