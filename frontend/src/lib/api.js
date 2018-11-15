/* eslint-disable */
let stage = 0

export default {
  ['POST */auth/login'](pathMatch, query, request, passThrough) {
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
  ['GET */api/judge/contests/1/submissions'](pathMatch, query, request, passThrough) {
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
            procedure:
              '[{ "name": "初赛", "startTime": "2014-03-25T06:26:01.927Z", "endTime": "2018-03-25T06:26:01.927Z" }, { "name": "复赛", "startTime": "2018-06-25T06:26:01.927Z", "endTime": "2019-03-25T06:26:01.927Z" }]',
            stage: 2
          },
          task: {
            count: 9,
            done: 3
          },
          submissions: [
            {
              title: '网络优化器',
              reviewed: true,
              rating: 83
            },
            {
              title: '网络优化器',
              reviewed: true,
              rating: 78
            },
            {
              title: '网络优化器',
              reviewed: true,
              rating: 94
            },
            {
              title: '网络优化器',
              reviewed: false,
              rating: 0
            },
            {
              title: '网络优化器',
              reviewed: false,
              rating: 0
            },
            {
              title: '网络优化器',
              reviewed: false,
              rating: 0
            },
            {
              title: '网络优化器',
              reviewed: false,
              rating: 0
            },
            {
              title: '网络优化器',
              reviewed: false,
              rating: 0
            },
            {
              title: '网络优化器',
              reviewed: false,
              rating: 0
            }
          ]
        }
      },
      status: 200,
      statusText: 'OK'
    }
  },
  ['GET */api/enrolled_competitions'](pathMatch, query, request, passThrough) {
    return {
      body: {
        code: 0,
        error: '',
        data: [
          {
            group: {
              hasCommit: false,
              name: '咸鱼划水队',
              leaderName: 'zhang',
              rank: '0'
            },
            contest: {
              id: 333333,
              name: '垃圾划水大赛',
              imgUrl: 'https://picsum.photos/400/300/?random&amp;k=2',
              publisher: '华清大学',
              procedure:
                '[{ "name": "初赛", "startTime": "2014-03-25T06:26:01.927Z", "endTime": "2018-03-25T06:26:01.927Z" }, { "name": "复赛", "startTime": "2018-06-25T06:26:01.927Z", "endTime": "2019-03-25T06:26:01.927Z" }]',
              stage: 0
            }
          },
          {
            group: {
              hasCommit: false,
              name: '咸鱼划水队',
              leaderName: 'zhang',
              rank: '0'
            },
            contest: {
              id: 5467,
              name: '垃圾划水大赛',
              imgUrl: 'https://picsum.photos/400/300/?random&amp;k=2dfg',
              publisher: '华清大学',
              procedure:
                '[{ "name": "初赛", "startTime": "2014-03-25T06:26:01.927Z", "endTime": "2018-03-25T06:26:01.927Z" }, { "name": "复赛", "startTime": "2018-06-25T06:26:01.927Z", "endTime": "2019-03-25T06:26:01.927Z" }]',
              stage: 1
            }
          },
          {
            group: {
              hasCommit: true,
              name: '咸鱼划水队',
              leaderName: 'zhang',
              rank: '0'
            },
            contest: {
              id: 976857,
              name: '垃圾划水大赛',
              imgUrl: 'https://picsum.photos/400/300/?random&amp;k=2sdrg3',
              publisher: '华清大学',
              procedure:
                '[{ "name": "初赛", "startTime": "2014-03-25T06:26:01.927Z", "endTime": "2018-03-25T06:26:01.927Z" }, { "name": "复赛", "startTime": "2018-06-25T06:26:01.927Z", "endTime": "2019-03-25T06:26:01.927Z" }]',
              stage: 2
            }
          },
          {
            group: {
              hasCommit: false,
              name: '咸鱼划水队',
              leaderName: 'zhang',
              rank: '0'
            },
            contest: {
              id: 2345234,
              name: '垃圾划水大赛',
              imgUrl: 'https://picsum.photos/400/300/?random&amp;k=2g34gwer',
              publisher: '华清大学',
              procedure:
                '[{ "name": "初赛", "startTime": "2014-03-25T06:26:01.927Z", "endTime": "2018-03-25T06:26:01.927Z" }, { "name": "复赛", "startTime": "2018-06-25T06:26:01.927Z", "endTime": "2019-03-25T06:26:01.927Z" }]',
              stage: 3
            }
          },
          {
            group: {
              hasCommit: true,
              name: '咸鱼划水队',
              leaderName: 'zhang',
              rank: '0'
            },
            contest: {
              id: 567456,
              name: '垃圾划水大赛',
              imgUrl: 'https://picsum.photos/400/300/?random&amp;k=2ggw34g',
              publisher: '华清大学',
              procedure:
                '[{ "name": "初赛", "startTime": "2014-03-25T06:26:01.927Z", "endTime": "2018-03-25T06:26:01.927Z" }, { "name": "复赛", "startTime": "2018-06-25T06:26:01.927Z", "endTime": "2019-03-25T06:26:01.927Z" }]',
              stage: 4
            }
          },
          {
            group: {
              hasCommit: true,
              name: '咸鱼划水队',
              leaderName: 'zhang',
              rank: '0'
            },
            contest: {
              id: 23463456,
              name: '垃圾划水大赛',
              imgUrl: 'https://picsum.photos/400/300/?random&amp;k=2sdffg3',
              publisher: '华清大学',
              procedure:
                '[{ "name": "初赛", "startTime": "2014-03-25T06:26:01.927Z", "endTime": "2018-03-25T06:26:01.927Z" }, { "name": "复赛", "startTime": "2018-06-25T06:26:01.927Z", "endTime": "2019-03-25T06:26:01.927Z" }]',
              stage: -1
            }
          },
          {
            group: {
              hasCommit: true,
              name: '咸鱼划水队',
              leaderName: 'zhang',
              rank: '0'
            },
            contest: {
              id: 111111,
              name: '垃圾划水大赛',
              imgUrl: 'https://picsum.photos/400/300/?random&amp;k=23rfewg',
              publisher: '华清大学',
              procedure:
                '[{ "name": "初赛", "startTime": "2014-03-25T06:26:01.927Z", "endTime": "2018-03-25T06:26:01.927Z" }, { "name": "复赛", "startTime": "2018-06-25T06:26:01.927Z", "endTime": "2019-03-25T06:26:01.927Z" }]',
              stage: 1
            }
          }
        ]
      },
      status: 200,
      statusText: 'OK'
    }
  },
  ['GET */api/judged_competitions'](pathMatch, query, request, passThrough) {
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
              procedure:
                '[{ "name": "初赛", "startTime": "2014-03-25T06:26:01.927Z", "endTime": "2018-03-25T06:26:01.927Z" }, { "name": "复赛", "startTime": "2018-06-25T06:26:01.927Z", "endTime": "2019-03-25T06:26:01.927Z" }]',
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
              procedure:
                '[{ "name": "初赛", "startTime": "2014-03-25T06:26:01.927Z", "endTime": "2018-03-25T06:26:01.927Z" }, { "name": "复赛", "startTime": "2018-06-25T06:26:01.927Z", "endTime": "2019-03-25T06:26:01.927Z" }]',
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
              procedure:
                '[{ "name": "初赛", "startTime": "2014-03-25T06:26:01.927Z", "endTime": "2018-03-25T06:26:01.927Z" }, { "name": "复赛", "startTime": "2018-06-25T06:26:01.927Z", "endTime": "2019-03-25T06:26:01.927Z" }]',
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
              procedure:
                '[{ "name": "初赛", "startTime": "2014-03-25T06:26:01.927Z", "endTime": "2018-03-25T06:26:01.927Z" }, { "name": "复赛", "startTime": "2018-06-25T06:26:01.927Z", "endTime": "2019-03-25T06:26:01.927Z" }]',
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
              procedure:
                '[{ "name": "初赛", "startTime": "2014-03-25T06:26:01.927Z", "endTime": "2018-03-25T06:26:01.927Z" }, { "name": "复赛", "startTime": "2018-06-25T06:26:01.927Z", "endTime": "2019-03-25T06:26:01.927Z" }]',
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
              procedure:
                '[{ "name": "初赛", "startTime": "2014-03-25T06:26:01.927Z", "endTime": "2018-03-25T06:26:01.927Z" }, { "name": "复赛", "startTime": "2018-06-25T06:26:01.927Z", "endTime": "2019-03-25T06:26:01.927Z" }]',
              stage: -1
            }
          }
        ]
      },
      status: 200,
      statusText: 'OK'
    }
  }
}
