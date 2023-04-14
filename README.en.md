



# Google Drive
  
Google Drive connection module  

## How to install this module
  
To install the module in Rocketbot Studio, it can be done in two ways:
1. Manual: __Download__ the .zip file and unzip 
it in the modules folder. The folder name must be the same as the module and inside it must have the following files and
 folders: \__init__.py, package.json, docs, example and libs. If you have the application open, refresh your browser to 
be able to use the new module.
2. Automatic: When entering Rocketbot Studio on the right margin you will find the 
**Addons** section, select **Install Mods**, search for the desired module and press install.  



## How to use this module

Before using this module, you must register your app into the Google Cloud Portal.

1. Sign 
in with a google account to the following link: 
https://console.cloud.google.com/projectcreate?previousPage=%2Fhome%2Fdashboard
2. Complete the form and then press 
Create
3. Within the Navigation Menu (Left), enter API and Services
4. In the upper section, go to "+ ENABLE API AND 
SERVICES"
5. Search for "Google Drive API", select it and finally enable it
6. Again, go to the Navigation Menu (Left) >
 API and Services > Credentials
7. Press Create Credentials > OAuth Client ID, select Application Type: Desktop App, 
enter a name and create.
8. Download the credentials JSON file.
9. Finally go to the Navigation Menu (Left) > Consent 
Screen and add a user in the "Test Users" section

Note: When the first connection is made, a .pickle file will be 
created in the Rocketbot root folder, to connect to the same service from another account you must delete
that file. Do 
the same procedure for the case in which the credentials expire.


## Overview


1. Setup G-Suite credentials  
Configure Google Drive credentials

2. List files in Drive  
List files of Google Drive

3. Download file  
Download file from Drive

4. Export file  
Export a file from Drive to the requested format type

5. Create Folder  
Create Folder

6. Copy or move file  
Copy or move a file

7. Upload file  
Upload a file to Google Drive

8. Delete a file or folder  
Delete a file or folder from Drive

9. Share file  
Share a file in Drive  




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