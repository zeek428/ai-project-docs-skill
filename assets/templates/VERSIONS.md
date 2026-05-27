# 版本文档索引

## 当前版本：v{major}.{minor}.{patch}

- **发布日期**: YYYY-MM-DD
- **主要变更**: 
- **文档入口**: [README.md](./README.md)

---

## 历史版本

| 版本 | 发布日期 | 状态 | 文档入口 | 主要变更 |
|------|----------|------|----------|----------|
| v1.0.0 | YYYY-MM-DD | 已归档 | [v1.0/](./v1.0/) | 初始版本 |
| v0.1.0 | YYYY-MM-DD | 已归档 | [v0.1/](./v0.1/) | 项目启动 |

---

## 版本命名规范

遵循 [语义化版本](https://semver.org/lang/zh-CN/)：

```
v{MAJOR}.{MINOR}.{PATCH}

MAJOR: 不兼容的 API 变更
MINOR: 向后兼容的功能新增
PATCH: 向后兼容的问题修复
```

## 版本状态说明

| 状态 | 说明 | 文档处理 |
|------|------|----------|
| 开发中 | 开发分支，未发布 | 当前目录，Draft 状态 |
| 当前版本 | 已发布，正在使用 | 当前目录，Approved 状态 |
| 维护中 | 旧版本，仍在维护 | 归档目录，标记维护状态 |
| 已归档 | 不再维护 | 归档目录，标记 deprecated |
| 已废弃 | 不可使用 | 归档目录，标记废弃原因 |

---

## 多版本并行说明

<!-- 如有多个版本同时运行，在此说明 -->

### 版本生命周期

```
v1.0 ──▶ v1.1 ──▶ v2.0 (当前)
  │        │
  │        └── 维护至 2024-06-01
  │
  └── 2024-03-01 停止维护
```

### 版本选择指南

| 使用场景 | 推荐版本 |
|----------|----------|
| 新客户接入 | v2.0 |
| 存量客户维护 | v1.1 |
| 历史数据迁移 | v1.0 |

---

## 文档归档规则

### 归档触发条件

- [ ] 大版本发布（MAJOR 版本升级）
- [ ] 重大架构变更
- [ ] 产品方向调整
- [ ] 版本停止维护

### 归档操作

```bash
# 1. 创建归档目录
VERSION=v1.0
mkdir -p docs/$VERSION

# 2. 复制当前文档
cp -r docs/prd docs/$VERSION/
cp -r docs/specs docs/$VERSION/
cp -r docs/architecture docs/$VERSION/

# 3. 更新归档文档状态
find docs/$VERSION -name "*.md" -exec sed -i '' 's/status: Approved/status: Archived/' {} \;

# 4. 记录归档日志
echo "$(date '+%Y-%m-%d') - Archived $VERSION" >> docs/.archive-log

# 5. 更新本文件
# 添加版本记录到"历史版本"表格
```

---

最后更新: YYYY-MM-DD
