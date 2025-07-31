from typing import Dict, Any, Optional
from ..http_client import EvolutionAPIClient

class ProxyClient(EvolutionAPIClient):
    async def set_proxy(
        self,
        instance_name: str,
        enabled: bool,
        host: str,
        port: str,
        protocol: str,
        username: Optional[str] = None,
        password: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Configura el proxy para una instancia
        """
        data = {
            "enabled": enabled,
            "host": host,
            "port": port,
            "protocol": protocol
        }
        if username:
            data["username"] = username
        if password:
            data["password"] = password

        return await self.post(f"/proxy/set/{instance_name}", json=data)

    async def find_proxy(self, instance_name: str) -> Dict[str, Any]:
        """
        Obtiene la configuración actual del proxy
        """
        return await self.get(f"/proxy/find/{instance_name}") 