import pytest
from fastapi.testclient import TestClient
from src.main import app

client = TestClient(app)

def test_create_instance():
    """Test creating a new WhatsApp instance"""
    response = client.post("/instance/create", json={
        "instance_name": "test_instance",
        "qrcode": True,
        "integration": "WHATSAPP-BAILEYS"
    })
    assert response.status_code == 200
    data = response.json()
    assert "hash" in data

def test_fetch_instances():
    """Test fetching all instances"""
    response = client.get("/instance/fetch")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

def test_connect_instance():
    """Test connecting to an instance"""
    response = client.get("/instance/connect/test_instance")
    assert response.status_code == 200

def test_restart_instance():
    """Test restarting an instance"""
    response = client.post("/instance/restart/test_instance")
    assert response.status_code == 200

def test_set_presence():
    """Test setting presence status"""
    response = client.post("/instance/presence/test_instance", json={
        "presence": "available"
    })
    assert response.status_code == 200

def test_get_connection_state():
    """Test getting connection state"""
    response = client.get("/instance/status/test_instance")
    assert response.status_code == 200
    data = response.json()
    assert "state" in data

def test_logout_instance():
    """Test logging out from an instance"""
    response = client.delete("/instance/logout/test_instance")
    assert response.status_code == 200

def test_delete_instance():
    """Test deleting an instance"""
    response = client.delete("/instance/delete/test_instance")
    assert response.status_code == 200 