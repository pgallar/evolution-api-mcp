from typing import Dict, Any, Optional, List
from ..http_client import EvolutionAPIClient

class ChatClient(EvolutionAPIClient):
    async def check_whatsapp_numbers(
        self,
        instance_name: str,
        numbers: List[str]
    ) -> Dict[str, Any]:
        """Check if numbers are registered on WhatsApp"""
        data = {"numbers": numbers}
        return await self.post(f"chat/whatsappNumbers/{instance_name}", json=data)

    async def mark_message_as_read(
        self,
        instance_name: str,
        messages: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Mark messages as read"""
        data = {"readMessages": messages}
        return await self.post(f"chat/markMessageAsRead/{instance_name}", json=data)

    async def archive_chat(
        self,
        instance_name: str,
        chat: str,
        last_message: Dict[str, Any],
        archive: bool = True
    ) -> Dict[str, Any]:
        """Archive or unarchive a chat"""
        data = {
            "lastMessage": last_message,
            "chat": chat,
            "archive": archive
        }
        return await self.post(f"chat/archiveChat/{instance_name}", json=data)

    async def mark_chat_unread(
        self,
        instance_name: str,
        chat: str,
        last_message: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Mark a chat as unread"""
        data = {
            "lastMessage": last_message,
            "chat": chat
        }
        return await self.post(f"chat/markChatUnread/{instance_name}", json=data)

    async def delete_message(
        self,
        instance_name: str,
        message_id: str,
        remote_jid: str,
        from_me: bool,
        participant: Optional[str] = None
    ) -> Dict[str, Any]:
        """Delete a message for everyone"""
        data = {
            "id": message_id,
            "remoteJid": remote_jid,
            "fromMe": from_me,
            **({"participant": participant} if participant else {})
        }
        return await self.delete(f"chat/deleteMessageForEveryone/{instance_name}", params=data)

    async def fetch_profile_picture(
        self,
        instance_name: str,
        number: str
    ) -> Dict[str, Any]:
        """Fetch profile picture URL"""
        data = {"number": number}
        return await self.post(f"chat/fetchProfilePictureUrl/{instance_name}", json=data)

    async def get_base64_from_media(
        self,
        instance_name: str,
        message_id: str,
        convert_to_mp4: bool = False
    ) -> Dict[str, Any]:
        """Get base64 from media message"""
        data = {
            "message": {
                "key": {
                    "id": message_id
                }
            },
            "convertToMp4": convert_to_mp4
        }
        return await self.post(f"chat/getBase64FromMediaMessage/{instance_name}", json=data)

    async def update_message(
        self,
        instance_name: str,
        number: str,
        key: Dict[str, Any],
        text: str
    ) -> Dict[str, Any]:
        """Update a message"""
        data = {
            "number": number,
            "key": key,
            "text": text
        }
        return await self.post(f"chat/updateMessage/{instance_name}", json=data)

    async def send_presence(
        self,
        instance_name: str,
        number: str,
        presence: str,
        delay: Optional[int] = None
    ) -> Dict[str, Any]:
        """Send presence status"""
        data = {
            "number": number,
            "presence": presence,
            **({"delay": delay} if delay else {})
        }
        return await self.post(f"chat/sendPresence/{instance_name}", json=data)

    async def find_messages(
        self,
        instance_name: str,
        remote_jid: Optional[str] = None,
        page: Optional[int] = None,
        offset: Optional[int] = None
    ) -> Dict[str, Any]:
        """Find messages"""
        data = {
            "where": {
                "key": {
                    **({"remoteJid": remote_jid} if remote_jid else {})
                }
            },
            **({"page": page} if page else {}),
            **({"offset": offset} if offset else {})
        }
        return await self.post(f"chat/findMessages/{instance_name}", json=data)

    async def find_chats(
        self,
        instance_name: str
    ) -> Dict[str, Any]:
        """Find all chats"""
        return await self.post(f"chat/findChats/{instance_name}", json={}) 

    async def update_block_status(
        self,
        instance_name: str,
        number: str,
        status: str  # block, unblock
    ) -> Dict[str, Any]:
        """Update block status for a number"""
        data = {
            "number": number,
            "status": status
        }
        return await self.post(f"message/updateBlockStatus/{instance_name}", json=data)

    async def find_contacts(
        self,
        instance_name: str,
        where: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        """Find contacts"""
        data = {"where": where} if where else {}
        return await self.post(f"chat/findContacts/{instance_name}", json=data)

    async def find_status_message(
        self,
        instance_name: str,
        where: Optional[Dict[str, Any]] = None,
        page: Optional[int] = None,
        offset: Optional[int] = None
    ) -> Dict[str, Any]:
        """Find status messages"""
        data = {
            **({"where": where} if where else {}),
            **({"page": page} if page else {}),
            **({"offset": offset} if offset else {})
        }
        return await self.post(f"chat/findStatusMessage/{instance_name}", json=data) 