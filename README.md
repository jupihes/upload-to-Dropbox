# upload-to-Dropbox

Simple python script for Windows to do following for predefined list of files


1. [Daily xcopy your files to specific folder](https://github.com/jupihes/upload-to-Dropbox/blob/master/toDropBox.py)
```
import subprocess
srcs = [r"C:\Users\<username>\Desktop\Document 1.pdf",
       r"C:\Users\<username>\Desktop\Document 2.pdf",
       r"C:\Users\<username>\Desktop\Document 3.txt",
       r"C:\Users\<username>\Desktop\Document 4.xlsx"]
dst = r"D:\...\Xcopy folder\\"

for i in srcs:
    subprocess.call(["xcopy", src, dst,"/s", "/d"])
```
2. [Upload list of files to DropBox](https://github.com/jupihes/upload-to-Dropbox/blob/master/toDropBox.py)
```
import dropbox
# Get your app key and secret from the Dropbox developer website
access_token = '**'

def upload_file(file_from, file_to):
    dbx = dropbox.Dropbox(access_token)
    f = open(file_from, 'rb')
    dbx.files_upload(f.read(), file_to)

# sample list of files to be uploaded
L = ["F:\M\W\SQL sample.sql",
     "E:\R\M\Email list.txt"]

for i in L: # for i in list of files:
    file_from = i  #//local file path
    # i.split('\\')[-1] == file name

    file_to = '/Folder name/' + i.split('\\')[-1]      #// dropbox path
    upload_file(file_from,file_to)
```
  * Upload only if there is a change in files [To be added]
