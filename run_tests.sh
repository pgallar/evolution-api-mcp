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

# Ejecutar las pruebas con cobertura
echo "Ejecutando pruebas con cobertura..."
pytest --cov=src tests/ --cov-report=term-missing

# Generar reporte HTML de cobertura
echo "Generando reporte HTML de cobertura..."
pytest --cov=src tests/ --cov-report=html

echo "Las pruebas han finalizado. El reporte de cobertura está disponible en htmlcov/index.html" 