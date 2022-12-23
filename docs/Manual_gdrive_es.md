# Google Drive
  
Módulo de conexión con Google Drive  
  
![banner](imgs/Banner_gdrive.png)
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


## Descripción de los comandos

### Configurar credenciales G-Suite
  
Configura credenciales de Google Drive
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta archivo de credenciales||C:\Usuario\Desktop\credentials.json|

### Listar archivos en Drive
  
Lista los archivos de Google Drive
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Filtro||mimeType = 'application/vnd.google-apps.folder'|
|Asignar resultado a variable||var|

### Descargar archivo
  
Descargar un archivo desde Drive
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del archivo (Drive)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Ruta donde guardar archivo||C:\users\usuario\Downloads|

### Exportar archivo
  
Exportar un archivo de Drive al tipo de formato solicitado
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del archivo (Drive)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Formato del archivo (Drive)||---- Select format ----|
|Ruta donde guardar archivo||C:\users\usuario\Downloads|

### Crear carpeta
  
Crear carpeta
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del archivo (Drive)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Nombre de la carpeta||Nueva carpeta|
|Asignar resultado a variable||var|

### Copiar o mover archivo
  
Copiar o mover archivo
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del archivo (Drive)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Carpeta destino (ID)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Mover o Copiar||var|
|Asignar resultado a variable||var|

### Subir archivo
  
Subir un archivo a Google Drive
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta del archivo||C:\archivo.txt|
|Nombre nuevo (opcional)||nuevo_nombre.txt|
|Guardar en carpeta - ID (opcional)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Asignar resultado a variable||var|

### Eliminar un archivo o carpeta
  
Eliminar un archivo o carpeta de Google Drive
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del archivo (Drive)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Asignar resultado a variable||var|

### Compartir archivo
  
Comparte un archivo de Drive
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del archivo (Drive)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Asignar resultado a variable||var|