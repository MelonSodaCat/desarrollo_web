# Tarea 2 - Desarrollo Web
## Por Antonia G. Calvo
   
## Descripción
Esta tarea incluye la implementación de una aplicaciónn de flask para un sitio de adopciones en la carpeta flask_app.

 ```bash
flask_app
├── app.py
├── database
│      ├── avisos.sql
│      ├── create_user.sql
│      ├── db.py
│      ├── drop_db.sql
│      ├── region-comuna.sql
│      └── tarea2.sql
├── static
│   ├── css
│   │   └── new_styles.css
│   ├── js
│   │    ├── aviso.js
│   │    ├── fila_listado.js
│   │    └── validaciones.js
│   └── imgs
│       
└── templates
    ├── add_aviso.html
    ├── base.html
    ├── baseOtherPages.html
    ├── bienvenida.html
    ├── estadisticas.html
    └── ver_listado.html
```

#### Database

De los archivos `.sql` se habla en la siguiente sección más a fondo, son quienes construyen la base de datos.

El archivo db.py se encarga de implementar la lógica con sqlalchemy para realizar consultas e inserciones durante la ejecución de la aplicación.

#### CSS
Diseño de la aplicación

#### js
Se mantienen las validaciones de la entrega anterior en `validaciones.js` con algunas de las mejoras del feedback entregado.

El archivo `fila_listado.js ` se encarga del modal al clickear una fila.

El archivo `aviso.js` gestiona la actualización de las fechas, las comunas y las redes sociales en el formulario.

#### templates

Se encuentran dos archivos que funcionan de base para `bienvenida.html`, `base.html`, y para las otras dos páginas princiaples de esta tarea `add_aviso.html` y `ver_listado.html`, `baseOtherPages.html`. Esta diferencia viene del botón de regreso al final de la página que tienen estos dos últimos. 

En cuanto a estos, se adaptaron como plantillas de Jinja2 y se habilitó la recolección de datos desde el backend. 

#### validations.py

Archivo que posee todas las validaciones de parte del backend para el formulario. 

#### app.py

Aplicación principal con las rutas pedidas y manejo de redirecciones.


## Ejecución

Primero descargar los requirements con:

```
pip install -r requirements.txt
```
Luego correr los archivos de base de datos en el siguiente orden:
```
- tarea2.sql
- region-comuna.sql
- avisos.sql
- create_user.sql
```
De los archivos nuevos, ``avisos.sql`` genera 5 avisos en la base de datos, junto con fotos e información de contacto. Por otro lado, ``create_user.sql` genera el usuario en la base de datos.

Si se desea eliminar la base de datos, se puede ejecutar ``drop_db.sql``.

Luego ejecute la aplicación de flask con el comando: 

```
python app.py
```
Esta se encuentra en el puerto 5000, con lo que se puede acceder a traves de ``http://127.0.0.1:5000``

## Decisiones tomadas
- No se implementó el guardado en la tabla 'Contactar_Por'
- Se dejarón avisos en la base de datos a modo de demostración de las funcionalidades.
- Se utilizan mensajes flash para las alertas con el fin de que no persistan al recargar la página.

