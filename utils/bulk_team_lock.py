import aiohttp
import asyncio
import json


async def lock(session, i):
    # login
    payload = {
        'username': f'并发测试用户_{i:05}',
        'password': '123'
    }
    resp = await session.post('https://729222.iterator-traits.com/auth/login', json=payload)
    cookies = resp.cookies

    # get team info
    params = {
        'username': f'并发测试用户_{i:05}'
    }
    resp = await session.get('https://729222.iterator-traits.com/apiv2/contests/7/groups', params=params)
    team_id = json.loads(await resp.text())['data'][0]['teamId']

    # lock
    resp = await session.post(f'https://729222.iterator-traits.com/apiv2/contests/7/groups/{team_id}/lock', cookies=cookies)


async def main():
    async with aiohttp.ClientSession() as session:
        for j in range(20):
            print(j)
            futures = []
            for i in range(50):
                futures.append(lock(session, j * 50 + i))
            await asyncio.gather(*futures)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
