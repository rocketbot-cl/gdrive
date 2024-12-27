



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

3. Listar archivos en Drive  
Lista los archivos de Google Drive. Este comando devuelve todos los archivos de forma predeterminada, incluidos los archivos desechados. Si no desea que los archivos desechados aparezcan en la lista, utilice trashed=false como filtro.

4. Descargar archivo  
Descargar un archivo desde Drive

5. Descargar carpeta  
Descargar una carpeta desde Drive

6. Exportar archivo  
Exportar un archivo de Drive al tipo de formato solicitado

7. Crear carpeta  
Crear carpeta

8. Copiar o mover archivo  
Copiar o mover un archivo

9. Subir archivo  
Subir un archivo a Google Drive

10. Subir carpeta  
Subir una carpeta a Google Drive

11. Eliminar un archivo o carpeta  
Eliminar un archivo o carpeta de Google Drive

12. Compartir archivo  
Comparte un archivo de Drive

13. Manejar permisos de carpeta  
Crea, actualiza o elimina un permiso. Los tipos de accesos son de usuarios: User o Group, y de acceso general: Domain o Anyone.

14. Listar permisos  
Obtener lista de permisos de un archivo

15. Borra permiso  
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
  
![MIT](https://camo.githubusercontent.com/107590fac8cbd65071396bb4d04040f76cde5bde/687474703a2f2f696d672e736869656c64732e696f2f3a6c6963656e73652d6d69742d626c75652e7376673f7374796c653d666c61742d737175617265)  
[MIT](http://opensource.org/licenses/mit-license.ph)