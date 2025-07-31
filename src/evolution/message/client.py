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