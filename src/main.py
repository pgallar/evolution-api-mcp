import logging
import sys
import os
import asyncio
from typing import Dict, Any
from fastmcp import FastMCP
from dotenv import load_dotenv

# Import routes
from evolution.instance.routes import InstanceRoutes
from evolution.message.routes import MessageRoutes
from evolution.chat.routes import ChatRoutes
from evolution.label.routes import LabelRoutes
from evolution.profile.routes import ProfileRoutes
from evolution.group.routes import GroupRoutes
from evolution.proxy.routes import ProxyRoutes
from evolution.settings.routes import SettingsRoutes
from evolution.integrations.webhook.routes import WebhookRoutes

def setup_logging() -> None:
    """Configurar logging para la aplicación"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout),
            logging.FileHandler('logs/evolution_api_mcp.log')
        ]
    )

def get_credentials() -> tuple:
    """Obtener credenciales desde variables de entorno"""
    load_dotenv()
    
    api_url = os.getenv('EVOLUTION_API_URL')
    api_key = os.getenv('EVOLUTION_API_KEY')
    
    if not api_url or not api_key:
        raise ValueError("EVOLUTION_API_URL y EVOLUTION_API_KEY environment variables are required")
    
    return api_url, api_key

def get_server_config() -> Dict[str, Any]:
    """Obtener configuración del servidor SSE desde variables de entorno"""
    host = os.getenv('MCP_HOST', '0.0.0.0')
    port = int(os.getenv('MCP_PORT', '8002'))  # Puerto por defecto para SSE
    
    return {
        'host': host,
        'port': port,
        'environment': os.getenv('ENVIRONMENT', 'development'),
        'log_level': os.getenv('LOG_LEVEL', 'INFO').lower()
    }

def create_mcp_server() -> FastMCP:
    """Crear y configurar el servidor MCP"""
    try:
        mcp = FastMCP("evolution-api")
        return mcp
    except Exception as e:
        logging.getLogger(__name__).critical(f"Failed to create MCP server: {str(e)}")
        raise

def register_routers(mcp: FastMCP) -> None:
    """Registrar todas las rutas y herramientas"""
    logger = logging.getLogger(__name__)
    routers = [
        InstanceRoutes(),
        MessageRoutes(),
        ChatRoutes(),
        LabelRoutes(),
        ProfileRoutes(),
        GroupRoutes(),
        ProxyRoutes(),
        SettingsRoutes(),
        WebhookRoutes()
    ]

    for router in routers:
        try:
            router.register_tools(mcp)
            logger.debug(f"Registered router: {router.__class__.__name__}")
        except Exception as e:
            logger.error(f"Failed to register router {router.__class__.__name__}: {str(e)}")
            raise

async def run_sse_server(mcp: FastMCP, host: str, port: int) -> None:
    """Ejecuta el servidor SSE"""
    logger = logging.getLogger(__name__)
    logger.info(f"Starting SSE server on {host}:{port}")
    
    # Agregar un delay para asegurar que el servidor esté completamente inicializado
    await asyncio.sleep(1)
    logger.info("Server initialization complete, ready to accept connections")
    
    await mcp.run_async(transport="sse", host=host, port=port)

def main() -> None:
    setup_logging()
    logger = logging.getLogger(__name__)
    
    try:
        logger.info("Initializing Evolution API MCP server with SSE...")
        
        # Obtener credenciales y configuración
        api_url, api_key = get_credentials()
        config = get_server_config()
        
        logger.info("Credentials loaded successfully")
        logger.info(f"SSE Server configuration: {config}")
        
        mcp = create_mcp_server()
        
        logger.info("Registering routers...")
        register_routers(mcp)
        logger.info("All routers registered successfully")
        
        # Ejecutar servidor SSE
        logger.info(f"Starting SSE server on port {config['port']}...")
        asyncio.run(run_sse_server(mcp, config['host'], config['port']))
            
    except Exception as e:
        logger.critical(f"Fatal error: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main() 