# Usar la imagen oficial de MySQL
FROM mysql:8.0

# Copiar el script de inicialización de la base de datos
COPY db/init.sql /docker-entrypoint-initdb.d/

# Establecer la contraseña del root y la base de datos que se debe crear
ENV MYSQL_ROOT_PASSWORD=example
ENV MYSQL_DATABASE=fintech
