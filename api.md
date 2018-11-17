- [1. 前后端数据交互接口设计](#1-%E5%89%8D%E5%90%8E%E7%AB%AF%E6%95%B0%E6%8D%AE%E4%BA%A4%E4%BA%92%E6%8E%A5%E5%8F%A3%E8%AE%BE%E8%AE%A1)
- [1. 返回数据格式说明(详细格式与简略格式)](#1-%E8%BF%94%E5%9B%9E%E6%95%B0%E6%8D%AE%E6%A0%BC%E5%BC%8F%E8%AF%B4%E6%98%8E%E8%AF%A6%E7%BB%86%E6%A0%BC%E5%BC%8F%E4%B8%8E%E7%AE%80%E7%95%A5%E6%A0%BC%E5%BC%8F)
- [2. 具体接口](#2-%E5%85%B7%E4%BD%93%E6%8E%A5%E5%8F%A3)
  - [已完成](#%E5%B7%B2%E5%AE%8C%E6%88%90)
    - [GET /api/contests: 返回所有比赛](#get-apicontests-%E8%BF%94%E5%9B%9E%E6%89%80%E6%9C%89%E6%AF%94%E8%B5%9B)
    - [POST /api/contests: 创建一个比赛](#post-apicontests-%E5%88%9B%E5%BB%BA%E4%B8%80%E4%B8%AA%E6%AF%94%E8%B5%9B)
    - [GET /api/contests/<id\>: 获取一个比赛的详情](#get-apicontestsid-%E8%8E%B7%E5%8F%96%E4%B8%80%E4%B8%AA%E6%AF%94%E8%B5%9B%E7%9A%84%E8%AF%A6%E6%83%85)
    - [POST /api/contests/<id\>: 修改一个比赛的阶段](#post-apicontestsid-%E4%BF%AE%E6%94%B9%E4%B8%80%E4%B8%AA%E6%AF%94%E8%B5%9B%E7%9A%84%E9%98%B6%E6%AE%B5)
    - [GET /api/contests/<id\>/enroll: 获得比赛的报名表单](#get-apicontestsidenroll-%E8%8E%B7%E5%BE%97%E6%AF%94%E8%B5%9B%E7%9A%84%E6%8A%A5%E5%90%8D%E8%A1%A8%E5%8D%95)
    - [POST /api/contests/<id\>/enroll: 报名比赛](#post-apicontestsidenroll-%E6%8A%A5%E5%90%8D%E6%AF%94%E8%B5%9B)
    - [GET /api/contests/<id\>/groups: 获得一个比赛所有队伍的信息](#get-apicontestsidgroups-%E8%8E%B7%E5%BE%97%E4%B8%80%E4%B8%AA%E6%AF%94%E8%B5%9B%E6%89%80%E6%9C%89%E9%98%9F%E4%BC%8D%E7%9A%84%E4%BF%A1%E6%81%AF)
    - [POST /api/contests/<id\>/groups: 修改一个比赛某些队伍的阶段](#post-apicontestsidgroups-%E4%BF%AE%E6%94%B9%E4%B8%80%E4%B8%AA%E6%AF%94%E8%B5%9B%E6%9F%90%E4%BA%9B%E9%98%9F%E4%BC%8D%E7%9A%84%E9%98%B6%E6%AE%B5)
    - [GET /api/users/enrolled: 获取用户参加的所有比赛](#get-apiusersenrolled-%E8%8E%B7%E5%8F%96%E7%94%A8%E6%88%B7%E5%8F%82%E5%8A%A0%E7%9A%84%E6%89%80%E6%9C%89%E6%AF%94%E8%B5%9B)
    - [GET /api/users/created: 获取用户创建的比赛](#get-apiuserscreated-%E8%8E%B7%E5%8F%96%E7%94%A8%E6%88%B7%E5%88%9B%E5%BB%BA%E7%9A%84%E6%AF%94%E8%B5%9B)
    - [GET /api/users/judged: 获取用户评审的比赛](#get-apiusersjudged-%E8%8E%B7%E5%8F%96%E7%94%A8%E6%88%B7%E8%AF%84%E5%AE%A1%E7%9A%84%E6%AF%94%E8%B5%9B)
    - [GET /api/contests/<id\>/submission: 获得本队在比赛中某阶段的提交](#get-apicontestsidsubmission-%E8%8E%B7%E5%BE%97%E6%9C%AC%E9%98%9F%E5%9C%A8%E6%AF%94%E8%B5%9B%E4%B8%AD%E6%9F%90%E9%98%B6%E6%AE%B5%E7%9A%84%E6%8F%90%E4%BA%A4)
    - [POST /api/contests/<id\>/submission: 提交比赛作品](#post-apicontestsidsubmission-%E6%8F%90%E4%BA%A4%E6%AF%94%E8%B5%9B%E4%BD%9C%E5%93%81)
    - [GET /api/judges/<id\>: 获得某比赛某阶段的评审信息](#get-apijudgesid-%E8%8E%B7%E5%BE%97%E6%9F%90%E6%AF%94%E8%B5%9B%E6%9F%90%E9%98%B6%E6%AE%B5%E7%9A%84%E8%AF%84%E5%AE%A1%E4%BF%A1%E6%81%AF)
    - [POST /api/judges/<id\>: 评委打分](#post-apijudgesid-%E8%AF%84%E5%A7%94%E6%89%93%E5%88%86)
    - [POST /auth/login: 登录](#post-authlogin-%E7%99%BB%E5%BD%95)
    - [POST /auth/register: 注册](#post-authregister-%E6%B3%A8%E5%86%8C)
    - [POST /auth/logout: 登出](#post-authlogout-%E7%99%BB%E5%87%BA)
    - [POST /auth/info: 获取用户信息](#post-authinfo-%E8%8E%B7%E5%8F%96%E7%94%A8%E6%88%B7%E4%BF%A1%E6%81%AF)
  - [未完成](#%E6%9C%AA%E5%AE%8C%E6%88%90)

# 1. 前后端数据交互接口设计

后端返回的是 json 对象, 格式为:

```javascript
{
  code: int,
  error: str,
  data: object,
}
```

其中 `code === 0` 表示请求正常, 此时 `data` 里面保存的是返回的数据. `code !== 0` 表示请求有误, 具体的错误消息在 `error` 中.

**下面的描述中, 只需要描述 `data` 域的结构**

# 1. 返回数据格式说明(详细格式与简略格式)

`notice` 和 `contest` 的返回格式有简略格式和具体格式两种, 具体格式中, `notice`会有公告详情(key 为 content ), `contest` 会有比赛细节(key 为 detail).
其他具体的域见 models 中的 `to_dict` 定义

# 2. 具体接口

## 已完成

### GET  /api/contests: 返回所有比赛

权限要求: 无

传入参数:

1. `search` 比赛名称关键词
2. `subject` 比赛学科
3. `status` 比赛进行状态
4. `groupsize` 比赛队伍人数
5. `user` 比赛参赛人员名称
6. `judge` 比赛的评委
7. `sortby` 比赛排序依据
8. `from, to` 排序后的开始索引与结束索引

返回数据:

```javascript
[
  {
    id: int,
    name: str,
    subject: str,
    groupSize: int,
    enrollStart: str,
    enrollEnd: str,
    imgUrl: str,
    enrollUrl: str,
    charge: int,
    upvote: int,
    downvote: int,
    stage: int,
    procedure: [
      {
        name: str,
        startTime: str,
        endTime: str,
        stage: int,
      }
    ],
  }
]
```

---

### POST /api/contests: 创建一个比赛

权限要求: 组织者账户, 已登录

传入参数:

```javascript
{
  name: str,
  subject: str,
  groupSize: int,
  enrollStart: str,
  enrollEnd: str,
  detail: str,
  procedure: [
    {
      name: str,
      startTime: str,
      endTime: str,
    }
  ],
  enrollUrl: str,
  imgUrl: str,
  charge: int,
  publisher: str,
}
```

返回数据: 无

---

### GET /api/contests/<id\>: 获取一个比赛的详情

权限要求: 已登录

传入参数: 无

返回数据:

```javascript
{
  id: int,
  name: str,
  subject: str,
  groupSize: int,
  enrollStart: str,
  enrollEnd: str,
  imgUrl: str,
  enrollUrl: str,
  charge: int,
  upvote: int,
  downvote: int,
  publisher: str,
  stage: int,
  procedure: [
    {
      name: str,
      startTime: str,
      endTime: str,
      stage: int,
    }
  ],
  detail: str,
}
```

---

### POST /api/contests/<id\>: 修改一个比赛的阶段

权限要求: 已登录

传入参数:

```javascript
{
  stage: int
}
```

返回数据: 无

---

### GET /api/contests/<id\>/enroll: 获得比赛的报名表单

权限要求: 已登录

传入参数: 无

返回数据:

```javascript
{
  enrollForm: json
}
```

---

### POST /api/contests/<id\>/enroll: 报名比赛

权限要求: 个人账户, 已登录

传入参数:

```javascript
{
  name: str,
  leaderName: str,
  members: [str],
  form: json,
}
```

返回数据: 无

---

### GET /api/contests/<id\>/groups: 获得一个比赛所有队伍的信息

权限要求: 已登录

传入参数: 无

返回数据:

```javascript
[
  {
    id: int,
    name: str,
    competitionId: int,
    competitionName: str,
    hasCommit: bool,
    leaderName: int,
    membersName: [int],
    rank: str,
    stage: int
  }
]
```

---

### POST /api/contests/<id\>/groups: 修改一个比赛某些队伍的阶段

权限要求: 已登录

传入参数:

```javascript
{
  group_ids: [int],
  stage: int
}
```

返回数据: 无

---

### GET /api/users/enrolled: 获取用户参加的所有比赛

权限要求: 无

返回数据: 无

```javascript
[
  {
    group: {
      id: int,
      name: str,
      competitionId: int,
      competitionName: str,
      hasCommit: bool,
      leaderName: int,
      membersName: [int],
      rank: str,
      stage: int
    },
    contest: {
      id: int,
      name: str,
      subject: str,
      groupSize: int,
      enrollStart: str,
      enrollEnd: str,
      imgUrl: str,
      enrollUrl: str,
      charge: int,
      upvote: int,
      downvote: int,
      publisher: str,
      stage: int,
      procedure: [
        {
          name: str,
          startTime: str,
          endTime: str,
          stage: int,
        }
      ],
    },
  }
]
```

---

### GET  /api/users/created: 获取用户创建的比赛

权限要求: 已登录

传入参数: 无

返回参数:

```javascript
[
  {
    id: int,
    name: str,
    subject: str,
    groupSize: int,
    enrollStart: str,
    enrollEnd: str,
    detail: str,
    procedure: [
      {
        name: str,
        startTime: str,
        endTime: str,
        stage: int,
      }
    ],
    enrollUrl: str,
    imgUrl: str,
    charge: int,
    upvote: int,
    downvote: int,
    publisher: str
  }
]
```

---

### GET /api/users/judged: 获取用户评审的比赛

权限要求: 已登录

传入参数: 无

返回参数:

```javascript
[
  task: {
    count: int
    done: int
  },
  contest: {
    id: int,
    name: str,
    subject: str,
    groupSize: int,
    enrollStart: str,
    enrollEnd: str,
    detail: str,
    procedure: [
      {
        name: str,
        startTime: str,
        endTime: str,
        stage: int,
      }
    ],
    enrollUrl: str,
    imgUrl: str,
    charge: int,
    upvote: int,
    downvote: int,
    publisher: str
  }
]
```

---

### GET /api/contests/<id\>/submission: 获得本队在比赛中某阶段的提交

权限要求: 已登录

传入参数:

```javascript
{
  stage: int?
}
```

返回数据:

```javascript
{
  submissionName: str,
  url: str
}
```

如果没有指定 `stage`, 则默认返回最新阶段的提交

---

### POST /api/contests/<id\>/submission: 提交比赛作品

权限要求: 个人账户, 已登陆

传入参数: 格式为 FormData

```javascript
{
  file: object,
  submissionName: str,
}
```

返回参数: 无

---

### GET /api/judges/<id\>: 获得某比赛某阶段的评审信息

权限要求: 已登录

传入参数:

```javascript
{
  stage: int?
}
```

返回数据:

```javascript
{
  contest: {
    id: int,
    name: str,
    subject: str,
    groupSize: int,
    enrollStart: str,
    enrollEnd: str,
    detail: str,
    procedure: [
      {
        name: str,
        startTime: str,
        endTime: str,
        stage: int,
      }
    ],
    enrollUrl: str,
    imgUrl: str,
    charge: int,
    upvote: int,
    downvote: int,
    publisher: str
  },
  task: {
    count: int,
    done: int
  },
  submissions: [
    {
      id: int,
      submissionName: str,
      reviewed: bool,
      rating: int,
      url: str
    }
  ]
}
```

---

### POST /api/judges/<id\>: 评委打分

权限要求: 已登录

传入参数:

```javascript
{
  reviews: [
    {
      id: int,
      reviewed: bool,
      rating: int
    }
  ]
}
```
返回参数: 无

---

### POST /auth/login: 登录

权限要求: 无

传入参数:

```javascript
{
  username: str,
  password: str,
}
```

返回数据:

```javascript
{
  username: str,
  email: str,
  introduction: str,
  school: str,
  individual: int,
}
```

---

### POST /auth/register: 注册

权限要求: 无

传入参数:

```javascript
{
  username: str,
  password: str,
  email: str,
  individual: int,
}
```

返回数据:

```javascript
{
  username: str,
  email: str,
  introduction: str,
  school: str,
  individual: int,
}
```

---

### POST /auth/logout: 登出

权限要求: 已登录

传入参数: 无

返回数据: 无

---

### POST /auth/info: 获取用户信息

权限要求: 已登录

传入参数: 无

返回数据:

```javascript
{
  username: str,
  email: str,
  introduction: str,
  school: str,
  individual: int,
}
```

---

## 未完成
