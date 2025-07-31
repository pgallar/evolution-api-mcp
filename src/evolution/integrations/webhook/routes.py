from typing import Dict, Any, List, Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field
from ..base import BaseIntegrationRoutes, IntegrationConfig

class WebhookConfig(IntegrationConfig):
    url: str = Field(description="URL del webhook")
    headers: Dict[str, str] = Field(default_factory=dict, description="Headers adicionales")
    by_events: bool = Field(False, description="Enviar eventos por separado")
    base64: bool = Field(False, description="Codificar contenido multimedia en base64")

class WebhookRoutes(BaseIntegrationRoutes):
    def __init__(self):
        super().__init__("webhook")

    def register_tools(self, mcp: FastAPI):
        @mcp.tool(
            description="Configurar webhook para una instancia",
            tags={"webhook", "config"}
        )
        async def set_webhook(
            instance_name: str,
            config: WebhookConfig
        ) -> Dict[str, Any]:
            """
            Configura un webhook para una instancia específica
            """
            return await self.webhook_client.set_webhook(
                instance_name=instance_name,
                enabled=config.enabled,
                url=config.url,
                events=config.events,
                headers=config.headers,
                by_events=config.by_events,
                base64=config.base64
            )

        @mcp.tool(
            description="Obtener configuración del webhook",
            tags={"webhook", "info"}
        )
        async def find_webhook(
            instance_name: str
        ) -> Dict[str, Any]:
            """
            Obtiene la configuración actual del webhook
            """
            return await self.webhook_client.find_integration(instance_name) 