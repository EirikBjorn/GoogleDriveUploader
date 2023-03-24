from pydrive2.auth import GoogleAuth, ServiceAccountCredentials
from pydrive2.drive import GoogleDrive
from subprocess import call
import os
import time

AUTH_FILE = 'auth.json'

# Authenticate with a service account
gauth = GoogleAuth()
scope = ['https://www.googleapis.com/auth/drive']
gauth.credentials = ServiceAccountCredentials.from_json_keyfile_name(AUTH_FILE, scope)
drive = GoogleDrive(gauth)

# Directory to upload from
path = ''

# Delete all files older than 24 hours
for file in os.listdir(path):
  age = os.stat(os.path.join(path, file)).st_mtime
  if age < time.time() - 86400:
    os.remove(os.path.join(path, file))
    print(f'Deleted: {file}')
  else:
    print(f'{file} is too young to be deleted')

# Create, name and upload files to google drive
name = ''
folderID = '' # ID of target folder in Google Drive
i = 1

for file in os.listdir(path):
  newFile = drive.CreateFile({'title': f'{name}-{i}', 'parents': [{'id': folderID}]})
  newFile.SetContentFile(os.path.join(path, file))
  print(f'Starting upload of {file}')
  newFile.Upload()
  call(["node", "notify.js"])
  print(f'{file} has been uploaded to Google Drive as {name}-{i}')
  i+=1
  