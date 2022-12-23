# Google Drive
  
Módulo de conexión con Google Drive  

## Como instalar este módulo
  
__Descarga__ e __instala__ el contenido en la carpeta 'modules' en la ruta de Rocketbot.  


## Como usar este modulo

Antes de usar este modulo, es necesario registrar tu aplicación en el portal de Google Cloud. 

1. Ingresar con una cuenta de google al siguiente link: https://console.cloud.google.com/projectcreate?previousPage=%2Fhome%2Fdashboard
2. Completar el formulario y luego presionar Crear
3. Dentro del Menu de Navegación (Izquierdo), ingresar en API y Servicios
4. En la sección superior, ingresar a "+ HABILITAR API Y SERVICIOS"
5. Buscar "Google Drive API", seleccionar y por ultimo habilitar
6. Nuevamente dirigirse a Menu de Navegación (Izquierdo) > API y Servicios > Credenciales
7. Presionas Crear Credenciales > ID de cliente de OAuth, seleccionar como Tipo de Aplicación: App de Escritorio, colocar un nombre y crear.
8. Descargar el achivo JSON de credenciales.
9. Por ultimo dirigirse a Menu de Navegación (Izquierdo) > Pantalla de Consentimiento y agregar usuario dentro de la seccion "Usuarios de prueba"

Nota: Cuando se realice la primera conexión, se creará un archivo .pickle en la carpeta raíz de Rocketbot, para conectarse al mismo servicio desde otra cuenta, debe eliminar
ese archivo Realice el mismo procedimiento para el caso en que caduquen las credenciales.


## Overview


1. Configurar credenciales G-Suite  
Configura credenciales de Google Drive

2. Listar archivos en Drive  
Lista los archivos de Google Drive

3. Descargar archivo  
Descargar un archivo desde Drive

4. Exportar archivo  
Exportar un archivo de Drive al tipo de formato solicitado

5. Crear carpeta  
Crear carpeta

6. Copiar o mover archivo  
Copiar o mover archivo

7. Subir archivo  
Subir un archivo a Google Drive

8. Eliminar un archivo o carpeta  
Eliminar un archivo o carpeta de Google Drive

9. Compartir archivo  
Comparte un archivo de Drive  




----
### OS

- windows
- mac
- linux
- docker

### Dependencies
- [**google-api-python-client**](https://pypi.org/project/google-api-python-client/)- [**google-auth-httplib2**](https://pypi.org/project/google-auth-httplib2/)- [**google-auth-oauthlib**](https://pypi.org/project/google-auth-oauthlib/)
### License
  
![MIT](https://camo.githubusercontent.com/107590fac8cbd65071396bb4d04040f76cde5bde/687474703a2f2f696d672e736869656c64732e696f2f3a6c6963656e73652d6d69742d626c75652e7376673f7374796c653d666c61742d737175617265)  
[MIT](http://opensource.org/licenses/mit-license.ph)