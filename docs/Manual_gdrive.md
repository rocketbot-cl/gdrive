



# Google Drive
  
Module to connect to Google Drive and manage your files. You can work with owned or shared files and folders, move, delete, download, export and upload them.  

*Read this in other languages: [English](Manual_gdrive.md), [Português](Manual_gdrive.pr.md), [Español](Manual_gdrive.es.md)*
  
![banner](imgs/Banner_gdrive.png)
## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip it in the modules folder. The folder name must be the same as the module and inside it must have the following files and folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the **Addons** section, select **Install Mods**, search for the desired module and press install.  


## How to use this module

Before using this module, you must register your app into the Google Cloud Portal.

1. Sign in with a google account to the following link: https://console.cloud.google.com/projectcreate?previousPage=%2Fhome%2Fdashboard
2. Complete the form and then press Create
3. Within the Navigation Menu (Left), enter API and Services
4. In the upper section, go to "+ ENABLE API AND SERVICES"
5. Search for "Google Drive API", select it and finally enable it
6. Again, go to the Navigation Menu (Left) > API and Services > Credentials
7. Press Create Credentials > OAuth Client ID, select Application Type: Desktop App, enter a name and create.
8. Download the credentials JSON file.
9. Finally go to the Navigation Menu (Left) > Consent Screen and add a user in the "Test Users" section

Note: When the first connection is made, a .pickle file will be created in the Rocketbot root folder, to connect to the same service from another account you must delete
that file. Do the same 
procedure for the case in which the credentials expire.


## Description of the commands

### Setup G-Suite credentials
  
Configure Google Drive credentials
|Parameters|Description|example|
| --- | --- | --- |
|Credentials file path||C:\Usuario\Desktop\credentials.json|
|Session||session|

### List files in Drive
  
List files of Google Drive. This command returns all files by default, including trashed files. If you don't want trashed files to appear in the list, use the trashed=false as filter.
|Parameters|Description|example|
| --- | --- | --- |
|Filter||mimeType = 'application/vnd.google-apps.folder' and trashed = false|
|Owned files only||-|
|Shared with me files only||-|
|Assign result to var||var|
|Session||session|

### Download file
  
Download file from Drive
|Parameters|Description|example|
| --- | --- | --- |
|File ID (Drive)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Path where to save file||C:\users\usuario\Downloads|
|Session||session|

### Export file
  
Export a file from Drive to the requested format type
|Parameters|Description|example|
| --- | --- | --- |
|File ID (Drive)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|File format (Drive)||---- Select format ----|
|Path where to save file||C:\users\usuario\Downloads|
|Session||session|

### Create Folder
  
Create Folder
|Parameters|Description|example|
| --- | --- | --- |
|File ID (Drive)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Folder name||New Folder|
|Assign result to var||var|
|Session||session|

### Copy or move file
  
Copy or move a file
|Parameters|Description|example|
| --- | --- | --- |
|File ID (Drive)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Destiny Folder ID||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Move or Copy||var|
|Assign result to var||var|
|Session||session|

### Upload file
  
Upload a file to Google Drive
|Parameters|Description|example|
| --- | --- | --- |
|File path||C:\file.txt|
|New name (optional)||new_name.txt|
|Save to folder - ID (optional)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Convert to Google format|If checked, it will try to upload the file as Google's equivalent format (if any), if not, it will upload the original file.||
|Assign result to var||var|
|Session||session|

### Delete a file or folder
  
Delete a file or folder from Drive
|Parameters|Description|example|
| --- | --- | --- |
|File ID (Drive)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Assign result to var||var|
|Session||session|

### Share file
  
Share a file in Drive
|Parameters|Description|example|
| --- | --- | --- |
|File ID (Drive)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Assign result to var||var|
|Session||session|
