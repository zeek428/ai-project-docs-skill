# ai-project-docs-skill

[中文](README.md) | English

`ai-project-docs-skill` is a documentation initializer skill and template repository for AI-native software development. It helps teams generate a consistent `docs/` structure for PRDs, technical specs, API docs, test cases, ADRs, runbooks, and project standards.

This repository is not application code. It is a reusable source of documentation templates for other software projects.

## What It Provides

| Capability | Description |
|------------|-------------|
| Documentation bootstrap | Generate a complete `docs/` structure for a target project |
| Multiple modes | Use `full`, `minimal`, or `api-only` depending on project scope |
| AI-friendly context | Provide stable entry points and reading order for coding agents |
| Safe defaults | Skip existing files by default, preview with `--dry-run`, overwrite only with `--overwrite` |
| Templates and examples | Keep reusable templates separate from reference examples |

## Quick Start

```bash
git clone https://github.com/zeek428/ai-project-docs-skill.git
cd ai-project-docs-skill

python3 scripts/init_docs.py \
  --target /path/to/your-project \
  --mode full \
  --project-name "Your Project" \
  --owner "@team" \
  --dry-run
```

Run again without `--dry-run` after checking the output.

## Modes

| Mode | Use When | Included Content |
|------|----------|------------------|
| `full` | New or medium/large projects | Core files, PRD, Spec, API, test cases, guides, ADRs, runbooks, standards |
| `minimal` | Small projects or early prototypes | Core files, PRD template, spec template, test case template, ADR template |
| `api-only` | API/service documentation | Core files, API/spec/test-case templates, architecture docs, ADRs, standards |

## Repository Layout

| Path | Purpose |
|------|---------|
| [SKILL.md](SKILL.md) | Current skill entry point |
| [scripts/init_docs.py](scripts/init_docs.py) | Documentation initializer script |
| [assets/templates/](assets/templates/) | Template source copied into target projects |
| [01-prd/](01-prd/) | PRD templates and examples |
| [02-specs/](02-specs/) | Spec, API, test-case, and architecture templates |
| [03-guides/](03-guides/) | AI development and contribution guides |
| [04-decisions/](04-decisions/) | ADR template |
| [05-runbooks/](05-runbooks/) | Operations runbook templates |
| [06-standards/](06-standards/) | Testing, coding, and security standards |

## Related Docs

- [README.md](README.md): Primary Chinese README
- [SKILL.md](SKILL.md): Skill instructions
- [zqf-doc-init.md](zqf-doc-init.md): Backward-compatible entry point
- [VERSIONS.md](VERSIONS.md): Version documentation index

Last updated: 2026-06-30
