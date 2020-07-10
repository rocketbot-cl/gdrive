# coding: utf-8
"""
Base para desarrollo de modulos externos.
Para obtener el modulo/Funcion que se esta llamando:
     GetParams("module")

Para obtener las variables enviadas desde formulario/comando Rocketbot:
    var = GetParams(variable)
    Las "variable" se define en forms del archivo package.json

Para modificar la variable de Rocketbot:
    SetVar(Variable_Rocketbot, "dato")

Para obtener una variable de Rocketbot:
    var = GetVar(Variable_Rocketbot)

Para obtener la Opcion seleccionada:
    opcion = GetParams("option")


Para instalar librerias se debe ingresar por terminal a la carpeta "libs"
    
    pip install <package> -t .

"""
from __future__ import print_function

import os.path
import pickle

base_path = tmp_global_obj["basepath"]
cur_path = base_path + 'modules' + os.sep + 'gdrive' + os.sep + 'libs' + os.sep
sys.path.append(cur_path)

from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

import magic
from googleapiclient.http import MediaFileUpload
import io

"""
    Obtengo el modulo que fueron invocados
"""
module = GetParams("module")

# creds = None
global creds

mimes = {
    'application/vnd.google-apps.spreadsheet': 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
    'application/vnd.google-apps.document': 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
    #'application/pdf': 'application/pdf',
    'application/vnd.google-apps.presentation': 'application/vnd.openxmlformats-officedocument.presentationml.presentation'
}

if module == "GoogleSuite":
    cred = None
    # global creds
    credential_path = GetParams("credentials_path")
    print(credential_path)
    if not os.path.exists(credential_path):
        raise Exception("El archivo de credenciales no existe en la ruta especificada")

    SCOPES = [
        'https://www.googleapis.com/auth/drive',
        'https://www.googleapis.com/auth/spreadsheets'
    ]

    if os.path.exists('token_drive.pickle'):
        with open('token_drive.pickle', 'rb') as token:
            cred = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
    if not cred or not cred.valid:
        if cred and cred.expired and cred.refresh_token:
            cred.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                credential_path, SCOPES)
            cred = flow.run_local_server()
        # Save the credentials for the next run
        with open('token_drive.pickle', 'wb') as token:
            pickle.dump(cred, token)

    # global creds
    creds = cred
    print(creds)

if module == "ListFiles":
    # print('CREDS',creds)
    # global creds
    if not creds:
        raise Exception("No hay credenciales ni token válidos, por favor configure sus credenciales")

    var = GetParams('var_file_list')
    filter_ = GetParams("filter")

    service = build('drive', 'v3', credentials=creds)

    results = service.files().list(
        q=filter_,
        pageSize=1000, spaces="drive", fields="files(id, name, mimeType)", includeItemsFromAllDrives=True, supportsAllDrives=True).execute()
    items = results.get('files', [])
    # print('ITEMS',items)
    files = []
    if len(items) > 0:
        for item in items:
            files.append({'name': item['name'], 'id': item['id'], 'mimeType': item['mimeType']})
    #
    SetVar(var, files)

if module == 'DownloadFile':
    if not creds:
        raise Exception("No hay credenciales ni token válidos, por favor configure sus credenciales")

    drive_id = GetParams('drive_id')
    if not drive_id:
        raise Exception("ID de archivo no enviado")

    file_path = GetParams('path_to_file')
    if not file_path:
        raise Exception("No se ingreso ruta donde guardar el archivo")

    service = build('drive', 'v3', credentials=creds)
    file = service.files().get(fileId=drive_id).execute()
    request = None
    if file['mimeType'] in mimes:
        request = service.files().export_media(fileId=drive_id, mimeType=mimes[file['mimeType']])
    else:
        request = service.files().get_media(fileId=drive_id)
    fh = io.BytesIO()
    downloader = MediaIoBaseDownload(fh, request)
    # downloader = MediaIoBaseDownload(fh, request)
    done = False
    while done is False:
        status, done = downloader.next_chunk()
        print("Download %d%%." % int(status.progress() * 100))

    with io.open(file_path + os.sep + file['name'], 'wb') as out:
        fh.seek(0)
        out.write(fh.read())

if module == 'CreateFolder':
    if not creds:
        raise Exception("No hay credenciales ni token válidos, por favor configure sus credenciales")

    var = GetParams('var')
    folder_name = GetParams('folder_name')
    parent_id = GetParams('parent_id')

    body = {
        'name': folder_name,
        'mimeType': "application/vnd.google-apps.folder"
    }
    if parent_id:
        body['parents'] = [parent_id]

    service = build('drive', 'v3', credentials=creds)
    root_folder = service.files().create(body=body).execute()

    if var:
        SetVar(var, root_folder)

    print(root_folder)

