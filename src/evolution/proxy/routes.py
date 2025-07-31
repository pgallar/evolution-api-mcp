from typing import Dict, Any, Optional
from fastapi import FastAPI
from pydantic import BaseModel, Field
from ..base_routes import BaseRoutes

class ProxyConfig(BaseModel):
    enabled: bool = Field(description="Si el proxy está habilitado")
    host: str = Field(description="Host del proxy")
    port: str = Field(description="Puerto del proxy")
    protocol: str = Field(description="Protocolo del proxy (http, https, socks)")
    username: Optional[str] = Field(None, description="Usuario para autenticación del proxy")
    password: Optional[str] = Field(None, description="Contraseña para autenticación del proxy")

class ProxyRoutes(BaseRoutes):
    def register_tools(self, mcp: FastAPI):
        @mcp.tool(
            description="Configurar proxy para una instancia",
            tags={"proxy", "config"}
        )
        async def set_proxy(
            instance_name: str,
            config: ProxyConfig
        ) -> Dict[str, Any]:
            """
            Configura el proxy para una instancia específica
            """
            return await self.proxy_client.set_proxy(
                instance_name=instance_name,
                enabled=config.enabled,
                host=config.host,
                port=config.port,
                protocol=config.protocol,
                username=config.username,
                password=config.password
            )

        @mcp.tool(
            description="Obtener configuración del proxy",
            tags={"proxy", "info"}
        )
        async def find_proxy(
            instance_name: str
        ) -> Dict[str, Any]:
            """
            Obtiene la configuración actual del proxy para una instancia
            """
            return await self.proxy_client.find_proxy(instance_name) 