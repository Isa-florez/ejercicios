# ejercicios
🧠 1. ¿Qué es PostgreSQL?

PostgreSQL es un gestor de bases de datos relacional.

Traducción humana:

Guarda información en tablas

Las tablas tienen filas (datos)

Y columnas (atributos)

Ejemplo mental:

Tabla usuarios:

id	nombre	correo
1	Ana	ana@gmail.com
🏗 2. Crear Base de Datos
CREATE DATABASE mi_prueba;

Conectarse:

\c mi_prueba;
🧱 3. Crear Tablas (lo más importante del examen)

Ejemplo completo según lo que te han pedido antes:

🔹 Tabla roles
CREATE TABLE roles (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL
);

🔎 Explicación:

SERIAL → autoincremental

PRIMARY KEY → clave primaria

NOT NULL → obligatorio

🔹 Tabla cortes
CREATE TABLE cortes (
    id SERIAL PRIMARY KEY,
    numero_corte INT UNIQUE NOT NULL
);

UNIQUE → no se puede repetir

🔹 Tabla usuarios
CREATE TABLE usuarios (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    correo VARCHAR(100) NOT NULL UNIQUE,
    contraseña TEXT NOT NULL,
    rol_id INT,
    FOREIGN KEY (rol_id) REFERENCES roles(id)
);

🔥 Aquí aparece algo clave del examen:
FOREIGN KEY = relación entre tablas.

🔑 4. Insertar datos
INSERT INTO roles (nombre)
VALUES ('admin');

Usuario admin:

INSERT INTO usuarios (nombre, correo, contraseña, rol_id)
VALUES ('Admin Principal', 'admin@gmail.com', '123456_encriptado', 1);
🔎 5. Consultas (SELECT)

Ver todo:

SELECT * FROM usuarios;

Buscar por correo:

SELECT * FROM usuarios
WHERE correo = 'admin@gmail.com';
🧹 6. Normalización (Excel → Base de datos)

Esto casi seguro sale.

Si en Excel tienes esto:

nombre	correo	rol
Ana	ana@gmail	admin

❌ MAL diseño
Porque el rol se repite muchas veces.

✔ Normalización correcta:

Tabla roles
Tabla usuarios con rol_id

Regla simple para mañana:

No repetir información

Separar entidades diferentes en tablas distintas

📥 7. Cargar Excel a PostgreSQL

Opciones:

En pgAdmin:

Click derecho tabla

Import/Export

Seleccionas CSV

O por SQL:

COPY usuarios(nombre, correo)
FROM '/ruta/archivo.csv'
DELIMITER ','
CSV HEADER;
⚙ 8. Procedimientos almacenados

Son funciones dentro de PostgreSQL.

Ejemplo:

CREATE OR REPLACE FUNCTION obtener_usuarios()
RETURNS TABLE(id INT, nombre VARCHAR)
AS $$
BEGIN
    RETURN QUERY SELECT id, nombre FROM usuarios;
END;
$$ LANGUAGE plpgsql;

Ejecutar:

SELECT * FROM obtener_usuarios();
🌐 9. Conexión con Express (Node.js)

Instalar:

npm install pg

Conexión básica:

const { Pool } = require('pg');

const pool = new Pool({
  user: 'postgres',
  host: 'localhost',
  database: 'mi_prueba',
  password: '1234',
  port: 5432,
});

module.exports = pool;

Consulta en una API:

app.get('/usuarios', async (req, res) => {
   const result = await pool.query('SELECT * FROM usuarios');
   res.json(result.rows);
});
📮 10. Postman y Thunder

Son herramientas para probar APIs.

GET → consultar

POST → insertar

PUT → actualizar

DELETE → eliminar

Si tu API está en:

http://localhost:3000/usuarios

En Postman haces:
GET → y te devuelve JSON.

📘 11. README.md

Debe explicar:

Qué hace el proyecto

Cómo instalarlo

Cómo correrlo

Ejemplo:

# Proyecto API Usuarios

## Instalación
npm install

## Ejecutar
npm start

## Endpoints
GET /usuarios
POST /usuarios
🚨 12. Cosas que seguro preguntan mañana

✔ Qué es PRIMARY KEY
✔ Qué es FOREIGN KEY
✔ Qué es UNIQUE
✔ Diferencia entre DELETE y DROP
✔ Cómo eliminar tabla

Eliminar tabla:

DROP TABLE usuarios;

Eliminar datos:

DELETE FROM usuarios;
🧩 Resumen Mental para el Examen

Leo Excel

Normalizo

Creo tablas

Agrego claves foráneas

Inserto datos

Hago consultas

Conecto Express

Documento

Ese es el flujo completo.
