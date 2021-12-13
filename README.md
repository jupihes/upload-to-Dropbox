# upload-to-Dropbox

Simple python script for Windows to do following for predefined list of files


1. Daily xcopy your files to specific folder
```import subprocess
   srcs = [r"C:\Users\<username>\Desktop\Document 1.pdf",
          r"C:\Users\<username>\Desktop\Document 2.pdf",
          r"C:\Users\<username>\Desktop\Document 3.txt",
          r"C:\Users\<username>\Desktop\Document 4.xlsx"]
   dst = r"D:\...\Xcopy folder\\"

   for i in srcs:
       subprocess.call(["xcopy", src, dst,"/s", "/d"])
```
2. Upload list of files to DropBox
  * Upload only if there is a change in files [To be added]
