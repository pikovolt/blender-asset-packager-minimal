from __future__ import annotations

import argparse
import os
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parents[1]


def run(command: list[str]) -> int:
    print("+ " + " ".join(command))
    env = os.environ.copy()
    src = str(ROOT / "src")
    env["PYTHONPATH"] = src + os.pathsep + env.get("PYTHONPATH", "")
    return subprocess.call(command, cwd=ROOT, env=env)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", default="fast", choices=["fast", "export-safe"])
    args = parser.parse_args()

    commands = [
        [sys.executable, "scripts/check_boundaries.py"],
        [sys.executable, "-m", "pytest", "-q"],
    ]

    if args.profile == "export-safe":
        print("export-safe currently aliases fast in this TODO sample; strengthen it when safe-copy is implemented")

    for command in commands:
        code = run(command)
        if code != 0:
            return code
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
