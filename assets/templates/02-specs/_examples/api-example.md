# API 文档示例：用户模块

> 本文件为完整示例，仅供参考，不复制到实际项目。

## 概述

用户模块 API，包含注册、登录、用户信息管理接口。

## 认证方式

### 认证类型
- 方式: Bearer Token (JWT)
- Header: `Authorization: Bearer <token>`

### 获取 Token
```bash
curl -X POST https://api.example.com/v1/auth/login \
  -H "Content-Type: application/json" \
  -d '{"phone": "13800138000", "code": "123456"}'
```

---

## 接口列表

### 1. 发送验证码

**描述**: 发送手机验证码，用于登录/注册

**请求**:
```
POST /v1/auth/sms-code
```

**请求体**:
```json
{
  "phone": "string"  // 手机号，11位
}
```

**请求示例**:
```bash
curl -X POST "https://api.example.com/v1/auth/sms-code" \
  -H "Content-Type: application/json" \
  -d '{"phone": "13800138000"}'
```

**响应示例**:
```json
{
  "code": 0,
  "message": "success",
  "data": {
    "expireIn": 300
  }
}
```

**错误码**:
| 错误码 | 说明 |
|--------|------|
| 400 | 手机号格式错误 |
| 429 | 发送频率超限（60秒内只能发送一次） |

---

### 2. 手机号登录/注册

**描述**: 使用手机号和验证码登录，若用户不存在则自动注册

**请求**:
```
POST /v1/auth/login
```

**请求体**:
```json
{
  "phone": "string",
  "code": "string"
}
```

**请求示例**:
```bash
curl -X POST "https://api.example.com/v1/auth/login" \
  -H "Content-Type: application/json" \
  -d '{"phone": "13800138000", "code": "123456"}'
```

**响应示例**:
```json
{
  "code": 0,
  "message": "success",
  "data": {
    "user": {
      "id": "1001",
      "phone": "138****8000",
      "nickname": "用户_13800138000",
      "avatar": null,
      "createdAt": "2024-01-15T10:30:00Z"
    },
    "accessToken": "eyJhbGciOiJIUzI1NiIs...",
    "refreshToken": "eyJhbGciOiJIUzI1NiIs...",
    "expiresIn": 7200
  }
}
```

**错误码**:
| 错误码 | 说明 |
|--------|------|
| 400 | 参数错误 |
| 401 | 验证码错误或已过期 |

---

### 3. 获取用户信息

**描述**: 获取当前登录用户信息

**请求**:
```
GET /v1/users/me
```

**请求示例**:
```bash
curl -X GET "https://api.example.com/v1/users/me" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIs..."
```

**响应示例**:
```json
{
  "code": 0,
  "message": "success",
  "data": {
    "id": "1001",
    "phone": "138****8000",
    "nickname": "张三",
    "avatar": "https://cdn.example.com/avatar/1001.jpg",
    "createdAt": "2024-01-15T10:30:00Z"
  }
}
```

---

### 4. 更新用户信息

**描述**: 更新当前用户昵称或头像

**请求**:
```
PUT /v1/users/me
```

**请求体**:
```json
{
  "nickname": "string",  // 可选，昵称，2-20字符
  "avatar": "string"     // 可选，头像URL
}
```

**请求示例**:
```bash
curl -X PUT "https://api.example.com/v1/users/me" \
  -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIs..." \
  -H "Content-Type: application/json" \
  -d '{"nickname": "张三"}'
```

**响应示例**:
```json
{
  "code": 0,
  "message": "success",
  "data": {
    "id": "1001",
    "nickname": "张三",
    "avatar": "https://cdn.example.com/avatar/1001.jpg",
    "updatedAt": "2024-01-20T14:30:00Z"
  }
}
```

---

## 速率限制

| 接口 | 限制 | 窗口 |
|------|------|------|
| 发送验证码 | 1 次 | 60 秒 |
| 登录 | 10 次 | 1 分钟 |
| 其他接口 | 100 次 | 1 分钟 |

---

## 变更日志

| 版本 | 日期 | 变更内容 |
|------|------|----------|
| v1.0.0 | 2024-01-15 | 初始版本 |
| v1.1.0 | 2024-01-20 | 新增更新用户信息接口 |

---
最后更新: 2024-01-20
