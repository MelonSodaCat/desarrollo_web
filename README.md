# Tarea 5 - Examen - Desarrollo Web
## Por Antonia G. Calvo
   
## Descripción
Esta tarea incluye la implementación de una aplicaciónn en Spring Boot que posee tres principales rutas.

- / : Visualización de los avisos publicados.
Las siguientes rutas requiren autenticación con las credenciales indicadas en el enunciado.
- admin-fotos : panel de administración para eliminar fotos con un motivo
- logs : panel de visualización de últimas eliminaciones de fotos.

La aplicación se encuentra bajo el directorio examen siendo desarrollada en SpringBoot 4.0.0 y Java 25.
El directorio database se encarga de poblar la base de datos.

 ```bash

database
├── avisos.sql
├── create_user.sql
├── drop_db.sql
├── modificaciones-base-datos.sql
├── region-comuna.sql
├── tarea2.sql
examen
├── .mvn
├── main
│      ├── java\examen\prueba\examen
│      │   ├── config         
│      │   │    └── WebSecurityConfig.java 
│      │   ├── controllers
│      │   │    └── AppController.java 
│      │   ├── models    
│      │   └── services
│      │       └── AppServices.java 
│      └──  ExamenApplication.java
├── resources
│   ├── static
│   │    ├── css
│   │    │    └── new_styles.css
│   │    ├── imgs
│   │    ├── js
│   │    │    └── admin_foto.js
│   ├── templates
│   │    ├── fragments
│   │    │      ├── navbar.html
│   │    │      └── pagination.html
│   │    ├── admin-fotos.html
│   │    ├── bienvenida.html
│   │    ├── login.html
│   │    └── logs.html
│   └── application.properties
│
└── 
```

## Database

De los archivos `.sql` se habla en la siguiente sección más a fondo, son quienes construyen la base de datos.

## Main

### Config

Continene la configuración de Spring Security para las rutas resguardadas.

### Controllers

Controlador de la aplicación con las rutas relevantes.

### Models

Modelos de las entidades de la base de datos, la representación de la agrupación necesaria para obtener los datos de la foto y los repositorios necesarios para desplegar la información.

Una excepción son `Tipo` y `UnidadMedida` los cuales son enumeraciones utilizadas en los modelos.

### Services

Servicios de la aplicación a las rutas relevantes.

## Static

### CSS
Diseño de la aplicación

### img
Ímagenes utilizadas en la app

### js
Contiene el código para el modal de motivo en la ruta `t5-admin-fotos` y la validación de ese mismo input.


## Templates

En este se encuentra las rutas principales y dos fragmentos para la construcción.

### Fragments

Tenemos `navbar` que agrupa la barra de navegación hacia las otras rutas y `pagination` que considera la funcionalidad de cambio de página en la vista de los avisos, fotos y logs.

### Rutas Principales

- `admin-fotos`: corresponde al panel de administración para eliminar fotos
- `login`: corresponde al login para ingresar a las páginas con autenticación requerida.
- `logs`: corresponde al panel de registro eliminaciones de fotos.
- `bienvenida`: página principal que muestra los avisos actuales.



## Ejecución

Primero es necesario poblar la base de datos con los valores de prueba ejecutando los siguientes archivos en database.

```
- tarea2.sql
- region-comuna.sql
- create_user.sql
- modificaciones-base-datos.sql
- avisos.sql
```

De los archivos nuevos, ``avisos.sql`` genera 5 avisos en la base de datos, junto con fotos, información de contacto y comentarios. Esto apesar de no utilizarse contacto ni comentarios en esta tarea.

Por otro lado, ``create_user.sql` genera el usuario en la base de datos.

Si se desea eliminar la base de datos, se puede ejecutar ``drop_db.sql``.

Luego se requiere ejecutar el archivo `ExamenApplication.java` para correr la aplicación la cual se encuentra en `localhost:8080`

## Decisiones tomadas

- La tabla logs parte sin datos de prueba.
- No se eliminan los avisos, principalmente aún se ven en la ruta principal pero ya no se pueden eliminar en el panel.
- Se incluyen las fotos para el testeo