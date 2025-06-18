import pytest
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_send_email_valid():
    response = client.post("/emails/send", json={
        "to": ["test@example.com"],
        "subject": "Тестовое письмо",
        "body": "Привет!",
        "is_html": False
    })
    assert response.status_code == 200
    assert "success" in response.text.lower()

def test_get_email_stats_valid():
    response = client.get("/emails/stats", params={
        "from_date": "2024-01-01",
        "to_date": "2025-01-01"
    })
    assert response.status_code == 200
    body = response.json()
    assert "incoming" in body
    assert "outgoing" in body
    assert isinstance(body["incoming"], int)
    assert isinstance(body["outgoing"], int)
