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
  ['GET */api/enrolled_competitions'](pathMatch, query, request, passThrough) {
    return {
      body: {
        code: 0,
        error: '',
        data: [
          {
            group: { name: '咸鱼划水大组', leaderName: 'zhang', rank: 233 },
            contest: {
              id: 567456,
              name: '垃圾划水大赛',
              imgUrl: 'https://picsum.photos/400/300/?random&amp;k=2',
              publisher: '华清大学',
              procedure:
                '[{ "name": "初赛", "startTime": "2014-03-25T06:26:01.927Z", "endTime": "2018-03-25T06:26:01.927Z" }, { "name": "复赛", "startTime": "2018-06-25T06:26:01.927Z", "endTime": "2019-03-25T06:26:01.927Z" }]',
              stage: 1
            }
          },
          {
            group: { name: '咸鱼吹逼大组', leaderName: 'zhang', rank: 233 },
            contest: {
              id: 4634,
              name: '垃圾划水大赛',
              imgUrl: 'https://picsum.photos/400/300/?random&amp;k=2',
              publisher: '华清大学',
              procedure:
                '[{ "name": "初赛", "startTime": "2014-03-25T06:26:01.927Z", "endTime": "2018-03-25T06:26:01.927Z" }, { "name": "复赛", "startTime": "2018-06-25T06:26:01.927Z", "endTime": "2019-03-25T06:26:01.927Z" }]',
              stage: 1
            }
          },
          {
            group: { name: '咸鱼洗澡大组', leaderName: 'zhang', rank: 233 },
            contest: {
              id: 2,
              name: '垃圾划水大赛',
              imgUrl: 'https://picsum.photos/400/300/?random&amp;k=2',
              publisher: '华清大学',
              procedure:
                '[{ "name": "初赛", "startTime": "2014-03-25T06:26:01.927Z", "endTime": "2018-03-25T06:26:01.927Z" }, { "name": "复赛", "startTime": "2018-06-25T06:26:01.927Z", "endTime": "2019-03-25T06:26:01.927Z" }]',
              stage: 1
            }
          },
          {
            group: { name: '咸牛逼划水小组', leaderName: 'hello', rank: 0 },
            contest: {
              id: 3,
              name: '垃圾划水大赛',
              imgUrl: 'https://picsum.photos/400/300/?random&amp;k=3',
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
  },
  ['GET */api/judged_competitions'](pathMatch, query, request, passThrough) {
    return {
      body: {
        code: 0,
        error: '',
        data: [
          {
            contest: {
              id: 567456,
              name: '垃圾划水大赛',
              imgUrl: 'https://picsum.photos/400/300/?random&amp;k=2',
              publisher: '华清大学',
              procedure:
                '[{ "name": "初赛", "startTime": "2014-03-25T06:26:01.927Z", "endTime": "2018-03-25T06:26:01.927Z" }, { "name": "复赛", "startTime": "2018-06-25T06:26:01.927Z", "endTime": "2019-03-25T06:26:01.927Z" }]',
              stage: 1
            },
            task: {
              count: 100,
              done: 80
            }
          },
          {
            contest: {
              id: 567456,
              name: '垃圾划水大赛',
              imgUrl: 'https://picsum.photos/400/300/?random&amp;k=2',
              publisher: '华清大学',
              procedure:
                '[{ "name": "初赛", "startTime": "2014-03-25T06:26:01.927Z", "endTime": "2018-03-25T06:26:01.927Z" }, { "name": "复赛", "startTime": "2018-06-25T06:26:01.927Z", "endTime": "2019-03-25T06:26:01.927Z" }]',
              stage: -1
            },
            task: {
              count: 100,
              done: 20
            }
          },
          {
            contest: {
              id: 567456,
              name: '垃圾划水大赛',
              imgUrl: 'https://picsum.photos/400/300/?random&amp;k=2',
              publisher: '华清大学',
              procedure:
                '[{ "name": "初赛", "startTime": "2014-03-25T06:26:01.927Z", "endTime": "2018-03-25T06:26:01.927Z" }, { "name": "复赛", "startTime": "2018-06-25T06:26:01.927Z", "endTime": "2019-03-25T06:26:01.927Z" }]',
              stage: 0},
            task: {
              count: 100,
              done: 100
            }
          },
          {
            contest: {
              id: 567456,
              name: '垃圾划水大赛',
              imgUrl: 'https://picsum.photos/400/300/?random&amp;k=2',
              publisher: '华清大学',
              procedure:
                '[{ "name": "初赛", "startTime": "2014-03-25T06:26:01.927Z", "endTime": "2018-03-25T06:26:01.927Z" }, { "name": "复赛", "startTime": "2018-06-25T06:26:01.927Z", "endTime": "2019-03-25T06:26:01.927Z" }]',
              stage: 1},
            task: {
              count: 100,
              done: 65
            }
          }
        ]
      },
      status: 200,
      statusText: 'OK'
    }
  }
}
