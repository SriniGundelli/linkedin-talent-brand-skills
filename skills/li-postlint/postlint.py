#!/usr/bin/env python3
"""postlint.py - lint a LinkedIn post before you paste it.

    python3 postlint.py draft.txt
    echo "..." | python3 postlint.py -
    python3 postlint.py draft.txt --json

Checks the things that cost reach and the things that read as AI or as spam.
It does not judge whether the post is any good. That is still your job.
Standard library only. Nothing leaves your machine.
"""
import argparse
import json
import re
import sys

HOOK_LIMIT = 140        # characters visible on mobile before "...see more"
BODY_SOFT = (900, 1300)  # working range for a text post
BODY_HARD = 3000         # LinkedIn's post limit

BAIT = [
    r"comment (?:yes|\"?yes\"?|below|\"?interested\"?|\"?send\"?)\b", r"\blike (?:if|this post if)\b",
    r"\btag (?:someone|a friend|your)\b", r"\bagree\?\s*$", r"\bthoughts\?\s*$", r"\brepost (?:if|this)\b",
    r"\bshare (?:if|this if)\b", r"\bdrop a (?:\W+|emoji|fire)\b",
]
CLICHE_OPEN = [
    r"^i'?m (?:thrilled|excited|humbled|delighted|proud) to (?:announce|share)", r"^big news",
    r"^(?:so )?(?:i|we) (?:have|got) (?:some )?(?:news|an announcement)", r"^in today'?s (?:fast-paced|world|landscape)",
    r"^as a [a-z ]+, i (?:believe|know)", r"^here'?s the thing",
]
INVISIBLE = "​‌‍⁠﻿­  "
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿]")
URL = re.compile(r"https?://\S+|www\.\S+")


