import re
from fastapi.testclient import TestClient
from app.main import app
import pytest

SEMVER = re.compile(
    r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)(?:[-+].*)?$"
)

def test_version_semver_and_field():
    client = TestClient(app)
    response = client.get("/version")
    assert response.status_code == 200
    body = response.json()
    assert "version" in body
    assert SEMVER.match(body["version"]) is not None
