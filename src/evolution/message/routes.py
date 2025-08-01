from typing import Dict, Any, Optional, List
from pydantic import BaseModel, Field
from ..base_routes import BaseRoutes
from .client import MessageClient

class ButtonModel(BaseModel):
    title: str = Field(description="Título del botón")
    displayText: str = Field(description="Texto a mostrar en el botón")
    id: str = Field(description="Identificador único del botón")

    class Config:
        json_schema_extra = {
            "example": {
                "title": "Botón 1",
                "displayText": "Click aquí",
                "id": "btn1"
            }
        }

class ListRowModel(BaseModel):
    title: str = Field(description="Título de la fila")
    description: str = Field(description="Descripción de la fila")
    rowId: str = Field(description="Identificador único de la fila")

class ListSectionModel(BaseModel):
    title: str = Field(description="Título de la sección")
    rows: List[ListRowModel] = Field(description="Filas de la sección")

class MessageRoutes(BaseRoutes):
    def register_tools(self, mcp):
        @mcp.tool(
            description="Enviar mensaje de texto",
            tags={"message", "text"}
        )
        async def send_text(
            instance_name: str,
            number: str,
            text: str,
            quoted: Optional[Dict[str, Any]] = None,
            delay: Optional[int] = None,
            mentions: Optional[List[str]] = None
        ) -> Dict[str, Any]:
            """Enviar mensaje de texto"""
            try:
                self.client = MessageClient()
                result = await self.client.send_text(
                    instance_name=instance_name,
                    number=number,
                    text=text,
                    quoted=quoted,
                    delay=delay,
                    mentions=mentions
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error enviando mensaje: {str(e)}"}

        @mcp.tool(
            description="Enviar mensaje multimedia",
            tags={"message", "media"}
        )
        async def send_media(
            instance_name: str,
            number: str,
            media_type: str,
            media: str,
            caption: Optional[str] = None,
            filename: Optional[str] = None,
            mimetype: Optional[str] = None
        ) -> Dict[str, Any]:
            """Enviar mensaje multimedia (imagen, video, documento)"""
            try:
                self.client = MessageClient()
                result = await self.client.send_media(
                    instance_name=instance_name,
                    number=number,
                    media_type=media_type,
                    media=media,
                    caption=caption,
                    filename=filename,
                    mimetype=mimetype
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error enviando media: {str(e)}"}

        @mcp.tool(
            description="Enviar mensaje de audio",
            tags={"message", "audio"}
        )
        async def send_audio(
            instance_name: str,
            number: str,
            audio: str
        ) -> Dict[str, Any]:
            """Enviar mensaje de audio"""
            try:
                self.client = MessageClient()
                result = await self.client.send_audio(
                    instance_name=instance_name,
                    number=number,
                    audio=audio
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error enviando audio: {str(e)}"}

        @mcp.tool(
            description="Enviar ubicación",
            tags={"message", "location"}
        )
        async def send_location(
            instance_name: str,
            number: str,
            latitude: float,
            longitude: float,
            name: Optional[str] = None,
            address: Optional[str] = None
        ) -> Dict[str, Any]:
            """Enviar ubicación"""
            try:
                self.client = MessageClient()
                result = await self.client.send_location(
                    instance_name=instance_name,
                    number=number,
                    latitude=latitude,
                    longitude=longitude,
                    name=name,
                    address=address
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error enviando ubicación: {str(e)}"}

        @mcp.tool(
            description="Enviar contacto",
            tags={"message", "contact"}
        )
        async def send_contact(
            instance_name: str,
            number: str,
            contacts: List[Dict[str, str]]
        ) -> Dict[str, Any]:
            """Enviar información de contacto"""
            try:
                self.client = MessageClient()
                result = await self.client.send_contact(
                    instance_name=instance_name,
                    number=number,
                    contacts=contacts
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error enviando contacto: {str(e)}"}

        @mcp.tool(
            description="Enviar reacción a mensaje",
            tags={"message", "reaction"}
        )
        async def send_reaction(
            instance_name: str,
            message_key: Dict[str, Any],
            reaction: str
        ) -> Dict[str, Any]:
            """Enviar reacción a un mensaje"""
            try:
                self.client = MessageClient()
                result = await self.client.send_reaction(
                    instance_name=instance_name,
                    message_key=message_key,
                    reaction=reaction
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error enviando reacción: {str(e)}"}

        @mcp.tool(
            description="Enviar encuesta",
            tags={"message", "poll"}
        )
        async def send_poll(
            instance_name: str,
            number: str,
            name: str,
            options: List[str],
            selectable_count: int = 1
        ) -> Dict[str, Any]:
            """Enviar encuesta"""
            try:
                self.client = MessageClient()
                result = await self.client.send_poll(
                    instance_name=instance_name,
                    number=number,
                    name=name,
                    options=options,
                    selectable_count=selectable_count
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error enviando encuesta: {str(e)}"}

        @mcp.tool(
            description="Enviar sticker",
            tags={"message", "sticker"}
        )
        async def send_sticker(
            instance_name: str,
            number: str,
            sticker: str  # url o base64
        ) -> Dict[str, Any]:
            """Enviar sticker"""
            try:
                self.client = MessageClient()
                result = await self.client.send_sticker(
                    instance_name=instance_name,
                    number=number,
                    sticker=sticker
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error enviando sticker: {str(e)}"}

        @mcp.tool(
            description="Enviar estado/historia",
            tags={"message", "status"}
        )
        async def send_status(
            instance_name: str,
            type: str,  # text, image, video, audio
            content: str,  # texto o url
            caption: Optional[str] = None,
            backgroundColor: Optional[str] = None,
            font: Optional[int] = None,  # 1=SERIF, 2=NORICAN_REGULAR, 3=BRYNDAN_WRITE, 4=BEBASNEUE_REGULAR, 5=OSWALD_HEAVY
            allContacts: bool = False,
            statusJidList: Optional[List[str]] = None
        ) -> Dict[str, Any]:
            """Enviar estado/historia"""
            try:
                self.client = MessageClient()
                result = await self.client.send_status(
                    instance_name=instance_name,
                    type=type,
                    content=content,
                    caption=caption,
                    backgroundColor=backgroundColor,
                    font=font,
                    allContacts=allContacts,
                    statusJidList=statusJidList
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error enviando estado: {str(e)}"}

        @mcp.tool(
            description="Enviar mensaje con botones",
            tags={"message", "buttons"}
        )
        async def send_buttons(
            instance_name: str,
            number: str,
            title: str,
            description: str,
            buttons: List[ButtonModel],
            footer: Optional[str] = None,
            delay: Optional[int] = None,
            link_preview: Optional[bool] = None,
            mentions_everyone: Optional[bool] = None,
            mentioned: Optional[List[str]] = None,
            quoted: Optional[Dict[str, Any]] = None
        ) -> Dict[str, Any]:
            """Enviar mensaje con botones"""
            try:
                self.client = MessageClient()
                # Formatear los botones según la estructura requerida
                formatted_buttons = []
                for button in buttons:
                    formatted_button = {
                        "title": str(button.title),
                        "displayText": str(button.displayText),
                        "id": str(button.id)
                    }
                    formatted_buttons.append(formatted_button)

                result = await self.client.send_buttons(
                    instance_name=instance_name,
                    number=str(number),
                    title=str(title),
                    description=str(description),
                    buttons=formatted_buttons,
                    footer=str(footer) if footer is not None else None,
                    delay=delay,
                    link_preview=link_preview,
                    mentions_everyone=mentions_everyone,
                    mentioned=mentioned,
                    quoted=quoted
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error enviando mensaje con botones: {str(e)}"}

        @mcp.tool(
            description="Enviar mensaje con lista",
            tags={"message", "list"}
        )
        async def send_list(
            instance_name: str,
            number: str,
            title: str,
            description: str,
            button_text: str,
            values: List[ListSectionModel],
            footer_text: Optional[str] = None,
            delay: Optional[int] = None,
            link_preview: Optional[bool] = None,
            mentions_everyone: Optional[bool] = None,
            mentioned: Optional[List[str]] = None,
            quoted: Optional[Dict[str, Any]] = None
        ) -> Dict[str, Any]:
            """Enviar mensaje con lista"""
            try:
                self.client = MessageClient()
                result = await self.client.send_list(
                    instance_name=instance_name,
                    number=number,
                    title=title,
                    description=description,
                    button_text=button_text,
                    values=[section.dict() for section in values],
                    footer_text=footer_text,
                    delay=delay,
                    link_preview=link_preview,
                    mentions_everyone=mentions_everyone,
                    mentioned=mentioned,
                    quoted=quoted
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error enviando mensaje con lista: {str(e)}"} 