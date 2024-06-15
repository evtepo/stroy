import aiohttp
import pytest_asyncio


@pytest_asyncio.fixture
async def client_session():
    session = aiohttp.ClientSession()
    yield session
    await session.close()


@pytest_asyncio.fixture
def make_request(client_session: aiohttp.ClientSession):
    async def inner(method: str, url: str, params: dict = {}) -> dict:
        async with client_session.request(method, url, json=params) as response:
            body = await response.json(encoding="utf-8")
            status = response.status

        return {"body": body, "status": status}

    return inner
