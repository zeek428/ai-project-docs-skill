# ai-project-docs-skill

English | [中文](README.zh.md)

`ai-project-docs-skill` is a documentation initializer skill and template repository for AI-native software development. It provides a reusable, scriptable documentation structure that helps teams keep product requirements, technical design, API documentation, test cases, operations notes, and architecture decisions in one shared context.

This repository is not application code. It is a template source used to generate a standardized `docs/` system for other projects.

## What Problem It Solves

- New projects often start without a consistent structure for PRDs, specs, APIs, test cases, and ADRs.
- AI coding assistants need stable entry points and a predictable reading order to understand project context quickly.
- Requirements, design decisions, testing notes, and release records are often scattered across different places.
- Teams want reusable documentation standards that can be installed as a skill instead of copied by hand every time.

## Core Capabilities

| Capability | Description |
|------------|-------------|
| Documentation bootstrap | Generate a complete `docs/` directory with templates, guides, standards, and runbooks |
| Multiple initialization modes | Supports `full`, `minimal`, and `api-only` template sets |
| AI-friendly entry points | Provides `CLAUDE.md`, `README.md`, PRD, spec, API, and test-case reading order |
| Safe reuse | Skips existing files by default, supports preview with `--dry-run`, and overwrites only with `--overwrite` |
| Templates and examples separated | `_template/` files are meant to be copied and filled in; `_examples/` files are references only |

## Quick Start

### Option 1: Use the Initializer Script

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

After reviewing the planned changes, run it again without `--dry-run`:

```bash
python3 scripts/init_docs.py \
  --target /path/to/your-project \
  --mode full \
  --project-name "Your Project" \
  --owner "@team"
```

### Option 2: Install as a Skill

Copy this repository into your Codex or Claude Code skills directory, then follow the skill instructions from your target project.

```bash
mkdir -p ~/.codex/skills/zqf-doc-init
cp -R /path/to/ai-project-docs-skill/* ~/.codex/skills/zqf-doc-init/
```

The current skill entry point is [SKILL.md](SKILL.md). The legacy entry point [zqf-doc-init.md](zqf-doc-init.md) is kept for backward compatibility.

## Initialization Modes

| Mode | Best For | Included Content |
|------|----------|------------------|
| `full` | New projects, medium/large projects, teams that need complete collaboration standards | Core files, PRDs, specs, API docs, test cases, guides, ADRs, runbooks, security and coding standards |
| `minimal` | Small projects, prototypes, early validation | Core files, PRD template, spec template, test-case template, ADR template |
| `api-only` | API services, backend services, interface governance | Core files, API/spec/test-case templates, architecture docs, ADRs, standards |

Common options:

| Option | Description |
|--------|-------------|
| `--target` | Target project root. The script writes to `<target>/docs` |
| `--mode` | Template mode: `full`, `minimal`, or `api-only` |
| `--project-name` | Replaces `{项目名称}` and `{project_name}` placeholders |
| `--owner` | Replaces the `@xxx` owner placeholder |
| `--date` | Replaces `YYYY-MM-DD`; defaults to the current date |
| `--dry-run` | Previews files that would be created, skipped, or overwritten |
| `--overwrite` | Overwrites existing files; disabled by default |
| `--include-examples` | Copies `_examples` reference directories |

## Generated Documentation Structure

```text
docs/
├── CLAUDE.md              # AI entry point: project context and reading order
├── README.md              # Human entry point: documentation navigation
├── VERSIONS.md            # Version documentation index
├── changelog.md           # Change history
├── glossary.md            # Project glossary
│
├── 01-prd/                # Product requirements documents
│   ├── _template/
│   │   ├── prd.md
│   │   ├── prototype.html
│   │   └── prototype/index.html
│   └── _examples/
│       └── prd-example.md
│
├── 02-specs/              # Technical specifications
│   ├── _template/
│   │   ├── spec.md
│   │   ├── api.md
│   │   └── test-case.md
│   ├── _examples/
│   │   ├── spec-example.md
│   │   ├── api-example.md
│   │   └── test-case-example.md
│   └── architecture/
│       ├── system-overview.md
│       └── tech-stack.md
│
├── 03-guides/             # Development, contribution, and local setup guides
├── 04-decisions/          # Architecture Decision Records (ADRs)
├── 05-runbooks/           # Deployment, monitoring, and incident response runbooks
├── 06-standards/          # Testing, coding, and security standards
└── 07-deprecated/         # Deprecated documentation notes
```

## Documentation Workflow

```text
Requirements        Technical Design        Development & QA        Release & Ops
     │                    │                       │                     │
     ▼                    ▼                       ▼                     ▼
   PRD Docs ─────▶ Spec/API Docs ─────▶ Test Cases ─────▶ Changelog/Runbook
     │                    │                       │
     └────────────────────┴───────────────────────┘
                          │
                          ▼
                        Review
```

Recommended reading order:

1. `docs/CLAUDE.md`
2. `docs/01-prd/{feature}/prd.md`
3. `docs/02-specs/{feature}/spec.md`
4. `docs/02-specs/{feature}/api.md`
5. `docs/02-specs/{feature}/test-case.md`
6. `docs/04-decisions/`

## Repository Contents

| Path | Description |
|------|-------------|
| [SKILL.md](SKILL.md) | Current skill entry point and execution rules |
| [scripts/init_docs.py](scripts/init_docs.py) | Documentation initializer script |
| [assets/templates/](assets/templates/) | Template source copied into target projects |
| [01-prd/](01-prd/) | PRD template copy in this repository |
| [02-specs/](02-specs/) | Spec, API, and test-case template copy in this repository |
| [03-guides/](03-guides/) | AI development workflow, contribution, and local development guides |
| [04-decisions/](04-decisions/) | ADR template |
| [05-runbooks/](05-runbooks/) | Operations runbook templates |
| [06-standards/](06-standards/) | Testing, coding, and security standards |

## Usage Recommendations

- Use `--mode full` for new projects so requirements, design, testing, and release records are available from the start.
- Use `--mode minimal` for small projects that only need README, PRD, spec, test-case, and ADR basics.
- Run `--dry-run` first for existing projects to confirm important documents will not be overwritten.
- Do not copy `_examples/` by default; add `--include-examples` only when reference examples are useful.
- Prefer Git tags for documentation versioning. Avoid filename versions such as `prd-v1.0.md`.

## Related Documentation

- [SKILL.md](SKILL.md): Current skill entry point
- [zqf-doc-init.md](zqf-doc-init.md): Backward-compatible legacy entry point
- [VERSIONS.md](VERSIONS.md): Version documentation index
- [changelog.md](changelog.md): Repository change history
- [glossary.md](glossary.md): Glossary

## Maintenance Status

- Current template version: `1.0.0`
- Repository purpose: documentation template and skill source repository
- Default output directory: `docs/` in the target project
- Last updated: 2026-06-30
