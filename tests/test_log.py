import pytest
from pathlib import Path

@pytest.mark.order(5)
def test_log(client):
    logger = client[1]

    logger.info("pytest test log")
    
    log_file = Path.cwd() / "log" / "app.log"
    file_text = log_file.read_text()

    assert "pytest test log" in file_text

