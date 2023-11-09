



# Google Drive
  
Módulo para conectarse a Google Drive y administrar sus archivos. Puede trabajar con archivos y carpetas propios o compartidos, moverlos, eliminarlos, descargarlos, exportarlos y cargarlos.  

*Read this in other languages: [English](Manual_gdrive.md), [Português](Manual_gdrive.pr.md), [Español](Manual_gdrive.es.md)*
  
![banner](imgs/Banner_gdrive.png)
## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  



## Como usar este modulo

Antes de usar este modulo, es necesario registrar tu aplicación en el portal de Google Cloud. 

1. Ingresar con una cuenta de google al siguiente link: https://console.cloud.google.com/projectcreate?previousPage=%2Fhome%2Fdashboard
2. Completar el formulario y luego presionar Crear
3. Dentro del Menu de Navegación (Izquierdo), ingresar en API y Servicios
4. En la sección superior, ingresar a "+ HABILITAR API Y SERVICIOS"
5. Buscar "Google Drive API", seleccionar y por ultimo habilitar
6. Nuevamente dirigirse a Menu de Navegación (Izquierdo) > API y Servicios > Credenciales
7. Presionas Crear Credenciales > ID de cliente de OAuth, seleccionar como Tipo de Aplicación: App de Escritorio, colocar un nombre y crear.
8. Descargar el archivo JSON de credenciales.
9. Por ultimo dirigirse a Menu de Navegación (Izquierdo) > Pantalla de Consentimiento y agregar usuario dentro de la seccion "Usuarios de prueba"

Nota: Cuando se realice la primera conexión, se creará un 
archivo .pickle en la carpeta raíz de Rocketbot, para conectarse al mismo servicio desde otra cuenta, debe eliminar
ese archivo Realice el mismo procedimiento para el caso en que caduquen las credenciales.


## Descripción de los comandos

### Configurar credenciales G-Suite
  
Configura credenciales de Google Drive
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta archivo de credenciales||C:\Usuario\Desktop\credentials.json|
|Session||session|

### Listar archivos en Drive
  
Lista los archivos de Google Drive. Este comando devuelve todos los archivos de forma predeterminada, incluidos los archivos desechados. Si no desea que los archivos desechados aparezcan en la lista, utilice trashed=false como filtro.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Filtro||mimeType = 'application/vnd.google-apps.folder' and trashed = false|
|Sólo archivos propios||-|
|Sólo archivos compartidos conmigo||-|
|Más datos||-|
|Asignar resultado a variable||var|
|Session||session|

### Descargar archivo
  
Descargar un archivo desde Drive
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del archivo (Drive)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Ruta donde guardar archivo||C:\users\usuario\Downloads|
|Session||session|

### Exportar archivo
  
Exportar un archivo de Drive al tipo de formato solicitado
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del archivo (Drive)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Formato del archivo (Drive)||---- Select format ----|
|Ruta donde guardar archivo||C:\users\usuario\Downloads|
|Session||session|

### Crear carpeta
  
Crear carpeta
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del archivo (Drive)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Nombre de la carpeta||Nueva carpeta|
|Asignar resultado a variable||var|
|Session||session|

### Copiar o mover archivo
  
Copiar o mover un archivo
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del archivo (Drive)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Carpeta destino (ID)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Mover o Copiar||var|
|Asignar resultado a variable||var|
|Session||session|

### Subir archivo
  
Subir un archivo a Google Drive
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta del archivo||C:\archivo.txt|
|Nombre nuevo (opcional)||nuevo_nombre.txt|
|Guardar en carpeta - ID (opcional)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Convertir a formato Google|Si se marca, intentará subir el archivo como el formato equivalente de Google (de existir), si no, subira el archivo original.||
|Asignar resultado a variable||var|
|Session||session|

### Eliminar un archivo o carpeta
  
Eliminar un archivo o carpeta de Google Drive
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del archivo (Drive)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Asignar resultado a variable||var|
|Session||session|

### Compartir archivo
  
Comparte un archivo de Drive
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del archivo (Drive)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Tipo||---- Select ----|
|Rol||---- Select ----|
|Email o Dominio|||
|Enviar correo de notificación||-|
|Transferir propiedad||-|
|Mover archivo a la carpeta raíz del nuevo propietario||-|
|Asignar resultado a variable||var|
|Session||session|

### Listar permisos
  
Obtener lista de permisos de un archivo
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del archivo (Drive)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Asignar resultado a variable||var|
|Session||session|

### Borra permiso
  
Eliminar un permiso de un archivo
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del archivo (Drive)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|ID del permiso (Drive)||15224413836718185781|
|Asignar resultado a variable||var|
|Session||session|
