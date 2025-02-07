import pytest
from src.app import app

@pytest.fixture
def client():
    """Creates a test client using Flask's test client"""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_index_page(client):
    """Test the index route"""
    response = client.get('/')
    assert response.status_code == 200
    assert b"hostname" in response.data or b"ip" in response.data  # Ensure the response contains hostname or IP

def test_error_handling(mocker, client):
    """Simulate an error and check error page rendering"""
    mocker.patch('socket.gethostname', side_effect=Exception("Mocked error"))
    response = client.get('/')
    assert response.status_code == 200
    assert b"error" in response.data.lower()  # Ensure the error page is returned
