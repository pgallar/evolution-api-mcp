from typing import Dict, Any, Optional, List
from ..http_client import EvolutionAPIClient

class MessageClient(EvolutionAPIClient):
    async def send_text(
        self,
        instance_name: str,
        number: str,
        text: str,
        quoted: Optional[Dict[str, Any]] = None,
        delay: Optional[int] = None,
        mentions: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """Send a text message"""
        data = {
            "number": number,
            "text": text,
            **({"quoted": quoted} if quoted else {}),
            **({"delay": delay} if delay else {}),
            **({"mentioned": mentions} if mentions else {})
        }
        return await self.post(f"message/sendText/{instance_name}", json=data)

    async def send_media(
        self,
        instance_name: str,
        number: str,
        media_type: str,
        media: str,
        caption: Optional[str] = None,
        filename: Optional[str] = None,
        mimetype: Optional[str] = None
    ) -> Dict[str, Any]:
        """Send a media message (image, video, document)"""
        data = {
            "number": number,
            "mediatype": media_type,
            "media": media,
            **({"caption": caption} if caption else {}),
            **({"fileName": filename} if filename else {}),
            **({"mimetype": mimetype} if mimetype else {})
        }
        return await self.post(f"message/sendMedia/{instance_name}", json=data)

    async def send_audio(
        self,
        instance_name: str,
        number: str,
        audio: str
    ) -> Dict[str, Any]:
        """Send an audio message"""
        data = {
            "number": number,
            "audio": audio
        }
        return await self.post(f"message/sendWhatsAppAudio/{instance_name}", json=data)

    async def send_location(
        self,
        instance_name: str,
        number: str,
        latitude: float,
        longitude: float,
        name: Optional[str] = None,
        address: Optional[str] = None
    ) -> Dict[str, Any]:
        """Send a location message"""
        data = {
            "number": number,
            "latitude": latitude,
            "longitude": longitude,
            **({"name": name} if name else {}),
            **({"address": address} if address else {})
        }
        return await self.post(f"message/sendLocation/{instance_name}", json=data)

    async def send_contact(
        self,
        instance_name: str,
        number: str,
        contacts: List[Dict[str, str]]
    ) -> Dict[str, Any]:
        """Send contact information"""
        data = {
            "number": number,
            "contact": contacts
        }
        return await self.post(f"message/sendContact/{instance_name}", json=data)

    async def send_reaction(
        self,
        instance_name: str,
        message_key: Dict[str, Any],
        reaction: str
    ) -> Dict[str, Any]:
        """Send a reaction to a message"""
        data = {
            "key": message_key,
            "reaction": reaction
        }
        return await self.post(f"message/sendReaction/{instance_name}", json=data)

    async def send_poll(
        self,
        instance_name: str,
        number: str,
        name: str,
        options: List[str],
        selectable_count: int = 1
    ) -> Dict[str, Any]:
        """Send a poll message"""
        data = {
            "number": number,
            "name": name,
            "values": options,
            "selectableCount": selectable_count
        }
        return await self.post(f"message/sendPoll/{instance_name}", json=data)

    async def send_sticker(
        self,
        instance_name: str,
        number: str,
        sticker: str
    ) -> Dict[str, Any]:
        """Send a sticker message"""
        data = {
            "number": number,
            "sticker": sticker
        }
        return await self.post(f"message/sendSticker/{instance_name}", json=data)

    async def send_status(
        self,
        instance_name: str,
        type: str,
        content: str,
        caption: Optional[str] = None,
        backgroundColor: Optional[str] = None,
        font: Optional[int] = None,
        allContacts: bool = False,
        statusJidList: Optional[List[str]] = None
    ) -> Dict[str, Any]:
        """Send a status/story message"""
        data = {
            "type": type,
            "content": content,
            **({"caption": caption} if caption else {}),
            **({"backgroundColor": backgroundColor} if backgroundColor else {}),
            **({"font": font} if font else {}),
            "allContacts": allContacts,
            **({"statusJidList": statusJidList} if statusJidList else [])
        }
        return await self.post(f"message/sendStatus/{instance_name}", json=data)

    async def send_buttons(
        self,
        instance_name: str,
        number: str,
        title: str,
        description: str,
        footer: Optional[str] = None,
        buttons: Optional[List[Dict[str, Any]]] = None,
        delay: Optional[int] = None,
        link_preview: Optional[bool] = None,
        mentions_everyone: Optional[bool] = None,
        mentioned: Optional[List[str]] = None,
        quoted: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Enviar mensaje con botones"""
        # Asegurarnos de que cada botón tenga la estructura correcta
        formatted_buttons = []
        if buttons:
            for button in buttons:
                formatted_button = {
                    "title": str(button.get("title", "")),
                    "displayText": str(button.get("displayText", "")),
                    "id": str(button.get("id", ""))
                }
                formatted_buttons.append(formatted_button)

        data = {
            "number": str(number),
            "title": str(title),
            "description": str(description),
            "buttons": formatted_buttons
        }
        
        if footer is not None:
            data["footer"] = str(footer)
        if delay is not None:
            data["delay"] = delay  # Mantener como int
        if link_preview is not None:
            data["linkPreview"] = link_preview  # Mantener como bool
        if mentions_everyone is not None:
            data["mentionsEveryOne"] = mentions_everyone  # Mantener como bool
        if mentioned is not None:
            data["mentioned"] = [str(m) for m in mentioned]  # Convertir cada mención a string
        if quoted is not None:
            data["quoted"] = quoted  # Mantener la estructura original

        return await self.post(f"/message/sendButtons/{instance_name}", json=data)

    async def send_list(
        self,
        instance_name: str,
        number: str,
        title: str,
        description: str,
        button_text: str,
        footer_text: Optional[str] = None,
        values: Optional[List[Dict[str, Any]]] = None,
        delay: Optional[int] = None,
        link_preview: Optional[bool] = None,
        mentions_everyone: Optional[bool] = None,
        mentioned: Optional[List[str]] = None,
        quoted: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Enviar mensaje con lista"""
        data = {
            "number": number,
            "title": title,
            "description": description,
            "buttonText": button_text
        }

        if footer_text is not None:
            data["footerText"] = footer_text
        if values is not None:
            data["values"] = values
        if delay is not None:
            data["delay"] = delay
        if link_preview is not None:
            data["linkPreview"] = link_preview
        if mentions_everyone is not None:
            data["mentionsEveryOne"] = mentions_everyone
        if mentioned is not None:
            data["mentioned"] = mentioned
        if quoted is not None:
            data["quoted"] = quoted

        return await self.post(f"/message/sendList/{instance_name}", json=data) 