# =========================
# Etapa 1: Compilar la app
# =========================
FROM maven:3.9.4-eclipse-temurin-21 AS build

# Creamos una carpeta de trabajo para tu proyecto
WORKDIR /app

# Copiamos pom.xml y descargamos dependencias (caché de Maven)
COPY pom.xml .
RUN mvn dependency:go-offline

# Copiamos el resto del código fuente
COPY ./src ./src

# Compilamos y construimos el WAR
RUN mvn package -DskipTests


# =========================
# Etapa 2: Tomcat standalone
# =========================
FROM tomcat:10-jdk21-temurin

# (Opcional) eliminar las aplicaciones por defecto de Tomcat
RUN rm -rf /usr/local/tomcat/webapps/*

# Copiamos el WAR al directorio webapps, renombrándolo a ROOT.war
# (para que se sirva directamente en http://host:8080/)
COPY --from=build /app/target/*.war /usr/local/tomcat/webapps/ROOT.war

EXPOSE 8080

# Iniciar Tomcat
CMD ["catalina.sh", "run"]