def lint(text):
    t = text.strip("\n")
    findings = []  # (severity, rule, message)

    def add(sev, rule, msg):
        findings.append({"severity": sev, "rule": rule, "message": msg})

    lines = t.split("\n")
    first = next((l for l in lines if l.strip()), "")
    chars = len(t)
    paras = [p for p in re.split(r"\n\s*\n", t) if p.strip()]

    # ---- hook
    if len(first) > HOOK_LIMIT:
        add("warn", "hook-truncates", f"Line 1 is {len(first)} chars. Mobile cuts at ~{HOOK_LIMIT}, so the reader meets '...see more' mid-sentence. Land the point before char {HOOK_LIMIT}.")
    if len(first.split()) < 3:
        add("warn", "hook-thin", "Line 1 is under three words. Make it carry a claim, a number or a tension.")
    for pat in CLICHE_OPEN:
        if re.search(pat, first.strip().lower()):
            add("warn", "cliche-opener", "Opener is a stock LinkedIn announcement. Lead with the result or the problem instead.")
            break
    if len(lines) > 1 and lines[1].strip() != "" and len(paras) > 0:
        add("info", "hook-not-alone", "Line 2 sits right under the hook. A blank line after the hook gives it room to land.")

    # ---- length
    if chars > BODY_HARD:
        add("error", "too-long", f"{chars} chars is over LinkedIn's {BODY_HARD} limit.")
    elif chars > 2000:
        add("warn", "long", f"{chars} chars. Over 2,000 has to earn every line.")
    elif chars < 400:
        add("info", "short", f"{chars} chars reads as a thought, not a post. Fine if that is the intent.")

    # ---- shape
    walls = [p for p in paras if len(p) > 320 and "\n" not in p.strip()]
    if walls:
        add("warn", "wall-of-text", f"{len(walls)} paragraph(s) run over ~320 chars with no line break. Split them; white space is the format.")
    if len(paras) < 4 and chars > 600:
        add("info", "few-paragraphs", "Fewer than four paragraphs. Short paragraphs of 1-3 lines scan better on mobile.")

    # ---- links and tags
    urls = URL.findall(t)
    if urls:
        add("warn", "link-in-body", f"{len(urls)} link(s) in the body. Links in the post body tend to depress reach. Put it in the first comment and say so.")
    tags = re.findall(r"(?<!\w)#\w+", t)
    if len(tags) > 3:
        add("warn", "hashtag-wall", f"{len(tags)} hashtags. Three or fewer, at the end.")
    mid = [m.group(0) for m in re.finditer(r"(?<!\w)#\w+", "\n".join(paras[:-1]))] if len(paras) > 1 else []
    if mid:
        add("info", "mid-hashtags", "Hashtags in the middle of the post break the read. Move them to the last line.")
    mentions = re.findall(r"(?<!\w)@\w+", t)
    if len(mentions) > 5:
        add("warn", "tag-spray", f"{len(mentions)} @-mentions looks like tag-spraying. Tag only people who are actually in the story.")

    # ---- bait and AI tells
    low = t.lower()
    for pat in BAIT:
        m = re.search(pat, low, re.M)
        if m:
            add("warn", "engagement-bait", f"Reflex engagement bait: '{m.group(0).strip()}'. Ask a specific question instead.")
            break
    dashes = t.count("—")
    if dashes:
        add("warn", "em-dash", f"{dashes} em dash(es). Commonly read as an AI tell. Use a comma, a full stop or a hyphen.")
    inv = [c for c in t if c in INVISIBLE]
    if inv:
        add("error", "invisible-chars", f"{len(inv)} invisible character(s). Run /li-human to strip them.")
    if re.search(r"\bnot just [^.!?\n]{2,60},? (?:but|it'?s)\b", low) or re.search(r"\bit'?s not [^.!?\n]{2,50}, it'?s\b", low):
        add("warn", "not-x-but-y", "'Not X, it's Y' construction. Say the Y.")
    emojis = len(EMOJI.findall(t))
    if emojis > 5:
        add("warn", "emoji-heavy", f"{emojis} emoji. More than a handful reads as AI or as an ad.")

    # ---- close
    qs = len(re.findall(r"\?", paras[-1])) if paras else 0
    if qs > 1:
        add("info", "multiple-asks", "More than one question in the close. One specific ask converts better than two.")
    if chars >= 400 and qs == 0 and not re.search(r"\b(dm|comment|reply|tell me|share|send)\b", (paras[-1] if paras else "").lower()):
        add("info", "no-close", "No question or instruction at the end. Not always wrong, but say what you want the reader to do.")

    weights = {"error": 25, "warn": 8, "info": 2}
    score = max(0, 100 - sum(weights[f["severity"]] for f in findings))
    stats = {"chars": chars, "words": len(t.split()), "paragraphs": len(paras), "hook_chars": len(first),
             "hashtags": len(tags), "links": len(urls)}
    return {"score": score, "stats": stats, "findings": findings}


def render(r):
    s = r["stats"]
    print(f"\nPOST LINT  -  {s['chars']} chars  -  {s['words']} words  -  {s['paragraphs']} paragraphs  -  hook {s['hook_chars']}/{HOOK_LIMIT}")
    print("=" * 66)
    if not r["findings"]:
        print("  Nothing to fix.")
    for sev in ("error", "warn", "info"):
        for f in (x for x in r["findings"] if x["severity"] == sev):
            print(f"  [{sev.upper():5}] {f['rule']}: {f['message']}")
    print("-" * 66)
    print(f"  SCORE {r['score']}/100\n")


def main():
    ap = argparse.ArgumentParser(description="Lint a LinkedIn post.")
    ap.add_argument("input", nargs="?", default="-", help="file, or - for stdin")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    text = sys.stdin.read() if a.input == "-" else open(a.input, encoding="utf-8").read()
    r = lint(text)
    print(json.dumps(r, indent=2)) if a.json else render(r)
    sys.exit(1 if any(f["severity"] == "error" for f in r["findings"]) else 0)


if __name__ == "__main__":
    main()
