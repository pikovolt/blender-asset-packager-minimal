from __future__ import annotations

import argparse
import sys
from pathlib import Path

from .manifest import build_export_plan, load_json, scan_tree, validate_manifest, write_json


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="assetpack")
    sub = parser.add_subparsers(dest="command", required=True)

    scan = sub.add_parser("scan", help="scan an asset tree and write a manifest")
    scan.add_argument("root")
    scan.add_argument("--out", required=True)

    validate = sub.add_parser("validate", help="validate a manifest")
    validate.add_argument("manifest")

    plan = sub.add_parser("plan-export", help="create a dry-run export plan")
    plan.add_argument("manifest")
    plan.add_argument("--out-root", required=True)
    plan.add_argument("--dry-run", action="store_true", required=True)
    plan.add_argument("--out")

    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    try:
        if args.command == "scan":
            manifest = scan_tree(args.root)
            write_json(manifest, args.out)
            print(f"wrote manifest: {Path(args.out)}")
            return 0

        if args.command == "validate":
            manifest = load_json(args.manifest)
            errors = validate_manifest(manifest)
            if errors:
                for error in errors:
                    print(f"ERROR: {error}", file=sys.stderr)
                return 1
            print("OK")
            return 0

        if args.command == "plan-export":
            manifest = load_json(args.manifest)
            plan = build_export_plan(manifest, args.out_root)
            if args.out:
                write_json(plan, args.out)
                print(f"wrote export plan: {Path(args.out)}")
            else:
                import json
                print(json.dumps(plan, indent=2, ensure_ascii=False, sort_keys=True))
            return 0

    except Exception as exc:  # fail closed for CLI use
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2

    print(f"ERROR: unknown command: {args.command}", file=sys.stderr)
    return 2
