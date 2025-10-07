CREATE DATABASE IF NOT EXISTS master_python;
USE master_python;

CREATE TABLE usuarios (
    id INT(25) AUTO_INCREMENT not null,
    nombre VARCHAR(100),
    apellido VARCHAR(255),
    email VARCHAR(255) not null,
    password VARCHAR(255) not null,
    fecha DATE not null,
    CONSTRAINT pk_usuarios PRIMARY KEY(id),
    CONSTRAINT uq_email UNIQUE(email)
) ENGINE=InnoDb;

CREATE TABLE notas(
    id INT(25) AUTO_INCREMENT not null,
    usuario_id INT(25) not null,
    titulo VARCHAR(255) not null,
    descripcion MEDIUMTEXT,
    fecha DATE not null,
    CONSTRAINT pk_notas PRIMARY KEY(id),
    CONSTRAINT fk_nota_usuario FOREIGN KEY(usuario_id) REFERENCES usuarios(id)
)ENGINE=InnoDb;