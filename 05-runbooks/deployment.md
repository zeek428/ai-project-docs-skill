# 部署流程

## 触发条件
- 功能发布
- Bug 修复
- 紧急修复

## 前置条件
- [ ] 代码已合并到主分支
- [ ] CI 测试通过
- [ ] 变更日志已更新

## 部署步骤

### 1. 准备阶段

```bash
# 切换到目标分支
git checkout main
git pull origin main

# 确认版本号
cat VERSION
```

### 2. 构建阶段

```bash
# 构建镜像
docker build -t app:latest .

# 推送镜像
docker push registry.example.com/app:latest
```

### 3. 部署阶段

```bash
# 部署到测试环境
kubectl apply -f k8s/test/

# 验证测试环境
curl https://test.example.com/health

# 部署到生产环境
kubectl apply -f k8s/prod/
```

### 4. 验证阶段

```bash
# 健康检查
curl https://api.example.com/health

# 检查日志
kubectl logs -f deployment/app

# 检查监控
# 访问监控面板确认服务正常
```

## 回滚方案

```bash
# 查看历史版本
kubectl rollout history deployment/app

# 回滚到上一版本
kubectl rollout undo deployment/app

# 回滚到指定版本
kubectl rollout undo deployment/app --to-revision=N
```

## 验证清单
- [ ] 服务健康检查通过
- [ ] 关键接口测试通过
- [ ] 监控指标正常
- [ ] 无错误日志

## 常见问题

| 现象 | 原因 | 解决方案 |
|------|------|----------|
| 镜像拉取失败 | 网络问题/镜像不存在 | 检查镜像是否推送成功 |
| 服务启动失败 | 配置错误/依赖不可用 | 检查配置和依赖服务 |
| 健康检查失败 | 服务未就绪 | 增加就绪探针等待时间 |

## 联系人
- 负责人: @xxx
- 升级路径: @xxx

---
最后更新: YYYY-MM-DD
