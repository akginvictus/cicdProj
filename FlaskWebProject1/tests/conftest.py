import pytest

from FlaskWebProject1 import create_app


@pytest.fixture
def app():
    application = create_app()
    application.config.update(TESTING=True)
    return application


@pytest.fixture
def client(app):
    with app.test_client() as client:
        yield client

