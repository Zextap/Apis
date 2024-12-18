# Dockerfile para Apache
FROM httpd
RUN mkdir -p /var/log/apache2

# Copiar configuración personalizada
COPY proxy.conf /usr/local/apache2/conf/proxy.conf

# Habilitar los módulos proxy y proxy_http
RUN echo "LoadModule proxy_module modules/mod_proxy.so" >> /usr/local/apache2/conf/httpd.conf
RUN echo "LoadModule proxy_http_module modules/mod_proxy_http.so" >> /usr/local/apache2/conf/httpd.conf

# Incluir la configuración personalizada en el archivo principal de Apache
RUN echo "Include /usr/local/apache2/conf/proxy.conf" >> /usr/local/apache2/conf/httpd.conf

# Exponer el puerto 80
EXPOSE 80

# Comando de inicio
CMD ["httpd-foreground"]