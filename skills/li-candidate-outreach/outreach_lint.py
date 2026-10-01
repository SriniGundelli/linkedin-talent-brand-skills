#!/usr/bin/env python3
"""outreach_lint.py - lint recruiter outreach to passive candidates.

    python3 outreach_lint.py messages.txt            # blocks separated by a line of ---
    python3 outreach_lint.py messages.txt --kinds note,first,followup1,followup2
    python3 outreach_lint.py - --kind note --limit 300

Block kinds: note (connection note, 200 chars, 300 on Premium), first (first
message after accept), followup1, followup2, inmail. If you pass no --kinds the
blocks are read in that order. Standard library only.
"""
import argparse
import json
import re
import sys

ORDER = ["note", "first", "followup1", "followup2"]
FILLER = [r"i hope this (?:message |email )?finds you well", r"i came across your profile", r"your background is impressive",
          r"i was impressed by your", r"just reaching out", r"just checking in", r"just bumping", r"touch base",
          r"exciting opportunit(?:y|ies)", r"perfect fit", r"great fit", r"rockstar", r"i know you'?re busy", r"circle back"]
URLRE = re.compile(r"https?://\S+|calendly\.com\S*|cal\.com\S*")
SPECIFIC = re.compile(r"\d|[A-Z][a-z]+ [A-Z][a-z]+|\b(?:your (?:post|talk|article|launch|team|work on)|saw (?:your|that)|read (?:your|that))\b")
PAYWORD = re.compile(r"[$£€]\s?\d|\b\d{2,3}\s?[kK]\b|\bsalary|\bcomp(?:ensation)?\b|\bequity\b", re.I)


def lint_block(kind, text, note_limit):
    t = text.strip()
    f = []

    def add(sev, rule, msg):
        f.append({"severity": sev, "rule": rule, "message": msg})

    n = len(t)
    w = len(t.split())
    if kind == "note":
        if n > note_limit:
            add("error", "over-limit", f"{n}/{note_limit} chars. LinkedIn truncates or rejects it.")
        if "?" in t or re.search(r"\b(call|chat|role|opening|position|job|hiring)\b", t.lower()):
            add("warn", "note-asks", "A connection note that asks or pitches a role gets declined. Make the accept obvious; ask nothing.")
        if URLRE.search(t):
            add("error", "note-link", "No links in a connection note.")
    else:
        lo, hi = (40, 120) if kind in ("first", "inmail") else (15, 70)
        if w > hi:
            add("warn", "too-long", f"{w} words. Over ~{hi} reads as a mass message. Cut to what this person needs to decide.")
        if w < lo:
            add("info", "too-thin", f"{w} words. Under ~{lo} may not carry a reason to reply.")
        if kind in ("first", "inmail") and URLRE.search(t):
            add("warn", "early-link", "Scheduling link in the first message reads as a funnel. Offer a call; send the link after they say yes.")
        qs = t.count("?")
        if kind != "followup2" and qs == 0 and not re.search(r"\b(worth|open to|would you|can i|happy to)\b", t.lower()):
            add("warn", "no-ask", "No clear ask. One small, specific question.")
        if qs > 2:
            add("warn", "many-asks", f"{qs} questions. One ask per message.")
        if kind in ("first", "inmail") and not SPECIFIC.search(t):
            add("warn", "generic", "Nothing specific to this person (a post, a project, a number, a name). Without it this is the message everyone sends.")
        if kind in ("first", "inmail") and not PAYWORD.search(t):
            add("info", "no-comp-signal", "No pay signal. Senior candidates decide faster when the range is in the first message or offered immediately.")
        if kind.startswith("followup") and re.search(r"\b(bump|following up|follow-up on my (?:last|previous)|checking in)\b", t.lower()):
            add("warn", "empty-followup", "A follow-up that only chases. Add something new (a detail about the team, a number, a reference) or do not send it.")
    for pat in FILLER:
        m = re.search(pat, t.lower())
        if m:
            add("warn", "filler", f"Filler phrase '{m.group(0)}'. Open with the specific reason you are writing to them.")
    if "—" in t:
        add("warn", "em-dash", "Em dash. Common AI tell. Use a comma or a full stop.")
    score = max(0, 100 - sum({"error": 25, "warn": 10, "info": 3}[x["severity"]] for x in f))
    return {"kind": kind, "chars": n, "words": w, "score": score, "findings": f}


def main():
    ap = argparse.ArgumentParser(description="Lint recruiter outreach.")
    ap.add_argument("input", nargs="?", default="-")
    ap.add_argument("--kinds", help="comma list, one per block (default: note,first,followup1,followup2)")
    ap.add_argument("--kind", help="treat the whole input as one block of this kind")
    ap.add_argument("--limit", type=int, default=200, help="connection-note limit (200 free, 300 Premium)")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    raw = sys.stdin.read() if a.input == "-" else open(a.input, encoding="utf-8").read()
    blocks = [raw] if a.kind else [b for b in re.split(r"^\s*---+\s*$", raw, flags=re.M) if b.strip()]
    kinds = [a.kind] if a.kind else (a.kinds.split(",") if a.kinds else ORDER)
    res = [lint_block(kinds[i] if i < len(kinds) else "followup2", b, a.limit) for i, b in enumerate(blocks)]
    if a.json:
        print(json.dumps(res, indent=2))
        return
    for r in res:
        print(f"\n{r['kind'].upper()}  -  {r['chars']} chars  -  {r['words']} words  -  score {r['score']}")
        print("-" * 60)
        for x in r["findings"]:
            print(f"  [{x['severity'].upper():5}] {x['rule']}: {x['message']}")
        if not r["findings"]:
            print("  Clean.")
    print()


if __name__ == "__main__":
    main()
