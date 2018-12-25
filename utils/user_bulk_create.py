import aiohttp
import asyncio


async def download(session, i):
    payload = {
        'username': f'并发测试用户_{i:05}',
        'email': f'binfa_{i:05}@binfa.com',
        'password': '123',
        'individual': 'individual'
    }
    await session.post('127.0.0.1/auth/register', json=payload)
    if i % 10 == 0:
        print(i)


async def main():
    futures = []
    async with aiohttp.ClientSession() as session:
        for i in range(20000):
            futures.append(download(session, i))
        await asyncio.gather(*futures)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
