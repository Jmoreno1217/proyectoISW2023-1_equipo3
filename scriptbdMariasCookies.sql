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
DROP TABLE IF EXISTS producto;
CREATE TABLE producto (
    producto_id int NOT NULL UNIQUE,
    producto_nombre varchar(25) NOT NULL,
    producto_precio varchar(25) NOT NULL,
    producto_descripcion varchar(100) NOT NULL,
    producto_sabor varchar(100) NOT NULL,
    producto_tamanio varchar(100) NOT NULL,
    PRIMARY KEY (producto_id)
);
INSERT INTO producto VALUES(
    '1',
    'Conchitas',
    '$15.00',
    'Tradicional pan dulce, ideal para degustar junto una tasa de cafe o leche con chocolate.',
    'Vainilla-Chocolate',
    'Chico-Mediano'
),(
    '2',
    'Polvoron',
    '$12.00',
    'Pan dulce similar a una galleta, muy popular entre los niños.',
    'Vainilla-Chocolate-Fresa-Napolitano-Chispado',
    'Chico-Mediano'
),(
    '3',
    'Galletas de formas',
    '$5.00',
    'Galletas de distintas formas, ideal para regalos a ese alguien especial.',
    'Vainilla-Chocolate-Fresa',
    'Estrella chica-Estrella mediana-Corazon chico'
),(
    '4',
    'Cupcakes',
    '$10.00',
    'Pan dulce similar envuelto en papel cera, ideal para fiestas de cumpleaños.',
    'Vainilla-Chocolate-Fresa',
    'Chico-Mediano'
);

DROP USER IF EXISTS 'mcdbCliente'@'localhost';
CREATE USER 'mcdbCliente'@'localhost' IDENTIFIED BY 'mariasCookies2023/';
REVOKE ALL PRIVILEGES ON *.* FROM 'mcdbCliente'@'localhost';

DROP USER IF EXISTS 'mcdbAdmin'@'localhost';
CREATE USER 'mcdbAdmin'@'localhost' IDENTIFIED BY 'mariasCookies2023ADMIN/';
REVOKE ALL PRIVILEGES ON *.* FROM 'mcdbAdmin'@'localhost';
GRANT ALL PRIVILEGES ON mcdb.* TO 'mcdbAdmin'@'localhost';

FLUSH PRIVILEGES;