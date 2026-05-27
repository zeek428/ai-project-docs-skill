# 技术规格示例：用户管理

> 本文件为完整示例，仅供参考，不复制到实际项目。

---
**版本信息**

| 项目 | 值 |
|------|------|
| 功能版本 | v1.1.0 |
| 适用系统版本 | ≥ v1.0.0 |
| 文档状态 | Approved |

**版本历史**

| 版本 | 日期 | 变更内容 | 作者 |
|------|------|----------|------|
| v1.0.0 | 2024-01-15 | 初始版本：手机号登录 | @zhangsan |
| v1.1.0 | 2024-02-01 | 新增微信授权登录 | @zhangsan |

---

## 概述

实现用户注册、登录、信息管理功能，支持手机号验证码登录和微信授权登录。

## 设计决策

| 决策点 | 方案 | 理由 |
|--------|------|------|
| 认证方式 | JWT Token | 无状态，适合分布式架构 |
| 密码存储 | bcrypt + salt | 安全性高，防止彩虹表攻击 |
| 验证码 | Redis 存储，5分钟过期 | 平衡安全性和用户体验 |

## 系统设计

### 架构图

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Client    │ ──▶ │   API GW    │ ──▶ │  Auth Svc   │
└─────────────┘     └─────────────┘     └─────────────┘
                                               │
                          ┌────────────────────┼────────────────────┐
                          ▼                    ▼                    ▼
                    ┌──────────┐        ┌──────────┐        ┌──────────┐
                    │  MySQL   │        │  Redis   │        │   SMS    │
                    └──────────┘        └──────────┘        └──────────┘
