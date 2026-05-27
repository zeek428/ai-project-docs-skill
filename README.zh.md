# AI 原生开发文档规范

中文 | [English](README.md)

一个面向 AI 原生软件开发的标准化文档模板仓库。本仓库提供完整的文档结构，可应用于任何软件项目，确保文档的一致性和完整性。

## 概述

这**不是**应用程序代码——这是一个文档模板系统，旨在：

- 标准化项目和团队的文档结构
- 提供开箱即用的 PRD、技术规格、API 文档和测试用例模板
- 支持 `/zqf-doc-init` 技能自动初始化文档
- 帮助 AI 助手快速理解项目上下文

## 快速开始

### Skill 安装（首次使用）

如果使用 Claude Code，需要先安装 skill：

```bash
# 1. 克隆仓库
git clone http://192.168.2.120:81/ai-skills/it-project-docs-for-ai-coding.git /tmp/doc-template

# 2. 创建 skill 文件夹并安装
mkdir -p ~/.claude/skills/zqf-doc-init
cp -R /tmp/doc-template/* ~/.claude/skills/zqf-doc-init/

# 3. 重启 Claude Code
```

安装后即可使用 `/zqf-doc-init` 命令。详见 [zqf-doc-init.md](zqf-doc-init.md)。

### 方式一：使用 Skill（推荐）

如果你已配置 Claude Code：

```bash
# 进入目标项目目录
cd /path/to/your-project

# 初始化完整文档结构
/zqf-doc-init --full

# 或选择精简版文档
/zqf-doc-init --minimal
```

### 方式二：手动复制

```bash
# 克隆模板仓库
git clone http://192.168.2.120:81/ai-skills/it-project-docs-for-ai-coding.git

# 复制到目标项目
mkdir -p /path/to/your-project/docs
cp -R it-project-docs-for-ai-coding/assets/templates/* /path/to/your-project/docs/

# 删除示例目录（仅供参考用）
rm -rf /path/to/your-project/docs/01-prd/_examples
rm -rf /path/to/your-project/docs/02-specs/_examples
```

## 文档结构

```
docs/
├── CLAUDE.md              # AI 入口 - 项目上下文
├── README.md              # 人类入口 - 导航中心
├── VERSIONS.md            # 版本文档索引
├── changelog.md           # 版本变更历史
├── glossary.md            # 项目术语表
│
├── 01-prd/                # 产品需求文档
│   ├── _template/         # 模板（复制使用）
│   └── _examples/         # 示例（仅供参考）
│
├── 02-specs/              # 技术规格文档
│   ├── _template/         # 模板
│   ├── _examples/         # 示例
│   └── architecture/      # 架构文档
│
├── 03-guides/             # 用户指南
│   ├── ai-development-guide.md    # AI 开发流程指南
│   ├── ai-development-workflow.md # AI 开发流程图
│   └── ...
├── 04-decisions/          # 架构决策记录 (ADR)
├── 05-runbooks/           # 运维操作手册
└── 06-standards/          # 项目标准规范
```

## 模板与示例

| 目录 | 用途 | 是否复制到项目 |
|------|------|---------------|
| `_template/` | 空白模板，只有结构 | ✅ 复制后填充内容 |
| `_examples/` | 完整示例，展示如何填写 | ❌ 仅供参考 |

## 文档工作流

```
需求阶段          开发阶段          测试阶段          上线阶段
    │                │                │                │
    ▼                ▼                ▼                ▼
PRD文档 ──────▶ Spec文档 ──────▶ 测试用例 ──────▶ 更新ChangeLog
    │                │                │
    └────────────────┴────────────────┘
                    │
                    ▼
              Review通过
```

## 文档状态流转

```
Draft ──▶ Review ──▶ Approved ──▶ Implemented ──▶ Archived
  │          │           │              │
  └── 修改 ──┘           │              │
                         └── 需求变更 ──┘
```

## 文档命名规范

