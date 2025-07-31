from typing import Dict, Any
from pydantic import BaseModel, Field
from ..base_routes import BaseRoutes
from .client import LabelClient

class LabelRoutes(BaseRoutes):
    def register_tools(self, mcp):
        @mcp.tool(
            description="Buscar etiquetas",
            tags={"label", "list"}
        )
        async def find_labels(
            instance_name: str
        ) -> Dict[str, Any]:
            """Buscar todas las etiquetas"""
            try:
                self.client = LabelClient()
                result = await self.client.find_labels(instance_name)
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error buscando etiquetas: {str(e)}"}

        @mcp.tool(
            description="Manejar etiquetas",
            tags={"label", "manage"}
        )
        async def handle_label(
            instance_name: str,
            number: str,
            labelId: str,
            action: str  # add, remove
        ) -> Dict[str, Any]:
            """Manejar operaciones de etiquetas"""
            try:
                self.client = LabelClient()
                result = await self.client.handle_label(
                    instance_name=instance_name,
                    number=number,
                    labelId=labelId,
                    action=action
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error manejando etiqueta: {str(e)}"} 