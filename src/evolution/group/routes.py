from typing import Dict, Any, Optional, List
from pydantic import BaseModel, Field
from ..base_routes import BaseRoutes
from .client import GroupClient

class GroupRoutes(BaseRoutes):
    def register_tools(self, mcp):
        @mcp.tool(
            description="Crear un nuevo grupo",
            tags={"group", "create"}
        )
        async def create_group(
            instance_name: str,
            subject: str,
            description: Optional[str] = None,
            participants: List[str] = []
        ) -> Dict[str, Any]:
            """Crear un nuevo grupo"""
            try:
                self.client = GroupClient()
                result = await self.client.create_group(
                    instance_name=instance_name,
                    subject=subject,
                    description=description,
                    participants=participants
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error creando grupo: {str(e)}"}

        @mcp.tool(
            description="Actualizar foto de grupo",
            tags={"group", "update"}
        )
        async def update_group_picture(
            instance_name: str,
            groupJid: str,
            image: str
        ) -> Dict[str, Any]:
            """Actualizar foto de grupo"""
            try:
                self.client = GroupClient()
                result = await self.client.update_group_picture(
                    instance_name=instance_name,
                    groupJid=groupJid,
                    image=image
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error actualizando foto: {str(e)}"}

        @mcp.tool(
            description="Actualizar nombre de grupo",
            tags={"group", "update"}
        )
        async def update_group_subject(
            instance_name: str,
            groupJid: str,
            subject: str
        ) -> Dict[str, Any]:
            """Actualizar nombre de grupo"""
            try:
                self.client = GroupClient()
                result = await self.client.update_group_subject(
                    instance_name=instance_name,
                    groupJid=groupJid,
                    subject=subject
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error actualizando nombre: {str(e)}"}

        @mcp.tool(
            description="Actualizar descripción de grupo",
            tags={"group", "update"}
        )
        async def update_group_description(
            instance_name: str,
            groupJid: str,
            description: str
        ) -> Dict[str, Any]:
            """Actualizar descripción de grupo"""
            try:
                self.client = GroupClient()
                result = await self.client.update_group_description(
                    instance_name=instance_name,
                    groupJid=groupJid,
                    description=description
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error actualizando descripción: {str(e)}"}

        @mcp.tool(
            description="Obtener código de invitación",
            tags={"group", "invite"}
        )
        async def fetch_invite_code(
            instance_name: str,
            groupJid: str
        ) -> Dict[str, Any]:
            """Obtener código de invitación"""
            try:
                self.client = GroupClient()
                result = await self.client.fetch_invite_code(
                    instance_name=instance_name,
                    groupJid=groupJid
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo código: {str(e)}"}

        @mcp.tool(
            description="Revocar código de invitación",
            tags={"group", "invite"}
        )
        async def revoke_invite_code(
            instance_name: str,
            groupJid: str
        ) -> Dict[str, Any]:
            """Revocar código de invitación"""
            try:
                self.client = GroupClient()
                result = await self.client.revoke_invite_code(
                    instance_name=instance_name,
                    groupJid=groupJid
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error revocando código: {str(e)}"}

        @mcp.tool(
            description="Enviar invitación de grupo",
            tags={"group", "invite"}
        )
        async def send_invite(
            instance_name: str,
            groupJid: str,
            description: str,
            numbers: List[str]
        ) -> Dict[str, Any]:
            """Enviar invitación de grupo"""
            try:
                self.client = GroupClient()
                result = await self.client.send_invite(
                    instance_name=instance_name,
                    groupJid=groupJid,
                    description=description,
                    numbers=numbers
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error enviando invitación: {str(e)}"}

        @mcp.tool(
            description="Buscar grupo por código de invitación",
            tags={"group", "search"}
        )
        async def find_group_by_invite(
            instance_name: str,
            inviteCode: str
        ) -> Dict[str, Any]:
            """Buscar grupo por código de invitación"""
            try:
                self.client = GroupClient()
                result = await self.client.find_group_by_invite(
                    instance_name=instance_name,
                    inviteCode=inviteCode
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error buscando grupo: {str(e)}"}

        @mcp.tool(
            description="Obtener información de grupo",
            tags={"group", "info"}
        )
        async def find_group_info(
            instance_name: str,
            groupJid: str
        ) -> Dict[str, Any]:
            """Obtener información de grupo"""
            try:
                self.client = GroupClient()
                result = await self.client.find_group_info(
                    instance_name=instance_name,
                    groupJid=groupJid
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo información: {str(e)}"}

        @mcp.tool(
            description="Obtener todos los grupos",
            tags={"group", "list"}
        )
        async def fetch_all_groups(
            instance_name: str,
            getParticipants: bool = False
        ) -> Dict[str, Any]:
            """Obtener todos los grupos"""
            try:
                self.client = GroupClient()
                result = await self.client.fetch_all_groups(
                    instance_name=instance_name,
                    getParticipants=getParticipants
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo grupos: {str(e)}"}

        @mcp.tool(
            description="Obtener participantes del grupo",
            tags={"group", "participants"}
        )
        async def get_participants(
            instance_name: str,
            groupJid: str
        ) -> Dict[str, Any]:
            """Obtener participantes del grupo"""
            try:
                self.client = GroupClient()
                result = await self.client.get_participants(
                    instance_name=instance_name,
                    groupJid=groupJid
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo participantes: {str(e)}"}

        @mcp.tool(
            description="Actualizar participante del grupo",
            tags={"group", "participants"}
        )
        async def update_participant(
            instance_name: str,
            groupJid: str,
            action: str,  # add, remove, promote, demote
            participants: List[str]
        ) -> Dict[str, Any]:
            """Actualizar participante del grupo"""
            try:
                self.client = GroupClient()
                result = await self.client.update_participant(
                    instance_name=instance_name,
                    groupJid=groupJid,
                    action=action,
                    participants=participants
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error actualizando participante: {str(e)}"}

        @mcp.tool(
            description="Actualizar configuración del grupo",
            tags={"group", "settings"}
        )
        async def update_setting(
            instance_name: str,
            groupJid: str,
            action: str  # announcement, not_announcement, locked, unlocked
        ) -> Dict[str, Any]:
            """Actualizar configuración del grupo"""
            try:
                self.client = GroupClient()
                result = await self.client.update_setting(
                    instance_name=instance_name,
                    groupJid=groupJid,
                    action=action
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error actualizando configuración: {str(e)}"}

        @mcp.tool(
            description="Activar/desactivar mensajes temporales",
            tags={"group", "settings"}
        )
        async def toggle_ephemeral(
            instance_name: str,
            groupJid: str,
            expiration: int  # 0, 86400, 604800, 7776000
        ) -> Dict[str, Any]:
            """Activar/desactivar mensajes temporales"""
            try:
                self.client = GroupClient()
                result = await self.client.toggle_ephemeral(
                    instance_name=instance_name,
                    groupJid=groupJid,
                    expiration=expiration
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error configurando mensajes temporales: {str(e)}"}

        @mcp.tool(
            description="Salir del grupo",
            tags={"group", "leave"}
        )
        async def leave_group(
            instance_name: str,
            groupJid: str
        ) -> Dict[str, Any]:
            """Salir del grupo"""
            try:
                self.client = GroupClient()
                result = await self.client.leave_group(
                    instance_name=instance_name,
                    groupJid=groupJid
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error saliendo del grupo: {str(e)}"} 