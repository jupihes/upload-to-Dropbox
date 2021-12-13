import subprocess
srcs = [r"C:\Users\<username>\Desktop\Document 1.pdf",
       r"C:\Users\<username>\Desktop\Document 2.pdf",
       r"C:\Users\<username>\Desktop\Document 3.txt",
       r"C:\Users\<username>\Desktop\Document 4.xlsx"]
dst = r"D:\...\Xcopy folder\\"

for i in srcs:
    subprocess.call(["xcopy", src, dst,"/s", "/d"])
