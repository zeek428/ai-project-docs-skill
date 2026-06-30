# ai-project-docs-skill

这是中文说明文件。GitHub 仓库首页请以 [README.md](README.md) 为准。

`ai-project-docs-skill` 是一个面向 AI 原生软件开发的文档初始化 Skill 与模板仓库。它提供一套可复制、可自动初始化的项目文档结构，帮助团队快速建立 PRD、技术规格、API 文档、测试用例、ADR、runbook 和项目标准。

## 快速使用

```bash
git clone https://github.com/zeek428/ai-project-docs-skill.git
cd ai-project-docs-skill

python3 scripts/init_docs.py \
  --target /path/to/your-project \
  --mode full \
  --project-name "Your Project" \
  --owner "@team"
```

完整说明见 [README.md](README.md)，Skill 入口见 [SKILL.md](SKILL.md)。
