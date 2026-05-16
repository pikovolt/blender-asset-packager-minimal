from __future__ import annotations

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
SCAN_DIR = ROOT / "src" / "assetpack"
FORBIDDEN = [
    "import socket",
    "import subprocess",
    "shutil.rmtree",
    "os.remove",
    "os.unlink",
    "commandPort",
    "cmds.file(save=True",
]


def main() -> int:
    failures: list[str] = []
    for path in sorted(SCAN_DIR.rglob("*.py")):
        text = path.read_text(encoding="utf-8")
        for token in FORBIDDEN:
            if token in text:
                failures.append(f"{path.relative_to(ROOT)} contains forbidden token: {token}")

    if failures:
        for failure in failures:
            print(f"ERROR: {failure}", file=sys.stderr)
        return 1

    print("forbidden-token check OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
