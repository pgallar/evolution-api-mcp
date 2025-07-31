from typing import Dict, Any, Optional, List
from pydantic import BaseModel, Field
from ..base_routes import BaseRoutes
from .client import ChatClient

class ChatRoutes(BaseRoutes):
    def register_tools(self, mcp):
        @mcp.tool(
            description="Verificar números de WhatsApp",
            tags={"chat", "numbers"}
        )
        async def check_whatsapp_numbers(
            instance_name: str,
            numbers: List[str]
        ) -> Dict[str, Any]:
            """Verificar si los números están registrados en WhatsApp"""
            try:
                self.client = ChatClient()
                result = await self.client.check_whatsapp_numbers(
                    instance_name=instance_name,
                    numbers=numbers
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error verificando números: {str(e)}"}

        @mcp.tool(
            description="Marcar mensajes como leídos",
            tags={"chat", "read"}
        )
        async def mark_messages_as_read(
            instance_name: str,
            messages: List[Dict[str, Any]]
        ) -> Dict[str, Any]:
            """Marcar mensajes como leídos"""
            try:
                self.client = ChatClient()
                result = await self.client.mark_message_as_read(
                    instance_name=instance_name,
                    messages=messages
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error marcando mensajes: {str(e)}"}

        @mcp.tool(
            description="Archivar o desarchivar chat",
            tags={"chat", "archive"}
        )
        async def archive_chat(
            instance_name: str,
            chat: str,
            last_message: Dict[str, Any],
            archive: bool = True
        ) -> Dict[str, Any]:
            """Archivar o desarchivar un chat"""
            try:
                self.client = ChatClient()
                result = await self.client.archive_chat(
                    instance_name=instance_name,
                    chat=chat,
                    last_message=last_message,
                    archive=archive
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error archivando chat: {str(e)}"}

        @mcp.tool(
            description="Marcar chat como no leído",
            tags={"chat", "unread"}
        )
        async def mark_chat_unread(
            instance_name: str,
            chat: str,
            last_message: Dict[str, Any]
        ) -> Dict[str, Any]:
            """Marcar un chat como no leído"""
            try:
                self.client = ChatClient()
                result = await self.client.mark_chat_unread(
                    instance_name=instance_name,
                    chat=chat,
                    last_message=last_message
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error marcando chat: {str(e)}"}

        @mcp.tool(
            description="Eliminar mensaje",
            tags={"chat", "delete"}
        )
        async def delete_message(
            instance_name: str,
            message_id: str,
            remote_jid: str,
            from_me: bool,
            participant: Optional[str] = None
        ) -> Dict[str, Any]:
            """Eliminar un mensaje"""
            try:
                self.client = ChatClient()
                result = await self.client.delete_message(
                    instance_name=instance_name,
                    message_id=message_id,
                    remote_jid=remote_jid,
                    from_me=from_me,
                    participant=participant
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error eliminando mensaje: {str(e)}"}

        @mcp.tool(
            description="Obtener foto de perfil",
            tags={"chat", "profile"}
        )
        async def fetch_profile_picture(
            instance_name: str,
            number: str
        ) -> Dict[str, Any]:
            """Obtener URL de foto de perfil"""
            try:
                self.client = ChatClient()
                result = await self.client.fetch_profile_picture(
                    instance_name=instance_name,
                    number=number
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo foto: {str(e)}"}

        @mcp.tool(
            description="Obtener base64 de mensaje multimedia",
            tags={"chat", "media"}
        )
        async def get_base64_from_media(
            instance_name: str,
            message_id: str,
            convert_to_mp4: bool = False
        ) -> Dict[str, Any]:
            """Obtener base64 de un mensaje multimedia"""
            try:
                self.client = ChatClient()
                result = await self.client.get_base64_from_media(
                    instance_name=instance_name,
                    message_id=message_id,
                    convert_to_mp4=convert_to_mp4
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo media: {str(e)}"}

        @mcp.tool(
            description="Actualizar mensaje",
            tags={"chat", "update"}
        )
        async def update_message(
            instance_name: str,
            number: str,
            key: Dict[str, Any],
            text: str
        ) -> Dict[str, Any]:
            """Actualizar un mensaje"""
            try:
                self.client = ChatClient()
                result = await self.client.update_message(
                    instance_name=instance_name,
                    number=number,
                    key=key,
                    text=text
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error actualizando mensaje: {str(e)}"}

        @mcp.tool(
            description="Enviar presencia",
            tags={"chat", "presence"}
        )
        async def send_presence(
            instance_name: str,
            number: str,
            presence: str,
            delay: Optional[int] = None
        ) -> Dict[str, Any]:
            """Enviar estado de presencia"""
            try:
                self.client = ChatClient()
                result = await self.client.send_presence(
                    instance_name=instance_name,
                    number=number,
                    presence=presence,
                    delay=delay
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error enviando presencia: {str(e)}"}

        @mcp.tool(
            description="Buscar mensajes",
            tags={"chat", "search"}
        )
        async def find_messages(
            instance_name: str,
            remote_jid: Optional[str] = None,
            page: Optional[int] = None,
            offset: Optional[int] = None
        ) -> Dict[str, Any]:
            """Buscar mensajes"""
            try:
                self.client = ChatClient()
                result = await self.client.find_messages(
                    instance_name=instance_name,
                    remote_jid=remote_jid,
                    page=page,
                    offset=offset
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error buscando mensajes: {str(e)}"}

        @mcp.tool(
            description="Obtener lista de chats",
            tags={"chat", "list"}
        )
        async def find_chats(
            instance_name: str
        ) -> Dict[str, Any]:
            """Obtener lista de chats"""
            try:
                self.client = ChatClient()
                result = await self.client.find_chats(instance_name)
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error obteniendo chats: {str(e)}"}

        @mcp.tool(
            description="Actualizar estado de bloqueo",
            tags={"chat", "block"}
        )
        async def update_block_status(
            instance_name: str,
            number: str,
            status: str  # block, unblock
        ) -> Dict[str, Any]:
            """Actualizar estado de bloqueo de un número"""
            try:
                self.client = ChatClient()
                result = await self.client.update_block_status(
                    instance_name=instance_name,
                    number=number,
                    status=status
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error actualizando bloqueo: {str(e)}"}

        @mcp.tool(
            description="Buscar contactos",
            tags={"chat", "contacts"}
        )
        async def find_contacts(
            instance_name: str,
            where: Optional[Dict[str, Any]] = None
        ) -> Dict[str, Any]:
            """Buscar contactos"""
            try:
                self.client = ChatClient()
                result = await self.client.find_contacts(
                    instance_name=instance_name,
                    where=where
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error buscando contactos: {str(e)}"}

        @mcp.tool(
            description="Buscar mensajes de estado",
            tags={"chat", "status"}
        )
        async def find_status_message(
            instance_name: str,
            where: Optional[Dict[str, Any]] = None,
            page: Optional[int] = None,
            offset: Optional[int] = None
        ) -> Dict[str, Any]:
            """Buscar mensajes de estado"""
            try:
                self.client = ChatClient()
                result = await self.client.find_status_message(
                    instance_name=instance_name,
                    where=where,
                    page=page,
                    offset=offset
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error buscando mensajes de estado: {str(e)}"} 