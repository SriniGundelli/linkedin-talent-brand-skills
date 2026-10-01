#!/usr/bin/env python3
"""analyze.py - rank your LinkedIn posts by what they earned, not by impressions.

    python3 analyze.py posts.csv
    python3 analyze.py posts.csv --json

Input: a CSV with one row per post. Column names are matched loosely, so a
LinkedIn analytics export, a Shield or Taplio export, or a hand-made sheet all
work. It looks for: date, text (or url/title), impressions, reactions (likes),
comments, reposts (shares), clicks, and optionally saves/sends.

Reports engagement rate, the multiple each post earned against YOUR median,
which formats and days carry, and what to repeat. Needs at least 8 posts to say
anything; fewer than that is noise. Standard library only.
"""
import argparse
import csv
import json
import re
import statistics as st
import sys
from datetime import datetime

ALIASES = {
    "date": ["date", "published", "post date", "created", "time"],
    "text": ["text", "post", "content", "title", "post text", "commentary", "url", "link"],
    "impressions": ["impressions", "views", "reach"],
    "reactions": ["reactions", "likes", "reaction"],
    "comments": ["comments", "comment"],
    "reposts": ["reposts", "shares", "repost", "share"],
    "clicks": ["clicks", "click"],
    "saves": ["saves", "saved"],
    "sends": ["sends", "send"],
    "format": ["format", "type", "media", "post type"],
}
DATE_FORMATS = ["%Y-%m-%d", "%Y-%m-%d %H:%M", "%Y-%m-%d %H:%M:%S", "%m/%d/%Y", "%m/%d/%Y %H:%M", "%d/%m/%Y", "%b %d, %Y", "%d %b %Y", "%Y-%m-%dT%H:%M:%S"]


def norm(s):
    return re.sub(r"[^a-z ]", "", s.lower()).strip()


def map_columns(header):
    cols = {}
    for key, names in ALIASES.items():
        for h in header:
            if norm(h) in names:
                cols[key] = h
                break
    return cols


def num(v):
    if v is None:
        return 0.0
    v = str(v).replace(",", "").replace("%", "").strip()
    try:
        return float(v) if v else 0.0
    except ValueError:
        return 0.0


def parse_date(v):
    v = (v or "").strip()
    for f in DATE_FORMATS:
        try:
            return datetime.strptime(v, f)
        except ValueError:
            pass
    return None


def detect_format(row, cols, text):
    if "format" in cols and row.get(cols["format"]):
        return row[cols["format"]].strip().lower()
    t = (text or "").lower()
    if "document" in t or "carousel" in t:
        return "carousel"
    if "poll" in t[:60]:
        return "poll"
    return "text"


def analyse(rows, cols):
    posts = []
    for r in rows:
        imp = num(r.get(cols.get("impressions")))
        if imp <= 0:
            continue
        react, com, rep = num(r.get(cols.get("reactions"))), num(r.get(cols.get("comments"))), num(r.get(cols.get("reposts")))
        clk, sav, snd = num(r.get(cols.get("clicks"))), num(r.get(cols.get("saves"))), num(r.get(cols.get("sends")))
        weighted = react + 3 * com + 4 * rep + 3 * sav + 4 * snd + clk
        d = parse_date(r.get(cols.get("date"), "")) if "date" in cols else None
        text = (r.get(cols.get("text"), "") or "").strip().replace("\n", " ")
        posts.append({
            "text": text[:90], "date": d.strftime("%Y-%m-%d") if d else "", "dow": d.strftime("%a") if d else "",
            "hour": d.hour if d and d.hour else None, "impressions": imp, "reactions": react, "comments": com, "reposts": rep,
            "clicks": clk, "format": detect_format(r, cols, text),
            "er": (react + com + rep + clk) / imp * 100, "weighted_er": weighted / imp * 100,
        })
    return posts


def report(posts):
    n = len(posts)
    med_imp = st.median(p["impressions"] for p in posts)
    med_er = st.median(p["weighted_er"] for p in posts)
    for p in posts:
        p["reach_x"] = p["impressions"] / med_imp if med_imp else 0
        p["er_x"] = p["weighted_er"] / med_er if med_er else 0
        p["score"] = (p["reach_x"] + p["er_x"]) / 2
    ranked = sorted(posts, key=lambda p: p["score"], reverse=True)

    def group(key):
        g = {}
        for p in posts:
            if p[key] not in ("", None):
                g.setdefault(p[key], []).append(p)
        return {k: {"posts": len(v), "median_er": round(st.median(x["weighted_er"] for x in v), 2),
                    "median_impressions": round(st.median(x["impressions"] for x in v))} for k, v in g.items() if len(v) >= 2}

    return {
        "posts": n, "median_impressions": round(med_imp), "median_weighted_er_pct": round(med_er, 2),
        "top": [{k: (round(v, 2) if isinstance(v, float) else v) for k, v in p.items() if k in ("text", "date", "format", "impressions", "weighted_er", "reach_x", "er_x")} for p in ranked[:5]],
        "bottom": [{k: (round(v, 2) if isinstance(v, float) else v) for k, v in p.items() if k in ("text", "date", "format", "impressions", "weighted_er")} for p in ranked[-3:]],
        "by_format": group("format"), "by_weekday": group("dow"),
    }


def render(r):
    print(f"\nLINKEDIN METRICS  -  {r['posts']} posts  -  median {r['median_impressions']:,} impressions, {r['median_weighted_er_pct']}% weighted ER")
    print("(weighted ER = reactions + 3x comments + 4x reposts + saves/sends + clicks, over impressions)")
    print("=" * 78)
    print("\nWHAT TO REPEAT (reach and engagement versus your own median)")
    for p in r["top"]:
        print(f"  {p['reach_x']:.1f}x reach  {p['er_x']:.1f}x ER  [{p['format']}] {p['date']}  {p['text']}")
    print("\nWHAT TO STOP")
    for p in r["bottom"]:
        print(f"  {p['impressions']:>8,.0f} imp  {p['weighted_er']:.2f}% ER  [{p['format']}] {p['date']}  {p['text']}")
    for title, key in (("BY FORMAT", "by_format"), ("BY WEEKDAY", "by_weekday")):
        if r[key]:
            print(f"\n{title}  (groups with 2+ posts)")
            for k, v in sorted(r[key].items(), key=lambda kv: -kv[1]["median_er"]):
                print(f"  {k:10} {v['posts']:>3} posts   median ER {v['median_er']}%   median impressions {v['median_impressions']:,}")
    print("\nA multiple only means something against your own median. Do not compare it to anyone else's.\n")


def main():
    ap = argparse.ArgumentParser(description="Rank LinkedIn posts by engagement.")
    ap.add_argument("csv")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    with open(a.csv, encoding="utf-8-sig", newline="") as fh:
        rd = csv.DictReader(fh)
        rows = list(rd)
        header = rd.fieldnames or []
    cols = map_columns(header)
    if "impressions" not in cols:
        sys.exit(f"No impressions column found. Columns seen: {', '.join(header)}. Rename one to 'impressions'.")
    posts = analyse(rows, cols)
    if len(posts) < 8:
        sys.exit(f"Only {len(posts)} usable posts. Need at least 8 for a median that means anything.")
    r = report(posts)
    print(json.dumps(r, indent=2)) if a.json else render(r)


if __name__ == "__main__":
    main()
