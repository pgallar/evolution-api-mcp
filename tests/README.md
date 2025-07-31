# Pruebas del Evolution API MCP Server

Este directorio contiene las pruebas automatizadas para el Evolution API MCP Server.

## Estructura

```
tests/
├── conftest.py          # Configuración y fixtures comunes de pytest
├── test_instance.py     # Pruebas del módulo de instancia
├── test_message.py      # Pruebas del módulo de mensajes
└── test_chat.py         # Pruebas del módulo de chat
```

## Ejecución de las Pruebas

Para ejecutar todas las pruebas:

```bash
pytest
```

Para ejecutar un módulo específico:

```bash
pytest tests/test_instance.py
pytest tests/test_message.py
pytest tests/test_chat.py
```

Para ejecutar una prueba específica:

```bash
pytest tests/test_instance.py::test_create_instance
```

## Fixtures

Los fixtures comunes están definidos en `conftest.py` y están disponibles automáticamente para todas las pruebas:

- `client`: Cliente de prueba de FastAPI
- `instance_name`: Nombre de instancia de prueba
- `test_number`: Número de teléfono de prueba
- `message_key`: Clave de mensaje de prueba
- `test_contact`: Datos de contacto de prueba
- `test_location`: Datos de ubicación de prueba
- `test_media`: Datos de medios de prueba
- `test_poll`: Datos de encuesta de prueba

## Cobertura de Pruebas

Para ejecutar las pruebas con cobertura:

```bash
pytest --cov=src tests/
```

Para generar un reporte HTML de cobertura:

```bash
pytest --cov=src --cov-report=html tests/
```

## Mocking

Para las pruebas que requieren mocking de la Evolution API, se utilizan los fixtures y funciones de `pytest-mock`. Ejemplo:

```python
def test_api_call(mocker):
    mock_response = mocker.patch('httpx.AsyncClient.request')
    mock_response.return_value.json.return_value = {"success": True}
    # ... resto de la prueba
```

## Añadir Nuevas Pruebas

1. Crear un nuevo archivo de prueba si es necesario
2. Usar los fixtures existentes cuando sea posible
3. Seguir el patrón de las pruebas existentes
4. Documentar cualquier nuevo fixture en este README 