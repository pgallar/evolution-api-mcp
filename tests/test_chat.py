import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

INSTANCE_NAME = "test_instance"
TEST_NUMBER = "1234567890"

def test_check_whatsapp_numbers():
    """Test checking WhatsApp numbers"""
    response = client.post(f"/chat/{INSTANCE_NAME}/whatsapp-numbers", json={
        "numbers": [TEST_NUMBER]
    })
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_mark_messages_as_read():
    """Test marking messages as read"""
    response = client.post(f"/chat/{INSTANCE_NAME}/mark-read", json={
        "messages": [{
            "remoteJid": f"{TEST_NUMBER}@s.whatsapp.net",
            "fromMe": True,
            "id": "test_message_id"
        }]
    })
    assert response.status_code == 200

def test_archive_chat():
    """Test archiving a chat"""
    response = client.post(f"/chat/{INSTANCE_NAME}/archive", json={
        "chat": f"{TEST_NUMBER}@s.whatsapp.net",
        "last_message": {
            "key": {
                "remoteJid": f"{TEST_NUMBER}@s.whatsapp.net",
                "fromMe": True,
                "id": "test_message_id"
            }
        },
        "archive": True
    })
    assert response.status_code == 200

def test_mark_chat_unread():
    """Test marking a chat as unread"""
    response = client.post(f"/chat/{INSTANCE_NAME}/mark-unread", json={
        "chat": f"{TEST_NUMBER}@s.whatsapp.net",
        "last_message": {
            "key": {
                "remoteJid": f"{TEST_NUMBER}@s.whatsapp.net",
                "fromMe": True,
                "id": "test_message_id"
            }
        }
    })
    assert response.status_code == 200

def test_delete_message():
    """Test deleting a message"""
    response = client.delete(f"/chat/{INSTANCE_NAME}/message", json={
        "message_id": "test_message_id",
        "remote_jid": f"{TEST_NUMBER}@s.whatsapp.net",
        "from_me": True
    })
    assert response.status_code == 200

def test_fetch_profile_picture():
    """Test fetching profile picture"""
    response = client.post(f"/chat/{INSTANCE_NAME}/profile-picture", json={
        "number": TEST_NUMBER
    })
    assert response.status_code == 200

def test_get_base64_from_media():
    """Test getting base64 from media message"""
    response = client.post(f"/chat/{INSTANCE_NAME}/media-base64", json={
        "message_id": "test_message_id",
        "convert_to_mp4": False
    })
    assert response.status_code == 200

def test_update_message():
    """Test updating a message"""
    response = client.post(f"/chat/{INSTANCE_NAME}/update-message", json={
        "number": TEST_NUMBER,
        "key": {
            "remoteJid": f"{TEST_NUMBER}@s.whatsapp.net",
            "fromMe": True,
            "id": "test_message_id"
        },
        "text": "Updated message"
    })
    assert response.status_code == 200

def test_send_presence():
    """Test sending presence status"""
    response = client.post(f"/chat/{INSTANCE_NAME}/presence", json={
        "number": TEST_NUMBER,
        "presence": "composing",
        "delay": 1000
    })
    assert response.status_code == 200

def test_find_messages():
    """Test finding messages"""
    response = client.post(f"/chat/{INSTANCE_NAME}/messages", json={
        "remote_jid": f"{TEST_NUMBER}@s.whatsapp.net",
        "page": 1,
        "offset": 10
    })
    assert response.status_code == 200

def test_find_chats():
    """Test finding all chats"""
    response = client.get(f"/chat/{INSTANCE_NAME}/chats")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list) 