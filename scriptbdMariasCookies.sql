CREATE SCHEMA IF NOT EXISTS mcdb;
USE mcdb;
DROP TABLE IF EXISTS cuenta;
DROP TABLE IF EXISTS cliente;
CREATE TABLE cliente (
    cliente_id int NOT NULL UNIQUE,
    cliente_nombre varchar(30) NOT NULL,
    cliente_apellidop varchar(30) NOT NULL,
    cliente_apellidom varchar(30),
    cliente_telefono varchar(10),
    cliente_correo varchar(50),
    PRIMARY KEY (cliente_id)
);
CREATE TABLE cuenta (
    cliente_id int NOT NULL UNIQUE,
    cuenta_usuario varchar(25) NOT NULL UNIQUE,
    cuenta_contrasenia varchar(25) NOT NULL,
    cuenta_administrador bit NOT NULL,
    FOREIGN KEY (cliente_id) REFERENCES cliente(cliente_id)
);

DROP USER IF EXISTS 'mcdbCliente'@'localhost';
CREATE USER 'mcdbCliente'@'localhost' IDENTIFIED BY 'mariasCookies2023/';
REVOKE ALL PRIVILEGES ON *.* FROM 'mcdbCliente'@'localhost';

DROP USER IF EXISTS 'mcdbAdmin'@'localhost';
CREATE USER 'mcdbAdmin'@'localhost' IDENTIFIED BY 'mariasCookies2023ADMIN/';
REVOKE ALL PRIVILEGES ON *.* FROM 'mcdbAdmin'@'localhost';
GRANT ALL PRIVILEGES ON mcdb.* TO 'mcdbAdmin'@'localhost';

FLUSH PRIVILEGES;