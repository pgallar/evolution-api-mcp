import os
import pytest
from fastapi.testclient import TestClient
from src.main import app

# Verificar que las variables de entorno necesarias estén configuradas
def check_env_vars():
    required_vars = ["EVOLUTION_API_URL", "EVOLUTION_API_KEY"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    if missing_vars:
        pytest.skip(f"Variables de entorno faltantes: {', '.join(missing_vars)}")

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture(autouse=True)
def setup_env():
    check_env_vars()

def test_create_and_delete_instance(client):
    """Test completo de creación y eliminación de instancia"""
    # Crear instancia
    create_response = client.post("/instance/create", json={
        "instance_name": "test_integration",
        "qrcode": True,
        "integration": "WHATSAPP-BAILEYS"
    })
    assert create_response.status_code == 200
    data = create_response.json()
    assert "hash" in data

    # Verificar que la instancia existe
    fetch_response = client.get("/instance/fetch")
    assert fetch_response.status_code == 200
    instances = fetch_response.json()
    assert any(i.get("instanceName") == "test_integration" for i in instances)

    # Eliminar instancia
    delete_response = client.delete("/instance/delete/test_integration")
    assert delete_response.status_code == 200

    # Verificar que la instancia fue eliminada
    fetch_response = client.get("/instance/fetch")
    assert fetch_response.status_code == 200
    instances = fetch_response.json()
    assert not any(i.get("instanceName") == "test_integration" for i in instances)

def test_instance_lifecycle(client):
    """Test del ciclo de vida completo de una instancia"""
    instance_name = "test_lifecycle"

    # Crear instancia
    create_response = client.post("/instance/create", json={
        "instance_name": instance_name,
        "qrcode": True,
        "integration": "WHATSAPP-BAILEYS"
    })
    assert create_response.status_code == 200

    # Conectar instancia
    connect_response = client.get(f"/instance/connect/{instance_name}")
    assert connect_response.status_code == 200

    # Verificar estado de conexión
    status_response = client.get(f"/instance/status/{instance_name}")
    assert status_response.status_code == 200
    assert "state" in status_response.json()

    # Establecer presencia
    presence_response = client.post(f"/instance/presence/{instance_name}", json={
        "presence": "available"
    })
    assert presence_response.status_code == 200

    # Reiniciar instancia
    restart_response = client.post(f"/instance/restart/{instance_name}")
    assert restart_response.status_code == 200

    # Cerrar sesión
    logout_response = client.delete(f"/instance/logout/{instance_name}")
    assert logout_response.status_code == 200

    # Eliminar instancia
    delete_response = client.delete(f"/instance/delete/{instance_name}")
    assert delete_response.status_code == 200

@pytest.mark.skip(reason="Requiere una instancia autenticada")
def test_message_operations(client):
    """Test de operaciones de mensajes"""
    instance_name = "test_messages"
    test_number = os.getenv("TEST_WHATSAPP_NUMBER", "1234567890")

    # Enviar mensaje de texto
    text_response = client.post(f"/message/{instance_name}/text", json={
        "number": test_number,
        "text": "Test message from integration tests"
    })
    assert text_response.status_code == 200
    message_id = text_response.json().get("key", {}).get("id")

    # Enviar reacción al mensaje
    reaction_response = client.post(f"/message/{instance_name}/reaction", json={
        "key": {
            "remoteJid": f"{test_number}@s.whatsapp.net",
            "fromMe": True,
            "id": message_id
        },
        "reaction": "👍"
    })
    assert reaction_response.status_code == 200

    # Buscar mensajes
    messages_response = client.post(f"/chat/{instance_name}/messages", json={
        "remote_jid": f"{test_number}@s.whatsapp.net"
    })
    assert messages_response.status_code == 200
    messages = messages_response.json()
    assert len(messages) > 0

@pytest.mark.skip(reason="Requiere una instancia autenticada")
def test_chat_operations(client):
    """Test de operaciones de chat"""
    instance_name = "test_chats"
    test_number = os.getenv("TEST_WHATSAPP_NUMBER", "1234567890")

    # Verificar número de WhatsApp
    numbers_response = client.post(f"/chat/{instance_name}/whatsapp-numbers", json={
        "numbers": [test_number]
    })
    assert numbers_response.status_code == 200

    # Obtener foto de perfil
    profile_response = client.post(f"/chat/{instance_name}/profile-picture", json={
        "number": test_number
    })
    assert profile_response.status_code == 200

    # Buscar chats
    chats_response = client.get(f"/chat/{instance_name}/chats")
    assert chats_response.status_code == 200
    chats = chats_response.json()
    assert isinstance(chats, list) 