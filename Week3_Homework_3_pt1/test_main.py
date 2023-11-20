#pytest
#Looks for file names with syntax text_.py

from fastapi.testclient import TestClient
from main import app


#unittest
def test_basic_example():
    assert (True)

client = TestClient(app)

def test_put_api():
    response = client.put("/items/101a", json={
        "name": "Debugtest123",
        "quantity": 5,
        "serial_num": "101a",
        "origin": {
            "country": "China",
            "production_date": "11/11/2011"
        }
    })
    print(response.json())
    assert response.status_code == 200


