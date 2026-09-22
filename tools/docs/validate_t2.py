#!/usr/bin/env python3
"""Check T2 documentation structure; not an application or semantic acceptance test."""
import csv
import json
import re
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[2]
data = json.loads((root / "docs/t2/requirements-register.json").read_text(encoding="utf-8"))
spec_path = root / "docs/T2_REQUIREMENTS.md"
spec = spec_path.read_text(encoding="utf-8")
errors = []

def check(condition, message):
    if not condition:
        errors.append(message)

def index(items, label):
    result = {x["id"]: x for x in items}
    check(len(result) == len(items), f"Duplicate {label} IDs")
    return result

sources = index(data["sources"], "source")
requirements = index(data["requirements"], "requirement")
stories = index(data["stories"], "story")
epics = index(data["epics"], "epic")
membership = {}
for e in epics.values():
    for sid in e["stories"]:
        check(sid in stories, f"{e['id']} unknown story {sid}")
        membership.setdefault(sid, []).append(e["id"])

for r in requirements.values():
    check(bool(r["origins"]) and bool(r["stories"]), f"{r['id']} missing links")
    check(len(r["origins"]) == len(set(r["origins"])), f"{r['id']} duplicate source")
    check(len(r["stories"]) == len(set(r["stories"])), f"{r['id']} duplicate story")
    for source in r["origins"]:
        check(source in sources, f"{r['id']} unknown source {source}")
    for sid in r["stories"]:
        check(sid in stories, f"{r['id']} unknown story {sid}")
    check(r["shall"] in spec, f"{r['id']} text differs from specification")
    check(r["verification"] in spec, f"{r['id']} missing verification")
    marker = f'| [{r["id"]}](#{r["id"].lower()}) |'
    check(marker in spec, f"{r['id']} missing forward trace row")

for sid, source in sources.items():
    check(any(sid in r["origins"] for r in requirements.values()), f"Uncovered source {sid}")
    check(f'| [{sid}](#{sid.lower()}) |' in spec, f"{sid} missing reverse table row")

for sid, story in stories.items():
    check(len(membership.get(sid, [])) == 1, f"{sid} must belong to exactly one epic")
    check(any(sid in r["stories"] for r in requirements.values()), f"Orphan story {sid}")
    check(len(story["criteria"]) > 0, f"{sid} missing criteria")
    check(story["story"] in spec, f"{sid} text mismatch")
    for i, criterion in enumerate(story["criteria"], 1):
        check(criterion in spec and f"{sid}-AC{i}" in spec, f"{sid}-AC{i} mismatch")
    check(f'| [{sid}](#{sid.lower()}) |' in spec, f"{sid} missing reverse row")

with (root / "docs/t2/traceability.csv").open(encoding="utf-8", newline="") as f:
    rows = list(csv.DictReader(f))
expected = {(r["id"], o, s) for r in requirements.values()
            for o in r["origins"] for s in r["stories"]}
actual = {(r["requirement_id"], r["charter_source"], r["story_id"]) for r in rows}
check(actual == expected, "CSV trace relationships differ from register")
check(len(rows) == len(actual), "Duplicate CSV relationships")
for row in rows:
    rid, sid, source = row["requirement_id"], row["story_id"], row["charter_source"]
    if rid in requirements and sid in stories and source in sources:
        check(row["epic_id"] in membership.get(sid, []), f"CSV epic mismatch: {sid}")
        check(row["charter_locator"] == sources[source]["locator"], f"CSV locator mismatch: {source}")
        check(row["verification"] == requirements[rid]["verification"], f"CSV verification mismatch: {rid}")

# Check every Markdown relative-file link and explicit same-document anchor.
for path in root.rglob("*.md"):
    if ".git" in path.parts:
        continue
    text = path.read_text(encoding="utf-8")
    explicit = set(re.findall(r'<a id="([^"]+)"></a>', text))
    for target in re.findall(r'\]\(([^)]+)\)', text):
        if target.startswith(("https://", "http://", "mailto:")):
            continue
        if target.startswith("#"):
            check(target[1:] in explicit, f"{path.name}: missing explicit anchor {target}")
        else:
            filename = target.split("#", 1)[0]
            check((path.parent / filename).exists(), f"{path.name}: missing link {target}")

check(spec.count('<a id=') == len(set(re.findall(r'<a id="([^"]+)"', spec))),
      "Duplicate anchors in specification")
check(sum(1 for r in requirements if r.startswith("FR")) == 22, "Unexpected FR count")
check(sum(1 for r in requirements if r.startswith("NFR")) == 10, "Unexpected NFR count")
check(len(stories) == 20 and len(epics) == 6, "Unexpected story/epic count")
if errors:
    print("FAIL")
    print("\n".join(errors))
    sys.exit(1)
print(f"PASS: {len(sources)} charter sources; {len(requirements)} requirements; "
      f"{len(stories)} stories; {len(epics)} epics; "
      f"{sum(len(s['criteria']) for s in stories.values())} acceptance criteria; "
      f"{len(rows)} CSV trace rows.")
print("PASS: no orphan sources, requirements, or stories; text/CSV links and local anchors agree.")
print("LIMIT: structural documentation validation only; human semantic audit and product testing remain pending.")
