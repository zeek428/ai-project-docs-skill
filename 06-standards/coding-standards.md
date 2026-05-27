# 编码规范

## 通用原则

1. **可读性优先**: 代码是写给人看的
2. **一致性**: 遵循团队约定
3. **简洁性**: 简单直接的实现
4. **可维护性**: 易于理解和修改

## 命名规范

### 变量命名
```typescript
// 使用有意义的名称
const userCount = 10;  // Good
const n = 10;          // Bad

// 布尔值使用 is/has/can 前缀
const isValid = true;
const hasPermission = false;
const canEdit = true;

// 常量使用大写
const MAX_RETRY_COUNT = 3;
const API_BASE_URL = 'https://api.example.com';
```

### 函数命名
```typescript
// 使用动词开头
function getUser() {}
function createUser() {}
function deleteUser() {}
function calculateTotal() {}

// 布尔返回值使用 is/has/can
function isValidEmail() {}
function hasPermission() {}
```

### 类命名
```typescript
// 使用 PascalCase
class UserService {}
class OrderController {}
class PaymentGateway {}
```

## 代码组织

### 文件结构
```
src/
├── modules/
│   └── user/
│       ├── user.controller.ts    # 控制器
│       ├── user.service.ts       # 业务逻辑
│       ├── user.repository.ts    # 数据访问
│       ├── user.model.ts         # 数据模型
│       ├── user.dto.ts           # 数据传输对象
│       ├── user.types.ts         # 类型定义
│       └── user.test.ts          # 测试文件
```

### 函数长度
- 单个函数不超过 50 行
- 超过则拆分为多个函数

### 文件长度
- 单个文件不超过 400 行
- 超过则拆分为多个模块

## Git 提交规范

### 提交信息格式
```
<type>: <description>

type: feat | fix | refactor | docs | test | chore | perf
```

### 示例
```
feat: 添加用户登录功能

- 支持 手机号 + 验证码 登录
- 支持 微信授权 登录
- 添加登录日志记录
```

---
最后更新: YYYY-MM-DD
