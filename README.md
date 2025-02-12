



# Google Drive
  
Module to connect to Google Drive and manage your files. You can work with owned or shared files and folders, move, delete, download, export and upload them.  

*Read this in other languages: [English](README.md), [Português](README.pr.md), [Español](README.es.md)*

## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## Overview


1. Setup G-Suite credentials  
Configure Google Drive credentials

2. Login without json file  
Login to Google Drive without json file

3. List files in Drive  
List files of Google Drive. This command returns all files by default, including trashed files. If you don't want trashed files to appear in the list, use the trashed=false as filter.

4. Download file  
Download file from Drive

5. Download folder  
Download folder from Drive

6. Export file  
Export a file from Drive to the requested format type

7. Create Folder  
Create Folder

8. Copy or move file  
Copy or move a file

9. Upload file  
Upload a file to Google Drive

10. Upload folder  
Upload a folder to Google Drive

11. Delete a file or folder  
Delete a file or folder from Drive

12. Share file  
Share a file in Drive

13. Manage folder permissions  
Create, update or delete a folder permission. The types of access are user: User or Group, and general: Domain or Anyone.

14. List permissions  
Get list of permissions from a file

15. Delete permission  
Delete a permission from a file  




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