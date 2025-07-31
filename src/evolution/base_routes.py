from typing import Dict, Any, Optional
from .http_client import EvolutionAPIClient

class BaseRoutes:
    def __init__(self):
        self.client = None
        
    def register_tools(self, mcp):
        """Método que debe ser implementado por las clases hijas para registrar herramientas FastMCP"""
        raise NotImplementedError("Las clases hijas deben implementar register_tools")
        
    def get_auth_headers(self) -> Dict[str, str]:
        """Obtener headers de autenticación"""
        return {
            "apikey": self.client.api_key,
            "Content-Type": "application/json"
        } 