if module == 'CopyMoveFile':
    if not creds:
        raise Exception("No hay credenciales ni token válidos, por favor configure sus credenciales")

    var = GetParams('var')
    folder_id = GetParams('folder_id')
    file_id = GetParams('file_id')

    if not folder_id or not file_id:
        raise Exception("No ha ingresado archivo o carpeta")

    option = GetParams('option')

    print(option)

    service = build('drive', 'v3', credentials=creds)
    file = service.files().get(fileId=file_id,
                               fields='parents').execute()
    previous_parents = ",".join(file.get('parents'))

    print(previous_parents)

    copy = option == "Copiar" or option == "Copy"

    if copy:
        previous_parents = ''

    file = service.files().update(fileId=file_id,
                                  addParents=folder_id,
                                  removeParents=previous_parents,
                                  fields='id, parents').execute()

    if var:
        SetVar(var, file)

    print(file)

if module == "UploadFile":
    if not creds:
        raise Exception("No hay credenciales ni token válidos, por favor configure sus credenciales")

    file_path = GetParams("file_path")

    if not file_path:
        raise Exception("No ha ingresado una ruta")

    if not os.path.exists(file_path):
        raise Exception("Archivo ingresado no existe")

    new_name = GetParams("new_name")
    folder = GetParams("folder")
    var = GetParams("var")

    service = build('drive', 'v3', credentials=creds)



    file_mime = magic.from_file(file_path, mime=True)
    if file_path.endswith('.csv'):
        file_mime = 'text/csv'

    name = new_name or os.path.basename(file_path)

    file_metadata = {'name': name}
    media = MediaFileUpload(file_path,
                            mimetype=file_mime)

    if folder:
        file_metadata['parents'] = [folder]

    file = service.files().create(body=file_metadata,
                                  media_body=media,
                                  fields='id').execute()
    if var:
        SetVar(var, file)

    print(file)

# if module == 'Search':
#     var = GetParams("var")
#     service = build('drive', 'v3', credentials=creds)
#     page_token = None
#     while True:
#         response = service.files().list(q="name contains '{}'".format(var),
#                                         spaces='drive',
#                                         fields='nextPageToken, files(id, name)',
#                                         pageToken=page_token).execute()
#         for file in response.get('files', []):
#             # Process change
#             print('Found file: %s (%s)' % (file.get('name'), file.get('id')))
#         page_token = response.get('nextPageToken', None)
#         if page_token is None:
#             break


"""{
      "en": {
        "title": "Search file or folder",
        "description": "Description",
        "title_options": "Copy or move",
        "options": null
      },
      "es": {
        "title": "Buscar archivo o carpeta",
        "description": "Descripcion",
        "title_options": "Copiar o mover",
        "options": null
      },
      "cn": {
        "title": "列出驅動器中的文件",
        "description": "Description",
        "title_options": "选择选项",
        "options": null
      },
      "form": {
        "css": "modal-lg",
        "inputs": [
          {
            "type": "input",
            "placeholder": {
              "es": "Ruta",
              "en": "Path",
              "cn": "Path"
            },
            "title": {
              "es": "Ruta del archivo",
              "en": "File path",
              "cn": "File path"
            },
            "id": "file_path",
            "css": "col-md-12"
          },
          {
            "type": "input",
            "placeholder": {
              "es": "Ruta",
              "en": "Path",
              "cn": "Path"
            },
            "title": {
              "es": "Nombre nuevo (opcional)",
              "en": "New name (optional)",
              "cn": "new name (optional)"
            },
            "id": "new_name",
            "css": "col-md-12"
          },
          {
            "type": "input",
            "placeholder": {
              "es": "Ruta",
              "en": "Path",
              "cn": "Path"
            },
            "title": {
              "es": "Guardar en carpeta - ID (opcional)",
              "en": "File path",
              "cn": "File path"
            },
            "id": "folder",
            "css": "col-md-12"
          },
          {
            "type": "input",
            "placeholder": {
              "es": "Ruta",
              "en": "Path",
              "cn": "Path"
            },
            "title": {
              "es": "Guardar en variable",
              "en": "File path",
              "cn": "File path"
            },
            "id": "var",
            "css": "col-md-12"
          }
        ]
      },
      "video_youtube": "aMV6cXPMMSo",
      "icon": "data:image/png;base64,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",
      "module": "Search",
      "module_name": "gdrive",
      "visible": true,
      "options": false,
      "father": "module",
      "group": "scripts",
      "linux": true,
      "windows":true,
      "mac":true,
      "docker":true
    }"""