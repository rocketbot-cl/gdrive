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
if cur_path not in sys.path:
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
    # 'application/pdf': 'application/pdf',
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
        pageSize=1000, spaces="drive", fields="files(id, name, mimeType)", includeItemsFromAllDrives=True,
        supportsAllDrives=True).execute()
    items = results.get('files', [])
    # print('ITEMS',items)
    files = []
    if len(items) > 0:
        for item in items:
            files.append({'name': item['name'], 'id': item['id'], 'mimeType': item['mimeType']})
    #
    SetVar(var, files)

if module == 'DownloadFile':
    try:
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

    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e

if module == 'CreateFolder':
    try:
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

    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e

if module == 'CopyMoveFile':
    try:
        if not creds:
            raise Exception("No hay credenciales ni token válidos, por favor configure sus credenciales")

        var = GetParams('var')
        folder_id = GetParams('folder_id')
        file_id = GetParams('file_id')

        if not folder_id or not file_id:
            raise Exception("No ha ingresado archivo o carpeta")

        option = GetParams('options')

        print(option)

        service = build('drive', 'v3', credentials=creds)
        
        file_to_move = service.files().get(fileId=file_id,
                                           fields='parents, name').execute()
        
        print(file_to_move.get('parents'), file_to_move)
        previous_parents = ",".join(file_to_move.get('parents'))

        print("parents", previous_parents)

        copy = option == "copy"

        parents = folder_id
        if copy:
            file_id = service.files().copy(fileId=file_id).execute()["id"]

        file = service.files().update(fileId=file_id,
                                      removeParents = previous_parents,
                                      addParents = parents,
                                      enforceSingleParent = True,
                                      fields='id, parents, name').execute()

        if copy:
            file = service.files().update(fileId=file_id,
                                          body={
                                              "name": file_to_move["name"]
                                          },
                                          fields='id, name, parents').execute()

        if var:
            SetVar(var, file)


    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e

if module == "UploadFile":
    try:
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
        print("mime type: ", file_mime)
        if file_path.endswith('.csv'):
            file_mime = 'text/csv'
        if file_path.endswith('.xlsx'):
            file_mime = 'application/vnd.ms-excel'

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
    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e

if module == "DeleteFile":
    try:
        if not creds:
            raise Exception("No hay credenciales ni token válidos, por favor configure sus credenciales")
        file_id = GetParams("file_id")
        if not file_id:
            raise Exception("No ha ingresado un ID")
        service = build('drive', 'v3', credentials=creds)
        result = GetParams("result")
        try:
            file = service.files().delete(fileId=file_id).execute()
            SetVar(result, True)
        except Exception as e:
            print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
            PrintException()
            SetVar(result, False)

    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e

if module == "ShareFile":
    try:
        if not creds:
            raise Exception("No hay credenciales ni token válidos, por favor configure sus credenciales")
        file_id = GetParams("file_id")
        if not file_id:
            raise Exception("No ha ingresado un ID")
        service = build('drive', 'v3', credentials=creds)
        result = GetParams("result")
        try:
            service.permissions().create(body={"role": "reader", "type": "anyone"}, fileId=file_id).execute()
            SetVar(result, True)
        except Exception as e:
            print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
            PrintException()
            SetVar(result, False)

    except Exception as e:
        print("\x1B[" + "31;40mAn error occurred\x1B[" + "0m")
        PrintException()
        raise e