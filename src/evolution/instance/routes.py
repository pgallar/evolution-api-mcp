from typing import Dict, Any, Optional, List
from pydantic import BaseModel, Field
from ..base_routes import BaseRoutes
from .client import InstanceClient

class InstanceRoutes(BaseRoutes):
    def register_tools(self, mcp):
        @mcp.tool(
            description="Crear una nueva instancia de WhatsApp",
            tags={"instance", "create"}
        )
        async def create_instance(
            instance_name: str,
            qrcode: bool = True,
            integration: str = "WHATSAPP-BAILEYS",
            webhook: Optional[Dict[str, Any]] = None,
            settings: Optional[Dict[str, Any]] = None
        ) -> Dict[str, Any]:
            """Crear una nueva instancia de WhatsApp"""
            try:
                self.client = InstanceClient()
                result = await self.client.create_instance(
                    instance_name=instance_name,
                    qrcode=qrcode,
                    integration=integration,
                    webhook=webhook,
                    settings=settings
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error creando instancia: {str(e)}"}

        @mcp.tool(
            description="Obtener lista de instancias",
            tags={"instance", "list"}
        )
        async def fetch_instances(
            instance_name: Optional[str] = None
        ) -> Dict[str, Any]:
            """Obtener lista de instancias"""
            try:
                self.client = InstanceClient()
                instances = await self.client.fetch_instances(instance_name)
                return {
                    "success": True,
                    "instances": instances
                }
            except Exception as e:
                return {"error": f"Error obteniendo instancias: {str(e)}"}

        @mcp.tool(
            description="Conectar a una instancia",
            tags={"instance", "connect"}
        )
        async def connect_instance(
            instance_name: str
        ) -> Dict[str, Any]:
            """Conectar a una instancia"""
            try:
                self.client = InstanceClient()
                result = await self.client.connect_instance(instance_name)
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error conectando instancia: {str(e)}"}

        @mcp.tool(
            description="Reiniciar una instancia",
            tags={"instance", "restart"}
        )
        async def restart_instance(
            instance_name: str
        ) -> Dict[str, Any]:
            """Reiniciar una instancia"""
            try:
                self.client = InstanceClient()
                result = await self.client.restart_instance(instance_name)
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error reiniciando instancia: {str(e)}"}

        @mcp.tool(
            description="Establecer presencia de una instancia",
            tags={"instance", "presence"}
        )
        async def set_presence(
            instance_name: str,
            presence: str
        ) -> Dict[str, Any]:
            """Establecer presencia de una instancia"""
            try:
                self.client = InstanceClient()
                result = await self.client.set_presence(instance_name, presence)
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error estableciendo presencia: {str(e)}"}

        @mcp.tool(
            description="Obtener estado de conexión de una instancia",
            tags={"instance", "status"}
        )
        async def get_connection_state(
            instance_name: str
        ) -> Dict[str, Any]:
            """Obtener estado de conexión de una instancia"""
            try:
                self.client = InstanceClient()
                state = await self.client.get_connection_state(instance_name)
                return {
                    "success": True,
                    "state": state
                }
            except Exception as e:
                return {"error": f"Error obteniendo estado: {str(e)}"}

        @mcp.tool(
            description="Cerrar sesión de una instancia",
            tags={"instance", "logout"}
        )
        async def logout_instance(
            instance_name: str
        ) -> Dict[str, Any]:
            """Cerrar sesión de una instancia"""
            try:
                self.client = InstanceClient()
                result = await self.client.logout_instance(instance_name)
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error cerrando sesión: {str(e)}"}

        @mcp.tool(
            description="Eliminar una instancia",
            tags={"instance", "delete"}
        )
        async def delete_instance(
            instance_name: str
        ) -> Dict[str, Any]:
            """Eliminar una instancia"""
            try:
                self.client = InstanceClient()
                result = await self.client.delete_instance(instance_name)
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error eliminando instancia: {str(e)}"} 