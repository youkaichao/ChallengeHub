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
  }
}