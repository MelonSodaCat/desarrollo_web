-- Active: 1761333108155@@127.0.0.1@3306@tarea2

-- Crear usuario para la tarea
CREATE USER 'cc5002'@'localhost' IDENTIFIED BY 'programacionweb';

SHOW GRANTS FOR 'cc5002'@'localhost';
-- Eliminar usuario si es necesario
DROP USER 'cc5002'@'localhost'