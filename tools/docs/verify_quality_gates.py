"""Exercise real gate tools on disposable fixtures, not a fictional product app."""

import argparse
import hashlib
import importlib.metadata
import json
import os
import shutil
import subprocess
import sys
import tempfile
from datetime import UTC, datetime
from pathlib import Path
from xml.etree import ElementTree

from gate_scope import scope

ROOT = Path(__file__).resolve().parents[2]


def verify():
    records = []

    def run(label, folder, args, expected):
        result = subprocess.run(
            [sys.executable, *args],
            cwd=folder,
            text=True,
            capture_output=True,
            timeout=90,
            check=False,
        )
        records.append(
            {
                "check": label,
                "command": ["python", *args],
                "expected_exit": expected,
                "exit_code": result.returncode,
                "passed": result.returncode == expected,
                "stdout": result.stdout.replace(str(base), "<fixture-root>"),
                "stderr": result.stderr.replace(str(base), "<fixture-root>"),
            }
        )
        print(f"{'PASS' if records[-1]['passed'] else 'FAIL'}: {label}", flush=True)
        return result

    def assert_case(label, result):
        records.append({"check": label, "passed": bool(result)})
        print(f"{'PASS' if result else 'FAIL'}: {label}", flush=True)

    assert_case(
        "documentation helpers do not activate product pytest",
        not scope(["tools/docs/validate_t2.py", "tools/docs/gate_scope.py"])[
            "application"
        ],
    )
    for name in (
        "src/tickets/models.py",
        "services/api/handler.py",
        "tests/test_api.py",
    ):
        assert_case(
            f"tracked source activates pytest: {name}", scope([name])["application"]
        )
    assert_case(
        "nested Django projects are detected",
        scope(["services/api/manage.py"])["manage"] == ["services/api/manage.py"],
    )

    with tempfile.TemporaryDirectory(prefix="team-quality-gates-") as temp:
        base = Path(temp)
        inventory = base / "inventory"
        (inventory / "tools/docs").mkdir(parents=True)
        shutil.copy2(
            ROOT / "tools/docs/gate_scope.py", inventory / "tools/docs/gate_scope.py"
        )
        run(
            "Git inventory failure cannot silently skip gates",
            inventory,
            ["tools/docs/gate_scope.py"],
            1,
        )
        subprocess.run(["git", "init", "-q"], cwd=inventory, check=True)
        (inventory / "services/api").mkdir(parents=True)
        (inventory / "services/api/handler.py").write_text("value = 1\n")
        subprocess.run(["git", "add", "."], cwd=inventory, check=True)
        result = run(
            "real tracked-file inventory succeeds",
            inventory,
            ["tools/docs/gate_scope.py"],
            0,
        )
        assert_case(
            "real inventory activates arbitrary-layout source",
            json.loads(result.stdout)["application"],
        )
        lint = base / "lint"
        lint.mkdir()
        shutil.copy2(ROOT / "ruff.toml", lint / "ruff.toml")
        (lint / "sample.py").write_text("value = 1\n")
        run("Ruff accepts clean source", lint, ["-m", "ruff", "check", "."], 0)
        run(
            "Ruff accepts formatted source",
            lint,
            ["-m", "ruff", "format", "--check", "."],
            0,
        )
        (lint / "sample.py").write_text("import os\n")
        run("Ruff rejects unused import", lint, ["-m", "ruff", "check", "."], 1)
        (lint / "sample.py").write_text("value=1\n")
        run(
            "Ruff rejects bad formatting",
            lint,
            ["-m", "ruff", "format", "--check", "."],
            1,
        )

        docs = base / "documentation"
        docs.mkdir()
        shutil.copytree(ROOT / "docs/t2", docs / "docs/t2")
        shutil.copy2(ROOT / "docs/T2_REQUIREMENTS.md", docs / "docs/T2_REQUIREMENTS.md")
        # Include all tracked documentation so the original links remain meaningful.
        tracked = (
            subprocess.check_output(["git", "ls-files", "-z"], cwd=ROOT)
            .decode()
            .split("\0")
        )
        for name in tracked:
            if name:
                destination = docs / name
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(ROOT / name, destination)
        (docs / "tools/docs").mkdir(parents=True, exist_ok=True)
        shutil.copy2(
            ROOT / "tools/docs/validate_t2.py", docs / "tools/docs/validate_t2.py"
        )
        run(
            "T2 validator accepts valid documentation",
            docs,
            ["tools/docs/validate_t2.py"],
            0,
        )
        (docs / "broken.md").write_text("[broken](missing-file.md)\n")
        run(
            "T2 validator rejects a broken link", docs, ["tools/docs/validate_t2.py"], 1
        )
        (docs / "broken.md").write_text("[valid](docs/T2_REQUIREMENTS.md)\n")
        csv = docs / "docs/t2/traceability.csv"
        csv.write_text(csv.read_text().replace('"FR01"', '"BROKEN"', 1))
        run(
            "T2 validator rejects traceability drift",
            docs,
            ["tools/docs/validate_t2.py"],
            1,
        )

        app = base / "application"
        app.mkdir()
        (app / "sample.py").write_text("def answer():\n    return 42\n")
        pytest = [
            "-m",
            "pytest",
            "-q",
            "--cov=sample",
            "--cov-report=term-missing",
            "--cov-report=xml:coverage.xml",
        ]
        run("pytest rejects application without tests", app, pytest, 5)
        test = app / "test_sample.py"
        test.write_text(
            "from sample import answer\n\ndef test_answer():\n    assert answer() == 42\n"
        )
        run("pytest passes with coverage output", app, pytest, 0)
        report = app / "coverage.xml"
        assert_case(
            "coverage XML exists and is parseable",
            report.exists() and ElementTree.parse(report).getroot().tag == "coverage",
        )
        test.write_text("def test_failure():\n    assert False\n")
        run("pytest rejects a failing test", app, pytest, 1)

        django = base / "django"
        (django / "demoapp/migrations").mkdir(parents=True)
        (django / "demoapp/__init__.py").write_text("")
        (django / "demoapp/migrations/__init__.py").write_text("")
        model = django / "demoapp/models.py"
        model.write_text(
            "from django.db import models\nclass Entry(models.Model):\n    name = models.CharField(max_length=32)\n"
        )
        (django / "settings.py").write_text(
            "SECRET_KEY = 'synthetic-fixture-only'\nINSTALLED_APPS = ['demoapp']\n"
            "DATABASES = {'default': {'ENGINE': 'django.db.backends.sqlite3', 'NAME': ':memory:'}}\n"
            "DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'\n"
        )
        (django / "manage.py").write_text(
            "import os, sys\nos.environ['DJANGO_SETTINGS_MODULE'] = 'settings'\n"
            "from django.core.management import execute_from_command_line\nexecute_from_command_line(sys.argv)\n"
        )
        run(
            "Django system check accepts valid model", django, ["manage.py", "check"], 0
        )
        run(
            "Django detects missing initial migration",
            django,
            ["manage.py", "makemigrations", "--check", "--dry-run"],
            1,
        )
        run(
            "create fixture migration",
            django,
            ["manage.py", "makemigrations", "demoapp"],
            0,
        )
        run(
            "Django accepts committed model/migration agreement",
            django,
            ["manage.py", "makemigrations", "--check", "--dry-run"],
            0,
        )
        (django / "pytest.ini").write_text(
            "[pytest]\nDJANGO_SETTINGS_MODULE = settings\n"
        )
        (django / "test_django.py").write_text(
            "from demoapp.models import Entry\n\ndef test_django_setup():\n"
            "    assert Entry._meta.get_field('name').max_length == 32\n"
        )
        run(
            "pytest-django initializes fixture with coverage",
            django,
            ["-m", "pytest", "-q", "--cov=demoapp", "--cov-report=xml:coverage.xml"],
            0,
        )
        model.write_text(model.read_text().replace("max_length=32", "max_length=64"))
        run(
            "Django rejects migration drift",
            django,
            ["manage.py", "makemigrations", "--check", "--dry-run"],
            1,
        )
        model.write_text(model.read_text().replace("max_length=64", "max_length=-1"))
        run(
            "Django rejects invalid model configuration",
            django,
            ["manage.py", "check"],
            1,
        )

    return records


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = {
        "utc": datetime.now(UTC).isoformat(),
        "revision": subprocess.check_output(
            ["git", "rev-parse", "HEAD"], cwd=ROOT, text=True
        ).strip(),
        "python": sys.version,
        "working_tree_modified": bool(
            subprocess.check_output(["git", "status", "--porcelain"], cwd=ROOT)
        ),
        "verified_file_sha256": {
            name: hashlib.sha256((ROOT / name).read_bytes()).hexdigest()
            for name in (
                "tools/docs/gate_scope.py",
                "tools/docs/verify_quality_gates.py",
                "tools/docs/validate_t2.py",
                ".github/workflows/quality-gates.yml",
                "ruff.toml",
            )
        },
        "tools": {
            name: importlib.metadata.version(name)
            for name in ("ruff", "pytest", "pytest-django", "pytest-cov", "Django")
        },
        "limitation": "Disposable fixtures verify gate behavior, not the unimplemented ticketing application.",
    }
    # Avoid inheriting an unrelated project's pytest/Django configuration.
    for name in ("PYTEST_ADDOPTS", "DJANGO_SETTINGS_MODULE", "COVERAGE_PROCESS_START"):
        os.environ.pop(name, None)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    try:
        report["checks"] = verify()
        report["passed"] = all(check["passed"] for check in report["checks"])
    except (
        OSError,
        ValueError,
        subprocess.SubprocessError,
        ElementTree.ParseError,
    ) as error:
        report.update(passed=False, error=f"{type(error).__name__}: {error}")
    finally:
        args.output.write_text(json.dumps(report, indent=2), encoding="utf-8")
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
