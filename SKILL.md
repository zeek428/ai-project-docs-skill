---
name: zqf-doc-init
description: Initialize or standardize software project documentation using the ZQF AI-native docs template. Use when the user asks to create docs structure, initialize PRD/spec/API/test-case templates, add AI coding project docs, or run /zqf-doc-init for a new or existing project.
---

# ZQF Documentation Initializer

Initialize a standardized documentation structure for AI-native software projects.

## Quick Start

Use the bundled script whenever possible:

```bash
python scripts/init_docs.py --target /path/to/project --mode full
```

Modes:

| Mode | Use When | Included Files |
|------|----------|----------------|
| `full` | New or medium/large projects | All templates, guides, standards, runbooks, ADRs |
| `minimal` | Small projects or early prototypes | Core files, PRD template, spec template, test-case template |
| `api-only` | API/service documentation | Core files, API/spec/test-case templates, standards |

## Workflow

1. Confirm the target project directory.
2. Inspect whether `docs/` already exists.
3. If existing docs are present, prefer `--dry-run` first or ask before overwriting.
4. Run `scripts/init_docs.py` with the selected mode.
5. Replace placeholders with project-specific values when known.
6. Report created, skipped, and updated files.

## Script Options

```bash
python scripts/init_docs.py \
  --target /path/to/project \
  --mode full \
  --project-name "Project Name" \
  --owner "@team" \
  --dry-run
```

Options:

- `--target`: Target project root. The script writes into `<target>/docs`.
- `--mode`: `full`, `minimal`, or `api-only`. Defaults to `full`.
- `--project-name`: Replaces `{项目名称}` and `{project_name}`.
- `--owner`: Replaces `@xxx` and bare owner placeholders where safe.
- `--date`: Replaces `YYYY-MM-DD`. Defaults to today.
- `--overwrite`: Replace existing files. Default is to skip existing files.
- `--dry-run`: Show planned changes without writing.
- `--include-examples`: Copy `_examples` directories. Defaults to false.

## Template Resources

Templates live in `assets/templates/`.

Core paths:

- `CLAUDE.md`: AI entry point for project context.
- `README.md`: Human navigation entry point.
- `01-prd/_template/prd.md`: PRD template.
- `01-prd/_template/prototype.html`: Backward-compatible single-file prototype placeholder.
- `01-prd/_template/prototype/index.html`: Preferred prototype folder entry point.
- `02-specs/_template/spec.md`: Technical spec template.
- `02-specs/_template/api.md`: API documentation template.
- `02-specs/_template/test-case.md`: Test case template.
- `04-decisions/0000-template.md`: ADR template.

## Documentation Rules

- Keep generated documentation under `docs/`.
- Do not overwrite existing docs unless the user explicitly approves or passes `--overwrite`.
- Do not copy `_examples` unless the user asks for examples.
- Keep feature folders in kebab-case, for example `01-prd/user-management/prd.md`.
- Put generated prototypes under `01-prd/{feature}/prototype/`, with `index.html` as the entry point.
- Every PRD acceptance criterion should map to at least one test case.
- Every technical spec should include design decisions, test strategy, risks, rollout, and rollback notes.
- Prefer Git tags for version history; do not create filename versions such as `prd-v1.0.md`.

## Expected Reading Order For AI Coding

1. `docs/CLAUDE.md`
2. `docs/01-prd/{feature}/prd.md`
3. `docs/02-specs/{feature}/spec.md`
4. `docs/02-specs/{feature}/api.md`, when APIs exist
5. `docs/02-specs/{feature}/test-case.md`
6. `docs/04-decisions/`
