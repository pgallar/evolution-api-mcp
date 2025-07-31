import pytest
from fastapi.testclient import TestClient
from src.main import app

@pytest.fixture
def client():
    """Test client fixture"""
    return TestClient(app)

@pytest.fixture
def instance_name():
    """Instance name fixture"""
    return "test_instance"

@pytest.fixture
def test_number():
    """Test phone number fixture"""
    return "1234567890"

@pytest.fixture
def message_key(test_number):
    """Message key fixture"""
    return {
        "remoteJid": f"{test_number}@s.whatsapp.net",
        "fromMe": True,
        "id": "test_message_id"
    }

@pytest.fixture
def test_contact():
    """Test contact fixture"""
    return {
        "fullName": "John Doe",
        "wuid": "1234567890",
        "phoneNumber": "+1234567890",
        "organization": "Test Org",
        "email": "john@example.com",
        "url": "https://example.com"
    }

@pytest.fixture
def test_location():
    """Test location fixture"""
    return {
        "latitude": 40.7128,
        "longitude": -74.0060,
        "name": "New York City",
        "address": "New York, NY, USA"
    }

@pytest.fixture
def test_media():
    """Test media fixture"""
    return {
        "media_type": "image",
        "media": "https://example.com/image.jpg",
        "caption": "Test image",
        "filename": "test.jpg",
        "mimetype": "image/jpeg"
    }

@pytest.fixture
def test_poll():
    """Test poll fixture"""
    return {
        "name": "Favorite color?",
        "options": ["Red", "Blue", "Green"],
        "selectable_count": 1
    } 