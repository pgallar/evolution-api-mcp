import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

INSTANCE_NAME = "test_instance"
TEST_NUMBER = "1234567890"

def test_send_text():
    """Test sending a text message"""
    response = client.post(f"/message/{INSTANCE_NAME}/text", json={
        "number": TEST_NUMBER,
        "text": "Test message"
    })
    assert response.status_code == 200

def test_send_media():
    """Test sending a media message"""
    response = client.post(f"/message/{INSTANCE_NAME}/media", json={
        "number": TEST_NUMBER,
        "media_type": "image",
        "media": "https://example.com/image.jpg",
        "caption": "Test image",
        "filename": "test.jpg",
        "mimetype": "image/jpeg"
    })
    assert response.status_code == 200

def test_send_audio():
    """Test sending an audio message"""
    response = client.post(f"/message/{INSTANCE_NAME}/audio", json={
        "number": TEST_NUMBER,
        "audio": "https://example.com/audio.mp3"
    })
    assert response.status_code == 200

def test_send_location():
    """Test sending a location message"""
    response = client.post(f"/message/{INSTANCE_NAME}/location", json={
        "number": TEST_NUMBER,
        "latitude": 40.7128,
        "longitude": -74.0060,
        "name": "New York City",
        "address": "New York, NY, USA"
    })
    assert response.status_code == 200

def test_send_contact():
    """Test sending contact information"""
    response = client.post(f"/message/{INSTANCE_NAME}/contact", json={
        "number": TEST_NUMBER,
        "contacts": [{
            "fullName": "John Doe",
            "wuid": "1234567890",
            "phoneNumber": "+1234567890",
            "organization": "Test Org",
            "email": "john@example.com",
            "url": "https://example.com"
        }]
    })
    assert response.status_code == 200

def test_send_reaction():
    """Test sending a reaction to a message"""
    response = client.post(f"/message/{INSTANCE_NAME}/reaction", json={
        "key": {
            "remoteJid": f"{TEST_NUMBER}@s.whatsapp.net",
            "fromMe": True,
            "id": "test_message_id"
        },
        "reaction": "👍"
    })
    assert response.status_code == 200

def test_send_poll():
    """Test sending a poll message"""
    response = client.post(f"/message/{INSTANCE_NAME}/poll", json={
        "number": TEST_NUMBER,
        "name": "Favorite color?",
        "options": ["Red", "Blue", "Green"],
        "selectable_count": 1
    })
    assert response.status_code == 200 