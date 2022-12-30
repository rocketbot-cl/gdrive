# Google Drive
  
Google Drive connection module  
  
![banner](imgs/Banner_gdrive.png)
## How to install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  



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
that file. Do the same procedure for the case in which the credentials expire.


## Description of the commands

### Setup G-Suite credentials
  
Configure Google Drive credentials
|Parameters|Description|example|
| --- | --- | --- |
|Credentials file path||C:\Usuario\Desktop\credentials.json|
|Session||session|

### List files in Drive
  
List files of Google Drive
|Parameters|Description|example|
| --- | --- | --- |
|Filter||mimeType = 'application/vnd.google-apps.folder'|
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
