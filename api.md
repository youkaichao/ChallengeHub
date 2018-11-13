这篇文档还在施工中 da☆ze

- [1. 前后端数据交互接口设计](#1-%E5%89%8D%E5%90%8E%E7%AB%AF%E6%95%B0%E6%8D%AE%E4%BA%A4%E4%BA%92%E6%8E%A5%E5%8F%A3%E8%AE%BE%E8%AE%A1)
- [2. 具体接口](#2-%E5%85%B7%E4%BD%93%E6%8E%A5%E5%8F%A3)
  - [已完成](#%E5%B7%B2%E5%AE%8C%E6%88%90)
    - [GET /api/contests](#get-apicontests)
    - [POST /api/contests](#post-apicontests)
    - [GET /api/contests/<id\>](#get-apicontestsid)
    - [GET /api/contests/<id\>/enroll](#get-apicontestsidenroll)
    - [GET /api/contests/<id\>/stage](#get-apicontestsidstage)
    - [POST /api/contests/<id\>/stage](#post-apicontestsidstage)
    - [GET /api/contests/<id\>/groups](#get-apicontestsidgroups)
    - [POST /api/contests/<id\>/groups](#post-apicontestsidgroups)
    - [POST /api/contests/<id\>/enroll](#post-apicontestsidenroll)
    - [GET /api/users](#get-apiusers)
    - [GET /api/users/<username\>](#get-apiusersusername)
    - [GET /api/users/created](#get-apiuserscreated)
    - [GET /api/users/enrolled](#get-apiusersenrolled)
    - [GET /users/judged](#get-usersjudged)
    - [POST /auth/login/](#post-authlogin)
    - [POST /auth/register/](#post-authregister)
    - [POST /auth/logout/](#post-authlogout)
    - [POST /auth/info](#post-authinfo)
  - [未完成](#%E6%9C%AA%E5%AE%8C%E6%88%90)
    - [GET /api/contests/<contest-id\>/submissions&status=unfinished](#get-apicontestscontest-idsubmissionsstatusunfinished)
    - [GET /api/contests/<contest-id\>/submissions/<submission_id\>](#get-apicontestscontest-idsubmissionssubmissionid)
    - [PUT /api/contests/<contest-id\>/submissions/<submission_id\>](#put-apicontestscontest-idsubmissionssubmissionid)
    - [POST /api/contests/<contest-id\>/reviewers](#post-apicontestscontest-idreviewers)
    - [POST /api/contests/<contest-id\>/allocate](#post-apicontestscontest-idallocate)
    - [POST /api/contests/<contest-id\>/reviewers/adjust?username=username&num=num](#post-apicontestscontest-idreviewersadjustusernameusernamenumnum)
    - [POST /groups/<group_id\>/submission](#post-groupsgroupidsubmission)
    - [GET /groups/?contest=id](#get-groupscontestid)
    - [GET /notices/?contest=id](#get-noticescontestid)
    - [POST /notices/?contest=id](#post-noticescontestid)

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

# 1. 返回数据格式说明（详细格式与简略格式）

``notice`` 和 ``contest`` 的返回格式有简略格式和具体格式两种，具体格式中，``notice``会有公告详情（key为content）, ``contest``会有比赛细节（key为detail）.
其他具体的域见models中的``to_dict``定义

# 2. 具体接口

## 已完成

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
contest 的简略版信息
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
  enrollUrl: str,
  imgUrl: str,
  charge: int,
  publisher: str,
}
```

返回数据: 无

### GET /api/contests/enrolled

权限要求: 

功能描述: 获取用户参加的比赛

传入参数:

```javascript
{
  username: str
}
```

返回数据: 空

```javascript
[
{
    group : group 的简略版信息,
    contest: contest 的简略版信息
}
]
```

***

### GET /api/contests/<id\>

权限要求: 已登录

功能描述: 获取一个比赛的详情

传入参数: 无

返回数据:

```javascript
{
contest 的详细版信息
}
```

------

### POST /api/contests/<id\>

权限要求: 已登录

功能描述: 修改一个比赛的阶段

传入参数: 

```javascript
{
  stage:int
}
```

返回数据:无

***

### GET /api/contests/<id\>/enroll

权限要求: 已登录

功能描述: 获得报名信息

传入参数: 无

返回数据:

```javascript
{
  enrollForm: str
}
```

***

### GET /api/contests/<id\>/groups

权限要求: 已登录

功能描述: 获得一个比赛所有队伍的信息

传入参数: 无

返回数据:

```javascript
[
group 的信息
]
```

***

### POST /api/contests/<id\>/groups

权限要求: 已登录

功能描述: 修改一个比赛某些队伍的阶段

传入参数:

```javascript
{
  group_ids: [int],
  stage: int
}
```

返回数据: 无

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

### GET /api/users

权限要求: 已登录

功能描述: 获取所有的个人/机构账号

传入参数:

```javascript
{
  type: str,
}
```

返回参数:

```javascript
[
  {
    username: str,
    firstName: str,
    lastName: str,
    email: str,
    introduction: str,
    school: str,
    isIndividual: bool
  }
]
```

其中 `type` 为 `individual` 表示获取个人账号, `organization` 表示获取机构账号

***

### GET /api/users/<username\>

权限要求: 已登录

功能描述: 获取用户详细信息

传入参数: 无

返回参数:

```javascript
{
  username: str,
  firstName: str,
  lastName: str,
  email: str,
  introduction: str,
  school: str,
  isIndividual: bool,
}
```

***

### GET /api/users/created

权限要求: 已登录

功能描述: 获取用户创建的比赛

传入参数:
```javascript
{
  username: str,
}
```
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
    procedure: str,
    enrollUrl: str,
    imgUrl: str,
    charge: int,
    upvote: int,
    downvote: int,
    publisher: str,
  }
]
```

***

### GET /users/judged

权限要求: 已登录

功能描述: 获取用户评审的比赛

传入参数:

```javascript
{
  username: str,
}
```

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
    procedure: str,
    enrollUrl: str,
    imgUrl: str,
    charge: int,
    upvote: int,
    downvote: int,
    publisher: str,
  }
]
```

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

### POST /auth/info

权限要求: 已登录

功能描述: 获取用户信息

传入参数:

```javascript
{
  username: str,
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

## 未完成

### GET /api/contests/<contest-id\>/submissions&status=unfinished

获得比赛的所有提交文件信息

***

### GET /api/contests/<contest-id\>/submissions/<submission_id\>

获得比赛的某一个提交文件

***

### PUT /api/contests/<contest-id\>/submissions/<submission_id\>

更新比赛的某一个提交文件的打分

***

### POST /api/contests/<contest-id\>/reviewers

为比赛添加评委

***

### POST /api/contests/<contest-id\>/allocate

为比赛自动分配评委

***

### POST /api/contests/<contest-id\>/reviewers/adjust?username=username&num=num

为某个评委调整需要评的作品数

***

### POST /groups/<group_id\>/submission

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
