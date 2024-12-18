# Usa una imagen base de Python
FROM python:3.11-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos del proyecto al contenedor
COPY . /app

# Instala las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que Gunicorn servirá la API
EXPOSE 8000

# Configura Gunicorn como servidor
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "ProyectoApi.wsgi:application"]
