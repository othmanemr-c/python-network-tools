import os
import shutil
import time
from time import strftime

file=input("Enter the source folder : ")
backup=input("Enter the backup folder : ")
if not os.path.exists(file) :
    print("The source folder doesn't exist")
else :
    if os.path.exists(backup):
      print("The backup folder already exist")
    else:
      shutil.copytree(file,backup)
      print("The source folder has been copied to your destination folder")
time_s=strftime("%Y-%m-%d %H:%M:%S", time.localtime())
backup_time=backup+" "+time_s
shutil.copytree(file,backup_time)
print(backup_time)
