from typing import Dict, Any, List, Optional
from ..base import BaseIntegrationClient

class WebhookClient(BaseIntegrationClient):
    def __init__(self):
        super().__init__("webhook")

    async def set_webhook(
        self,
        instance_name: str,
        enabled: bool,
        url: str,
        events: List[str],
        headers: Optional[Dict[str, str]] = None,
        by_events: bool = False,
        base64: bool = False
    ) -> Dict[str, Any]:
        """
        Configura un webhook
        """
        return await self.set_integration(
            instance_name=instance_name,
            enabled=enabled,
            events=events,
            url=url,
            headers=headers or {},
            byEvents=by_events,
            base64=base64
        ) 