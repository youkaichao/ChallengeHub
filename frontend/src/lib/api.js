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
          isOrganizer: request.body.username === 'organizer'
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
          isOrganizer: request.body.username === 'organizer'
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
  }
}
