import asyncio
import time
import aiohttp

REPOS = ["python/cpython", "psf/requests", "pallets/flask"]


async def fetch_repo(session: aiohttp.ClientSession, repo: str) -> dict:
    async with session.get(f"https://api.github.com/repos/{repo}") as resp:
        resp.raise_for_status()
        return await resp.json()


async def fetch_all_sequential(repos: list[str]) -> list[dict]:
    results = []
    async with aiohttp.ClientSession() as session:
        for repo in repos:
            data = await fetch_repo(session, repo)   # waits for each one before starting the next
            results.append(data)
    return results


async def fetch_all_concurrent(repos: list[str]) -> list[dict]:
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_repo(session, repo) for repo in repos]   # creates all coroutines first
        return await asyncio.gather(*tasks)                     # runs them concurrently


async def main():
    start = time.perf_counter()
    results = await fetch_all_sequential(REPOS)
    print("sequential:", round(time.perf_counter() - start, 2), "s")
    print([r["full_name"] for r in results])

    start = time.perf_counter()
    results = await fetch_all_concurrent(REPOS)
    print("concurrent:", round(time.perf_counter() - start, 2), "s")
    print([r["full_name"] for r in results])


if __name__ == "__main__":
    asyncio.run(main())