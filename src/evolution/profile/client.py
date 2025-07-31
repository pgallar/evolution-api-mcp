from typing import Dict, Any
from ..http_client import EvolutionAPIClient

class ProfileClient(EvolutionAPIClient):
    async def fetch_business_profile(
        self,
        instance_name: str,
        number: str
    ) -> Dict[str, Any]:
        """Fetch business profile"""
        data = {"number": number}
        return await self.post(f"chat/fetchBusinessProfile/{instance_name}", json=data)

    async def fetch_profile(
        self,
        instance_name: str,
        number: str
    ) -> Dict[str, Any]:
        """Fetch profile"""
        data = {"number": number}
        return await self.post(f"chat/fetchProfile/{instance_name}", json=data)

    async def update_profile_name(
        self,
        instance_name: str,
        name: str
    ) -> Dict[str, Any]:
        """Update profile name"""
        data = {"name": name}
        return await self.post(f"chat/updateProfileName/{instance_name}", json=data)

    async def update_profile_status(
        self,
        instance_name: str,
        status: str
    ) -> Dict[str, Any]:
        """Update profile status"""
        data = {"status": status}
        return await self.post(f"chat/updateProfileStatus/{instance_name}", json=data)

    async def update_profile_picture(
        self,
        instance_name: str,
        picture: str
    ) -> Dict[str, Any]:
        """Update profile picture"""
        data = {"picture": picture}
        return await self.post(f"chat/updateProfilePicture/{instance_name}", json=data)

    async def remove_profile_picture(
        self,
        instance_name: str
    ) -> Dict[str, Any]:
        """Remove profile picture"""
        return await self.delete(f"chat/removeProfilePicture/{instance_name}")

    async def fetch_privacy_settings(
        self,
        instance_name: str
    ) -> Dict[str, Any]:
        """Fetch privacy settings"""
        return await self.get(f"chat/fetchPrivacySettings/{instance_name}")

    async def update_privacy_settings(
        self,
        instance_name: str,
        readreceipts: str,  # all, none
        profile: str,  # all, contacts, contact_blacklist, none
        status: str,  # all, contacts, contact_blacklist, none
        online: str,  # all, match_last_seen
        last: str,  # all, contacts, contact_blacklist, none
        groupadd: str  # all, contacts, contact_blacklist
    ) -> Dict[str, Any]:
        """Update privacy settings"""
        data = {
            "readreceipts": readreceipts,
            "profile": profile,
            "status": status,
            "online": online,
            "last": last,
            "groupadd": groupadd
        }
        return await self.post(f"chat/updatePrivacySettings/{instance_name}", json=data) 