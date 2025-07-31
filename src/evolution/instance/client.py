from typing import Dict, Any, Optional
from ..http_client import EvolutionAPIClient

class InstanceClient(EvolutionAPIClient):
    async def create_instance(self, instance_name: str, **kwargs) -> Dict[str, Any]:
        """Create a new WhatsApp instance"""
        data = {
            "instanceName": instance_name,
            "qrcode": True,
            "integration": "WHATSAPP-BAILEYS",
            **kwargs
        }
        return await self.post("instance/create", json=data)

    async def fetch_instances(self, instance_name: Optional[str] = None) -> Dict[str, Any]:
        """Fetch all instances or a specific instance"""
        params = {"instanceName": instance_name} if instance_name else None
        return await self.get("instance/fetchInstances", params=params)

    async def connect_instance(self, instance_name: str) -> Dict[str, Any]:
        """Connect to a WhatsApp instance"""
        return await self.get(f"instance/connect/{instance_name}")

    async def restart_instance(self, instance_name: str) -> Dict[str, Any]:
        """Restart a WhatsApp instance"""
        return await self.post(f"instance/restart/{instance_name}", json={})

    async def set_presence(self, instance_name: str, presence: str) -> Dict[str, Any]:
        """Set presence status (available/unavailable)"""
        return await self.post(f"instance/setPresence/{instance_name}", json={"presence": presence})

    async def get_connection_state(self, instance_name: str) -> Dict[str, Any]:
        """Get connection state of an instance"""
        return await self.get(f"instance/connectionState/{instance_name}")

    async def logout_instance(self, instance_name: str) -> Dict[str, Any]:
        """Logout from a WhatsApp instance"""
        return await self.delete(f"instance/logout/{instance_name}")

    async def delete_instance(self, instance_name: str) -> Dict[str, Any]:
        """Delete a WhatsApp instance"""
        return await self.delete(f"instance/delete/{instance_name}") 