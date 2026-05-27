# AGENTS.md

This file provides guidance to Codex (Codex.ai/code) when working with code in this repository.

## Project Overview

This is a **documentation template repository** for AI-native development. It provides standardized documentation structures and templates that can be applied to other projects. This is NOT a code project - it contains documentation templates, not application code.

## Purpose

- Provide a standardized documentation structure for software projects
- Enable consistent PRD, Spec, API, and Test Case documentation
- Support the `/zqf-doc-init` skill for initializing docs in target projects
- Serve as a template source for team-wide documentation standards

## Directory Structure

```
docs/
├── AGENTS.md              # AI entry point (this file)
├── README.md              # Human entry point with navigation
├── VERSIONS.md            # Version documentation index
├── zqf-doc-init.md               # /zqf-doc-init skill definition
├── changelog.md           # Version history
├── glossary.md            # Terminology glossary
│
├── 01-prd/                # Product Requirements Documents
│   ├── _template/
│   │   ├── prd.md         # PRD template
│   │   └── prototype.html # Prototype placeholder
│   └── _examples/
│       └── prd-example.md # PRD complete example (reference only)
│
├── 02-specs/              # Technical Specifications
│   ├── _template/
│   │   ├── spec.md        # Technical design template
│   │   ├── api.md         # API documentation template
│   │   └── test-case.md   # Test case template
│   ├── _examples/
│   │   ├── spec-example.md      # Spec complete example
│   │   ├── api-example.md       # API doc complete example
│   │   └── test-case-example.md # Test case complete example
│   └── architecture/      # Architecture documentation
│
├── 03-guides/             # User guides
│   ├── ai-development-guide.md    # AI development workflow guide
│   ├── ai-development-workflow.md # AI development flow diagrams
│   └── ...
├── 04-decisions/          # Architecture Decision Records (ADR)
├── 05-runbooks/           # Operations runbooks
└── 06-standards/          # Project standards
    ├── testing.md         # Testing strategy and case standards
    ├── coding-standards.md
    └── security.md
```

## Using This Repository

### Apply to Another Project

**Method 1: Using the Skill (Recommended)**
```bash
# In target project directory
/zqf-doc-init --full      # Complete documentation structure
/zqf-doc-init --minimal   # README + PRD + Spec only
/zqf-doc-init --api-only  # API documentation focus
```

**Method 2: Manual Copy**
```bash
# Copy template to target project
mkdir -p /path/to/target-project/docs
cp -R assets/templates/* /path/to/target-project/docs/

# Remove example folders if not needed
rm -rf /path/to/target-project/docs/01-prd/_examples
rm -rf /path/to/target-project/docs/02-specs/_examples
```

### Customize for Target Project

After copying, update placeholders:
- `{项目名称}` → actual project name
- `{feature}` → feature folder names (kebab-case)
- `YYYY-MM-DD` → current date
- `@xxx` → actual owner
- Empty sections in templates → project-specific content

## AI Workflow

### Reading Order
1. `AGENTS.md` - Understand project context
2. `01-prd/{feature}/prd.md` - Understand requirements
3. `02-specs/{feature}/spec.md` - Understand technical approach
4. `04-decisions/` - Understand historical decision context

### Documentation Standards

| Document Type | Requirements |
|---------------|--------------|
| PRD | User story format, must include acceptance criteria |
| Spec | Must include design decisions, test strategy, risk analysis |
| Test Case | Must include preconditions, steps, expected results |
| ADR | Must include alternative comparison |
| API | Markdown preferred, YAML when tool support needed |

### Prohibitions
- Do not modify `07-deprecated/` directory contents
- Do not delete historical decisions from `04-decisions/`
- Do not skip test strategy sections in specs
- Do not omit test case documentation

## Template Version

Current template version is tracked in `.template-version`:
```yaml
---
version: 1.0.0
initialized_at: YYYY-MM-DD
project: {project_name}
---
```

## Related Links
- Version Index: [VERSIONS.md](VERSIONS.md)
- Skill Definition: [zqf-doc-init.md](zqf-doc-init.md)

---
Status: Approved
Owner: @
Created: YYYY-MM-DD
Updated: YYYY-MM-DD
