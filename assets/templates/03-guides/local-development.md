# 本地开发环境搭建

## 适用人群
需要在本地进行开发调试的开发人员

## 前置条件
- 已完成 [快速入门](getting-started.md)
- 熟悉项目基本结构

## 开发环境配置

### IDE 配置

#### 推荐插件
| 插件名 | 用途 |
|--------|------|
|        |      |

#### 配置文件
```json
// VS Code settings.json 示例
{
  "editor.formatOnSave": true
}
```

### 环境变量

```bash
# 开发环境必需变量
export DEBUG=true
export LOG_LEVEL=debug
export DATABASE_URL=
export REDIS_URL=
export API_KEY=
```

### 本地服务

#### 数据库
```bash
# 启动本地数据库
# 连接配置
```

#### 缓存
```bash
# 启动 Redis
# 连接配置
```

#### 其他依赖
```bash
# 启动其他服务
```

## 开发工作流

### 启动开发服务
```bash
# 开发模式（热重载）
```

### 运行测试
```bash
# 运行所有测试
# 运行单个测试文件
# 测试覆盖率报告
```

### 代码检查
```bash
# Lint
# Format
# Type check
```

### 调试

#### 断点调试
<!-- IDE 调试配置 -->

#### 日志调试
<!-- 日志配置说明 -->

#### 常用调试命令
```bash
# 调试命令
```

## 模拟数据

### 测试数据准备
```bash
# 导入测试数据
# 重置数据库
```

### Mock 服务
<!-- Mock 配置说明 -->

## 常见问题

| 问题 | 解决方案 |
|------|----------|
|      |          |

## 性能调优
<!-- 本地性能优化建议 -->

---
最后更新: YYYY-MM-DD
