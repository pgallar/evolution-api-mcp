from typing import Dict, Any
from ..http_client import EvolutionAPIClient

class LabelClient(EvolutionAPIClient):
    async def find_labels(
        self,
        instance_name: str
    ) -> Dict[str, Any]:
        """Find all labels"""
        return await self.get(f"label/findLabels/{instance_name}")

    async def handle_label(
        self,
        instance_name: str,
        number: str,
        labelId: str,
        action: str  # add, remove
    ) -> Dict[str, Any]:
        """Handle label operations"""
        data = {
            "number": number,
            "labelId": labelId,
            "action": action
        }
        return await self.post(f"label/handleLabel/{instance_name}", json=data) 