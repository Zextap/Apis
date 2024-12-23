# Dockerfile para Apache Proxy
FROM httpd:latest

# Copiar configuración personalizada
COPY ./proxy.conf /usr/local/apache2/conf/httpd.conf

# Habilitar los módulos necesarios para proxy y permisos
RUN echo "LoadModule proxy_module modules/mod_proxy.so" >> /usr/local/apache2/conf/httpd.conf && \
    echo "LoadModule proxy_http_module modules/mod_proxy_http.so" >> /usr/local/apache2/conf/httpd.conf && \
    echo "LoadModule authz_core_module modules/mod_authz_core.so" >> /usr/local/apache2/conf/httpd.conf

# Exponer el puerto del servidor Apache
EXPOSE 80
