import aiohttp
import asyncio


async def download(session, i):
    payload = {
        'username': f'并发测试用户_{i:05}',
        'email': f'binfa_{i:05}@binfa.com',
        'password': '123',
        'individual': 'individual'
    }
    await session.post('729222.iterator-traits.com/auth/register', json=payload)
    if i % 10 == 0:
        print(i)


async def main():
    async with aiohttp.ClientSession() as session:
        futures = []
        for j in range(200):
            print(j)
            for i in range(100):
                futures.append(download(session, j * 100 + i))
            await asyncio.gather(*futures)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
