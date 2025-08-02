from typing import Dict, Any, Optional, List
from pydantic import BaseModel, Field, validator
from ..base_routes import BaseRoutes
from .client import MessageClient

class ButtonModel(BaseModel):
    type: str = Field(description="Tipo de botón (reply, url, call, copy, pix)")
    reply: Optional[Dict[str, str]] = Field(default=None, description="Datos del botón de respuesta")
    url: Optional[str] = Field(default=None, description="URL para botón de enlace")
    phoneNumber: Optional[str] = Field(default=None, description="Número de teléfono para botón de llamada")
    copyCode: Optional[str] = Field(default=None, description="Código para botón de copiar")
    displayText: Optional[str] = Field(default=None, description="Texto a mostrar en el botón")
    id: Optional[str] = Field(default=None, description="Identificador único del botón")
    currency: Optional[str] = Field(default=None, description="Moneda para botón PIX")
    name: Optional[str] = Field(default=None, description="Nombre para botón PIX")
    keyType: Optional[str] = Field(default=None, description="Tipo de clave PIX (phone, email, cpf, cnpj, random)")
    key: Optional[str] = Field(default=None, description="Clave PIX")

    class Config:
        json_schema_extra = {
            "example": {
                "type": "reply",
                "reply": {"id": "btn_1", "title": "Sí"},
                "displayText": "Sí"
            }
        }
        extra = "ignore"  # Ignora campos adicionales
        validate_assignment = True
        
    @validator('*', pre=True)
    def empty_str_to_none(cls, v):
        if v == "":
            return None
        return v

class PTVModel(BaseModel):
    number: str = Field(description="Número de destino")
    video: str = Field(description="URL o base64 del video")
    delay: Optional[int] = Field(default=None, description="Retraso en milisegundos")
    quoted: Optional[Dict[str, Any]] = Field(default=None, description="Mensaje citado")
    mentions_everyone: Optional[bool] = Field(default=None, description="Mencionar a todos")
    mentioned: Optional[List[str]] = Field(default=None, description="Lista de números mencionados")

    class Config:
        extra = "ignore"
        validate_assignment = True

    @validator('*', pre=True)
    def empty_str_to_none(cls, v):
        if v == "":
            return None
        return v

class ListRowModel(BaseModel):
    title: str = Field(description="Título de la fila")
    description: str = Field(description="Descripción de la fila")
    rowId: str = Field(description="Identificador único de la fila")

    class Config:
        extra = "ignore"
        validate_assignment = True

    @validator('*', pre=True)
    def empty_str_to_none(cls, v):
        if v == "":
            return None
        return v

