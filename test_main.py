from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_hobbits():
    response = client.get("/hobbits")
    assert response.status_code == 200
    assert response.json() == ["Frodo Baggins", "Samwise Gamgee", "Peregrin Took", "Meriadoc Brandybuck"]
