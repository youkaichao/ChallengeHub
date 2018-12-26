import aiohttp
import asyncio


async def register(session, i):
    # login
    payload = {
        "username": f"并发测试用户_{i:05}",
        "password": "123"
    }
    resp = await session.post('https://729222.iterator-traits.com/auth/login', json=payload)
    cookies = resp.cookies
    # register
    payload = {
        "name": f"并发测试队伍_{i:05}",
        "leaderName": f"并发测试用户_{i:05}",
        "members": [f"并发测试用户_{i:05}"],
        "form": '{"学校":"清华大学", "是否有过往建模经历":"否"}'
    }
    await session.post('https://729222.iterator-traits.com/api/contests/7/enroll', json=payload, cookies=cookies)
    return


async def main():
    async with aiohttp.ClientSession() as session:
        for j in range(20):
            print(j)
            futures = []
            for i in range(50):
                futures.append(register(session, j * 50 + i))
            await asyncio.gather(*futures)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
