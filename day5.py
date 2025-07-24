import os

dossier = input("Enter your file path to scan : ")
extension =(".exe",".bat",".vbs",".sh",".js")
fichier_suspect=[]
dossier_sus="/Users/test/Desktop/folder1"
rapport=os.path.join(dossier_sus,"rapport.txt")
total =0
if not os.path.exists(dossier):
    print(f"File {dossier} doesn't exist")

else :
    print(f"Directory {dossier} exists, scanning...")
    for racine ,sous_dossier ,fichiers in os.walk(dossier):
        for fichier in fichiers:
            if fichier.endswith(tuple(extension)):
                    fichier_suspect.append(fichier)
                     # join entre la racine et le fichier
    os.makedirs(dossier_sus,exist_ok=True)   #for checking if the file exist
    with open(rapport,"w") as f:
         for fichier in fichier_suspect:
                    chemin = os.path.join(racine, fichier)
                    total += 1
                    f.write("Fichier suspect : ")
                    f.write(chemin)
                    f.write("\n")
                    print("Fichier suspect : ",chemin)
    print(f"Total des fichier trouvé: {total}")