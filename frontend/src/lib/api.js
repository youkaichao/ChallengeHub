/* eslint-disable */
let stage = 2

export default {
  [`POST */api/contests/uploadImage`](pathMatch, query, request, passThrough) {
    return {
      body: {
        code: 0,
        error: '',
        data: {}
      },
      status: 200,
      statusText: 'OK'
    }
  },
  ['PUT */apiv2/messages']() {
    return {
      body: {
        code: 0,
        error: '',
        data: {}
      },
      status: 200,
      statusText: 'OK'
    }
  },
  ['GET */apiv2/contests/1/groups']() {
    return {
      body: {
        code: 0,
        error: '',
        data: [
          {
            teamId: 1,
            teamName: 'ahfei',
            leader: 'fjaseilgj',
            members: ['haefhi', 'asehlugiaegiase'],
            invitees: ['fzzzz', 'asaaaa'],
            locked: false
          }
        ]
      },
      status: 200,
      statusText: 'OK'
    }
  },
  ['DELETE */apiv2/messages']() {
    return {
      body: {
        code: 0,
        error: '',
        data: {}
      },
      status: 200,
      statusText: 'OK'
    }
  },
  ['GET */apiv2/messages/unread_count'](_1, _2, _3, _4) {
    return {
      body: {
        code: 0,
        error: '',
        data: {
          count: 5
        }
      },
      status: 200,
      statusText: 'OK'
    }
  },
  ['GET */apiv2/messages'](pathMatch, query, request, passThrough) {
    if (request.params.isRead === 0) {
      return {
        body: {
          code: 0,
          error: '',
          data: [
            {
              id: 1,
              sender: '群主',
              content:
                '弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？弱渣和我组队不？',
              sendTime: '2018-03-25T06:26:01.927Z',
              type: 'letter'
            },
            {
              id: 2,
              sender: 'boxer',
              content: '你获得了一个杯子',
              sendTime: '2018-03-25T06:26:01.927Z',
              type: 'system'
            },
            {
              id: 3,
              sender: 'boxer',
              content: {
                leaderName: '群神',
                groupName: '交换群',
                contestName: '咸鱼划水大赛',
                status: 0
              },
              sendTime: '2018-03-25T06:26:01.927Z',
              type: 'invitation'
            },
            {
              id: 4,
              sender: 'boxer',
              content: '你获得了一个杯子',
              sendTime: '2018-03-25T06:26:01.927Z',
              type: 'system'
            },
            {
              id: 5,
              sender: '群主',
              content: '弱渣和我组队不？',
              sendTime: '2018-03-25T06:26:01.927Z',
              type: 'letter'
            },
            {
              id: 8,
              sender: '刘强',
              content: {
                contestName: '微信小程序大赛',
                contestId: 10086,
                status: 0
              },
              sendTime: '2018-03-25T06:26:01.927Z',
              type: 'reviewer_invitation'
            }
          ]
        },
        status: 200,
        statusText: 'OK'
      }
    } else {
      return {
        body: {
          code: 0,
          error: '',
          data: [
            {
              id: 10,
              sender: '群主',
              content: '弱渣和我组队不？',
              sendTime: '2018-03-25T06:26:01.927Z',
              type: 'letter'
            },
            {
              id: 50,
              sender: '群主',
              content: '弱渣和我组队不？',
              sendTime: '2018-03-25T06:26:01.927Z',
              type: 'letter'
            }
          ]
        },
        status: 200,
        statusText: 'OK'
      }
    }
  },
  ['POST */apiv2/contests/10086/reviewers/response'](_1, _2, _3, _4) {
    return {
      body: {
        code: 0,
        error: '',
        data: {}
      },
      status: 200,
      statusText: 'OK'
    }
  },
  ['GET */api/contests/1'](pathMatch, query, request, passThrough) {
    return {
      body: {
        code: 0,
        error: '',
        data: {
          id: 1,
          name: '咸鱼划水大赛',
          subject: '体育',
          groupSize: 4,
          enrollStart: '2015-03-25T06:26:01.927Z',
          enrollEnd: '2019-03-25T06:26:01.927Z',
          procedure: [
            { name: '初赛', startTime: '2014-03-25T06:26:01.927Z', endTime: '2018-03-25T06:26:01.927Z' },
            { name: '复赛', startTime: '2018-06-25T06:26:01.927Z', endTime: '2019-03-25T06:26:01.927Z' }
          ],
          imgUrl: 'https://picsum.photos/400/300/?random&amp;k=23rfewg',
          enrollUrl: '',
          charge: 100,
          upvote: 200,
          downvote: 300,
          publisher: '华清大学',
          detail: '# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功',
          userRelated: {
            upvoteStatus: 0
          }
        }
      },
      status: 200,
      statusText: 'OK'
    }
  },
  ['POST */api/contests/1/vote'](pathMatch, query, request, passThrough) {
    return {
      body: {
        code: 0,
        error: '',
        data: {
          upvote: 444,
          downvote: 666,
          upvoteStatus: 1
        }
      },
      status: 200,
      statusText: 'OK'
    }
  },
  ['GET */api/contests/1/notices/3'](pathMatch, query, request, passThrough) {
    return {
      body: {
        code: 0,
        error: '',
        data: {
          id: 3,
          competitionId: 7,
          competitionName: '吃垃圾大赛',
          modifiedTime: '2019-03-25T06:26:01.927Z',
          title: '请选手吃垃圾！',
          content:
            '# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功\n\n# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功\n\n# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功\n\n# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功\n\n# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功\n\n# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功\n\n# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功\n\n# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功\n\n# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功\n\n# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功\n\n# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功\n\n# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功\n\n# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功\n\n# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功\n\n# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功\n\n# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功\n\n# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功\n\n# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功\n\n# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功\n\n# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功\n\n# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功\n\n# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功\n\n# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功\n\n# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功\n\n# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功\n\n# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功\n\n# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功\n\n# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功\n\n# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功\n\n# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功\n\n# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功\n\n# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功\n\n# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功\n\n# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功\n\n# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功\n\n# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功\n\n# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功\n\n# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功\n\n# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功\n\n# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功\n\n# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功\n\n# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功\n\n# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功\n\n# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功\n\n# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功\n\n# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功\n\n# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功\n\n'
        }
      },
      status: 200,
      statusText: 'OK'
    }
  },
  ['GET */api/contests/1/notices'](pathMatch, query, request, passThrough) {
    return {
      body: {
        code: 0,
        error: '',
        data: {
          notices: [
            {
              id: 1,
              modifiedTime: '2019-03-25T06:26:01.927Z',
              title: '请选手吃垃圾！'
            },
            {
              id: 2,
              modifiedTime: '2019-03-25T06:26:01.927Z',
              title: '游神太强啦！'
            },
            {
              id: 3,
              modifiedTime: '2019-03-25T06:26:01.927Z',
              title: '叶神牛逼！'
            },
            {
              id: 4,
              modifiedTime: '2019-03-25T06:26:01.927Z',
              title: '请选手吃辣鸡！'
            }
          ],
          contest: {
            name: '咸鱼划水大赛',
            imgUrl: 'https://picsum.photos/400/300/?random&amp;k=2',
            publisher: '华清大学',
            standard: '# 评审标准\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持',
            procedure: [
              { name: '初赛', startTime: '2014-03-25T06:26:01.927Z', endTime: '2018-03-25T06:26:01.927Z' },
              { name: '复赛', startTime: '2018-06-25T06:26:01.927Z', endTime: '2019-03-25T06:26:01.927Z' }
            ],
            stage: 4
          }
        }
      },
      status: 200,
      statusText: 'OK'
    }
  },
  ['POST */api/contests/2345234/submission'](pathMatch, query, request, passThrough) {
    return {
      body: {
        code: 0,
        error: '',
        data: {}
      },
      status: 200,
      statusText: 'OK'
    }
  },
  ['POST */auth/login'](pathMatch, query, request, passThrough) {
    return {
      body: {
        code: 0,
        error: '',
        data: {
          username: request.body.username,
          email: `${request.body.username}@ts.com`,
          introduction: `I am a ${request.body.username}`,
          school: `${request.body.username} school`,
          individual: request.body.username !== 'organizer'
        }
      },
      status: 200,
      statusText: 'OK'
    }
  },
  ['POST */auth/register'](pathMatch, query, request, passThrough) {
    return {
      body: {
        code: 0,
        error: '',
        data: {
          username: request.body.username,
          email: `${request.body.username}@ts.com`,
          selfDescription: `I am a ${request.body.username}`,
          sourceSchool: `${request.body.username} school`,
          isIndividual: request.body.username === 'organizer'
        }
      },
      status: 200,
      statusText: 'OK'
    }
  },
  ['POST */auth/logout'](pathMatch, query, request, passThrough) {
    return {
      body: {
        code: 0,
        error: '',
        data: {}
      },
      status: 200,
      statusText: 'OK'
    }
  },
  ['POST */api/contests/1/stage'](pathMatch, query, request, passThrough) {
    stage = request.body.stage
    return {
      body: {
        code: 0,
        error: '',
        data: {}
      },
      status: 200,
      statusText: 'OK'
    }
  },
  ['GET */api/judges/2'](_1, _2, _3, _4) {
    return {
      body: {
        data: {
          contest: {
            id: 2,
            name: '2019\u5e74\u5168\u56fd\u5927\u5b66\u751f\u82f1\u8bed\u7ade\u8d5b\uff08NECCS\uff09',
            subject: '\u82f1\u8bed',
            groupSize: 5,
            enrollStart: '2018-12-24T16:00:00Z',
            enrollEnd: '2018-12-26T16:00:00Z',
            standard: '',
            imgUrl:
              'https://publicqn.saikr.com/2018/12/03/contest5c053a1bbbd6e3.395760691543846486795.png?imageView2/2/w/1080',
            enrollUrl: '',
            charge: 0,
            upvote: 0,
            downvote: 0,
            publisher: '\u8f6f\u4ef6\u5b66\u9662',
            stage: 0,
            procedure: [
              { name: '\u521d\u8d5b', startTime: '2019-03-31', endTime: '2019-04-29', stage: 1, isAssigned: false },
              { name: '\u51b3\u8d5b', startTime: '2019-08-31', endTime: '2019-09-29', stage: 3, isAssigned: false }
            ]
          },
          task: { count: 0, done: 0 },
          submissions: []
        },
        code: 0
      },
      status: 200,
      statusText: 'OK'
    }
  },
  ['GET */api/judges/1'](pathMatch, query, request, passThrough) {
    return {
      body: {
        code: 0,
        error: '',
        data: {
          contest: {
            id: 1,
            name: '咸鱼划水大赛',
            imgUrl: 'https://picsum.photos/20/20/?random&amp;k=2',
            publisher: '华清大学',
            standard: '# 评审标准\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持',
            procedure: [
              { name: '初赛', startTime: '2014-03-25T06:26:01.927Z', endTime: '2018-03-25T06:26:01.927Z' },
              { name: '复赛', startTime: '2018-06-25T06:26:01.927Z', endTime: '2019-03-25T06:26:01.927Z' }
            ],
            stage: 0
          },
          task: {
            count: 9,
            done: 3
          },
          submissions: [
            {
              id: 19998,
              submissionName: '网络又忽起',
              reviewed: true,
              rating: 12,
              url: 'http://www.baidu.com',
              extension: 'html',
              msg: '牛逼',
              groupName: '群主牛逼组'
            },
            {
              id: 19998,
              submissionName: '网络又忽起',
              reviewed: true,
              rating: 38,
              url: 'http://www.baidu.com',
              extension: 'html',
              msg: '牛逼',
              groupName: '群主牛逼组'
            },
            {
              id: 19998,
              submissionName: '网络又忽起',
              reviewed: true,
              rating: 80,
              url: 'http://www.baidu.com',
              extension: 'html',
              msg: '牛逼',
              groupName: '群主牛逼组'
            },
            {
              id: 19998,
              submissionName: '网络又忽起',
              reviewed: false,
              rating: 0,
              url: 'http://www.baidu.com',
              extension: 'html',
              msg: '牛逼',
              groupName: '群主牛逼组'
            },
            {
              id: 19998,
              submissionName: '网络又忽起',
              reviewed: false,
              rating: 0,
              url: 'http://www.baidu.com',
              extension: 'html',
              msg: '牛逼',
              groupName: '群主牛逼组'
            },
            {
              id: 19998,
              submissionName: '网络又忽起',
              reviewed: false,
              rating: 0,
              url: 'http://www.baidu.com',
              extension: 'html',
              msg: '牛逼',
              groupName: '群主牛逼组'
            },
            {
              id: 19998,
              submissionName: '网络又忽起',
              reviewed: false,
              rating: 0,
              url: 'http://www.baidu.com',
              extension: 'html',
              msg: '牛逼',
              groupName: '群主牛逼组'
            },
            {
              id: 19998,
              submissionName: '网络又忽起',
              reviewed: false,
              rating: 0,
              url: 'http://www.baidu.com',
              extension: 'html',
              msg: '牛逼',
              groupName: '群主牛逼组'
            },
            {
              id: 19998,
              submissionName: '网络又忽起',
              reviewed: false,
              rating: 0,
              url: 'http://www.baidu.com',
              extension: 'html',
              msg: '牛逼',
              groupName: '群主牛逼组'
            },
            {
              id: 19998,
              submissionName: '网络又忽起',
              reviewed: false,
              rating: 0,
              url: 'http://www.baidu.com',
              extension: 'html',
              msg: '牛逼',
              groupName: '群主牛逼组'
            },
            {
              id: 19998,
              submissionName: '网络又忽起',
              reviewed: false,
              rating: 0,
              url: 'http://www.baidu.com',
              extension: 'html',
              msg: '牛逼',
              groupName: '群主牛逼组'
            },
            {
              id: 19998,
              submissionName: '网络又忽起',
              reviewed: false,
              rating: 0,
              url: 'http://www.baidu.com',
              extension: 'html',
              msg: '牛逼',
              groupName: '群主牛逼组'
            }
          ]
        }
      },
      status: 200,
      statusText: 'OK'
    }
  },
  ['GET */api/contests/1/enroll'](_1, _2, _3, _4) {
    return {
      body: {
        code: 0,
        error: '',
        data: {
          enrollForm: `[
            { "label": "性取向", "description": "你的性取向", "formType": "文字题" },
            { "label": "你喜欢吃垃圾吗", "formType": "选择题", "options": ["喜欢", "不喜欢"] },
            { "label": "你吃过几次垃圾", "formType": "选择题", "options": ["1", "2", "3"] },
            { "label": "你喜欢吃什么类型的垃圾", "description": "填写垃圾的名字", "formType": "文字题" }
          ]`
        }
      },
      status: 200,
      statusText: 'OK'
    }
  },
  ['GET */api/judges/1&stage=4'](pathMatch, query, request, passThrough) {
    return {
      body: {
        code: 0,
        error: '',
        data: {
          contest: {
            id: 1,
            name: '咸鱼划水大赛',
            imgUrl: 'https://picsum.photos/400/300/?random&amp;k=2',
            publisher: '华清大学',
            standard: '# 评审标准\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持',
            procedure: [
              { name: '初赛', startTime: '2014-03-25T06:26:01.927Z', endTime: '2018-03-25T06:26:01.927Z' },
              { name: '复赛', startTime: '2018-06-25T06:26:01.927Z', endTime: '2019-03-25T06:26:01.927Z' }
            ],
            stage: 4
          },
          task: {
            count: 9,
            done: 3
          },
          submissions: [
            {
              id: 1,
              title: '网络优化器',
              reviewed: true,
              rating: 83,
              groupName: '群神小组',
              msg: '群主牛逼！'
            },
            {
              id: 2,
              title: '网络优化器',
              reviewed: true,
              groupName: '群神小组',
              rating: 78,
              msg: '群主太强了！'
            },
            {
              id: 2,
              title: '网络优化器',
              reviewed: true,
              groupName: '群神小组',
              rating: 94,
              msg: '群主好厉害！'
            },
            {
              id: 2,
              title: '网络优化器',
              groupName: '群神小组',
              reviewed: false,
              rating: 0,
              msg: ''
            },
            {
              id: 2,
              groupName: '群神小组',
              title: '网络优化器',
              reviewed: false,
              rating: 0,
              msg: ''
            },
            {
              id: 2,
              title: '网络优化器',
              reviewed: false,
              groupName: '群神小组',
              rating: 0,
              msg: ''
            },
            {
              id: 2,
              title: '网络优化器',
              reviewed: false,
              groupName: '群神小组',
              rating: 0,
              msg: ''
            },
            {
              id: 2,
              title: '网络优化器',
              reviewed: false,
              groupName: '群神小组',
              rating: 0,
              msg: ''
            },
            {
              id: 2,
              title: '网络优化器',
              reviewed: false,
              groupName: '群神小组',
              rating: 0,
              msg: ''
            }
          ]
        }
      },
      status: 200,
      statusText: 'OK'
    }
  },
  ['GET */api/judges/1&stage=2'](pathMatch, query, request, passThrough) {
    return {
      body: {
        code: 0,
        error: '',
        data: {
          contest: {
            name: '咸鱼划水大赛',
            imgUrl: 'https://picsum.photos/400/300/?random&amp;k=2',
            publisher: '华清大学',
            standard: '# 评审标准\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持',
            procedure: [
              { name: '初赛', startTime: '2014-03-25T06:26:01.927Z', endTime: '2018-03-25T06:26:01.927Z' },
              { name: '复赛', startTime: '2018-06-25T06:26:01.927Z', endTime: '2019-03-25T06:26:01.927Z' }
            ],
            stage: 4
          },
          task: {
            count: 4,
            done: 3
          },
          submissions: [
            {
              groupName: '群神小组',
              title: '吃垃圾教程',
              reviewed: true,
              rating: 83,
              msg: '要不怎么说你屌呢？'
            },
            {
              title: '吃垃圾教程',
              reviewed: true,
              rating: 78,
              groupName: '群神小组',
              msg: '要不怎么说你巨呢？'
            },
            {
              title: '吃垃圾教程',
              groupName: '群神小组',
              reviewed: true,
              rating: 94,
              msg: '要不怎么说你强呢？'
            },
            {
              title: '吃垃圾教程',
              groupName: '群神小组',
              reviewed: false,
              rating: 0,
              msg: '要不怎么说你牛逼呢？'
            }
          ]
        }
      },
      status: 200,
      statusText: 'OK'
    }
  },
  ['GET */api/contests/567456/submissions&stage=2']() {
    return {
      body: {
        code: 0,
        error: '',
        data: {
          submissionName: '吃垃圾的中级教程',
          url: 'https://picsum.photos/200/300/?random',
          score: 123,
          reviews: [
            {
              rating: 56,
              msg:
                '你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊v'
            },
            {
              rating: 98,
              msg: '膜！'
            },
            {
              rating: 100,
              msg: '膜满分！'
            },
            {
              rating: 80,
              msg: ''
            }
          ]
        }
      },
      status: 200,
      statusText: 'OK'
    }
  },
  ['GET */api/contests/23463456/submissions&stage=2']() {
    return {
      body: {
        code: 0,
        error: '',
        data: {
          submissionName: '吃垃圾的中级教程',
          url: 'https://picsum.photos/200/300/?random',
          score: 123,
          reviews: [
            {
              rating: 56,
              msg:
                '你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊你好牛逼啊v'
            },
            {
              rating: 98,
              msg: '膜！'
            },
            {
              rating: 100,
              msg: '膜满分！'
            },
            {
              rating: 80,
              msg: ''
            }
          ]
        }
      },
      status: 200,
      statusText: 'OK'
    }
  },
  ['POST */api/judges/1'](pathMatch, query, request, passThrough) {
    return {
      body: {
        code: 1,
        error: JSON.stringify([request, passThrough])
      },
      status: 200,
      statusText: 'OK'
    }
  },
  ['POST */api/contests/1/enroll'](_1, _2, _3, _4) {
    return {
      body: {
        code: 0,
        error: '',
        data: [_1, _2, _3, _4]
      },
      status: 200,
      statusText: 'OK'
    }
  },
  ['GET */api/users/enrolled'](pathMatch, query, request, passThrough) {
    return {
      body: {
        code: 0,
        error: '',
        data: [
          {
            group: {
              id: 123,
              hasCommit: false,
              name: '咸鱼划水队',
              leaderName: 'zhang',
              rank: '0',
              submissionUrl: 'https://picsum.photos/200/300/?random',
              stage: 1
            },
            contest: {
              id: 1,
              name:
                '垃圾划水大赛垃圾划水大赛垃圾划水大赛垃圾划水大赛垃圾划水大赛垃圾划水大赛垃圾划水大赛垃圾划水大赛垃圾划水大赛垃圾划水大赛',
              imgUrl: 'https://picsum.photos/400/300/?random&amp;k=2',
              publisher: '华清大学',
              procedure: [
                { name: '初赛', startTime: '2014-03-25T06:26:01.927Z', endTime: '2018-03-25T06:26:01.927Z' },
                { name: '复赛', startTime: '2018-06-25T06:26:01.927Z', endTime: '2019-03-25T06:26:01.927Z' }
              ],
              stage: 0
            }
          },
          {
            group: {
              id: 123,
              hasCommit: false,
              name: '咸鱼划水队',
              leaderName: 'zhang',
              rank: '0',
              submissionUrl: 'https://picsum.photos/200/300/?random',
              stage: 1
            },
            contest: {
              id: 5467,
              name: '垃圾划水大赛',
              imgUrl: 'https://picsum.photos/400/300/?random&amp;k=2dfg',
              publisher: '华清大学',
              procedure: [
                { name: '初赛', startTime: '2014-03-25T06:26:01.927Z', endTime: '2018-03-25T06:26:01.927Z' },
                { name: '复赛', startTime: '2018-06-25T06:26:01.927Z', endTime: '2019-03-25T06:26:01.927Z' }
              ],
              stage: 1
            }
          },
          {
            group: {
              id: 123,
              hasCommit: true,
              name: '咸鱼划水队',
              leaderName: 'zhang',
              rank: '0',
              submissionUrl: 'https://picsum.photos/200/300/?random',
              stage: 2
            },
            contest: {
              id: 976857,
              name: '垃圾划水大赛',
              imgUrl: 'https://picsum.photos/400/300/?random&amp;k=2sdrg3',
              publisher: '华清大学',
              procedure: [
                { name: '初赛', startTime: '2014-03-25T06:26:01.927Z', endTime: '2018-03-25T06:26:01.927Z' },
                { name: '复赛', startTime: '2018-06-25T06:26:01.927Z', endTime: '2019-03-25T06:26:01.927Z' }
              ],
              stage: 2
            }
          },
          {
            group: {
              id: 123,
              hasCommit: false,
              name: '咸鱼划水队',
              leaderName: 'zhang',
              rank: '0',
              submissionUrl: 'https://picsum.photos/200/300/?random',
              stage: 3
            },
            contest: {
              id: 2345234,
              name: '垃圾划水大赛',
              imgUrl: 'https://picsum.photos/400/300/?random&amp;k=2g34gwer',
              publisher: '华清大学',
              procedure: [
                { name: '初赛', startTime: '2014-03-25T06:26:01.927Z', endTime: '2018-03-25T06:26:01.927Z' },
                { name: '复赛', startTime: '2018-06-25T06:26:01.927Z', endTime: '2019-03-25T06:26:01.927Z' }
              ],
              stage: 3
            }
          },
          {
            group: {
              id: 123,
              hasCommit: true,
              name: '咸鱼划水队',
              leaderName: 'zhang',
              rank: '0',
              submissionUrl: 'https://picsum.photos/200/300/?random',
              stage: 4
            },
            contest: {
              id: 567456,
              name: '垃圾划水大赛',
              imgUrl: 'https://picsum.photos/400/300/?random&amp;k=2ggw34g',
              publisher: '华清大学',
              procedure: [
                { name: '初赛', startTime: '2014-03-25T06:26:01.927Z', endTime: '2018-03-25T06:26:01.927Z' },
                { name: '复赛', startTime: '2018-06-25T06:26:01.927Z', endTime: '2019-03-25T06:26:01.927Z' }
              ],
              stage: 4
            }
          },
          {
            group: {
              id: 123,
              hasCommit: true,
              name: '咸鱼划水队',
              leaderName: 'zhang',
              rank: '0',
              submissionUrl: 'https://picsum.photos/200/300/?random',
              stage: 4
            },
            contest: {
              id: 23463456,
              name: '垃圾划水大赛',
              imgUrl: 'https://picsum.photos/400/300/?random&amp;k=2sdffg3',
              publisher: '华清大学',
              procedure: [
                { name: '初赛', startTime: '2014-03-25T06:26:01.927Z', endTime: '2018-03-25T06:26:01.927Z' },
                { name: '复赛', startTime: '2018-06-25T06:26:01.927Z', endTime: '2019-03-25T06:26:01.927Z' }
              ],
              stage: -1
            }
          },
          {
            group: {
              id: 123,
              hasCommit: true,
              name: '咸鱼划水队',
              leaderName: 'zhang',
              rank: '0',
              submissionUrl:
                'https://banner2.kisspng.com/20180312/bqe/kisspng-flag-of-the-maldives-map-flag-of-el-salvador-maldives-round-button-5aa7201f1c1335.853572671520902175115.jpg',
              stage: 1
            },
            contest: {
              id: 111111,
              name: '垃圾划水大赛',
              imgUrl: 'https://picsum.photos/400/300/?random&amp;k=23rfewg',
              publisher: '华清大学',
              procedure: [
                { name: '初赛', startTime: '2014-03-25T06:26:01.927Z', endTime: '2018-03-25T06:26:01.927Z' },
                { name: '复赛', startTime: '2018-06-25T06:26:01.927Z', endTime: '2019-03-25T06:26:01.927Z' }
              ],
              stage: 1
            }
          }
        ]
      },
      status: 200,
      statusText: 'OK'
    }
  },
  ['GET */api/users/judged'](pathMatch, query, request, passThrough) {
    return {
      body: {
        code: 0,
        error: '',
        data: [
          {
            task: { count: 120, done: 80 },
            contest: {
              id: 1,
              name: '垃圾划水大赛',
              imgUrl: 'https://picsum.photos/400/300/?random&amp;k=2',
              publisher: '华清大学',
              procedure: [
                { name: '初赛', startTime: '2014-03-25T06:26:01.927Z', endTime: '2018-03-25T06:26:01.927Z' },
                { name: '复赛', startTime: '2018-06-25T06:26:01.927Z', endTime: '2019-03-25T06:26:01.927Z' }
              ],
              stage: 0
            }
          },
          {
            task: { count: 100, done: 100 },
            contest: {
              id: 389484,
              name: '垃圾划水大赛',
              imgUrl: 'https://picsum.photos/400/300/?random&amp;k=3',
              publisher: '华清大学',
              procedure: [
                { name: '初赛', startTime: '2014-03-25T06:26:01.927Z', endTime: '2018-03-25T06:26:01.927Z' },
                { name: '复赛', startTime: '2018-06-25T06:26:01.927Z', endTime: '2019-03-25T06:26:01.927Z' }
              ],
              stage: 1
            }
          },
          {
            task: { count: 100, done: 100 },
            contest: {
              id: 3892345484,
              name: '垃圾划水大赛',
              imgUrl: 'https://picsum.photos/400/300/?random&amp;k=34',
              publisher: '华清大学',
              procedure: [
                { name: '初赛', startTime: '2014-03-25T06:26:01.927Z', endTime: '2018-03-25T06:26:01.927Z' },
                { name: '复赛', startTime: '2018-06-25T06:26:01.927Z', endTime: '2019-03-25T06:26:01.927Z' }
              ],
              stage: 2
            }
          },
          {
            task: { count: 100, done: 100 },
            contest: {
              id: 4757,
              name: '垃圾划水大赛',
              imgUrl: 'https://picsum.photos/400/300/?random&amp;k=3345',
              publisher: '华清大学',
              procedure: [
                { name: '初赛', startTime: '2014-03-25T06:26:01.927Z', endTime: '2018-03-25T06:26:01.927Z' },
                { name: '复赛', startTime: '2018-06-25T06:26:01.927Z', endTime: '2019-03-25T06:26:01.927Z' }
              ],
              stage: 3
            }
          },
          {
            task: { count: 100, done: 72 },
            contest: {
              id: 678687,
              name: '垃圾划水大赛',
              imgUrl: 'https://picsum.photos/400/300/?random&amp;k=334t',
              publisher: '华清大学',
              procedure: [
                { name: '初赛', startTime: '2014-03-25T06:26:01.927Z', endTime: '2018-03-25T06:26:01.927Z' },
                { name: '复赛', startTime: '2018-06-25T06:26:01.927Z', endTime: '2019-03-25T06:26:01.927Z' }
              ],
              stage: 4
            }
          },
          {
            task: { count: 100, done: 74 },
            contest: {
              id: 678687,
              name: '垃圾划水大赛',
              imgUrl: 'https://picsum.photos/400/300/?random&amp;k=334t',
              publisher: '华清大学',
              procedure: [
                { name: '初赛', startTime: '2014-03-25T06:26:01.927Z', endTime: '2018-03-25T06:26:01.927Z' },
                { name: '复赛', startTime: '2018-06-25T06:26:01.927Z', endTime: '2019-03-25T06:26:01.927Z' }
              ],
              stage: -1
            }
          }
        ]
      },
      status: 200,
      statusText: 'OK'
    }
  },
  ['POST */api/contests/1/stage'](pathMatch, query, request, passThrough) {
    stage = request.body.stage
    return {
      body: {
        code: 0,
        error: '',
        data: {}
      },
      status: 200,
      statusText: 'OK'
    }
  },
  ['GET */api/contests/1/groups'](pathMatch, query, request, passThrough) {
    return {
      body: {
        code: 0,
        error: '',
        data: [
          {
            id: 1,
            name: 'ysdui',
            competitionId: 1,
            competitionName: '咸鱼划水大赛',
            leaderName: 'ykc',
            membersName: ['ny', 'zy', 'ljw'],
            hasCommit: true,
            rank: 2,
            stage: 1
          },
          {
            id: 2,
            name: '队伍名',
            competitionId: 1,
            competitionName: '咸鱼划水大赛',
            hasCommit: false,
            leaderName: '有神',
            membersName: ['养身', '浇筑'],
            rank: '获得奖项',
            stage: 2
          },
          {
            id: 4,
            name: 'ysdui',
            competitionId: 1,
            competitionName: '咸鱼划水大赛',
            leaderName: 'ykc',
            membersName: ['ny', 'zy', 'ljw'],
            hasCommit: true,
            rank: 3,
            stage: 2
          }
        ]
      },
      status: 200,
      statusText: 'OK'
    }
  },
  ['GET */api/users/created'](pathMatch, query, request, passThrough) {
    return {
      body: {
        code: 0,
        error: '',
        data: [
          {
            id: 1,
            name: '咸鱼划水大赛',
            subject: '体育',
            groupSize: '2',
            enrollStart: '2018-1-1',
            enrollEnd: '2018-12-31',
            detail: '哈哈',
            procedure: `[{
            "name":"决赛",
            "startTime":"2018-2-1",
            "endTime":"2018-2-2"
          },{
            "name":"决赛",
            "startTime":"2018-2-1",
            "endTime":"2018-2-2"
          },{
            "name":"决赛",
            "startTime":"2018-2-1",
            "endTime":"2018-2-2"
          },{
            "name":"决赛",
            "startTime":"2018-2-1",
            "endTime":"2018-2-2"
          }]`,
            enrollUrl: 'www.baidu.com',
            imgUrl: 'www.baidu.com',
            charge: 0,
            upvote: 100,
            downvote: 999,
            publisher: 'SSS',
            stage
          },
          {
            id: 1,
            name: '咸鱼划水大赛',
            subject: '体育',
            groupSize: '2',
            enrollStart: '2018-1-1',
            enrollEnd: '2018-12-31',
            detail: '哈哈',
            procedure: `[{
            "name":"决赛",
            "startTime":"2018-2-1",
            "endTime":"2018-2-2"
          },{
            "name":"决赛",
            "startTime":"2018-2-1",
            "endTime":"2018-2-2"
          },{
            "name":"决赛",
            "startTime":"2018-2-1",
            "endTime":"2018-2-2"
          },{
            "name":"决赛",
            "startTime":"2018-2-1",
            "endTime":"2018-2-2"
          }]`,
            enrollUrl: 'www.baidu.com',
            imgUrl: 'www.baidu.com',
            charge: 0,
            upvote: 100,
            downvote: 999,
            publisher: 'SSS',
            stage
          }
        ]
      },
      status: 200,
      statusText: 'OK'
    }
  },
  ['GET */auth/info'](pathMatch, query, request, passThrough) {
    return {
      body: {
        code: 0,
        error: '',
        data: {
          username: 'abc',
          email: `fuck@bornhub.com`,
          introduction: `I am a bornhuber.`,
          school: `BB school`,
          individual: 1
        }
      },
      status: 200,
      statusText: 'OK'
    }
  },
  ['GET */api/contests/1/reviewer'](pathMatch, query, request, passThrough) {
    if (request.params.all) {
      return {
        body: {
          code: 0,
          error: '',
          data: [
            {
              username: 'ykc',
              email: 'ykc@abc.com',
              school: 'THU',
              accepted: 1
            },
            {
              username: 'ykc',
              email: 'ykc@abc.com',
              school: 'THU',
              accepted: 1
            },
            {
              username: 'ykc',
              email: 'ykc@abc.com',
              school: 'THU',
              accepted: 0
            }
          ]
        },
        status: 200,
        statusText: 'OK'
      }
    }
    return {
      body: {
        code: 0,
        error: '',
        data: [
          {
            username: 'ykc',
            email: 'ykc@abc.com',
            school: 'THU'
          },
          {
            username: 'ykc',
            email: 'ykc@abc.com',
            school: 'THU'
          }
        ]
      },
      status: 200,
      statusText: 'OK'
    }
  },
  ['GET */api/contests/1/taskstat'](pathMatch, query, request, passThrough) {
    return {
      body: {
        code: 0,
        error: '',
        data: {
          totalTasks: 70,
          reviewedTasks: 50,
          qualifiedGroups: 20,
          submittedGroups: 10,
          isAssigned: false // 是否之前一键分配过
        }
      },
      status: 200,
      statusText: 'OK'
    }
  },
  ['GET */api/contests/1/reviewtask'](pathMatch, query, request, passThrough) {
    return {
      body: {
        code: 0,
        error: '',
        data: [
          {
            username: 'abbbbbbbb',
            email: '1@2.com',
            assigned: 33, // 被分配的作品数
            completed: 20
          },
          {
            username: 'abbbbbbbb',
            email: '1@2.com',
            assigned: 33, // 被分配的作品数
            completed: 20
          },
          {
            username: 'abbbbbbbb',
            email: '1@2.com',
            assigned: 33, // 被分配的作品数
            completed: 20
          }
        ]
      },
      status: 200,
      statusText: 'OK'
    }
  },
  ['GET */api/contests/1/criterion'](pathMatch, query, request, passThrough) {
    return {
      body: {
        code: 0,
        error: '',
        data: {
          criterion: '看脸给分\n'
        }
      },
      status: 200,
      statusText: 'OK'
    }
  },
  ['GET */api/contests/1/submission_all'](pathMatch, query, request, passThrough) {
    return {
      body: {
        code: 0,
        error: '',
        data: [
          {
            name: '网络优化器',
            teamName: '队伍名',
            submissionTime: '2018-1-1 12:00',
            judges: [{ name: '刘红', judged: true, score: 100 }, { name: '刘黄', judged: true, score: 100 }],
            average: 100
          },
          { name: '网络优化器', teamName: '队伍名', submissionTime: '2018-1-1 12:00', judges: [], average: 0 },
          { name: '网络优化器', teamName: '队伍名', submissionTime: '2018-1-1 12:00', judges: [], average: 0 }
        ]
      },
      status: 200,
      statusText: 'OK'
    }
  },
  ['GET */api/contests/1/groups_detail'](_1, _2, _3, _4) {
    return {
      body: {
        code: 0,
        error: '',
        data: {
          enrollForm: `[
            { "label": "性取向", "description": "你的性取向", "formType": "文字题" },
            { "label": "你喜欢吃垃圾吗", "formType": "选择题", "options": ["喜欢", "不喜欢"] },
            { "label": "你吃过几次垃圾", "formType": "选择题", "options": ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22", "23"] },
            { "label": "你喜欢吃什么类型的垃圾", "description": "填写垃圾的名字", "formType": "文字题" }
          ]`,
          info: [
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form: '{"性取向":"草马","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"威龙"}'
            },
            {
              name: '咸鱼划水小队',
              groupName: '化学小组',
              form: '{"性取向":"同性恋","你喜欢吃垃圾吗":"不喜欢","你吃过几次垃圾":"2","你喜欢吃什么类型的垃圾":"卫龙"}'
            },
            {
              name: '划水组',
              groupName: '化学小组',
              form:
                '{"性取向":"草猫","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"1","你喜欢吃什么类型的垃圾":"垃圾中的垃圾"}'
            },
            {
              name: '捡一下垃圾组',
              groupName: '化学小组',
              form: '{"性取向":"草狗","你喜欢吃垃圾吗":"喜欢","你吃过几次垃圾":"3","你喜欢吃什么类型的垃圾":"骨头垃圾"}'
            }
          ]
        }
      },
      status: 200,
      statusText: 'OK'
    }
  },
  ['POST */auth/reset_password'](_1, _2, _3, _4) {
    return {
      body: {
        code: 0,
        error: '',
        data: [_1, _2, _3, _4]
      },
      status: 200,
      statusText: 'OK'
    }
  },
  ['GET */api/users/profile/yousheng'](_1, _2, _3, _4) {
    return {
      body: {
        code: 0,
        error: '',
        data: {
          username: 'yousheng',
          email: 'thu@yousheng.com',
          introduction: '游神牛逼得很啊',
          school: '清华软院',
          individual: 1
        }
      },
      status: 200,
      statusText: 'OK'
    }
  },
  ['GET */api/contests'](_1, _2, _3, _4) {
    return {
      body: {
        code: 0,
        error: '',
        data: [
          {
            id: 1,
            name: '咸鱼划水大赛',
            subject: '体育',
            groupSize: 4,
            enrollStart: '2015-03-25T06:26:01.927Z',
            enrollEnd: '2019-03-25T06:26:01.927Z',
            procedure: [
              { name: '初赛', startTime: '2014-03-25T06:26:01.927Z', endTime: '2018-03-25T06:26:01.927Z' },
              { name: '复赛', startTime: '2018-06-25T06:26:01.927Z', endTime: '2019-03-25T06:26:01.927Z' }
            ],
            imgUrl: 'https://picsum.photos/800/300/?random&amp;k=23rfewg',
            enrollUrl: '',
            charge: 100,
            upvote: 200,
            downvote: 300,
            publisher: '华清大学',
            detail: '# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功',
            userRelated: {
              upvoteStatus: 0
            }
          },
          {
            id: 1,
            name: '咸鱼划水大赛',
            subject: '体育',
            groupSize: 4,
            enrollStart: '2015-03-25T06:26:01.927Z',
            enrollEnd: '2019-03-25T06:26:01.927Z',
            procedure: [
              { name: '初赛', startTime: '2014-03-25T06:26:01.927Z', endTime: '2018-03-25T06:26:01.927Z' },
              { name: '复赛', startTime: '2018-06-25T06:26:01.927Z', endTime: '2019-03-25T06:26:01.927Z' }
            ],
            imgUrl: 'https://picsum.photos/200/300/?random&amp;k=23rfewg',
            enrollUrl: '',
            charge: 100,
            upvote: 200,
            downvote: 300,
            publisher: '华清大学',
            detail: '# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功',
            userRelated: {
              upvoteStatus: 0
            }
          },
          {
            id: 1,
            name: '咸鱼划水大赛',
            subject: '体育',
            groupSize: 4,
            enrollStart: '2015-03-25T06:26:01.927Z',
            enrollEnd: '2019-03-25T06:26:01.927Z',
            procedure: [
              { name: '初赛', startTime: '2014-03-25T06:26:01.927Z', endTime: '2018-03-25T06:26:01.927Z' },
              { name: '复赛', startTime: '2018-06-25T06:26:01.927Z', endTime: '2019-03-25T06:26:01.927Z' }
            ],
            imgUrl: 'https://picsum.photos/800/300/?random&amp;k=23rfewg',
            enrollUrl: '',
            charge: 100,
            upvote: 200,
            downvote: 300,
            publisher: '华清大学',
            detail: '# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功',
            userRelated: {
              upvoteStatus: 0
            }
          },
          {
            id: 1,
            name: '咸鱼划水大赛',
            subject: '体育',
            groupSize: 4,
            enrollStart: '2015-03-25T06:26:01.927Z',
            enrollEnd: '2019-03-25T06:26:01.927Z',
            procedure: [
              { name: '初赛', startTime: '2014-03-25T06:26:01.927Z', endTime: '2018-03-25T06:26:01.927Z' },
              { name: '复赛', startTime: '2018-06-25T06:26:01.927Z', endTime: '2019-03-25T06:26:01.927Z' }
            ],
            imgUrl: 'https://picsum.photos/800/300/?random&amp;k=23rfewg',
            enrollUrl: '',
            charge: 100,
            upvote: 200,
            downvote: 300,
            publisher: '华清大学',
            detail: '# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功',
            userRelated: {
              upvoteStatus: 0
            }
          },
          {
            id: 1,
            name: '咸鱼划水大赛',
            subject: '体育',
            groupSize: 4,
            enrollStart: '2015-03-25T06:26:01.927Z',
            enrollEnd: '2019-03-25T06:26:01.927Z',
            procedure: [
              { name: '初赛', startTime: '2014-03-25T06:26:01.927Z', endTime: '2018-03-25T06:26:01.927Z' },
              { name: '复赛', startTime: '2018-06-25T06:26:01.927Z', endTime: '2019-03-25T06:26:01.927Z' }
            ],
            imgUrl: 'https://picsum.photos/200/300/?random&amp;k=23rfewg',
            enrollUrl: '',
            charge: 100,
            upvote: 200,
            downvote: 300,
            publisher: '华清大学',
            detail: '# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功',
            userRelated: {
              upvoteStatus: 0
            }
          },
          {
            id: 1,
            name: '咸鱼划水大赛',
            subject: '体育',
            groupSize: 4,
            enrollStart: '2015-03-25T06:26:01.927Z',
            enrollEnd: '2019-03-25T06:26:01.927Z',
            procedure: [
              { name: '初赛', startTime: '2014-03-25T06:26:01.927Z', endTime: '2018-03-25T06:26:01.927Z' },
              { name: '复赛', startTime: '2018-06-25T06:26:01.927Z', endTime: '2019-03-25T06:26:01.927Z' }
            ],
            imgUrl: 'https://picsum.photos/800/300/?random&amp;k=23rfewg',
            enrollUrl: '',
            charge: 100,
            upvote: 200,
            downvote: 300,
            publisher: '华清大学',
            detail: '# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功',
            userRelated: {
              upvoteStatus: 0
            }
          },
          {
            id: 1,
            name: '咸鱼划水大赛',
            subject: '体育',
            groupSize: 4,
            enrollStart: '2015-03-25T06:26:01.927Z',
            enrollEnd: '2019-03-25T06:26:01.927Z',
            procedure: [
              { name: '初赛', startTime: '2014-03-25T06:26:01.927Z', endTime: '2018-03-25T06:26:01.927Z' },
              { name: '复赛', startTime: '2018-06-25T06:26:01.927Z', endTime: '2019-03-25T06:26:01.927Z' }
            ],
            imgUrl: 'https://picsum.photos/800/300/?random&amp;k=23rfewg',
            enrollUrl: '',
            charge: 100,
            upvote: 200,
            downvote: 300,
            publisher: '华清大学',
            detail: '# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功',
            userRelated: {
              upvoteStatus: 0
            }
          },
          {
            id: 1,
            name: '咸鱼划水大赛',
            subject: '体育',
            groupSize: 4,
            enrollStart: '2015-03-25T06:26:01.927Z',
            enrollEnd: '2019-03-25T06:26:01.927Z',
            procedure: [
              { name: '初赛', startTime: '2014-03-25T06:26:01.927Z', endTime: '2018-03-25T06:26:01.927Z' },
              { name: '复赛', startTime: '2018-06-25T06:26:01.927Z', endTime: '2019-03-25T06:26:01.927Z' }
            ],
            imgUrl: 'https://picsum.photos/800/300/?random&amp;k=23rfewg',
            enrollUrl: '',
            charge: 100,
            upvote: 200,
            downvote: 300,
            publisher: '华清大学',
            detail: '# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功',
            userRelated: {
              upvoteStatus: 0
            }
          },
          {
            id: 1,
            name: '咸鱼划水大赛',
            subject: '体育',
            groupSize: 4,
            enrollStart: '2015-03-25T06:26:01.927Z',
            enrollEnd: '2019-03-25T06:26:01.927Z',
            procedure: [
              { name: '初赛', startTime: '2014-03-25T06:26:01.927Z', endTime: '2018-03-25T06:26:01.927Z' },
              { name: '复赛', startTime: '2018-06-25T06:26:01.927Z', endTime: '2019-03-25T06:26:01.927Z' }
            ],
            imgUrl: 'https://picsum.photos/800/300/?random&amp;k=23rfewg',
            enrollUrl: '',
            charge: 100,
            upvote: 200,
            downvote: 300,
            publisher: '华清大学',
            detail: '# 比赛简介\n\n- **测试**一下 *markdown*\n- 和 $\\KaTeX$ 支持\n\n## 测试成功',
            userRelated: {
              upvoteStatus: 0
            }
          }
        ]
      },
      status: 200,
      statusText: 'OK'
    }
  }
}
