# pytest
# Looks for file names with syntax text_.py

from fastapi.testclient import TestClient
from main import app


# unittest
def test_basic_example():
    assert True


client = TestClient(app)


# Test PUT API (200 Response):
def test_put200_api():
    response = client.put(
        "/items/23gma",
        json={
            "name": "Debugtest123",
            "quantity": 5,
            "serial_num": "101a",
            "origin": {"country": "China", "production_date": "11/11/2011"},
        },
    )
    print(response.json())
    assert response.status_code == 200


# Test PUT API (422 Response)
def test_put422_api():
    response = client.put(
        "/items/23gma",
        json={
            "name": "Debugtest123",
            "quantity": "A",  # Incorrect data type
            "serial_num": "101a",
            "origin": {"country": "China", "production_date": "11/11/2011"},
        },
    )
    print(response.json())
    assert response.status_code == 422


# Test GET API (GET ALL):
def test_get_api():
    response = client.get("/items/23gma")
    print(response.json())
    assert response.status_code == 200


# Test DELETE API:
def test_delete_api():
    response = client.delete("/items/23gma")
    assert response.status_code == 200
    print(response.json())
