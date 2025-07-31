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
    echo "Copiando archivo .env.example a .env..."
    cp .env.example .env
    echo "Por favor, configura las variables en el archivo .env"
fi

# Iniciar el servidor
echo "Iniciando el servidor..."
python src/main.py 