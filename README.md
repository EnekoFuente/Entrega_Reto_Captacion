# Entrega_Reto_Captacion
Entrega I de desarrollo para aplicaciones IoT

## Miembros

- Ekaitz Garcia
- Eneko Fuente
- Gaizka Miranda

## Pasos seguidos
### Preparación
 Lo primero que hicimos fue informarnos bien sobre cómo implementar Docker en el proyecto. Para ello, revisamos la documentación oficial de Docker y Mage AI, para entender cómo instalar y configurar ambos de la manera correcta. También buscamos ejemplos y guías que nos ayudarán a evitar problemas durante la instalación. 

### Creación ,configuración y ejecución archivo .yml
Una vez que tenemos claro cómo emplear Docker, pasamos a crear el archivo de configuración docker-compose.yml. Este archivo se emplea para definir y gestionar los contenedores necesarios para ejecutar Mage AI y la base de datos PostgreSQL. En el archivo docker-compose.yml, configuramos:
- Los contenedores de Mage AI: Creamos un contenedor Mage AI, especificando las versiones.
- Base de datos PostgreSQL: Configuramos un contenedor PostgreSQL, donde almacenaremos los datos que Mage AI procesara. Definimos el puerto, el usuario, la contraseña y el nombre de la base de datos.
 
Además, creamos un archivo .env para gestionar las variables de entorno. Este archivo nos permitirá definir las credenciales de la base de datos de manera segura y reutilizable.
Una vez que los archivos docker-compose.yml y .env están configurados, ejecutamos el comando docker-compose up para ejecutar los contenedores. De esta forma ejecutamos el entorno y así poder trabajar con Mage AI y con la base de datos PostgreSQL.

### Creación Pipeline
Una vez hemos ejecutado Mage AI, nos dirigimos a la interfaz de Mage AI para crear y gestionar los pipelines. Mage AI nos va a permitir crear pipelines de datos, lo que facilita la manipulación y transformación de grandes volúmenes de datos de manera eficiente. El pipeline va a realizar los siguientes procesos:

#### Pipeline para cargar datos desde PostgreSQL
El primer pipeline se va a encargar de conectar Mage AI con la base de datos PostgreSQL que habíamos creado. Utilizamos el bloque de cargar datos desde PostgreSQL en Mage AI, donde especificamos la consulta SQL necesaria para obtener los datos de la tabla de ventas que queríamos procesar. Configuramos los parámetros de conexión, como el usuario, la contraseña y el nombre de la base de datos, que ya habíamos definido en el archivo .env.
Este pipeline extrae los datos desde la base de datos PostgreSQL y los pasó a un DataFrame para su posterior procesamiento en los siguientes pasos.

#### Pipeline para transformar los datos
El segundo pipeline va a transformaciones a los datos obtenidos de la base de datos. Usamos el bloque “Transformer” en Mage AI, donde escribimos el código necesario para realizar las transformaciones:
- Convertir los nombres de los productos a minúsculas: Utilizamos el método str.lower() para asegurar que todos los nombres de los productos fueran consistentes.
- Aplicar un descuento del 10% al precio de los productos: Modificamos la columna de precios para aplicar un descuento del 10%.
Este bloque transforma los datos de acuerdo con nuestras necesidades y los dejó listos para ser almacenados en una nueva base de datos.

#### Pipeline para guardar los datos transformados en una nueva tabla de PostgreSQL
Finalmente, el tercer pipeline se encargará de tomar los datos transformados y guardarlos en una nueva tabla de PostgreSQL. Usamos el bloque de "Guardar en PostgreSQL" en Mage AI, donde configuramos la conexión a la base de datos de destino y especificamos el nombre de la nueva tabla, “ventas_transformadas”. 
Este paso nos va a permitir almacenar los resultados del procesamiento y las transformaciones de manera organizada y accesible para futuras consultas o análisis.

### Ejecución y validación: 
Una vez que los tres pipelines estaban configurados y conectados correctamente, ejecutamos el flujo de trabajo. Primero, Mage AI carga los datos desde PostgreSQL, luego le va a aplicar unas transformaciones y finalmente, guardará los datos en la nueva tabla de PostgreSQL.
A lo largo del proceso, validamos que todo estuviera funcionando correctamente. Mage AI proporciona bloques de prueba que nos permitieron asegurarnos de que los datos estuvieran siendo procesados y almacenados de manera correcta, sin errores. Realizamos pruebas para verificar que los nombres de los productos se hubieran convertido a minúsculas y que el descuento del 10% se hubiera aplicado correctamente a los precios.

## Instrucciones de uso
- Requisitos previos: Primero, asegúrate de tener instalados Docker, Docker-Compose, WSL/Linux y un editor de texto. Luego, clona el repositorio del proyecto con el comando “https://github.com/EnekoFuente/Entrega_Reto_Captacion.git”
El archivo .env ya está configurado, por lo que no necesitas modificarlo.
Para iniciar los contenedores, ejecutar:  docker-compose up -d y para verificar que esta corriendo el contenedor docker ps

Acceder a Mage AI: Una vez que los servicios estén activos, abre un navegador y accede a la interfaz de Mage AI empleando http://localhost:6789

Ejecutar pipeline: Dentro de la interfaz Mage AI se va a proceder a ejecutar los diferentes bloques empleados para la captacion, transformacion y almacenamiento de datos
