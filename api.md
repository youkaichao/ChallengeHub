这篇文档还在施工中 da☆ze

- [1. 前后端数据交互接口设计](#1-%E5%89%8D%E5%90%8E%E7%AB%AF%E6%95%B0%E6%8D%AE%E4%BA%A4%E4%BA%92%E6%8E%A5%E5%8F%A3%E8%AE%BE%E8%AE%A1)
- [2. 具体接口](#2-%E5%85%B7%E4%BD%93%E6%8E%A5%E5%8F%A3)
  - [已完成](#%E5%B7%B2%E5%AE%8C%E6%88%90)
    - [GET /api/contests](#get-apicontests)
    - [POST /api/contests](#post-apicontests)
    - [GET /api/contests/<id\>](#get-apicontestsid)
    - [GET /api/contests/<id\>/enroll](#get-apicontestsidenroll)
    - [POST /api/contests/<id\>/enroll](#post-apicontestsidenroll)
    - [POST /auth/login/](#post-authlogin)
    - [POST /auth/register/](#post-authregister)
    - [POST /auth/logout/](#post-authlogout)
  - [未完成](#%E6%9C%AA%E5%AE%8C%E6%88%90)
    - [GET /api/contests/<contest-id>/submissions&status=unfinished](#get-apicontestscontest-idsubmissionsstatusunfinished)
    - [GET /api/contests/<contest-id>/submissions/<submission_id>](#get-apicontestscontest-idsubmissionssubmissionid)
    - [PUT /api/contests/<contest-id>/submissions/<submission_id>](#put-apicontestscontest-idsubmissionssubmissionid)
    - [POST /api/contests/<contest-id>/reviewers](#post-apicontestscontest-idreviewers)
    - [POST /api/contests/<contest-id>/allocate](#post-apicontestscontest-idallocate)
    - [POST /api/contests/<contest-id>/reviewers/adjust?username=username&num=num](#post-apicontestscontest-idreviewersadjustusernameusernamenumnum)
    - [GET /users?type=[organization | contestant]](#get-userstypeorganization--contestant)
    - [POST /users](#post-users)
    - [GET /users/<username\>](#get-usersusername)
    - [GET /groups](#get-groups)
    - [POST /groups](#post-groups)
    - [POST /groups/<group_id>/submission](#post-groupsgroupidsubmission)
    - [GET /groups/?contest=id](#get-groupscontestid)
    - [GET /notices/?contest=id](#get-noticescontestid)
    - [POST /notices/?contest=id](#post-noticescontestid)
    - [POST /groups/?status=type](#post-groupsstatustype)

# 1. 前后端数据交互接口设计

后端返回的是json对象, 格式为:

```javascript
{
  code: int,
  error: str,
  data: object,
}
```

其中 `code === 0` 表示请求正常, 此时 `data` 里面保存的是返回的数据. `code !== 0` 表示请求有误, 具体的错误消息在 `error` 中.

**下面的描述中, 只需要描述 `data` 域的结构**

# 2. 具体接口


## 已完成

***
***

### GET /api/contests

权限要求: 无

功能描述: 返回所有比赛

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
    upvote: int,
    downvote: int,
    publisher: str,
  }
]
```

***

### POST /api/contests

权限要求: 组织者账户, 已登录

功能描述: 创建一个比赛

传入参数:

```javascript
{
  name: str,
  subject: str,
  groupSize: int,
  enrollStart: str,
  enrollEnd: str,
  detail: str,
  procedure: str,
  url: str,
  charge: int,
  publisher: str,
}
```

返回数据: 无

***

### GET /api/contests/<id\>

权限要求: 已登录

功能描述: 获取一个比赛的详情

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
  detail: str,
  procedure: str,
  url: str,
  charge: int,
  upvote: int,
  downvote: int,
  publisher: str,
}
```

***

### GET /api/contests/<id\>/enroll

权限要求: 已登录

功能描述: 获得报名信息

传入参数: 无

返回数据:

```
{
  enrollForm: str
}
```

***

### POST /api/contests/<id\>/enroll

权限要求: 个人账户, 已登录

功能描述: 报名比赛

传入参数:

```javascript
{
  name: str,
  leaderName: str,
  members: [str],
  form: str,
}
```

返回数据: 无

其中 `members` 字段是队伍成员用户名的列表, `form` 字段是队伍填写的报名表单的 json

***

### POST /auth/login/

权限要求: 无

功能描述: 登录

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

***

### POST /auth/register/

权限要求: 无

功能描述: 注册

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

***

### POST /auth/logout/

权限要求: 已登录

功能描述: 登出

传入参数: 无

返回数据: 无

***

## 未完成


***
***

### GET /api/contests/<contest-id>/submissions&status=unfinished

获得比赛的所有提交文件信息（评委使用）

***

### GET /api/contests/<contest-id>/submissions/<submission_id>

获得比赛的某一个提交文件（有权限限制）（评委使用）

***

### PUT /api/contests/<contest-id>/submissions/<submission_id>

更新比赛的某一个提交文件的打分（评委使用）

***

### POST /api/contests/<contest-id>/reviewers

为比赛添加评委

***

### POST /api/contests/<contest-id>/allocate

为比赛自动分配评委

***

### POST /api/contests/<contest-id>/reviewers/adjust?username=username&num=num

为某个评委调整需要评的作品数

***

### GET /users?type=[organization | contestant]

TBD

***

### POST /users

TBD

***

### GET /users/<username\>

TBD

***

### GET /groups

TBD

***

### POST /groups

TBD

***

### POST /groups/<group_id>/submission

提交比赛文件

***

### GET /groups/?contest=id

参加某比赛的所有群组

***

### GET /notices/?contest=id

获取某比赛的所有公告

***

### POST /notices/?contest=id

创建一个比赛公告

***

### POST /groups/?status=type

修改一个队伍在其比赛中的状态(阶段)，如让一支队伍进入复赛

***