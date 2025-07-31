from typing import Dict, Any, Optional
from ..http_client import EvolutionAPIClient

class SettingsClient(EvolutionAPIClient):
    async def set_settings(
        self,
        instance_name: str,
        reject_call: bool = False,
        msg_call: Optional[str] = None,
        groups_ignore: bool = False,
        always_online: bool = False,
        read_messages: bool = False,
        read_status: bool = False,
        sync_full_history: bool = False
    ) -> Dict[str, Any]:
        """
        Configura los ajustes de una instancia
        """
        data = {
            "rejectCall": reject_call,
            "groupsIgnore": groups_ignore,
            "alwaysOnline": always_online,
            "readMessages": read_messages,
            "readStatus": read_status,
            "syncFullHistory": sync_full_history
        }
        if msg_call:
            data["msgCall"] = msg_call

        return await self.post(f"/settings/set/{instance_name}", json=data)

    async def find_settings(self, instance_name: str) -> Dict[str, Any]:
        """
        Obtiene la configuración actual de la instancia
        """
        return await self.get(f"/settings/find/{instance_name}") 