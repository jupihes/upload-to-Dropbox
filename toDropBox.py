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
