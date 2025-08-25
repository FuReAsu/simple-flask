import pytest
from pathlib import Path

@pytest.mark.order(4)
def test_clear_input(client):
    client = client[0]
    
    response = client.post("/input", data={"button": "clearButton"})
    assert response.status_code == 200

    data_file = Path.cwd() / "data" / "data.txt"
    file_text = data_file.read_text()

    assert file_text == ""
    
