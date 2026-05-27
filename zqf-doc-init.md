---
name: zqf-doc-init
description: Initialize documentation structure for new or existing projects using the AI-native development template with PRD, Specs, API docs, and Test Cases
version: 1.0.0
status: deprecated-entrypoint
---

# ZQF Documentation Initializer

> This file is kept for backward compatibility. The canonical skill entry point is now [SKILL.md](SKILL.md), with templates in `assets/templates/` and the initializer script at `scripts/init_docs.py`.

Initialize a standardized documentation structure for AI-native development projects.

## Installation

### Quick Install

```bash
# Clone and install skill
git clone http://192.168.2.120:81/ai-skills/it-project-docs-for-ai-coding.git /tmp/doc-template

# Create skill folder and copy skill file
mkdir -p ~/.claude/skills/zqf-doc-init
cp -R /tmp/doc-template/* ~/.claude/skills/zqf-doc-init/
```

### Verify Installation

```bash
ls ~/.claude/skills/zqf-doc-init/SKILL.md
```

After installation, restart Claude Code and use `/zqf-doc-init`.

## Usage

```bash
/zqf-doc-init [options]

Options:
  --full       Complete documentation structure (default)
  --minimal    Minimal documentation set (README + PRD + Spec)
  --api-only   API documentation only
```

## Execution Steps

### Step 1: Detect Project Context

1. Check if target directory has an existing `docs/` folder
2. Identify project type (frontend/backend/fullstack)
3. Ask user for confirmation if docs already exist

### Step 2: Select Template

| Project Type | Template | Files |
|--------------|----------|-------|
| Full project | `--full` | All files |
| Small project | `--minimal` | README, CLAUDE.md, PRD template, Spec template |
| API project | `--api-only` | API documentation focused |

### Step 3: Create Directory Structure

```bash
mkdir -p docs/{01-prd/_template,02-specs/_template,02-specs/architecture,03-guides,04-decisions,05-runbooks,06-standards,07-deprecated}
```

### Step 4: Copy Template Files

**Core files (always copy):**
- CLAUDE.md
- README.md
- VERSIONS.md
- changelog.md
- glossary.md

**Template files:**
- 01-prd/_template/prd.md
- 01-prd/_template/prototype.html
- 01-prd/_template/prototype/index.html
- 02-specs/_template/spec.md
- 02-specs/_template/api.md
- 02-specs/_template/test-case.md

**Standards files:**
- 06-standards/testing.md
- 06-standards/coding-standards.md
- 06-standards/security.md

**Optional files:**
- 03-guides/ai-development-guide.md
- 03-guides/ai-development-workflow.md
- 02-specs/architecture/system-overview.md
- 02-specs/architecture/tech-stack.md

### Step 5: Customize for Project

Prompt user to fill in:
- Project name
- Project description
- Tech stack
- Team/owner

Update placeholders:
- `{项目名称}` → actual project name
- `{feature}` → feature folder names (kebab-case)
- `YYYY-MM-DD` → current date
- `@xxx` → actual owner

## Documentation Structure

```
docs/
├── CLAUDE.md              # AI entry point
├── README.md              # Human entry point
├── VERSIONS.md            # Version index
├── changelog.md           # Version history
├── glossary.md            # Terminology
│
├── 01-prd/                # Product Requirements
│   ├── _template/         # PRD templates
│   └── {feature}/         # Feature PRDs
│
├── 02-specs/              # Technical Specifications
│   ├── _template/         # Spec templates
│   ├── architecture/      # Architecture docs
│   └── {feature}/         # Feature specs
│
├── 03-guides/             # User guides
├── 04-decisions/          # Architecture Decision Records
├── 05-runbooks/           # Operations runbooks
└── 06-standards/          # Project standards
```

## AI Development Workflow

This template supports AI-native development:

```
需求分析 → 技术设计 → 代码实现 → 验收交付
   │          │          │          │
   ▼          ▼          ▼          ▼
 PRD文档   Spec文档    源代码    Changelog
 +原型
```

### AI Workflow Steps

1. **需求分析**: 人工提出需求 → AI生成PRD → 人工确认 → AI生成高保原型
2. **技术设计**: AI生成Spec → 人工Review → AI生成API文档和测试用例
3. **代码实现**: AI按层实现 → 生成测试
4. **验收交付**: AI执行测试 → 生成测试报告 → 人工复核 → 人工验收

## Examples

```bash
# Initialize full documentation
/zqf-doc-init --full

# Initialize minimal documentation
/zqf-doc-init --minimal

# Initialize API documentation only
/zqf-doc-init --api-only
```

## Version Management

Use Git Tags for version management:

```bash
# Tag on release
git tag -a v1.0.0 -m "Release v1.0.0"

# View historical docs
git show v1.0.0:docs/01-prd/{feature}/prd.md
```

Do NOT include version numbers in filenames (e.g., `prd-v1.0.md`).

## Related Resources

- [AI Development Guide](03-guides/ai-development-guide.md)
- [AI Development Workflow](03-guides/ai-development-workflow.md)
- [VERSIONS.md](VERSIONS.md)

---

*Generated from git history analysis of it-project-docs-for-ai-coding repository*
