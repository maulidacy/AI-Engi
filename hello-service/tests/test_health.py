from httpx import AsyncClient
from app.main import app

import pytest

@pytest.mark.asyncio
async def test_health_ok():
    async with AsyncClient(app=app, base_url="http://test") as ac:
        response = await ac.get("/health")
    assert r.status_code == 200