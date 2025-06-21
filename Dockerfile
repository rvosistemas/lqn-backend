FROM python:3.11-slim

# Establecer directorio de trabajo
WORKDIR /app

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y gcc libpq-dev && apt-get clean

# Copiar requirements e instalarlos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código (cuando no uses volumen)
COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
