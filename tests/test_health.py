import pytest

@pytest.mark.order(1)
def test_health(client):
    client = client[0]
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"Status": "Healthy"}
