import asyncio

import pytest


async def wait_one_second():
    await asyncio.sleep(0.1)
    return 1


@pytest.mark.asyncio
async def test_wait_one_second_with_pytest():
    res = await wait_one_second()
    assert res == 1


def test_wait_one_second_without_pytest():
    event_loop = asyncio.get_event_loop()
    res = event_loop.run_until_complete(wait_one_second())
    assert res == 1
