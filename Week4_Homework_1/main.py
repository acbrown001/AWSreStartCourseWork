# WIP
"""
from fastapi.testclient import TestClient
import pytest
from dto import InventoryItem, ItemOrigin
from main import app


@pytest.fixture
def client():
    return TestClient(app)


@pytest.mark.parametrize(
    "serial_num, expected_status_code",
    [
        ("valid_serial_num", 200),
        ("nonexistent_serial_num", 404),
    ],
)
def test_get_item(client, serial_num, expected_status_code):
    response = client.get(f"/items/{serial_num}")
    assert response.status_code == expected_status_code


@pytest.mark.parametrize(
    "serial_num, expected_status_code, expected_payload",
    [
        (
            "valid_serial_num",
            200,
            {"item_name": "Example Item", "origin": ItemOrigin.DOMESTIC},
        ),
        ("nonexistent_serial_num", 404, {}),
    ],
)
def test_get_item_with_payload(
    client, serial_num, expected_status_code, expected_payload
):
    response = client.get(f"/items/{serial_num}")
    assert response.status_code == expected_status_code
    assert response.json() == expected_payload
"""
