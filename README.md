# Evolution API MCP Server

Este es un servidor MCP (Message Communication Protocol) para la Evolution API, que proporciona una interfaz para interactuar con WhatsApp a través de la Evolution API.

## Características

- Integración completa con Evolution API
- Soporte para SSE (Server-Sent Events)
- Gestión de instancias de WhatsApp
- Envío de mensajes de texto, multimedia, ubicación, contactos y más
- Gestión de grupos
- Configuración de proxy y ajustes
- Manejo de eventos y webhooks

## Requisitos

- Python 3.11 o superior
- Docker y Docker Compose (opcional)
- Evolution API Server

## Instalación

1. Clonar el repositorio:
   ```bash
   git clone <repository-url>
   cd evolution-api-mcp
   ```

2. Crear y activar un entorno virtual:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   # o
   .\venv\Scripts\activate  # Windows
   ```

3. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

4. Copiar el archivo de ejemplo de variables de entorno:
   ```bash
   cp .env.example .env
   ```

5. Editar el archivo `.env` con tus configuraciones.

## Uso con Docker

1. Construir la imagen:
   ```bash
   docker-compose build
   ```

2. Iniciar el servicio:
   ```bash
   docker-compose up -d
   ```

## Uso sin Docker

1. Asegurarse de que el entorno virtual está activado.

2. Iniciar el servidor:
   ```bash
   python src/main.py
   ```

## Endpoints Principales

### Instancias

- `POST /instance/create` - Crear una nueva instancia
- `GET /instance/fetch` - Obtener lista de instancias
- `GET /instance/connect/{instance_name}` - Conectar a una instancia
- `POST /instance/restart/{instance_name}` - Reiniciar una instancia
- `DELETE /instance/delete/{instance_name}` - Eliminar una instancia

### Mensajes

- `POST /message/{instance_name}/text` - Enviar mensaje de texto
- `POST /message/{instance_name}/media` - Enviar mensaje multimedia
- `POST /message/{instance_name}/audio` - Enviar mensaje de audio
- `POST /message/{instance_name}/location` - Enviar ubicación
- `POST /message/{instance_name}/contact` - Enviar contacto
- `POST /message/{instance_name}/poll` - Enviar encuesta

## Configuración

El servidor se puede configurar a través de variables de entorno:

- `ENVIRONMENT`: Entorno de ejecución (development/production)
- `LOG_LEVEL`: Nivel de logging (INFO/DEBUG/ERROR)
- `EVOLUTION_API_URL`: URL del servidor Evolution API
- `EVOLUTION_API_KEY`: Clave de API para Evolution API
- `MCP_HOST`: Host para el servidor MCP
- `MCP_PORT`: Puerto para el servidor MCP
- `ENABLE_API_LOGGING`: Habilitar/deshabilitar logging de API

## Contribuir

1. Fork el repositorio
2. Crear una rama para tu feature (`git checkout -b feature/amazing-feature`)
3. Commit tus cambios (`git commit -m 'Add some amazing feature'`)
4. Push a la rama (`git push origin feature/amazing-feature`)
5. Abrir un Pull Request

## Licencia

Este proyecto está licenciado bajo la Licencia MIT - ver el archivo [LICENSE](LICENSE) para más detalles. 