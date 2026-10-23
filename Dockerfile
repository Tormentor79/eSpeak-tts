FROM python:3.10-slim

# Instalar dependencias del sistema (eSpeak NG)
RUN apt-get update && apt-get install -y \
    espeak-ng \
    && rm -rf /var/lib/apt/lists/*

# Configurar el directorio de trabajo
WORKDIR /app

# Copiar e instalar dependencias de Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código de la aplicación
COPY . .

# Comando para ejecutar la aplicación con Gunicorn
CMD gunicorn --bind 0.0.0.0:$PORT app:app
