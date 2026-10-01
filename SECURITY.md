# Security and privacy

These skills run locally and call no external service. The helper scripts use
the Python standard library and read only the files you give them.

## Reporting

For a vulnerability, or a case where a skill could leak personal data,
credentials or confidential client or candidate information, use GitHub's
private vulnerability reporting on this repository (Security tab, "Report a
vulnerability"). Please do not open a public issue for it.

## What we ask of contributors and forks

- Never commit credentials, candidate data, client names or personal paths.
  `python3 scripts/validate.py` checks for the common ones.
- Keep `voice.md`, `stories.md` and any exports in `~/.claude/linkedin/`, not
  in the repo.
- Skills must not post, send or schedule anything without an explicit yes, and
  must not automate LinkedIn.
