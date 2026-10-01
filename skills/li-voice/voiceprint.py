#!/usr/bin/env python3
"""voiceprint.py - measure how you actually write, so voice.md is evidence not guesswork.

    python3 voiceprint.py my-posts.txt          # posts separated by a line of ---
    python3 voiceprint.py post1.txt post2.txt post3.txt
    python3 voiceprint.py my-posts.txt --json

Reads three or more of your own posts and reports sentence rhythm, contraction
and emoji habits, how you open and close, the words you lean on, and phrases you
repeat. The numbers seed the "What I sound like" section of templates/voice.md.
Standard library only. Nothing leaves your machine.
"""
import argparse
import json
import re
import statistics as st
import sys
from collections import Counter

STOP = set("""a about after all also am an and any are as at be because been but by can could did do does for from had has have he her
his how i if in into is it its just like me more most my no not of on one or our out over so some than that the their them then
there these they this to up us was we were what when which who will with would you your i'm i've i'd i'll it's don't can't
didn't won't that's there's here's""".split())
EMOJI = re.compile("[\U0001F300-\U0001FAFF☀-➿]")
CONTRACTION = re.compile(r"\b\w+(?:'(?:t|s|re|ve|ll|d|m))\b", re.I)


def split_posts(texts):
    posts = []
    for t in texts:
        parts = re.split(r"^\s*---+\s*$", t, flags=re.M)
        posts += [p.strip() for p in parts if p.strip()]
    return posts


def sentences(p):
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+|\n+", p) if len(s.split()) > 0]


def analyse(posts):
    all_s, openers, closers = [], Counter(), []
    words_all, tri = [], Counter()
    contr = emoji = i_count = q_end = hashtags = dashes = ellipsis = 0
    word_total = 0
    paras, lens = [], []
    for p in posts:
        ss = sentences(p)
        all_s += ss
        w = re.findall(r"[A-Za-z0-9']+", p.lower())
        word_total += len(w)
        words_all += [x for x in w if x not in STOP and len(x) > 2 and not x.isdigit()]
        for i in range(len(w) - 2):
            tri[" ".join(w[i:i + 3])] += 1
        contr += len(CONTRACTION.findall(p))
        emoji += len(EMOJI.findall(p))
        i_count += len(re.findall(r"\bI\b|\bI'", p))
        hashtags += len(re.findall(r"(?<!\w)#\w+", p))
        dashes += p.count("—")
        ellipsis += p.count("...")
        first = p.split("\n")[0].split()
        if first:
            openers[" ".join(first[:2]).lower()] += 1
        last = [l for l in p.split("\n") if l.strip() and not l.strip().startswith("#")]
        if last:
            closers.append(last[-1].strip())
            q_end += last[-1].strip().endswith("?")
        paras.append(len([x for x in re.split(r"\n\s*\n", p) if x.strip()]))
        lens.append(len(p))
    sl = [len(s.split()) for s in all_s] or [0]
    top = [w for w, c in Counter(words_all).most_common(40) if c >= 2][:15]
    repeated = [f"{p} (x{c})" for p, c in tri.most_common(40) if c >= 2 and not all(x in STOP for x in p.split())][:8]
    n = len(posts)
    return {
        "posts": n,
        "words_per_post": round(word_total / n),
        "chars_per_post": round(st.mean(lens)),
        "paragraphs_per_post": round(st.mean(paras), 1),
        "sentence_words_mean": round(st.mean(sl), 1),
        "sentence_words_stdev": round(st.pstdev(sl), 1),
        "short_sentence_share": round(sum(1 for x in sl if x <= 6) / len(sl), 2),
        "long_sentence_share": round(sum(1 for x in sl if x >= 22) / len(sl), 2),
        "contractions_per_100_words": round(100 * contr / max(word_total, 1), 1),
        "first_person_per_100_words": round(100 * i_count / max(word_total, 1), 1),
        "emoji_per_post": round(emoji / n, 1),
        "hashtags_per_post": round(hashtags / n, 1),
        "em_dashes_per_post": round(dashes / n, 1),
        "ellipses_per_post": round(ellipsis / n, 1),
        "posts_ending_in_question": f"{q_end}/{n}",
        "common_openers": [f"{o} (x{c})" for o, c in openers.most_common(5) if c >= 1],
        "words_you_lean_on": top,
        "phrases_you_repeat": repeated,
        "sample_closers": closers[:3],
    }


def draft(m):
    rhythm = "short and punchy" if m["sentence_words_mean"] < 11 else ("long and considered" if m["sentence_words_mean"] > 18 else "mixed")
    contr = "yes, almost always" if m["contractions_per_100_words"] > 2.5 else ("sometimes" if m["contractions_per_100_words"] > 0.8 else "rarely")
    emo = "never" if m["emoji_per_post"] < 0.2 else ("one, rarely" if m["emoji_per_post"] < 1.5 else "freely")
    return f"""## What I sound like (measured from {m['posts']} posts)

- **Sentence length:** {rhythm} (mean {m['sentence_words_mean']} words, spread {m['sentence_words_stdev']}; {int(m['short_sentence_share']*100)}% are 6 words or fewer)
- **Contractions:** {contr} ({m['contractions_per_100_words']} per 100 words)
- **Emoji:** {emo} ({m['emoji_per_post']} per post)
- **Post size:** about {m['words_per_post']} words in {m['paragraphs_per_post']} paragraphs
- **How I open:** {', '.join(m['common_openers']) or 'varied'}
- **Words I actually use:** {', '.join(m['words_you_lean_on']) or '(not enough posts)'}
- **Phrases I repeat:** {', '.join(m['phrases_you_repeat']) or 'none found'}
- **Em dashes:** {m['em_dashes_per_post']} per post. Hashtags: {m['hashtags_per_post']} per post.
- **Ends on a question:** {m['posts_ending_in_question']} posts
"""


def main():
    ap = argparse.ArgumentParser(description="Measure your writing voice from your own posts.")
    ap.add_argument("inputs", nargs="+", help="files, or - for stdin; posts separated by a line of ---")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    texts = [sys.stdin.read() if p == "-" else open(p, encoding="utf-8").read() for p in a.inputs]
    posts = split_posts(texts)
    if len(posts) < 3:
        sys.exit(f"Found {len(posts)} post(s). Give me at least 3 of your own, ideally 8-10, separated by a line of ---.")
    m = analyse(posts)
    if len(posts) < 6:
        m["warning"] = "Fewer than 6 posts: treat these numbers as a sketch, not a fingerprint."
    print(json.dumps(m, indent=2)) if a.json else print(("\n! " + m["warning"] + "\n" if "warning" in m else "") + "\n" + draft(m))


if __name__ == "__main__":
    main()
