from typing import Dict, Any, Optional, List
from ..http_client import EvolutionAPIClient

class GroupClient(EvolutionAPIClient):
    async def create_group(
        self,
        instance_name: str,
        subject: str,
        description: Optional[str] = None,
        participants: List[str] = []
    ) -> Dict[str, Any]:
        """Create a new group"""
        data = {
            "subject": subject,
            **({"description": description} if description else {}),
            "participants": participants
        }
        return await self.post(f"group/create/{instance_name}", json=data)

    async def update_group_picture(
        self,
        instance_name: str,
        groupJid: str,
        image: str
    ) -> Dict[str, Any]:
        """Update group picture"""
        data = {"image": image}
        return await self.post(f"group/updateGroupPicture/{instance_name}", json=data, params={"groupJid": groupJid})

    async def update_group_subject(
        self,
        instance_name: str,
        groupJid: str,
        subject: str
    ) -> Dict[str, Any]:
        """Update group subject"""
        data = {"subject": subject}
        return await self.post(f"group/updateGroupSubject/{instance_name}", json=data, params={"groupJid": groupJid})

    async def update_group_description(
        self,
        instance_name: str,
        groupJid: str,
        description: str
    ) -> Dict[str, Any]:
        """Update group description"""
        data = {"description": description}
        return await self.post(f"group/updateGroupDescription/{instance_name}", json=data, params={"groupJid": groupJid})

    async def fetch_invite_code(
        self,
        instance_name: str,
        groupJid: str
    ) -> Dict[str, Any]:
        """Fetch group invite code"""
        return await self.get(f"group/inviteCode/{instance_name}", params={"groupJid": groupJid})

    async def revoke_invite_code(
        self,
        instance_name: str,
        groupJid: str
    ) -> Dict[str, Any]:
        """Revoke group invite code"""
        return await self.post(f"group/revokeInviteCode/{instance_name}", json={}, params={"groupJid": groupJid})

    async def send_invite(
        self,
        instance_name: str,
        groupJid: str,
        description: str,
        numbers: List[str]
    ) -> Dict[str, Any]:
        """Send group invite URL"""
        data = {
            "groupJid": groupJid,
            "description": description,
            "numbers": numbers
        }
        return await self.post(f"group/sendInvite/{instance_name}", json=data)

    async def find_group_by_invite(
        self,
        instance_name: str,
        inviteCode: str
    ) -> Dict[str, Any]:
        """Find group by invite code"""
        return await self.get(f"group/inviteInfo/{instance_name}", params={"inviteCode": inviteCode})

    async def find_group_info(
        self,
        instance_name: str,
        groupJid: str
    ) -> Dict[str, Any]:
        """Find group by Jid"""
        return await self.get(f"group/findGroupInfos/{instance_name}", params={"groupJid": groupJid})

    async def fetch_all_groups(
        self,
        instance_name: str,
        getParticipants: bool = False
    ) -> Dict[str, Any]:
        """Fetch all groups"""
        return await self.get(f"group/fetchAllGroups/{instance_name}", params={"getParticipants": getParticipants})

    async def get_participants(
        self,
        instance_name: str,
        groupJid: str
    ) -> Dict[str, Any]:
        """Get group participants"""
        return await self.get(f"group/participants/{instance_name}", params={"groupJid": groupJid})

    async def update_participant(
        self,
        instance_name: str,
        groupJid: str,
        action: str,  # add, remove, promote, demote
        participants: List[str]
    ) -> Dict[str, Any]:
        """Update group participant"""
        data = {
            "action": action,
            "participants": participants
        }
        return await self.post(f"group/updateParticipant/{instance_name}", json=data, params={"groupJid": groupJid})

    async def update_setting(
        self,
        instance_name: str,
        groupJid: str,
        action: str  # announcement, not_announcement, locked, unlocked
    ) -> Dict[str, Any]:
        """Update group setting"""
        data = {"action": action}
        return await self.post(f"group/updateSetting/{instance_name}", json=data, params={"groupJid": groupJid})

    async def toggle_ephemeral(
        self,
        instance_name: str,
        groupJid: str,
        expiration: int  # 0, 86400, 604800, 7776000
    ) -> Dict[str, Any]:
        """Toggle ephemeral messages"""
        data = {"expiration": expiration}
        return await self.post(f"group/toggleEphemeral/{instance_name}", json=data, params={"groupJid": groupJid})

    async def leave_group(
        self,
        instance_name: str,
        groupJid: str
    ) -> Dict[str, Any]:
        """Leave group"""
        return await self.delete(f"group/leaveGroup/{instance_name}", params={"groupJid": groupJid}) 