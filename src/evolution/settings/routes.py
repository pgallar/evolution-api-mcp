from typing import Dict, Any, Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field, validator
from ..base_routes import BaseRoutes

class SettingsConfig(BaseModel):
    reject_call: bool = Field(default=False, description="Rechazar llamadas entrantes")
    msg_call: Optional[str] = Field(default=None, description="Mensaje para llamadas rechazadas")
    groups_ignore: bool = Field(default=False, description="Ignorar mensajes de grupos")
    always_online: bool = Field(default=False, description="Mantener estado en línea")
    read_messages: bool = Field(default=False, description="Marcar mensajes como leídos automáticamente")
    read_status: bool = Field(default=False, description="Marcar estados como vistos automáticamente")
    sync_full_history: bool = Field(default=False, description="Sincronizar historial completo")

    class Config:
        extra = "ignore"
        validate_assignment = True

    @validator('*', pre=True)
    def empty_str_to_none(cls, v):
        if v == "":
            return None
        return v

class SettingsRoutes(BaseRoutes):
    def register_tools(self, mcp: FastAPI):
        @mcp.tool(
            description="Configurar ajustes de una instancia",
            tags={"settings", "config"}
        )
        async def set_settings(
            instance_name: str,
            config: SettingsConfig
        ) -> Dict[str, Any]:
            """
            Configura los ajustes para una instancia específica
            """
            return await self.settings_client.set_settings(
                instance_name=instance_name,
                reject_call=config.reject_call,
                msg_call=config.msg_call,
                groups_ignore=config.groups_ignore,
                always_online=config.always_online,
                read_messages=config.read_messages,
                read_status=config.read_status,
                sync_full_history=config.sync_full_history
            )

        @mcp.tool(
            description="Obtener configuración de una instancia",
            tags={"settings", "info"}
        )
        async def find_settings(
            instance_name: str
        ) -> Dict[str, Any]:
            """
            Obtiene la configuración actual de una instancia
            """
            return await self.settings_client.find_settings(instance_name) 