```

### 模块划分

| 模块 | 职责 | 依赖 |
|------|------|------|
| UserController | 处理 HTTP 请求 | UserService |
| UserService | 业务逻辑处理 | UserRepository, SmsService |
| UserRepository | 数据访问 | MySQL |
| SmsService | 短信发送 | 第三方 SMS 服务 |

---

## 数据库设计

### ER 图

```
┌─────────────┐       ┌─────────────┐
│   users     │       │ user_tokens │
│             │       │             │
│ id (PK)     │ ◀─────│ user_id(FK) │
│ phone       │       │ token       │
│ nickname    │       │ type        │
│ wx_openid   │       │ expired_at  │
└─────────────┘       └─────────────┘
```

### 表结构设计

#### 表 1: users

**表说明**: 用户主表，存储用户基本信息

| 字段名 | 类型 | 是否必填 | 默认值 | 说明 |
|--------|------|----------|--------|------|
| id | BIGINT | 是 | 自增 | 主键 |
| phone | VARCHAR(20) | 是 | - | 手机号，唯一 |
| nickname | VARCHAR(50) | 否 | NULL | 昵称 |
| avatar | VARCHAR(255) | 否 | NULL | 头像URL |
| wx_openid | VARCHAR(64) | 否 | NULL | 微信OpenID，唯一 |
| status | TINYINT | 是 | 1 | 状态：1正常 2禁用 |
| created_at | TIMESTAMP | 是 | CURRENT_TIMESTAMP | 创建时间 |
| updated_at | TIMESTAMP | 是 | CURRENT_TIMESTAMP | 更新时间 |

**建表语句**:
```sql
CREATE TABLE users (
    id          BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT '主键ID',
    phone       VARCHAR(20) UNIQUE NOT NULL COMMENT '手机号',
    nickname    VARCHAR(50) COMMENT '昵称',
    avatar      VARCHAR(255) COMMENT '头像URL',
    wx_openid   VARCHAR(64) UNIQUE COMMENT '微信OpenID',
    status      TINYINT NOT NULL DEFAULT 1 COMMENT '状态：1正常 2禁用',
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    updated_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT '更新时间'
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户表';
```

#### 表 2: user_tokens

**表说明**: 用户Token表，存储刷新Token

| 字段名 | 类型 | 是否必填 | 默认值 | 说明 |
|--------|------|----------|--------|------|
| id | BIGINT | 是 | 自增 | 主键 |
| user_id | BIGINT | 是 | - | 用户ID，外键 |
| token | VARCHAR(255) | 是 | - | 刷新Token |
| type | VARCHAR(20) | 是 | - | Token类型：phone/wechat |
| expired_at | TIMESTAMP | 是 | - | 过期时间 |
| created_at | TIMESTAMP | 是 | CURRENT_TIMESTAMP | 创建时间 |

**建表语句**:
```sql
CREATE TABLE user_tokens (
    id          BIGINT PRIMARY KEY AUTO_INCREMENT COMMENT '主键ID',
    user_id     BIGINT NOT NULL COMMENT '用户ID',
    token       VARCHAR(255) NOT NULL COMMENT '刷新Token',
    type        VARCHAR(20) NOT NULL COMMENT 'Token类型',
    expired_at  TIMESTAMP NOT NULL COMMENT '过期时间',
    created_at  TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
    INDEX idx_user_id (user_id),
    INDEX idx_token (token),
    FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COMMENT='用户Token表';
```

### 索引设计

| 表名 | 索引名 | 字段 | 类型 | 用途说明 |
|------|--------|------|------|----------|
| users | PRIMARY | id | 主键 | 主键索引 |
| users | uk_phone | phone | 唯一索引 | 手机号唯一约束 |
| users | uk_wx_openid | wx_openid | 唯一索引 | 微信OpenID唯一约束 |
| users | idx_status | status | 普通索引 | 按状态查询 |
| user_tokens | PRIMARY | id | 主键 | 主键索引 |
| user_tokens | idx_user_id | user_id | 普通索引 | 按用户ID查询 |
| user_tokens | idx_token | token | 普通索引 | Token校验 |

### 数据迁移

**新增表迁移**:
```sql
-- migration/001_create_users_table.sql
CREATE TABLE users (
    -- 见上方建表语句
);

CREATE TABLE user_tokens (
    -- 见上方建表语句
);
```

**存量数据处理**:
```sql
-- 如果有存量用户数据需要迁移
INSERT INTO users (id, phone, nickname, status)
SELECT id, phone, name, 1 FROM old_users;
```

**回滚脚本**:
```sql
DROP TABLE IF EXISTS user_tokens;
DROP TABLE IF EXISTS users;
```

---

## API 设计

见 [api-example.md](./api-example.md)

### 接口清单

| 接口 | 方法 | 路径 | 说明 |
|------|------|------|------|
| 发送验证码 | POST | /v1/auth/sms-code | 发送登录验证码 |
| 手机号登录 | POST | /v1/auth/login | 手机号验证码登录 |
| 微信登录 | POST | /v1/auth/wechat | 微信授权登录 |
| 获取用户信息 | GET | /v1/users/me | 获取当前用户信息 |
| 更新用户信息 | PUT | /v1/users/me | 更新昵称/头像 |

---

## 实现细节

### 模块 A: 用户登录服务

**职责**: 处理用户认证逻辑

**接口定义**:
```typescript
interface AuthService {
    sendSmsCode(phone: string): Promise<void>;
    loginByPhone(phone: string, code: string): Promise<LoginResult>;
    loginByWechat(code: string): Promise<LoginResult>;
    refreshToken(refreshToken: string): Promise<TokenPair>;
}

interface LoginResult {
    user: User;
    accessToken: string;
    refreshToken: string;
    expiresIn: number;
}
```

**核心逻辑**:
```typescript
async loginByPhone(phone: string, code: string): Promise<LoginResult> {
    // 1. 验证验证码
    const storedCode = await redis.get(`sms:${phone}`);
    if (!storedCode || storedCode !== code) {
        throw new BadRequestError('验证码错误或已过期');
    }
    
    // 2. 查找或创建用户
    let user = await userRepository.findByPhone(phone);
    if (!user) {
        user = await userRepository.create({ phone });
    }
    
    // 3. 生成 Token
    const tokens = this.generateTokens(user);
    
    // 4. 删除已使用的验证码
    await redis.del(`sms:${phone}`);
    
    return { user, ...tokens };
}
```

---

## 缓存策略

| 数据类型 | 缓存位置 | Key 格式 | 过期时间 | 更新策略 |
|----------|----------|----------|----------|----------|
| 验证码 | Redis | sms:{phone} | 5min | 发送时写入 |
| 用户信息 | Redis | user:{id} | 30min | 写入时更新 |
| Token黑名单 | Redis | blacklist:{token} | 7天 | 登出时写入 |

---

## 测试策略

### 单元测试
- 覆盖范围: Service 层所有方法
- Mock 策略: Mock Repository 和外部服务
- 目标覆盖率: 90%

### 集成测试
- 测试场景: 登录流程、Token 刷新、权限校验
- 测试数据: 使用测试数据库

### E2E 测试
- 关键流程: 注册 → 登录 → 获取用户信息 → 修改信息

---

## 上线检查清单

- [x] 代码审查通过
- [x] 测试用例编写完成
- [x] P0/P1 用例 100% 通过
- [x] 测试覆盖率 92%
- [x] 性能测试通过
- [x] 安全审查通过
- [x] 文档更新完成
- [x] 配置项确认
- [x] 回滚方案就绪
- [x] 数据库迁移脚本准备就绪

---

## 关联文档

- PRD: [01-prd/_examples/prd-example.md](../../01-prd/_examples/prd-example.md)
- 测试用例: [test-case-example.md](./test-case-example.md)
- API 文档: [api-example.md](./api-example.md)

---
**文档状态**: Approved
**负责人**: @zhangsan
**创建日期**: 2024-01-15
**更新日期**: 2024-02-01