class ListSectionModel(BaseModel):
    title: str = Field(description="Título de la sección")
    rows: List[ListRowModel] = Field(description="Filas de la sección")

    class Config:
        extra = "ignore"
        validate_assignment = True

    @validator('*', pre=True)
    def empty_str_to_none(cls, v):
        if v == "":
            return None
        return v

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
            description="Enviar video PTV",
            tags={"message", "ptv"}
        )
        async def send_ptv(
            instance_name: str,
            number: str,
            video: str,
            delay: Optional[int] = None,
            quoted: Optional[Dict[str, Any]] = None,
            mentions_everyone: Optional[bool] = None,
            mentioned: Optional[List[str]] = None
        ) -> Dict[str, Any]:
            """Enviar video PTV (Play Through Video)"""
            try:
                self.client = MessageClient()
                result = await self.client.send_ptv(
                    instance_name=instance_name,
                    number=number,
                    video=video,
                    delay=delay,
                    quoted=quoted,
                    mentions_everyone=mentions_everyone,
                    mentioned=mentioned
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error enviando video PTV: {str(e)}"}

        @mcp.tool(
            description="Enviar mensaje con botones",
            tags={"message", "buttons"}
        )
        async def send_buttons(
            instance_name: str,
            number: str,
            title: str,
            description: str,
            buttons: List[Dict[str, Any]],
            footer: Optional[str] = None,
            delay: Optional[int] = None,
            link_preview: Optional[bool] = None,
            mentions_everyone: Optional[bool] = None,
            mentioned: Optional[List[str]] = None,
            quoted: Optional[Dict[str, Any]] = None
        ) -> Dict[str, Any]:
            """Enviar mensaje con botones"""
            try:
                # Validar y convertir los botones usando el modelo
                validated_buttons = []
                for i, button_data in enumerate(buttons):
                    # Convertir formato antiguo al nuevo si es necesario
                    if "displayText" in button_data:
                        button_data = {
                            "type": "reply",
                            "reply": {
                                "id": button_data.get("buttonId", f"btn_{i + 1}"),
                                "title": button_data["displayText"]
                            }
                        }
                    elif "buttonText" in button_data:
                        button_data = {
                            "type": "reply",
                            "reply": {
                                "id": button_data["buttonId"],
                                "title": button_data["buttonText"]["displayText"]
                            }
                        }
                    
                    button = ButtonModel(**button_data)
                    validated_buttons.append(button)

                self.client = MessageClient()
                # Formatear los botones según la estructura requerida por la API
                formatted_buttons = []
                for button in validated_buttons:
                    if button.type == "reply":
                        formatted_button = {
                            "type": "reply",
                            "reply": {
                                "id": button.reply["id"],
                                "title": button.reply["title"]
                            }
                        }
                    elif button.type == "url":
                        formatted_button = {
                            "type": "url",
                            "displayText": button.displayText,
                            "url": button.url
                        }
                    elif button.type == "call":
                        formatted_button = {
                            "type": "call",
                            "displayText": button.displayText,
                            "phoneNumber": button.phoneNumber
                        }
                    elif button.type == "copy":
                        formatted_button = {
                            "type": "copy",
                            "displayText": button.displayText,
                            "copyCode": button.copyCode
                        }
                    elif button.type == "pix":
                        formatted_button = {
                            "type": "pix",
                            "currency": button.currency,
                            "name": button.name,
                            "keyType": button.keyType,
                            "key": button.key
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

        @mcp.tool(
            description="Enviar archivo multimedia",
            tags={"message", "media"}
        )
        async def send_media_file(
            instance_name: str,
            number: str,
            file: bytes,
            filename: str,
            caption: Optional[str] = None,
            delay: Optional[int] = None,
            quoted: Optional[Dict[str, Any]] = None,
            mentions_everyone: Optional[bool] = None,
            mentioned: Optional[List[str]] = None
        ) -> Dict[str, Any]:
            """Enviar archivo multimedia"""
            try:
                self.client = MessageClient()
                result = await self.client.send_media_file(
                    instance_name=instance_name,
                    number=number,
                    file=file,
                    filename=filename,
                    caption=caption,
                    delay=delay,
                    quoted=quoted,
                    mentions_everyone=mentions_everyone,
                    mentioned=mentioned
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error enviando archivo multimedia: {str(e)}"}

        @mcp.tool(
            description="Enviar archivo PTV",
            tags={"message", "ptv"}
        )
        async def send_ptv_file(
            instance_name: str,
            number: str,
            file: bytes,
            delay: Optional[int] = None,
            quoted: Optional[Dict[str, Any]] = None,
            mentions_everyone: Optional[bool] = None,
            mentioned: Optional[List[str]] = None
        ) -> Dict[str, Any]:
            """Enviar archivo PTV (Play Through Video)"""
            try:
                self.client = MessageClient()
                result = await self.client.send_ptv_file(
                    instance_name=instance_name,
                    number=number,
                    file=file,
                    delay=delay,
                    quoted=quoted,
                    mentions_everyone=mentions_everyone,
                    mentioned=mentioned
                )
                return {
                    "success": True,
                    "result": result
                }
            except Exception as e:
                return {"error": f"Error enviando archivo PTV: {str(e)}"} 