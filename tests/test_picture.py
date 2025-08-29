import pytest

@pytest.mark.order(6)
def test_picture(client):
    client = client[0]
    response = client.get("/picture")
    assert response.status_code == 200
