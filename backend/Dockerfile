FROM python:3.9-alpine

WORKDIR /app

# Dependencias necesarias para SQLite y compilación de paquetes Python
RUN apk add --no-cache gcc musl-dev libffi-dev sqlite-dev

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000
CMD ["python", "app.py"]


RUN touch inventario.db && chmod 666 inventario.db
