# IT Project Docs for AI Coding

[中文文档](README.zh.md) | English

A standardized documentation template repository for AI-native software development. This repository provides a comprehensive documentation structure that can be applied to any software project to ensure consistency and completeness.

## Overview

This is **not** application code—it's a documentation template system designed to:

- Standardize documentation structure across projects and teams
- Provide ready-to-use templates for PRD, Technical Specs, API docs, and Test Cases
- Support the `/zqf-doc-init` skill for automated documentation initialization
- Enable AI assistants to understand project context quickly

## Quick Start

### Skill Installation (First-time Setup)

If using Claude Code, install the skill first:

```bash
# 1. Clone repository
git clone http://192.168.2.120:81/ai-skills/it-project-docs-for-ai-coding.git /tmp/doc-template

# 2. Create skill folder and install
mkdir -p ~/.claude/skills/zqf-doc-init
cp -R /tmp/doc-template/* ~/.claude/skills/zqf-doc-init/

# 3. Restart Claude Code
```

After installation, `/zqf-doc-init` command becomes available. See [zqf-doc-init.md](zqf-doc-init.md) for details.

### Option 1: Using the Skill (Recommended)

If you have Claude Code configured:

```bash
# Navigate to your target project
cd /path/to/your-project

# Initialize full documentation structure
/zqf-doc-init --full

# Or choose minimal documentation
/zqf-doc-init --minimal

# Or API-only documentation
/zqf-doc-init --api-only
```

### Option 2: Manual Copy

```bash
# Copy the template directory
mkdir -p /path/to/your-project/docs
cp -R assets/templates/* /path/to/your-project/docs/

# Remove template placeholders, keep structure
cd /path/to/your-project/docs
rm -rf 01-prd/_examples 02-specs/_examples
```

## Documentation Structure

```
docs/
├── CLAUDE.md              # AI entry point - project context for AI
├── README.md              # Human entry point - navigation hub
├── VERSIONS.md            # Version documentation index
├── changelog.md           # Version change history
├── glossary.md            # Project terminology
│
├── 01-prd/                # Product Requirements Documents
│   ├── _template/
│   │   ├── prd.md              # PRD template (copy to use)
│   │   ├── prototype.html      # Backward-compatible prototype placeholder
│   │   └── prototype/
│   │       └── index.html      # Preferred prototype entry point
│   ├── _examples/
│   │   └── prd-example.md # Complete PRD example (reference only)
│   └── {feature}/
│       ├── prd.md              # Requirements document
│       └── prototype/
│           └── index.html      # High-fidelity prototype
│
├── 02-specs/              # Technical Specifications
│   ├── _template/
│   │   ├── spec.md        # Technical design template
│   │   ├── api.md         # API documentation template
│   │   └── test-case.md   # Test case template
│   ├── _examples/
│   │   ├── spec-example.md      # Complete spec example
│   │   ├── api-example.md       # Complete API doc example
│   │   └── test-case-example.md # Complete test case example
│   ├── architecture/      # Architecture documentation
│   │   ├── system-overview.md
│   │   └── tech-stack.md
│   └── {feature}/
│       ├── spec.md        # Technical design
│       ├── api.md         # API documentation
│       └── test-case.md   # Test cases
│
├── 03-guides/             # User guides
│   ├── ai-development-guide.md    # AI development workflow guide
│   ├── ai-development-workflow.md # AI development flow diagrams
│   ├── getting-started.md
│   ├── contributing.md
│   └── local-development.md
│
├── 04-decisions/          # Architecture Decision Records (ADR)
├── 05-runbooks/           # Operations runbooks
└── 06-standards/          # Project standards
    ├── testing.md
    ├── coding-standards.md
    └── security.md
```

## Template Contents

### Core Templates

| Template | Purpose | Required Sections |
|----------|---------|-------------------|
| `01-prd/_template/prd.md` | Product Requirements | User stories, acceptance criteria, scope |
| `02-specs/_template/spec.md` | Technical Design | Design decisions, test strategy, risks |
| `02-specs/_template/api.md` | API Documentation | Endpoints, request/response schemas |
| `02-specs/_template/test-case.md` | Test Cases | Preconditions, steps, expected results |
| `04-decisions/0000-template.md` | Architecture Decision Record | Alternatives, decision, consequences |

### Standards

| Document | Content |
|----------|---------|
| `06-standards/testing.md` | Test strategy, naming conventions, coverage requirements |
| `06-standards/coding-standards.md` | Code style and quality standards |
| `06-standards/security.md` | Security guidelines and checklists |

## Usage Scenarios

| Scenario | Recommended Approach |
|----------|---------------------|
| New project startup | `/zqf-doc-init --full` |
| Small project (< 3 months) | `/zqf-doc-init --minimal` |
| API-only project | `/zqf-doc-init --api-only` |
| Existing project standardization | Selective copy of needed templates |

## Customization

After applying templates, update these placeholders:

- `{项目名称}` → Your project name
- `{feature}` → Feature folder names (use kebab-case)
- `YYYY-MM-DD` → Current date
- `@xxx` → Actual owner/team
- Fill in empty sections with project-specific content

## Documentation Workflow

```
Requirement Phase        Development Phase        Testing Phase        Release Phase
       │                       │                      │                    │
       ▼                       ▼                      ▼                    ▼
   PRD Document  ──────▶  Spec Document  ──────▶  Test Cases  ──────▶  Update Changelog
       │                       │                      │
       └───────────────────────┴──────────────────────┘
                               │
                               ▼
                         Review Approved
```

## Version Management

### Recommended: Git Tags (Default)

**Do NOT** include version numbers in filenames or directory names (e.g., `prd-v1.0.md`). Reasons:

| Issue | Explanation |
|-------|-------------|
| Redundant | Git is already a version control system |
| Cluttered | Multiple version files crowd the directory |
| Out of sync | Document versions may not match code Tags |

**Recommended approach**:

```bash
# Tag on release (syncs code and docs)
git tag -a v1.0.0 -m "Release v1.0.0"
git push origin v1.0.0

# View historical docs
git show v1.0.0:docs/01-prd/user-management/prd.md

# Checkout historical version
git checkout v1.0.0
```

### Alternative: Directory Archiving (Major Versions)

For **major version upgrades** (e.g., v1 → v2 architecture change), archive historical docs:

```
docs/
├── v1.0/                  # Archived version (major release)
│   ├── 01-prd/
│   └── 02-specs/
├── v2.0/                  # Archived version (major release)
├── 01-prd/                # Current version (always latest)
└── 02-specs/              # Current version (always latest)
```

### Version Strategy Comparison

| Approach | Use Case | Pros | Cons |
|----------|----------|------|------|
| Git Tag (Recommended) | All projects | Code-docs synced, no redundancy | Need to checkout to view history |
| Directory Archiving | Major upgrades | History visible side-by-side | Storage overhead |
| Filename Version | ❌ Not recommended | - | Cluttered, prone to sync issues |

See [VERSIONS.md](VERSIONS.md) for details.

## Related Documentation

- [CLAUDE.md](CLAUDE.md) - AI entry point and context
- [VERSIONS.md](VERSIONS.md) - Version documentation index

## Contributing

See [03-guides/contributing.md](03-guides/contributing.md) for contribution guidelines.

## License

<!-- Add your license information here -->

---

Last Updated: YYYY-MM-DD
