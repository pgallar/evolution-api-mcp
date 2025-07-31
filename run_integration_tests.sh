#!/bin/bash

# Verificar si el entorno virtual existe
if [ ! -d "venv" ]; then
    echo "Creando entorno virtual..."
    python -m venv venv
fi

# Activar el entorno virtual
source venv/bin/activate

# Instalar dependencias si no están instaladas
if [ ! -f "requirements.txt" ]; then
    echo "Error: requirements.txt no encontrado"
    exit 1
fi

pip install -r requirements.txt

# Verificar si existe el archivo .env
if [ ! -f ".env" ]; then
    echo "Error: archivo .env no encontrado"
    echo "Por favor, crea el archivo .env con las variables necesarias"
    exit 1
fi

# Cargar variables de entorno
source .env

# Verificar variables requeridas
if [ -z "$EVOLUTION_API_URL" ] || [ -z "$EVOLUTION_API_KEY" ]; then
    echo "Error: EVOLUTION_API_URL y EVOLUTION_API_KEY son requeridas en el archivo .env"
    exit 1
fi

# Ejecutar las pruebas de integración
echo "Ejecutando pruebas de integración..."
pytest tests/integration/ -v

echo "Las pruebas de integración han finalizado." 