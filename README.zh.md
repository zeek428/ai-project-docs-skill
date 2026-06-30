# ai-project-docs-skill

[English](README.md) | 中文

`ai-project-docs-skill` 是一个面向 AI 原生软件开发的文档初始化 Skill 与模板仓库。它提供一套可复制、可自动初始化的项目文档结构，帮助团队在需求、技术方案、API、测试、运维和架构决策之间建立统一上下文。

这个仓库不是业务应用代码，而是用于给其他项目生成 `docs/` 文档体系的模板源。

## 解决什么问题

- 新项目一开始没有统一的 PRD、Spec、API、测试用例和 ADR 文档结构。
- AI 编程助手进入项目时缺少稳定的阅读入口和上下文顺序。
- 文档分散在不同位置，需求、设计、测试和上线记录难以互相追踪。
- 团队希望把文档模板沉淀成可复用的 Skill，而不是每个项目手工复制。

## 核心能力

| 能力 | 说明 |
|------|------|
| 文档结构初始化 | 一键生成 `docs/` 目录、模板、指南、标准和 runbook |
| 多种初始化模式 | 支持 `full`、`minimal`、`api-only` 三种模板集 |
| AI 友好入口 | 提供 `CLAUDE.md`、`README.md`、PRD、Spec、Test Case 等标准阅读顺序 |
| 可安全复用 | 默认跳过已有文件，可通过 `--dry-run` 预览，通过 `--overwrite` 显式覆盖 |
| 示例与模板分离 | `_template/` 用于复制填写，`_examples/` 仅作参考 |

## 快速开始

### 方式一：使用初始化脚本

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

确认输出无误后去掉 `--dry-run`：

```bash
python3 scripts/init_docs.py \
  --target /path/to/your-project \
  --mode full \
  --project-name "Your Project" \
  --owner "@team"
```

### 方式二：安装为 Skill

将本仓库复制到你的 Codex 或 Claude Code skills 目录，之后即可在目标项目中按 Skill 指南执行文档初始化。

```bash
mkdir -p ~/.codex/skills/zqf-doc-init
cp -R /path/to/ai-project-docs-skill/* ~/.codex/skills/zqf-doc-init/
```

Skill 的入口文件是 [SKILL.md](SKILL.md)。旧入口 [zqf-doc-init.md](zqf-doc-init.md) 仍保留，用于兼容历史用法。

## 初始化模式

| 模式 | 适用场景 | 包含内容 |
|------|----------|----------|
| `full` | 新项目、中大型项目、需要完整协作规范的项目 | 核心文件、PRD、Spec、API、测试用例、指南、ADR、runbook、安全与编码标准 |
| `minimal` | 小项目、原型、早期验证 | 核心文件、PRD 模板、Spec 模板、测试用例模板、ADR 模板 |
| `api-only` | API 服务、后端服务、接口治理项目 | 核心文件、API/Spec/Test Case 模板、架构文档、ADR、标准规范 |

常用参数：

| 参数 | 说明 |
|------|------|
| `--target` | 目标项目根目录，脚本会写入 `<target>/docs` |
| `--mode` | 模板模式：`full`、`minimal`、`api-only` |
| `--project-name` | 替换 `{项目名称}` 和 `{project_name}` 占位符 |
| `--owner` | 替换 `@xxx` 负责人占位符 |
| `--date` | 替换 `YYYY-MM-DD`，默认使用当天日期 |
| `--dry-run` | 只预览将创建、跳过或覆盖的文件 |
| `--overwrite` | 覆盖已有文件，默认不会覆盖 |
| `--include-examples` | 同步复制 `_examples` 示例目录 |

## 生成后的文档结构

```text
docs/
├── CLAUDE.md              # AI 入口：项目上下文与阅读顺序
├── README.md              # 人类入口：文档导航中心
├── VERSIONS.md            # 版本文档索引
├── changelog.md           # 变更记录
├── glossary.md            # 术语表
│
├── 01-prd/                # 产品需求文档
│   ├── _template/
│   │   ├── prd.md
│   │   ├── prototype.html
│   │   └── prototype/index.html
│   └── _examples/
│       └── prd-example.md
│
├── 02-specs/              # 技术规格文档
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
├── 03-guides/             # 开发、贡献、本地环境等指南
├── 04-decisions/          # ADR 架构决策记录
├── 05-runbooks/           # 部署、监控、事故响应 runbook
├── 06-standards/          # 测试、编码、安全标准
└── 07-deprecated/         # 废弃文档说明
```

## 文档工作流

```text
需求分析          技术设计          开发测试          发布运维
   │                 │                 │                 │
   ▼                 ▼                 ▼                 ▼
 PRD 文档 ─────▶ Spec/API 文档 ───▶ Test Case ─────▶ Changelog/Runbook
   │                 │                 │
   └─────────────────┴─────────────────┘
                     │
                     ▼
                  Review
```

建议阅读顺序：

1. `docs/CLAUDE.md`
2. `docs/01-prd/{feature}/prd.md`
3. `docs/02-specs/{feature}/spec.md`
4. `docs/02-specs/{feature}/api.md`
5. `docs/02-specs/{feature}/test-case.md`
6. `docs/04-decisions/`

## 仓库内容

| 路径 | 说明 |
|------|------|
| [SKILL.md](SKILL.md) | 当前 Skill 入口与执行规则 |
| [scripts/init_docs.py](scripts/init_docs.py) | 文档初始化脚本 |
| [assets/templates/](assets/templates/) | 可复制到目标项目的模板源 |
| [01-prd/](01-prd/) | 仓库内的 PRD 模板副本 |
| [02-specs/](02-specs/) | 仓库内的 Spec/API/Test Case 模板副本 |
| [03-guides/](03-guides/) | AI 开发流程、贡献、本地开发指南 |
| [04-decisions/](04-decisions/) | ADR 模板 |
| [05-runbooks/](05-runbooks/) | 运维 runbook 模板 |
| [06-standards/](06-standards/) | 测试、编码、安全规范 |

## 使用建议

- 新项目优先使用 `--mode full`，确保从一开始保留需求、设计、测试和上线记录。
- 小型项目可使用 `--mode minimal`，保留 README、PRD、Spec、Test Case 和 ADR 即可。
- 已有项目先执行 `--dry-run`，确认不会覆盖重要文档后再正式写入。
- 默认不要复制 `_examples/` 到目标项目；只有需要参考完整示例时再加 `--include-examples`。
- 文档版本优先使用 Git Tag 管理，不建议创建 `prd-v1.0.md` 这类文件名版本。

## 相关文档

- [SKILL.md](SKILL.md)：Skill 当前入口
- [zqf-doc-init.md](zqf-doc-init.md)：历史兼容入口
- [VERSIONS.md](VERSIONS.md)：版本文档索引
- [changelog.md](changelog.md)：仓库变更记录
- [glossary.md](glossary.md)：术语表

## 维护状态

- 当前模板版本：`1.0.0`
- 仓库用途：文档模板与 Skill 源仓库
- 默认输出目录：目标项目的 `docs/`
- 最后更新：2026-06-30
