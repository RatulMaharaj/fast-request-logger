from fastapi.testclient import TestClient

from fast_request_logger.main import app

client = TestClient(app)

def test_get():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "GET request successful."}

def test_post():
    response = client.post("/", headers={"Content-Type": "application/json"}, json={"test": "data"})
    assert response.status_code == 201
    assert response.json() == {"message": "POST request successful."}


def test_put():
    response = client.put("/", headers={"Content-Type": "application/json"}, json={"test": "data"})
    assert response.status_code == 200
    assert response.json() == {"message": "PUT request successful."}

def test_patch():
    response = client.patch("/", headers={"Content-Type": "application/json"}, json={"test": "data"})
    assert response.status_code == 200
    assert response.json() == {"message": "PATCH request successful."}

def test_delete():
    response = client.delete("/")
    assert response.status_code == 204

def test_delete_with_id():
    response = client.delete("/123")
    assert response.status_code == 204
