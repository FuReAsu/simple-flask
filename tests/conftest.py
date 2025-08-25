import pytest
from app.simpleflask import create_app
from pathlib import Path
import os

@pytest.fixture(scope='session')
def client():
    app = create_app()
    app.config.update({
        "TESTING": True,
    })
    logger = app.logger

    with app.test_client() as client:
        yield client, logger

    log_dir = Path.cwd() / "log"
    log_file = log_dir / "app.log" 

    data_dir = Path.cwd() / "data"
    data_file = data_dir / "data.txt"

    if log_file.exists():
        os.remove(log_file)
        os.removedirs(log_dir)
    if data_dir.exists():
        os.remove(data_file)
        os.removedirs(data_dir)
