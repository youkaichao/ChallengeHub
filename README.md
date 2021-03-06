[![Build Status](https://travis-ci.com/AerysNan/ChallengeHub.svg?token=UB5Xzp6dhS72fDX13on9&branch=master)](https://travis-ci.com/AerysNan/ubiquitous-potato)
[![code style: prettier](https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square)](https://github.com/prettier/prettier)
[![Open Source Love](https://badges.frapsoft.com/os/v2/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![MIT Licence](https://badges.frapsoft.com/os/mit/mit.svg?v=103)](https://opensource.org/licenses/mit-license.php)
# ChallengeHub

ChallengeHub 是一个面向大学生的竞赛平台.

## 前端构建

进入 frontend/ 目录

- 安装构建需要的包, 执行命令 `npm install` .
- 在开发模式下构建, 执行命令 `npm run serve` .
- 在生产模式下构建, 执行命令 `npm run build` .
- 进行前端单元测试, 执行命令 `npm run test` .
- 检查代码风格规范, 执行命令 `npm run lint` .

## 后端构建

在根目录执行命令 `python manage.py runserver` 启动 Django 服务器.

## 部署方法

执行 `npm run build` 后

`docker build -t challenge .`
`docker-compose up -d`

需要 `docker-compose.yml` 文件