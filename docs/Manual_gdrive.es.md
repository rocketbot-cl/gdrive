



# Google Drive
  
Módulo para conectarse a Google Drive y administrar sus archivos. Puede trabajar con archivos y carpetas propios o compartidos, moverlos, eliminarlos, descargarlos, exportarlos y cargarlos.  

*Read this in other languages: [English](Manual_gdrive.md), [Português](Manual_gdrive.pr.md), [Español](Manual_gdrive.es.md)*
  
![banner](imgs/Banner_gdrive.png)

## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  



## Como usar este modulo

Antes de usar este modulo, es necesario registrar tu aplicación en el portal de Google Cloud. Para esto, debes seguir los siguientes pasos:

1. Ir a [Consola de Google](https://console.cloud.google.com/projectcreate?previousPage=%2Fhome%2Fdashboard) para crear un nuevo proyecto (Si ya tienes uno creado, omita este paso) y complete los datos indicados en el formulario

![](imgs/proyectonuevo.png)

En la barra superior verás el nombre del proyecto. Si no se visualiza, cambie al proyecto creado haciendo click en la en el menu que se encuentra remarcado en la imagen.

![](imgs/seleccionarproyecto.png)

2. Ve a **API y Servicios** del panel izquierdo, y luego de cambiar a la página, hacer click en **HABILITAR APIs Y SERVICIOS**

![](imgs/habilitarapiyservicios.png)

3. Dentro del buscador "Buscar API y servicios" escriba **Google Drive API**. Luego, habilitar la API dando click en **Habilitar**

![](imgs/gdriveApi.png)

Se redireccionará a la página de 
configuración de la API.

4. En el panel lateral haga click en **Pantalla de consentimiento de OAuth**, si tienes una cuenta corporativa de gmail, podrás utilizar la API indefinidamente y verás que el tipo de usuario es **Interno**. Si cuentas con una cuenta gmail gratuita, tendrás que dar el consentimiento una vez a la semana para poder conectarte a tu cuenta de correo, tu tipo de usuario es **Externo** y deberás agregar usuarios de prueba. Luego presiona el botón **Crear**

![](imgs/pantallaDeCons.png)

5. Seleccionar el nombre de la app y los campos obligatorios según cada caso. A continuación haga click en siguiente.

![](imgs/infoApp.png)


6. Saltearse la pantalla de **Permisos**, haga click en el botón Guardar y Continuar que se encuentra a final de página.

![](imgs/permisos.png)

7. En la pantalla de **Usuarios de prueba** haga click en el botón **Add User** y agregue su usuario. Haga click en Guardar y Continuar

![](imgs/usuarioprueba.png)

8. Dirigirse desde el Menu de 
Navegación Izquierdo a **Credenciales**. Presione **+Crear Credenciales** e indique la opción **ID de cliente de OAuth**

![](imgs/crearcredencialesok.png)

9. Seleccionar como Tipo de Aplicación: **App de Escritorio**. Coloca un nombre para la aplicación y presione el botón **Crear**

![](imgs/appEscritorio.png)

10. Nos creará las credenciales, si queremos loguearnos con el archivo json damos click en **Descargar JSON** y luego en **Aceptar**. Es importante mantener el archivo descargado. Se utilizará más adelante en el módulo. Si queremos loguearnos con las credenciales, guardamos el Client ID y el Secret ID para usarlo más adelante el módulo.

![](imgs/credencialesDescarga.png)


Nota: Cuando se realice la primera conexión, se creará un archivo .pickle en la carpeta raíz de Rocketbot, para conectarse al mismo servicio desde otra cuenta, debe eliminar
ese archivo Realice el mismo procedimiento para el caso en que caduquen las credenciales.


## Descripción de los comandos

### Configurar credenciales G-Suite
  
Configura credenciales de Google Drive
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta del archivo de credenciales|Archivo JSON con las credenciales de acceso a la API de Google Drive.|C:\Usuario\Desktop\credentials.json|
|Puerto (Opcional)||8080|
|Session||session|

### Iniciar sesión sin archivo json
  
Iniciar sesión en Google Drive sin archivo json
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Client ID|ID de cliente de la consola de Google Cloud Platform.|123456789012-xxxxxxxxxxxxxxx.apps.googleusercontent.com|
|Client Secret|Secreto de cliente de la consola de Google Cloud Platform.|GOCSPX-xxxxxxxxx_Dc9TGFy32_xxxxxxxx|
|Puerto (Opcional)||8080|
|Session||session|

### Listar archivos en Drive
  
Lista los archivos de Google Drive. Este comando devuelve todos los archivos de forma predeterminada, incluidos los archivos desechados. Si no desea que los archivos desechados aparezcan en la lista, utilice trashed=false como filtro.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Filtro||mimeType = 'application/vnd.google-apps.folder' and trashed = false|
|Sólo archivos propios||-|
|Sólo archivos compartidos conmigo||-|
|Más datos||-|
|Session||session|
|Asignar resultado a variable||var|

### Descargar archivo
  
Descargar un archivo desde Drive
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del archivo (Drive)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Ruta donde guardar archivo||C:\users\usuario\Downloads|
|Session||session|
|Asignar resultado a variable|Devolverá True o False dependiendo del éxito de la ejecución.|var|

### Descargar carpeta
  
Descargar una carpeta desde Drive
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID de la carpeta (Drive)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Ruta donde guardar la carpeta||C:\users\usuario\Downloads|
|Session||session|
|Asignar resultado a variable|Devolverá True o False dependiendo del éxito de la ejecución.|var|

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
|ID de la carpeta (Drive)|Opcional si se quiere crear dentro de una carpeta específica|1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Nombre de la carpeta||Nueva carpeta|
|Session||session|
|Asignar resultado a variable||var|

### Copiar o mover archivo
  
Copiar o mover un archivo
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del archivo (Drive)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Carpeta destino (ID)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Mover o Copiar||var|
|Session||session|
|Asignar resultado a variable||var|

### Subir archivo
  
Subir un archivo a Google Drive
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta del archivo||C:\archivo.txt|
|Nombre nuevo (opcional)||nuevo_nombre.txt|
|Guardar en carpeta - ID (opcional)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Convertir a formato Google|Si se marca, intentará subir el archivo como el formato equivalente de Google (de existir), si no, subira el archivo original.||
|Session||session|
|Asignar resultado a variable||var|

### Subir carpeta
  
Subir una carpeta a Google Drive
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|Ruta de la carpeta||C:\folder|
|Guardar en carpeta - ID (opcional)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Nombre nuevo (opcional)|Nuevo nombre para la carpeta raíz a subir. Es opcional.|nuevo_nombre|
|Convertir a formato Google|Si se marca, intentará subir el archivo como el formato equivalente de Google (de existir), si no, subira el archivo original.||
|Session||session|
|Asignar resultado a variable||var|

### Eliminar un archivo o carpeta
  
Eliminar un archivo o carpeta de Google Drive
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del archivo (Drive)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Session||session|
|Asignar resultado a variable||var|

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
|Session||session|
|Asignar resultado a variable||var|

### Manejar permisos de carpeta
  
Crea, actualiza o elimina un permiso. Los tipos de accesos son de usuarios: User o Group, y de acceso general: Domain o Anyone.
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID de la carpeta (Drive)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Accion||---- Select ----|
|Tipo de Acceso||---- Select ----|
|Rol||---- Select ----|
|Email, Dominio o PermissionID|||
|Enviar correo de notificación||-|
|Session||session|
|Asignar resultado a variable||var|

### Listar permisos
  
Obtener lista de permisos de un archivo
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del archivo (Drive)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Session||session|
|Asignar resultado a variable||var|

### Borra permiso
  
Eliminar un permiso de un archivo
|Parámetros|Descripción|ejemplo|
| --- | --- | --- |
|ID del archivo (Drive)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|ID del permiso (Drive)||15224413836718185781|
|Session||session|
|Asignar resultado a variable||var|
