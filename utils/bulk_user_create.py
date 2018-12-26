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


async def main():
    async with aiohttp.ClientSession() as session:
        for j in range(20):
            print(j)
            futures = []
            for i in range(50):
                futures.append(download(session, j * 50 + i))
            await asyncio.gather(*futures)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
