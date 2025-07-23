import os
path=input("Enter the path of the log file: ")
dossier="/Users/test/Desktop/folder1"
error=os.path.join(dossier,"error.txt")
warning=os.path.join(dossier,"warning.txt") # joining a path
if not os.path.isfile(path):
       print("file does not exist")
else :
      with open(path,"r") as log_file:
          for line in log_file:
              if "ERROR" in line:
                  open(error,"a").write(line)
                  print(line)
              if "WARNING" in line:
                  print(line)
                  open(warning,"a").write(line)
print("done")
