from fastapi.testclient import TestClient
from app.main import app

import pytest

def test_health_ok():
    client = TestClient(app)
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}

