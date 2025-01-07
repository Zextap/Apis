FROM httpd:2.4

# Copiamos proxy.conf
COPY proxy.conf /usr/local/apache2/conf/extra/proxy.conf

# Descomentamos módulos en httpd.conf (si hiciera falta)
RUN sed -i 's/#LoadModule proxy_module/LoadModule proxy_module/' /usr/local/apache2/conf/httpd.conf && \
    sed -i 's/#LoadModule proxy_http_module/LoadModule proxy_http_module/' /usr/local/apache2/conf/httpd.conf

# Incluimos proxy.conf
RUN echo "Include /usr/local/apache2/conf/extra/proxy.conf" \
    >> /usr/local/apache2/conf/httpd.conf

EXPOSE 80
CMD ["httpd-foreground"]
