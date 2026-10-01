"""Tests for the helper scripts. Run: python3 -m unittest discover -s tests -v"""
import csv
import importlib.util
import os
import subprocess
import sys
import tempfile
import unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load(rel):
    path = os.path.join(ROOT, rel)
    spec = importlib.util.spec_from_file_location(os.path.basename(rel)[:-3], path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


postlint = load("skills/li-postlint/postlint.py")
jobpost = load("skills/li-job-post/jobpost_lint.py")
outreach = load("skills/li-candidate-outreach/outreach_lint.py")
voiceprint = load("skills/li-voice/voiceprint.py")
metrics = load("skills/li-metrics/analyze.py")


def rules(result):
    return {f["rule"] for f in result["findings"]}


class PostLint(unittest.TestCase):
    def test_flags_mechanical_problems(self):
        text = ("I'm thrilled to announce that we shipped the thing and I could not be prouder of everyone who "
                "worked on it over the last three years of effort\nTwo.\n\nSee https://x.com — now.\n\nComment YES!\n\n#a #b #c #d")
        r = rules(postlint.lint(text))
        for expected in ("hook-truncates", "cliche-opener", "link-in-body", "hashtag-wall", "engagement-bait", "em-dash"):
            self.assertIn(expected, r)

    def test_clean_post_scores_high(self):
        text = "We cut onboarding from 14 days to 3.\n\nHere is the one change.\n\n" + ("Short line of real content here.\n\n" * 12) + "What would you cut first?"
        res = postlint.lint(text)
        self.assertGreaterEqual(res["score"], 90, res["findings"])

    def test_invisible_char_is_error(self):
        res = postlint.lint("Hello​ world\n\nbody")
        self.assertIn("invisible-chars", rules(res))


class JobPostLint(unittest.TestCase):
    def test_missing_pay_and_location(self):
        r = rules(jobpost.lint("We need a rockstar ninja. Competitive salary. " * 10))
        self.assertIn("no-pay", r)
        self.assertIn("no-location", r)
        self.assertIn("masculine-coded", r)

    def test_good_post_has_no_errors(self):
        text = ("You will own onboarding for 200 customers.\n\nWe are hybrid in London, 2 days in office. Salary £85,000-£105,000 plus equity and pension.\n"
                "We welcome applications from everyone and will make reasonable adjustments.\n\n" + "You will ship and measure outcomes with your team. " * 30)
        res = jobpost.lint(text)
        self.assertFalse([f for f in res["findings"] if f["severity"] == "error"], res["findings"])


class OutreachLint(unittest.TestCase):
    def test_note_over_limit(self):
        res = outreach.lint_block("note", "x" * 250, 200)
        self.assertIn("over-limit", rules(res))

    def test_filler_and_early_link(self):
        res = outreach.lint_block("first", "I hope this finds you well. https://calendly.com/me", 200)
        self.assertTrue({"filler", "early-link"} <= rules(res))

    def test_specific_message_is_clean_enough(self):
        msg = ("Sam, your talk on cutting onboarding from 14 days to 3 is exactly the problem our platform team has. "
               "We are hiring a senior engineer to own it (£90-110k, hybrid London). Worth 15 minutes this week?")
        self.assertGreaterEqual(outreach.lint_block("first", msg, 200)["score"], 90)


class Voiceprint(unittest.TestCase):
    def test_measures_and_requires_three_posts(self):
        posts = ["I don't post often. We hired 4 engineers in 30 days.\n\nWhat would you change?"] * 4
        m = voiceprint.analyse(posts)
        self.assertEqual(m["posts"], 4)
        self.assertGreater(m["contractions_per_100_words"], 0)
        self.assertEqual(m["posts_ending_in_question"], "4/4")

    def test_split_posts(self):
        self.assertEqual(len(voiceprint.split_posts(["a\n---\nb\n---\nc"])), 3)


class Metrics(unittest.TestCase):
    def test_ranks_outlier_first(self):
        rows = []
        for i in range(10):
            rows.append({"Date": f"2026-08-{i+1:02d}", "Post": f"p{i}", "Impressions": "1000", "Reactions": "20", "Comments": "2", "Reposts": "1", "Clicks": "5"})
        rows.append({"Date": "2026-08-20", "Post": "viral", "Impressions": "20000", "Reactions": "400", "Comments": "80", "Reposts": "30", "Clicks": "50"})
        cols = metrics.map_columns(list(rows[0].keys()))
        rep = metrics.report(metrics.analyse(rows, cols))
        self.assertEqual(rep["top"][0]["text"], "viral")
        self.assertEqual(rep["posts"], 11)

    def test_cli_refuses_small_sample(self):
        with tempfile.TemporaryDirectory() as d:
            p = os.path.join(d, "m.csv")
            with open(p, "w", newline="") as fh:
                w = csv.writer(fh)
                w.writerow(["Impressions", "Reactions"])
                w.writerow(["100", "5"])
            r = subprocess.run([sys.executable, os.path.join(ROOT, "skills/li-metrics/analyze.py"), p], capture_output=True, text=True)
            self.assertNotEqual(r.returncode, 0)
            self.assertIn("at least 8", r.stderr)


class Humanizer(unittest.TestCase):
    def test_extra_lexicon_merges(self):
        hz = load("skills/li-human/humanize.py")
        base = os.path.join(ROOT, "skills/li-human/slop.json")
        extra = os.path.join(ROOT, "skills/li-human/lexicons/recruitment.json")
        lex = hz.load_lexicon(base, [extra])
        finds = {w["find"] for w in lex["words"]}
        self.assertIn("rockstar", finds)
        out, _ = hz.humanize("We want a rockstar.", lex)
        self.assertNotIn("rockstar", out.lower())


class Repo(unittest.TestCase):
    def test_validate_passes(self):
        r = subprocess.run([sys.executable, os.path.join(ROOT, "scripts/validate.py")], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stdout + r.stderr)


if __name__ == "__main__":
    unittest.main()
