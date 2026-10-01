#!/usr/bin/env bash
# Install the skills into ~/.claude/skills (or a project's .claude/skills).
#   ./scripts/install.sh                 all skills, user-level
#   ./scripts/install.sh --project       into ./.claude/skills of the current directory
#   ./scripts/install.sh li-post li-job-post li-human   only these (li-human is pulled in automatically)
#   ./scripts/install.sh --pack recruiting|brand|company
# Existing skills are never overwritten; pass --force to replace them.
set -euo pipefail

HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
DEST="$HOME/.claude/skills"
FORCE=0
PACK=""
WANT=()

while [ $# -gt 0 ]; do
  case "$1" in
    --project) DEST="$PWD/.claude/skills" ;;
    --force) FORCE=1 ;;
    --pack) PACK="$2"; shift ;;
    -h|--help) sed -n '2,8p' "$0"; exit 0 ;;
    *) WANT+=("$1") ;;
  esac
  shift
done

case "$PACK" in
  recruiting) WANT+=(li-job-post li-employer-brand li-candidate-outreach li-referral-campaign li-hiring-announcement li-recruiter-brand li-dm li-inbox) ;;
  brand)      WANT+=(li-positioning li-voice li-story-bank li-newsletter li-brand-sprint li-post li-comment li-reply li-profile li-plan li-carousel li-repurpose li-audit li-metrics) ;;
  company)    WANT+=(li-company-page li-case-study li-launch li-founder-ghost li-advocacy-kit li-event-promo li-carousel li-post) ;;
  "") ;;
  *) echo "unknown pack: $PACK (recruiting | brand | company)"; exit 1 ;;
esac

if [ ${#WANT[@]} -eq 0 ]; then
  for d in "$HERE"/skills/*/; do WANT+=("$(basename "$d")"); done
else
  WANT+=(li-human li-postlint)   # the humanizer and the linter are used by every drafting skill
fi

mkdir -p "$DEST"
installed=0; skipped=0
for n in $(printf '%s\n' "${WANT[@]}" | sort -u); do
  src="$HERE/skills/$n"
  [ -d "$src" ] || { echo "no such skill: $n"; exit 1; }
  if [ -e "$DEST/$n" ] && [ "$FORCE" -ne 1 ]; then
    echo "skip   $n (exists; use --force to replace)"; skipped=$((skipped+1)); continue
  fi
  rm -rf "$DEST/$n"; cp -R "$src" "$DEST/$n"
  find "$DEST/$n" -name '__pycache__' -prune -exec rm -rf {} + 2>/dev/null || true
  echo "ok     $n"; installed=$((installed+1))
done

mkdir -p "$HOME/.claude/linkedin"
if [ ! -e "$HOME/.claude/linkedin/voice.md" ]; then
  cp "$HERE/templates/voice.md" "$HOME/.claude/linkedin/voice.md"
  echo "created ~/.claude/linkedin/voice.md from the template. Fill it in, or run /li-voice."
fi
echo "done: $installed installed, $skipped skipped, into $DEST. Restart Claude Code to load them."
