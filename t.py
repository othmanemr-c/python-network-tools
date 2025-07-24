import os

# Ask the user for the root folder path
root_path = input("Enter the path of the folder to explore: ")

if not os.path.exists(root_path):
    print(f"The folder {root_path} doesn't exist")
else :
    print(f"The folder {root_path} exists")
    for root, subdirs, files in os.walk(root_path):
        if subdirs :
            print("sub folder " ,subdirs)
        else :
            print("no sub folder")

        if files :
            print("files " ,files)
        else :
            print("no files")

print("End scanning ")

