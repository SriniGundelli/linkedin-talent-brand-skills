# Fork this repo and make it yours

You can use this as is, or turn it into the LinkedIn playbook for your own
company, agency or practice. Ten minutes gets you a working fork.

## 1. Fork and clone

On GitHub press **Fork**, then:

```bash
git clone https://github.com/YOUR-USER/linkedin-talent-brand-skills.git
cd linkedin-talent-brand-skills
git remote add upstream https://github.com/SriniGundelli/linkedin-talent-brand-skills.git
python3 scripts/validate.py          # should print OK
python3 -m unittest discover -s tests
```

## 2. Make it speak for you

| change | where |
| --- | --- |
| Your voice, positions, off-limits topics | `templates/voice.md` (and each person's own `~/.claude/linkedin/voice.md`) |
| House rules: spelling, banned words, who approves | the **House rules** section of `voice.md` |
| Your banned words | copy `skills/li-human/lexicons/recruitment.json` to `lexicons/yourco.json`, edit, and pass `--extra` |
| Your hooks | `skills/li-post/hooks.json` |
| Your profile rubric | `skills/li-profile/rubric.json` |
| Your industry's compliance rules | add them to `skills/li-candidate-outreach/compliance.md` and the "Never" list of the skill concerned |

Keep company-specific facts (clients, rates, internal names) in `voice.md` on
each person's machine, not in this repo. A public repo must never contain
client names, candidate data, credentials or personal paths. `scripts/validate.py`
catches the obvious ones, and it is not a substitute for looking.

## 3. Rename it

Edit `.claude-plugin/plugin.json` and `.claude-plugin/marketplace.json`: name,
description, author, repository URL. Leave the credits in `NOTICE` and
`LICENSE` as they are; the MIT licence requires them.

## 4. Add a skill

```
skills/li-yourskill/
  SKILL.md          frontmatter: name (= folder), description ("... Use when ...")
  helper.py         optional; standard library only
  data.json         optional
```

Copy a short existing skill such as `skills/li-event-promo/SKILL.md` and keep
the structure: before you write, the steps, the rules, the output. Every skill
should say what it will never do and what the user must approve.

Run the checks:

```bash
python3 scripts/validate.py
python3 -m unittest discover -s tests
```

## 5. Stay in sync

```bash
git fetch upstream
git merge upstream/main        # or: git rebase upstream/main
```

If you edited a core skill, merge conflicts will land in its `SKILL.md`. Keep
your changes in `voice.md` and in lexicons where you can, so merges stay clean.

## 6. Share it back

If you built something others would use, open a pull request upstream. See
[CONTRIBUTING.md](CONTRIBUTING.md). Skills that help people hire, market or
publish honestly are welcome; skills that automate LinkedIn, scrape it or fake
engagement are not.
