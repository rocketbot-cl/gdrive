# Google Drive
  
Google Drive connection module  
  
![banner](imgs/Banner_gdrive.png)
## How to install this module
  
__Download__ and __install__ the content in 'modules' folder in Rocketbot path  



## Description of the commands

### Setup G-Suite credentials
  
Configure Google Drive credentials
|Parameters|Description|example|
| --- | --- | --- |
|Credentials file path||C:\Usuario\Desktop\credentials.json|

### List files in Drive
  
List files of Google Drive
|Parameters|Description|example|
| --- | --- | --- |
|Filter||mimeType = 'application/vnd.google-apps.folder'|
|Assign result to var||var|

### Download file
  
Download file from Drive
|Parameters|Description|example|
| --- | --- | --- |
|File ID (Drive)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Path where to save file||C:\users\usuario\Downloads|

### Export file
  
Export a file from Drive to the requested format type
|Parameters|Description|example|
| --- | --- | --- |
|File ID (Drive)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|File format (Drive)||---- Select format ----|
|Path where to save file||C:\users\usuario\Downloads|

### Create Folder
  
Create Folder
|Parameters|Description|example|
| --- | --- | --- |
|File ID (Drive)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Folder name||New Folder|
|Assign result to var||var|

### Copy or move file
  
Copy or move a file
|Parameters|Description|example|
| --- | --- | --- |
|File ID (Drive)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Destiny Folder ID||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Move or Copy||var|
|Assign result to var||var|

### Upload file
  
Upload a file to Google Drive
|Parameters|Description|example|
| --- | --- | --- |
|File path||C:\file.txt|
|New name (optional)||new_name.txt|
|Save to folder - ID (optional)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Assign result to var||var|

### Delete a file or folder
  
Delete a file or folder from Drive
|Parameters|Description|example|
| --- | --- | --- |
|File ID (Drive)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Assign result to var||var|

### Share file
  
Share a file in Drive
|Parameters|Description|example|
| --- | --- | --- |
|File ID (Drive)||1iySKcDSSHoRxjlNBS4WIANMi9RLp-t8mwYmc-61cvTo|
|Assign result to var||var|
