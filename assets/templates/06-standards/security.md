# 安全规范

## 安全原则

1. **最小权限原则**: 只授予必要的权限
2. **纵深防御**: 多层安全防护
3. **安全默认**: 默认配置应该是安全的
4. **永不信任**: 所有输入都是不可信的

## 认证与授权

### 认证方式
- 密码 + 验证码
- OAuth 2.0
- JWT Token

### Token 管理
```typescript
// Token 配置
const TOKEN_CONFIG = {
  accessTokenExpiry: '2h',
  refreshTokenExpiry: '7d',
  algorithm: 'RS256'
};
```

## 输入验证

### 必须验证的输入
- URL 参数
- Query 参数
- Request Body
- Header
- Cookie

### 防护措施
- SQL 注入: 使用参数化查询
- XSS: 输出编码
- CSRF: Token 验证
- 路径遍历: 路径规范化

## 敏感数据保护

### 敏感数据类型
- 密码
- 身份证号
- 手机号
- 银行卡号
- API Key

### 存储要求
```typescript
// 密码必须加密存储
const hashedPassword = await bcrypt.hash(password, 10);

// 日志脱敏
logger.info('User login', { phone: maskPhone(phone) });
```

## API 安全

### 认证
```typescript
// 所有接口必须验证 Token
@Middleware()
async validateToken(ctx: Context) {
  const token = ctx.headers.authorization;
  if (!token) {
    throw new UnauthorizedError('Missing token');
  }
}
```

### 限流
```typescript
// API 限流配置
const rateLimitConfig = {
  windowMs: 60 * 1000,  // 1 分钟
  max: 100,              // 最多 100 次请求
};
```

## 安全清单

### 开发阶段
- [ ] 所有输入已验证
- [ ] 所有输出已编码
- [ ] 敏感数据已加密
- [ ] 权限已检查
- [ ] 日志已脱敏

### 测试阶段
- [ ] 安全测试通过
- [ ] 渗透测试通过
- [ ] 依赖漏洞扫描通过

### 上线阶段
- [ ] HTTPS 已配置
- [ ] 安全头已配置
- [ ] 限流已配置
- [ ] 监控已配置

---
最后更新: YYYY-MM-DD
