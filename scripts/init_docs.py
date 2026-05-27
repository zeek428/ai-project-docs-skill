#!/usr/bin/env python3
"""Initialize ZQF AI-native project documentation."""

from __future__ import annotations

import argparse
import datetime as dt
import shutil
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE_ROOT = ROOT / "assets" / "templates"

CORE_FILES = [
    "CLAUDE.md",
    "README.md",
    "VERSIONS.md",
    "changelog.md",
    "glossary.md",
]

MODE_PATHS = {
    "full": [
        *CORE_FILES,
        "01-prd",
        "02-specs",
        "03-guides",
        "04-decisions",
        "05-runbooks",
        "06-standards",
        "07-deprecated",
    ],
    "minimal": [
        *CORE_FILES,
        "01-prd/_template/prd.md",
        "01-prd/_template/prototype.html",
        "01-prd/_template/prototype/index.html",
        "02-specs/_template/spec.md",
        "02-specs/_template/test-case.md",
        "04-decisions/0000-template.md",
    ],
    "api-only": [
        *CORE_FILES,
        "02-specs/_template/spec.md",
        "02-specs/_template/api.md",
        "02-specs/_template/test-case.md",
        "02-specs/architecture",
        "04-decisions",
        "06-standards",
    ],
}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Initialize docs/ with the ZQF AI-native documentation template."
    )
    parser.add_argument("--target", required=True, help="Target project root.")
    parser.add_argument(
        "--mode",
        choices=sorted(MODE_PATHS),
        default="full",
        help="Template set to copy.",
    )
    parser.add_argument("--project-name", default="", help="Project name placeholder value.")
    parser.add_argument("--owner", default="", help="Owner placeholder value, for example @team.")
    parser.add_argument(
        "--date",
        default=dt.date.today().isoformat(),
        help="Date placeholder value. Defaults to today.",
    )
    parser.add_argument("--overwrite", action="store_true", help="Overwrite existing files.")
    parser.add_argument("--dry-run", action="store_true", help="Print planned changes only.")
    parser.add_argument(
        "--include-examples",
        action="store_true",
        help="Copy _examples directories. Defaults to excluding examples.",
    )
    return parser.parse_args()


def should_skip(path: Path, include_examples: bool) -> bool:
    if path.name in {".DS_Store", "Thumbs.db"}:
        return True
    return not include_examples and "_examples" in path.parts


def render_text(text: str, project_name: str, owner: str, date: str) -> str:
    replacements = {
        "{项目名称}": project_name,
        "{project_name}": project_name,
        "YYYY-MM-DD": date,
    }
    if owner:
        replacements["@xxx"] = owner

    for old, new in replacements.items():
        if new:
            text = text.replace(old, new)
    return text


def copy_file(
    source: Path,
    destination: Path,
    args: argparse.Namespace,
    created: list[Path],
    skipped: list[Path],
    overwritten: list[Path],
) -> None:
    if destination.exists() and not args.overwrite:
        skipped.append(destination)
        return

    action_list = overwritten if destination.exists() else created
    action_list.append(destination)

    if args.dry_run:
        return

    destination.parent.mkdir(parents=True, exist_ok=True)
    if source.suffix.lower() in {".md", ".html", ".txt", ".json", ".yaml", ".yml"}:
        content = source.read_text(encoding="utf-8")
        content = render_text(content, args.project_name, args.owner, args.date)
        destination.write_text(content, encoding="utf-8")
    else:
        shutil.copy2(source, destination)


def copy_path(
    relative_path: str,
    docs_root: Path,
    args: argparse.Namespace,
    created: list[Path],
    skipped: list[Path],
    overwritten: list[Path],
) -> None:
    source = TEMPLATE_ROOT / relative_path
    if not source.exists():
        raise FileNotFoundError(f"Template path not found: {source}")

    if source.is_file():
        if should_skip(source, args.include_examples):
            return
        copy_file(source, docs_root / relative_path, args, created, skipped, overwritten)
        return

    for child in source.rglob("*"):
        if child.is_dir() or should_skip(child, args.include_examples):
            continue
        relative_child = child.relative_to(TEMPLATE_ROOT)
        copy_file(child, docs_root / relative_child, args, created, skipped, overwritten)


def write_template_version(docs_root: Path, args: argparse.Namespace) -> None:
    destination = docs_root / ".template-version"
    if destination.exists() and not args.overwrite:
        return

    content = "\n".join(
        [
            "---",
            "template: zqf-doc-init",
            "version: 1.0.0",
            f"initialized_at: {args.date}",
            f"mode: {args.mode}",
            f"project: {args.project_name or '{project_name}'}",
            "---",
            "",
        ]
    )
    if not args.dry_run:
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(content, encoding="utf-8")


def main() -> int:
    args = parse_args()
    if not TEMPLATE_ROOT.exists():
        raise SystemExit(f"Template root not found: {TEMPLATE_ROOT}")

    target_root = Path(args.target).expanduser().resolve()
    docs_root = target_root / "docs"

    created: list[Path] = []
    skipped: list[Path] = []
    overwritten: list[Path] = []

    for relative_path in MODE_PATHS[args.mode]:
        copy_path(relative_path, docs_root, args, created, skipped, overwritten)
    write_template_version(docs_root, args)

    prefix = "DRY RUN " if args.dry_run else ""
    print(f"{prefix}docs target: {docs_root}")
    print(f"{prefix}mode: {args.mode}")
    print(f"{prefix}created: {len(created)}")
    print(f"{prefix}overwritten: {len(overwritten)}")
    print(f"{prefix}skipped: {len(skipped)}")

    for label, paths in (
        ("created", created),
        ("overwritten", overwritten),
        ("skipped", skipped),
    ):
        if paths:
            print(f"\n{label}:")
            for path in paths:
                print(f"- {path}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
