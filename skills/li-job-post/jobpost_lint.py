#!/usr/bin/env python3
"""jobpost_lint.py - lint a job post for the things that cost you applicants.

    python3 jobpost_lint.py role.txt
    python3 jobpost_lint.py role.txt --json

Checks: pay range, location and work model, requirement bloat, gender-coded and
age-coded wording, jargon, candidate-vs-company voice, and an equal-opportunity
or accommodation line. It is a drafting aid, not legal advice: pay-transparency
and discrimination rules differ by country and state, so check yours.
Standard library only.
"""
import argparse
import json
import re
import sys

# Word lists follow the pattern in Gaucher, Friesen & Kay (2011) on gendered wording in job ads.
MASC = ["aggressive", "ambitious", "assertive", "competitive", "dominant", "driven", "fearless", "headstrong",
        "ninja", "rockstar", "rock star", "superior", "crush", "killer", "battle", "fierce", "hard-charging", "guru"]
FEM = ["collaborative", "supportive", "nurturing", "interpersonal", "sympathetic", "loyal", "committed to", "cooperative"]
AGE = ["digital native", "young and energetic", "young team", "recent graduate", "fresh graduate", "energetic young",
       "high energy", "mature", "overqualified", "junior-minded", "old school"]
JARGON = ["synergy", "best-in-class", "world-class", "cutting-edge", "exciting opportunity", "fast-paced", "work hard, play hard",
          "wear many hats", "self-starter", "hit the ground running", "dynamic", "passionate", "thought leader", "disruptive"]
EXCLUDE = ["native english speaker", "clean-shaven", "able-bodied", "man-hours", "manpower", "salesman", "chairman", "he or she"]

PAY = re.compile(r"(?:[$£€]\s?\d[\d,.]*\s?[kK]?(?:\s?(?:-|to|–)\s?[$£€]?\s?\d[\d,.]*\s?[kK]?)?|\b\d{2,3}\s?[kK]\b|\bsalary (?:range|band)\b|\b(?:usd|gbp|eur|aed)\s?\d)", re.I)
LOCATION = re.compile(r"\b(remote|hybrid|on-?site|in[- ]office|work from home|based in|located in|london|new york|san francisco|dubai|toronto|boston|berlin|singapore)\b", re.I)
EEO = re.compile(r"\b(equal opportunity|equal-opportunity|reasonable adjustments?|accommodations?|diversity|inclusive|we welcome (?:all |everyone|applications|applicants)|disability)\b", re.I)
BENEFITS = re.compile(r"\b(benefits|equity|pension|401\(?k\)?|bonus|holiday|vacation|pto|health|insurance|parental|learning budget)\b", re.I)


def find(words, low):
    return sorted({w for w in words if re.search(r"(?<![a-z])" + re.escape(w) + r"(?![a-z])", low)})


def lint(text):
    low = text.lower()
    words = re.findall(r"[A-Za-z']+", text)
    n = len(words)
    out = []

    def add(sev, rule, msg):
        out.append({"severity": sev, "rule": rule, "message": msg})

    if not PAY.search(text):
        add("error", "no-pay", "No pay figure or range. Pay-transparency rules now require one in many places, and candidates skip roles without it.")
    if not LOCATION.search(text):
        add("error", "no-location", "No location or work model (remote / hybrid / on-site). It is the first thing candidates filter on.")
    if not EEO.search(text):
        add("warn", "no-eeo", "No equal-opportunity or accommodation line. Add the one your counsel or country requires.")
    if not BENEFITS.search(text):
        add("info", "no-benefits", "Nothing on benefits, equity or growth. Say what the person gets, not only what they give.")

    if n < 200:
        add("warn", "thin", f"{n} words. Too little for a candidate to self-select; say what the first 90 days look like.")
    elif n > 700:
        add("warn", "long", f"{n} words. Over ~700 and applicants stop reading. Move boilerplate to the careers page.")

    bullets = [l for l in text.split("\n") if re.match(r"\s*(?:[-*•]|\d+[.)])\s+\S", l)]
    reqs = []
    in_req = False
    for l in text.split("\n"):
        if re.search(r"\b(requirements?|you have|you'?ll need|must have|what we'?re looking for|qualifications)\b", l, re.I) and not re.match(r"\s*[-*•]", l):
            in_req = True
            continue
        if in_req and re.match(r"\s*(?:[-*•]|\d+[.)])\s+\S", l):
            reqs.append(l)
        elif in_req and l.strip() == "":
            continue
        elif in_req and not re.match(r"\s*(?:[-*•]|\d+[.)])", l):
            in_req = False
    if len(reqs) > 8:
        add("warn", "requirement-wall", f"{len(reqs)} requirements. Cut to the 4-6 needed on day one; many strong candidates skip a role when they match fewer than all of a long list.")
    yrs = [int(m) for m in re.findall(r"(\d{1,2})\+?\s*(?:years|yrs)", low)]
    if yrs and max(yrs) >= 8:
        add("warn", "years-inflation", f"Asks for {max(yrs)}+ years. Describe the scope they must have handled instead of counting years; it also avoids age bias.")

    for label, lst, sev, msg in (
        ("masculine-coded", MASC, "warn", "Masculine-coded wording can deter women from applying: {}. Swap for what the job actually demands."),
        ("age-coded", AGE, "warn", "Age-coded wording ({}). It can create discrimination exposure and narrows the pool."),
        ("exclusionary", EXCLUDE, "error", "Exclusionary or non-neutral wording: {}. Remove it."),
        ("jargon", JARGON, "info", "Filler jargon: {}. Say the concrete thing."),
    ):
        hits = find(lst, low)
        if hits:
            add(sev, label, msg.format(", ".join(hits)))
    fem = find(FEM, low)
    masc = find(MASC, low)
    if masc and len(masc) >= 2 * max(1, len(fem)):
        add("info", "tone-skew", f"{len(masc)} masculine-coded vs {len(fem)} feminine-coded terms. Aim for a balanced description.")

    you = len(re.findall(r"\b(you|your|you'll|you're)\b", low))
    we = len(re.findall(r"\b(we|our|us|we'll|we're)\b", low))
    if n > 150 and you < we / 2:
        add("info", "company-voice", f"'we' outnumbers 'you' {we}:{you}. Posts written to the candidate ('you will ship...') convert better than posts about the company.")

    first = next((l for l in text.split("\n") if l.strip()), "")
    if len(first) > 140:
        add("info", "feed-hook", f"First line is {len(first)} chars; if this becomes a feed post, the hook is cut at ~140.")

    weights = {"error": 20, "warn": 8, "info": 2}
    score = max(0, 100 - sum(weights[f["severity"]] for f in out))
    return {"score": score, "words": n, "bullets": len(bullets), "findings": out}


def render(r):
    print(f"\nJOB POST LINT  -  {r['words']} words")
    print("=" * 66)
    if not r["findings"]:
        print("  Nothing to fix.")
    for sev in ("error", "warn", "info"):
        for f in (x for x in r["findings"] if x["severity"] == sev):
            print(f"  [{sev.upper():5}] {f['rule']}: {f['message']}")
    print("-" * 66)
    print(f"  SCORE {r['score']}/100   (a drafting aid, not legal advice)\n")


def main():
    ap = argparse.ArgumentParser(description="Lint a job post.")
    ap.add_argument("input", nargs="?", default="-")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    text = sys.stdin.read() if a.input == "-" else open(a.input, encoding="utf-8").read()
    r = lint(text)
    print(json.dumps(r, indent=2)) if a.json else render(r)


if __name__ == "__main__":
    main()
