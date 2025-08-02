from typing import Dict, Any, List, Optional
from ..http_client import EvolutionAPIClient
from pydantic import BaseModel, Field, validator

class IntegrationConfig(BaseModel):
    enabled: bool = Field(description="Si la integración está habilitada")
    events: List[str] = Field(description="Lista de eventos a escuchar")

    class Config:
        extra = "ignore"
        validate_assignment = True

    @validator('*', pre=True)
    def empty_str_to_none(cls, v):
        if v == "":
            return None
        return v

class BaseIntegrationClient(EvolutionAPIClient):
    def __init__(self, integration_type: str):
        super().__init__()
        self.integration_type = integration_type

    async def set_integration(
        self,
        instance_name: str,
        enabled: bool,
        events: List[str],
        **kwargs
    ) -> Dict[str, Any]:
        """
        Configura una integración
        """
        data = {
            self.integration_type: {
                "enabled": enabled,
                "events": events,
                **kwargs
            }
        }
        return await self.post(f"/{self.integration_type}/set/{instance_name}", json=data)

    async def find_integration(self, instance_name: str) -> Dict[str, Any]:
        """
        Obtiene la configuración de una integración
        """
        return await self.get(f"/{self.integration_type}/find/{instance_name}")

class BaseIntegrationRoutes:
    def __init__(self, integration_type: str):
        self.integration_type = integration_type

    def get_events_list(self) -> List[str]:
        """
        Lista de eventos disponibles para las integraciones
        """
        return [
            "APPLICATION_STARTUP",
            "QRCODE_UPDATED",
            "MESSAGES_SET",
            "MESSAGES_UPSERT",
            "MESSAGES_UPDATE",
            "MESSAGES_DELETE",
            "SEND_MESSAGE",
            "CONTACTS_SET",
            "CONTACTS_UPSERT",
            "CONTACTS_UPDATE",
            "PRESENCE_UPDATE",
            "CHATS_SET",
            "CHATS_UPSERT",
            "CHATS_UPDATE",
            "CHATS_DELETE",
            "GROUPS_UPSERT",
            "GROUP_UPDATE",
            "GROUP_PARTICIPANTS_UPDATE",
            "CONNECTION_UPDATE",
            "LABELS_EDIT",
            "LABELS_ASSOCIATION",
            "CALL",
            "TYPEBOT_START",
            "TYPEBOT_CHANGE_STATUS"
        ] 