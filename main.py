from pydrive2.drive import GoogleDrive
from pydrive2.auth import GoogleAuth
from datetime import date
import os
import time

gauth = GoogleAuth()

# Try to load saved client credentials
gauth.LoadCredentialsFile("mycreds.txt")
if gauth.credentials is None:
    # Fix refresh error by forcing offline
    gauth.GetFlow()
    gauth.flow.params.update({'access_type': 'offline'})
    gauth.flow.params.update({'approval_prompt': 'force'})
    # Authenticate if they're not there
    gauth.LocalWebserverAuth()
elif gauth.access_token_expired:
    # Refresh them if expired
    gauth.Refresh()
else:
    # Initialize the saved creds
    gauth.Authorize()
# Save the current credentials to a file
gauth.SaveCredentialsFile("mycreds.txt")

drive = GoogleDrive(gauth)

path = r"/home/pi/Documents/vods/vid"
i = 1
for file in os.listdir(path):
  newFile = drive.CreateFile({'title': f"{date.today()}--wubby-{i}", 'parents': [{'id': '1n1eeqQH4mr1J_gv_-d_cp1sqAj0nYNl_'}]})
  newFile.SetContentFile(os.path.join(path, file))
  newFile.Upload()
  print(f" {file} has been uploaded to Google Drive")
  i+=1
  f = None
  
for file in os.listdir(path):
  age = os.stat(os.path.join(path, file)).st_mtime
  if age < time.time() - 86400:
    print(f" Deleted: {file}")
    os.remove(os.path.join(path, file))
  else:
    print(f" {file} is too young to be deleted")
