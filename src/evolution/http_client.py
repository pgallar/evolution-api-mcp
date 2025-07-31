import os
from typing import Any, Dict, Optional
import httpx
from fastapi import HTTPException

class EvolutionAPIClient:
    def __init__(self):
        self.base_url = os.getenv("EVOLUTION_API_URL")
        self.api_key = os.getenv("EVOLUTION_API_KEY")
        
        if not self.base_url:
            raise ValueError("EVOLUTION_API_URL environment variable is not set")
            
        if not self.api_key:
            raise ValueError("EVOLUTION_API_KEY environment variable is not set")
            
        self.headers = {
            "apikey": self.api_key,
            "Content-Type": "application/json"
        }
        
    async def _make_request(
        self,
        method: str,
        endpoint: str,
        params: Optional[Dict[str, Any]] = None,
        json: Optional[Dict[str, Any]] = None
    ) -> Dict[str, Any]:
        url = f"{self.base_url.rstrip('/')}/{endpoint.lstrip('/')}"
        
        async with httpx.AsyncClient() as client:
            try:
                response = await client.request(
                    method=method,
                    url=url,
                    params=params,
                    json=json,
                    headers=self.headers
                )
                response.raise_for_status()
                return response.json()
            except httpx.HTTPError as e:
                raise HTTPException(
                    status_code=e.response.status_code if hasattr(e, 'response') else 500,
                    detail=str(e)
                )
            except Exception as e:
                raise HTTPException(status_code=500, detail=str(e))

    async def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        return await self._make_request("GET", endpoint, params=params)

    async def post(self, endpoint: str, json: Dict[str, Any]) -> Dict[str, Any]:
        return await self._make_request("POST", endpoint, json=json)

    async def put(self, endpoint: str, json: Dict[str, Any]) -> Dict[str, Any]:
        return await self._make_request("PUT", endpoint, json=json)

    async def delete(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        return await self._make_request("DELETE", endpoint, params=params) 