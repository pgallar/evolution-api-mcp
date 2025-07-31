from typing import Dict, Any
from pydantic import BaseModel, Field
from ..base_routes import BaseRoutes
from .client import ProfileClient

class ProfileRoutes(BaseRoutes):
    def register_tools(self, mcp):
        @mcp.tool(
            description="Obtener perfil de negocio",
            tags={"profile", "business"}
        )
        async def fetch_business_profile(
            instance_name: str,
            number: str
        ) -> Dict[str, Any]:
            """Obtener perfil de negocio"""
            try:
                self.client = ProfileClient()
                result = await self.client.fetch_business_profile(
                    instance_name=instance_name,
                    number=number
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo perfil de negocio: {str(e)}"}

        @mcp.tool(
            description="Obtener perfil",
            tags={"profile"}
        )
        async def fetch_profile(
            instance_name: str,
            number: str
        ) -> Dict[str, Any]:
            """Obtener perfil"""
            try:
                self.client = ProfileClient()
                result = await self.client.fetch_profile(
                    instance_name=instance_name,
                    number=number
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo perfil: {str(e)}"}

        @mcp.tool(
            description="Actualizar nombre de perfil",
            tags={"profile", "update"}
        )
        async def update_profile_name(
            instance_name: str,
            name: str
        ) -> Dict[str, Any]:
            """Actualizar nombre de perfil"""
            try:
                self.client = ProfileClient()
                result = await self.client.update_profile_name(
                    instance_name=instance_name,
                    name=name
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error actualizando nombre: {str(e)}"}

        @mcp.tool(
            description="Actualizar estado de perfil",
            tags={"profile", "update"}
        )
        async def update_profile_status(
            instance_name: str,
            status: str
        ) -> Dict[str, Any]:
            """Actualizar estado de perfil"""
            try:
                self.client = ProfileClient()
                result = await self.client.update_profile_status(
                    instance_name=instance_name,
                    status=status
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error actualizando estado: {str(e)}"}

        @mcp.tool(
            description="Actualizar foto de perfil",
            tags={"profile", "update"}
        )
        async def update_profile_picture(
            instance_name: str,
            picture: str  # url
        ) -> Dict[str, Any]:
            """Actualizar foto de perfil"""
            try:
                self.client = ProfileClient()
                result = await self.client.update_profile_picture(
                    instance_name=instance_name,
                    picture=picture
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error actualizando foto: {str(e)}"}

        @mcp.tool(
            description="Eliminar foto de perfil",
            tags={"profile", "delete"}
        )
        async def remove_profile_picture(
            instance_name: str
        ) -> Dict[str, Any]:
            """Eliminar foto de perfil"""
            try:
                self.client = ProfileClient()
                result = await self.client.remove_profile_picture(instance_name)
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error eliminando foto: {str(e)}"}

        @mcp.tool(
            description="Obtener configuración de privacidad",
            tags={"privacy"}
        )
        async def fetch_privacy_settings(
            instance_name: str
        ) -> Dict[str, Any]:
            """Obtener configuración de privacidad"""
            try:
                self.client = ProfileClient()
                result = await self.client.fetch_privacy_settings(instance_name)
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo configuración: {str(e)}"}

        @mcp.tool(
            description="Actualizar configuración de privacidad",
            tags={"privacy", "update"}
        )
        async def update_privacy_settings(
            instance_name: str,
            readreceipts: str,  # all, none
            profile: str,  # all, contacts, contact_blacklist, none
            status: str,  # all, contacts, contact_blacklist, none
            online: str,  # all, match_last_seen
            last: str,  # all, contacts, contact_blacklist, none
            groupadd: str  # all, contacts, contact_blacklist
        ) -> Dict[str, Any]:
            """Actualizar configuración de privacidad"""
            try:
                self.client = ProfileClient()
                result = await self.client.update_privacy_settings(
                    instance_name=instance_name,
                    readreceipts=readreceipts,
                    profile=profile,
                    status=status,
                    online=online,
                    last=last,
                    groupadd=groupadd
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error actualizando configuración: {str(e)}"} 