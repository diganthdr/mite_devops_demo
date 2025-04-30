import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_home_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Random Number Generator' in response.data

def test_generate_route(client):
    response = client.get('/api/v1/generate')
    assert response.status_code == 200
    data = response.get_json()
    assert 'number' in data
    assert isinstance(data['number'], int)
    assert 1 <= data['number'] <= 100 