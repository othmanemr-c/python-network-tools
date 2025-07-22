import os
import shutil

path_u = input("Enter the source path: ")
backup = "/Users/test/Desktop/backup"
backup_path = os.path.join(backup,"text_files_backup")

if not os.path.exists(path_u):
    print("Source path does not exist.")
else:
    # Create backup and subfolder if they don't exist
    if not os.path.exists(backup):
        os.makedirs(backup)
    if not os.path.exists(backup_path):
        os.makedirs(backup_path)
        print(f"Backup folder created: {backup_path}")

    for filename in os.listdir(path_u):
        if filename.endswith(".txt"):
            source_file = os.path.join(path_u, filename)
            destination_file = os.path.join(backup_path, filename)
            shutil.copy2(source_file, destination_file)
            print("Copied:", filename)

    print("All .txt files have been copied to the backup folder.")
