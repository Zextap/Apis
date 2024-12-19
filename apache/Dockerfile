# Usar la imagen oficial de Apache
FROM httpd:alpine

# Instalar utilidades y asegurarse de que el módulo de logs está disponible
RUN apk add --no-cache apache2-utils
# Crear directorios de logs si no existen
RUN mkdir -p /usr/local/apache2/logs && chmod -R 755 /usr/local/apache2/logs

# Habilitar los módulos necesarios, incluyendo log_config
RUN echo "LoadModule mpm_prefork_module modules/mod_mpm_prefork.so" >> /usr/local/apache2/conf/httpd.conf && \
    echo "LoadModule proxy_module modules/mod_proxy.so" >> /usr/local/apache2/conf/httpd.conf && \
    echo "LoadModule proxy_http_module modules/mod_proxy_http.so" >> /usr/local/apache2/conf/httpd.conf && \
    echo "LoadModule rewrite_module modules/mod_rewrite.so" >> /usr/local/apache2/conf/httpd.conf && \
    echo "LoadModule headers_module modules/mod_headers.so" >> /usr/local/apache2/conf/httpd.conf && \
    echo "LoadModule log_config_module modules/mod_log_config.so" >> /usr/local/apache2/conf/httpd.conf

# Copiar el archivo de configuración personalizada
COPY ./proxy.conf /usr/local/apache2/conf/httpd.conf

# Exponer el puerto 80 (HTTP)

# Ejecutar Apache en primer plano
CMD ["httpd-foreground"]
