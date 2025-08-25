import pytest
from pathlib import Path

@pytest.mark.order(3)
def test_input_submit(client):

    client = client[0]
    response = client.post("/input", data={"input": "pytest test data", "button": "submitButton"})
    assert response.status_code == 200

    response_text = client.get("/input").get_data(as_text=True)
    assert "pytest test data" in response_text
    
    data_file = Path.cwd() / "data" / "data.txt"
    file_text = data_file.read_text()

    assert "pytest test data" in file_text
