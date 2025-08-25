import pytest

@pytest.mark.order(2)
def test_cookies(client):
    
    client = client[0]
    response = client.get("/cookies")
    assert response.status_code == 200

    cookie = response.headers.get("Set-Cookie")
    assert cookie is not None

