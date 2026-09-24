



# Google Drive
  
Módulo para conectarse a Google Drive y administrar sus archivos. Puede trabajar con archivos y carpetas propios o compartidos, moverlos, eliminarlos, descargarlos, exportarlos y cargarlos.  

*Read this in other languages: [English](README.md), [Português](README.pr.md), [Español](README.es.md)*

## Como instalar este módulo
  
Para instalar el módulo en Rocketbot Studio, se puede hacer de dos formas:
1. Manual: __Descargar__ el archivo .zip y descomprimirlo en la carpeta modules. El nombre de la carpeta debe ser el mismo al del módulo y dentro debe tener los siguientes archivos y carpetas: \__init__.py, package.json, docs, example y libs. Si tiene abierta la aplicación, refresca el navegador para poder utilizar el nuevo modulo.
2. Automática: Al ingresar a Rocketbot Studio sobre el margen derecho encontrara la sección de **Addons**, seleccionar **Install Mods**, buscar el modulo deseado y presionar install.  


## Overview


1. Configurar credenciales G-Suite  
Configura credenciales de Google Drive

2. Iniciar sesión sin archivo json  
Iniciar sesión en Google Drive sin archivo json

3. Configurar credenciales de cuenta de Servicio G-Suite  
Obtiene los permisos para manejar Google Drive con Rocketbot

4. Listar archivos en Drive  
Lista los archivos de Google Drive. Este comando devuelve todos los archivos de forma predeterminada, incluidos los archivos desechados. Si no desea que los archivos desechados aparezcan en la lista, utilice trashed=false como filtro.

5. Listar unidades compartidas  
Lista las unidades compartidas (Shared Drives) disponibles para la sesión actual.

6. Listar archivos en unidad compartida  
Lista los archivos dentro de una unidad compartida específica usando driveId.

7. Descargar archivo  
Descargar un archivo desde Drive

8. Descargar carpeta  
Descargar una carpeta desde Drive

9. Exportar archivo  
Exportar un archivo de Drive al tipo de formato solicitado

10. Crear carpeta  
Crear carpeta

11. Copiar o mover archivo  
Copiar o mover un archivo

12. Subir archivo  
Subir un archivo a Google Drive

13. Subir carpeta  
Subir una carpeta a Google Drive

14. Eliminar un archivo o carpeta  
Eliminar un archivo o carpeta de Google Drive

15. Compartir archivo  
Comparte un archivo de Drive

16. Manejar permisos de carpeta  
Crea, actualiza o elimina un permiso. Los tipos de accesos son de usuarios: User o Group, y de acceso general: Domain o Anyone.

17. Listar permisos  
Obtener lista de permisos de un archivo

18. Borra permiso  
Eliminar un permiso de un archivo  




----
### OS

- windows
- mac
- linux
- docker

### Dependencies
- [**google-api-python-client**](https://pypi.org/project/google-api-python-client/)- [**google-auth-httplib2**](https://pypi.org/project/google-auth-httplib2/)- [**google-auth-oauthlib**](https://pypi.org/project/google-auth-oauthlib/)
### License
  
![MIT](https://img.shields.io/github/license/instaloader/instaloader.svg)  
[MIT](https://opensource.org/license/mit)