```
01-prd/
├── user-management/          # 功能目录，使用 kebab-case
│   ├── prd.md
│   └── prototype/
│       └── index.html
└── order-process/

02-specs/
├── user-management/
│   ├── spec.md
│   ├── api.md
│   └── test-case.md
└── order-process/

04-decisions/
├── 0001-database-selection.md   # ADR 编号
├── 0002-auth-strategy.md
```

## 版本迭代管理

### 推荐方案：Git Tag 管理（默认）

**不建议**在文件名或目录名中加版本号（如 `prd-v1.0.md`），原因：

| 问题 | 说明 |
|------|------|
| 冗余 | Git 本身是版本控制系统，文件名带版本重复管理 |
| 混乱 | 版本多时目录拥挤，同一功能多个文件并存 |
| 不同步 | 文档版本号可能与代码 Tag 不一致 |

**推荐做法**：

```bash
# 发布版本时打 Tag（代码和文档同步标记）
git tag -a v1.0.0 -m "Release v1.0.0"
git push origin v1.0.0

# 查看历史版本文档
git show v1.0.0:docs/01-prd/user-management/prd.md

# 切换到历史版本
git checkout v1.0.0
```

### 备选方案：目录归档（大版本迭代）

当进行**大版本重构**（如 v1 → v2 架构升级）时，可归档历史文档：

```bash
# 归档脚本
VERSION=v1.0
mkdir -p docs/$VERSION
cp -r docs/01-prd docs/$VERSION/
cp -r docs/02-specs docs/$VERSION/
```

归档后结构：
```
docs/
├── v1.0/                  # 归档版本（大版本保留）
│   ├── 01-prd/
│   └── 02-specs/
├── v2.0/                  # 归档版本（大版本保留）
├── 01-prd/                # 当前版本（始终是最新的）
└── 02-specs/              # 当前版本（始终是最新的）
```

### 版本管理策略对比

| 方案 | 适用场景 | 优点 | 缺点 |
|------|----------|------|------|
| Git Tag（推荐） | 所有项目 | 代码文档同步，无冗余 | 需切换分支查看历史 |
| 目录归档 | 大版本升级 | 历史版本直观可见 | 占用存储空间 |
| 文件名版本 | ❌ 不推荐 | - | 目录混乱，易不同步 |

## 定制化

应用模板后，更新以下占位符：

| 占位符 | 替换为 |
|--------|--------|
| `{项目名称}` | 实际项目名称 |
| `{feature}` | 功能目录名（kebab-case） |
| `YYYY-MM-DD` | 当前日期 |
| `@xxx` | 实际负责人 |

## 常见问题

### Q: 项目太小，需要这么多文档吗？

| 项目规模 | 推荐文档 |
|----------|----------|
| 小型（1-2人，<3月） | README + PRD + Spec |
| 中型（3-5人，3-6月） | + Test Case + API |
| 大型（>5人，>6月） | 完整结构 |

### Q: 文档和代码不同步怎么办？

1. PR/CR 流程中包含文档检查
2. 定期文档 Review（每月/每季度）
3. AI 辅助同步更新

### Q: 敏捷开发，文档太重怎么办？

1. 精简必填字段
2. 用户故事代替完整 PRD
3. 测试用例即需求文档

## 最小文档集

如果项目只需要最小文档集：

```
docs/
├── CLAUDE.md              # AI 入口
├── README.md              # 项目说明
├── 01-prd/{feature}/prd.md   # 需求文档
└── 02-specs/{feature}/
    ├── spec.md            # 技术设计
    └── test-case.md       # 测试用例
```

## 相关文档

- [CLAUDE.md](CLAUDE.md) - AI 入口
- [VERSIONS.md](VERSIONS.md) - 版本索引
- [zqf-doc-init.md](zqf-doc-init.md) - Skill 定义

## 贡献指南

详见 [03-guides/contributing.md](03-guides/contributing.md)。

---

最后更新: YYYY-MM-DD
