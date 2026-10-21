"""Use tracked source to select application gates without a fixed app layout."""

import argparse
import json
import subprocess
import sys
from pathlib import Path, PurePosixPath


def scope(paths):
    application = [
        name
        for name in paths
        if name.endswith(".py") and not name.startswith("tools/docs/")
    ]
    return {
        "application": bool(application),
        "sources": application,
        "manage": [
            name for name in application if PurePosixPath(name).name == "manage.py"
        ],
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--github-output", action="store_true")
    parser.add_argument("--django-checks", action="store_true")
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[2]
    paths = (
        subprocess.check_output(["git", "ls-files", "-z", "--", "*.py"], cwd=root)
        .decode("utf-8")
        .split("\0")
    )
    selected = scope([name for name in paths if name])
    if args.django_checks:
        if not selected["manage"]:
            print(
                "NOT APPLICABLE: no tracked Django manage.py; no Django checks passed."
            )
        for name in selected["manage"]:
            for command in (["check"], ["makemigrations", "--check", "--dry-run"]):
                print(f"Django {name}: {' '.join(command)}", flush=True)
                subprocess.run(
                    [sys.executable, "manage.py", *command],
                    cwd=root / PurePosixPath(name).parent,
                    check=True,
                )
    elif args.github_output:
        print(f"application={str(selected['application']).lower()}")
    else:
        print(json.dumps(selected, indent=2))


if __name__ == "__main__":
    main()
