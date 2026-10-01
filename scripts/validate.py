#!/usr/bin/env python3
"""validate.py - repo checks that run in CI and before you open a pull request.

    python3 scripts/validate.py

Checks every skill: frontmatter present, `name` matches the folder, description
is non-empty and under 1,024 characters, every `python3 x.py` it mentions
exists, every JSON file parses, every Python file compiles, and nothing in the
repo looks like a secret or a personal path. Exits 1 on any failure.
Standard library only.
"""
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SKILLS = os.path.join(ROOT, "skills")
fails = []


def fail(msg):
    fails.append(msg)
    print("  FAIL", msg)


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    fm, key = {}, None
    for line in m.group(1).split("\n"):
        kv = re.match(r"^([A-Za-z_-]+):\s*(.*)$", line)
        if kv:
            key = kv.group(1)
            val = kv.group(2).strip()
            fm[key] = "" if val in (">-", ">", "|", "|-") else val
        elif key and line.strip():
            fm[key] = (fm[key] + " " + line.strip()).strip()
    return fm


def check_skill(name):
    d = os.path.join(SKILLS, name)
    md = os.path.join(d, "SKILL.md")
    if not os.path.isfile(md):
        return fail(f"{name}: missing SKILL.md")
    text = open(md, encoding="utf-8").read()
    fm = frontmatter(text)
    if fm is None:
        return fail(f"{name}: no frontmatter")
    if fm.get("name") != name:
        fail(f"{name}: frontmatter name '{fm.get('name')}' does not match folder")
    desc = fm.get("description", "")
    if not desc:
        fail(f"{name}: empty description")
    if len(desc) > 1024:
        fail(f"{name}: description is {len(desc)} chars (limit 1024)")
    if "Use when" not in desc and "Use whenever" not in desc:
        fail(f"{name}: description should say when to use the skill ('Use when ...')")
    for script in set(re.findall(r"python3\s+((?:\.\./[\w-]+/)?[\w/.-]+\.py)", text)):
        if not os.path.isfile(os.path.normpath(os.path.join(d, script))):
            fail(f"{name}: mentions {script} but it does not exist")
    for fn in os.listdir(d):
        p = os.path.join(d, fn)
        if fn.endswith(".json"):
            try:
                json.load(open(p, encoding="utf-8"))
            except Exception as e:
                fail(f"{name}/{fn}: invalid JSON ({e})")
        if fn.endswith(".py"):
            try:
                compile(open(p, encoding="utf-8").read(), p, "exec")
            except SyntaxError as e:
                fail(f"{name}/{fn}: does not compile ({e.msg}, line {e.lineno})")
    lex = os.path.join(d, "lexicons")
    if os.path.isdir(lex):
        for fn in os.listdir(lex):
            try:
                json.load(open(os.path.join(lex, fn), encoding="utf-8"))
            except Exception as e:
                fail(f"{name}/lexicons/{fn}: invalid JSON ({e})")


SECRET = re.compile(r"(sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{30,}|xox[abp]-[A-Za-z0-9-]{10,}|AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]*PRIVATE KEY-----|(?:api[_-]?key|secret|token)\s*[:=]\s*['\"][A-Za-z0-9_\-]{16,}['\"])", re.I)
PERSONAL = re.compile(r"/Users/[A-Za-z0-9._-]+/|C:\\Users\\[A-Za-z0-9._-]+\\")


def scan_repo():
    for base, dirs, files in os.walk(ROOT):
        dirs[:] = [x for x in dirs if x not in (".git", "venv", ".venv", "__pycache__", "node_modules")]
        for fn in files:
            p = os.path.join(base, fn)
            rel = os.path.relpath(p, ROOT)
            if fn == ".env" or fn.endswith((".pem", ".key")):
                fail(f"{rel}: secret-bearing file must not be committed")
                continue
            if rel.replace("\\", "/") == "scripts/validate.py":
                continue
            if not fn.endswith((".md", ".py", ".json", ".yml", ".yaml", ".txt", ".sh", ".toml", "")):
                continue
            try:
                t = open(p, encoding="utf-8").read()
            except (UnicodeDecodeError, OSError):
                continue
            if SECRET.search(t):
                fail(f"{rel}: looks like it contains a secret")
            if PERSONAL.search(t):
                fail(f"{rel}: contains a personal filesystem path")


def main():
    names = sorted(n for n in os.listdir(SKILLS) if os.path.isdir(os.path.join(SKILLS, n)))
    print(f"checking {len(names)} skills")
    for n in names:
        check_skill(n)
    scan_repo()
    print("OK" if not fails else f"{len(fails)} problem(s)")
    sys.exit(1 if fails else 0)


if __name__ == "__main__":
    main()
