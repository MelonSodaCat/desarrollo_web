--- Insercion de Avisos



INSERT INTO tarea2.aviso_adopcion
(id, fecha_ingreso, comuna_id, sector, nombre, email, celular, tipo, cantidad, edad, unidad_medida, fecha_entrega, descripcion)
VALUES
(1, '2025-09-01 12:00:00', 130210, 'Metro Irarrázaval', 'Alisa Fuentes', 'alisa.fuentes@example.com', NULL, 'gato', 2, 2, 'm', '2025-09-04 12:00:00', 'Dos gatos de 2 meses encontrados cerca del Metro Irarrázaval, Ñuñoa.');

INSERT INTO tarea2.aviso_adopcion
(id, fecha_ingreso, comuna_id, sector, nombre, email, celular, tipo, cantidad, edad, unidad_medida, fecha_entrega, descripcion)
VALUES
(2, '2025-08-31 09:00:00', 80204, 'Jaime Repullo', 'Francisco Calvo', 'francisco.calvo@example.com', NULL, 'gato', 1, 6, 'm', '2025-09-02 15:00:00', 'Un gato de 6 meses en Talcahuano, sector Jaime Repullo.');

INSERT INTO tarea2.aviso_adopcion
(id, fecha_ingreso, comuna_id, sector, nombre, email, celular, tipo, cantidad, edad, unidad_medida, fecha_entrega, descripcion)
VALUES
(3, '2025-08-28 08:00:00', 80205, 'Unimarc', 'Josefina Gallardo', 'josefina.gallardo@example.com', NULL, 'gato', 1, 3, 'm', '2025-09-01 10:00:00', 'Gatito negro de 3 meses encontrado en Unimarc, Puerto Aysén.');

INSERT INTO tarea2.aviso_adopcion
(id, fecha_ingreso, comuna_id, sector, nombre, email, celular, tipo, cantidad, edad, unidad_medida, fecha_entrega, descripcion)
VALUES
(4, '2025-08-01 13:00:00', 80210, 'Supermercado Lider', 'Leon Aranguiz', 'leon.aranguiz@example.com', NULL, 'perro', 1, 6, 'm', '2025-08-28 10:00:00', 'Perro tipo Pomeranian de 6 meses encontrado en Chiguayante, Supermercado Líder.');

INSERT INTO tarea2.aviso_adopcion
(id, fecha_ingreso, comuna_id, sector, nombre, email, celular, tipo, cantidad, edad, unidad_medida, fecha_entrega, descripcion)
VALUES
(5, '2025-07-21 14:00:00', 80205, 'Parque Ecuador', 'Camilo Sanchez', 'camilo.sanchez@example.com', NULL, 'perro', 2, 5, 'm', '2025-07-29 19:00:00', 'Dos perros de 5 meses vistos en el Parque Ecuador, Concepción.');

INSERT INTO tarea2.aviso_adopcion
(id, fecha_ingreso, comuna_id, sector, nombre, email, celular, tipo, cantidad, edad, unidad_medida, fecha_entrega, descripcion)
VALUES
(6, '2025-10-21 14:00:00', 80205, 'Parque Ecuador', 'Camilo Meow', 'camilo.meow@example.com', NULL, 'perro', 2, 5, 'm', '2025-11-29 19:00:00', 'Dos perros de 5 meses vistos en el Parque Ecuador, Concepción.');

--- Insercion de Fotos

INSERT INTO foto (id, ruta_archivo, nombre_archivo, actividad_id)
VALUES (1, 'twocats.jpg', 'dosgatos_2meses', 1);

INSERT INTO foto (id, ruta_archivo, nombre_archivo, actividad_id)
VALUES (2, 'nala.jpg', '1gato_6meses', 2);

INSERT INTO foto (id, ruta_archivo, nombre_archivo, actividad_id)
VALUES (3, 'blackcat.jpg', '1gato_3meses', 3);

INSERT INTO foto (id, ruta_archivo, nombre_archivo, actividad_id)
VALUES (4, 'pomeranian.JPG', '1perro_6meses', 4);

INSERT INTO foto (id, ruta_archivo, nombre_archivo, actividad_id)
VALUES (5, 'twodogs.JPG', '2perros_5meses', 5);

INSERT INTO foto (id, ruta_archivo, nombre_archivo, actividad_id)
VALUES (6, 'twodogs.JPG', '2perros_5meses', 6);
