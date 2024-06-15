import asyncio

import pytest_asyncio


pytest_plugins = (
    "fixtures.fixture_session",
)


@pytest_asyncio.fixture(scope="session")
def event_loop():
    loop = asyncio.new_event_loop()
    yield loop
    loop.close()
