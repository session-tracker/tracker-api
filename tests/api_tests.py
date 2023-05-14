import pytest
import json

from starlette.testclient import TestClient
from main import app as application
from api.v1.models.pong import Pong

client = TestClient(application)

pong = Pong()

@pytest.mark.webtest
def test_ping():
    response = client.get("/api/v1/ping")
    data = json.loads(response.content)

    assert response.status_code == 200
    assert data['description'] == pong.description

