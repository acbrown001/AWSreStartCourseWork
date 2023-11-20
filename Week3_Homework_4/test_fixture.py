# Fixtures for testing = precondition to test case.
# Pre-initilize an object and return it for health check.

from fastapi.testclient import TestClient
from main import app
import pytest


@pytest.fixture
def client():  # every time a client fixture is called, it will return a new TestClient
    yield TestClient(app)  # yield is like return, but it will return a generator object


# Good payload
@pytest.fixture
def good_payload():
    return {
        "name": "Fixturetest123",
        "quantity": 5,
        "serial_num": "101a",
        "origin": {"country": "China", "production_date": "11/11/2011"},
    }


# Bad payload
@pytest.fixture
def bad_payload():
    return {
        "name": "Fixturetest123",
        "quantity": "A",  # Incorrect data type
        "serial_num": "101a",
        "origin": {"country": "China", "production_date": "11/11/2011"},
    }


def test_incorrect_input_type(client, bad_payload):
    response = client.put("/items/Tests/", json=bad_payload)
    assert response.status_code == 422
    # assert "Input should be valid integer, unable to parse string as integer" in str(
    #    response.json()
    # )


# Test PUT API (422 Response)
def test_putbad_api(client, bad_payload):
    response = client.put("/items/Tests/", json=bad_payload)
    assert response.status_code == 422
    # assert "Input should be valid integer, unable to parse string as integer" in str(
    #    response.json()
    # )


# Create and delete item
@pytest.fixture
def create_and_delete_item(client, good_payload):
    response = client.put("/items/Tests/", json=good_payload)
    yield "Item created"
    client.delete(f"/items/{good_payload['serial_num']}")


# Test GET API (GET ALL):
def test_get_api(client):
    response = client.get("/items/Tests/")
    assert response.status_code == 404


def test_put_then_get_api(client, good_payload):
    response = client.put("/items/Tests/", json=good_payload)
    assert response.status_code == 200
    response = client.get(f"/items/Tests/")
    assert response.status_code == 200
    # assert response.json() == good_payload


# Parametrized test
@pytest.mark.parametrize(
    "a, b, expected",
    [
        (1, 2, 3),
        (5, -1, 4),
        (3, 3, 6),
    ],
)
def test_addition(a, b, expected):
    assert a + b == expected


@pytest.mark.parametrize(
    "payload, http_code",
    [
        (
            {
                "name": "Fixturetest123",
                "quantity": 5,
                "serial_num": "101a",
                "origin": {"country": "China", "production_date": "11/11/2011"},
            },
            200,
        ),
        (
            {
                "name": "Fixturetest123",
                "quantity": "A",  # Incorrect data type
                "serial_num": "101a",
                "origin": {"country": "China", "production_date": "11/11/2011"},
            },
            422,
        ),
    ],
    indirect=["payload"],
)
def test_many_put_apis(client, payload, http_code):
    assert client.put("/items/Tests/", json=payload).status_code == http_code
