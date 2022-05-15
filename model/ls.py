from os import listdir as lsdir
from os.path import isfile, join
from pathlib import Path
import os

def error(do = False):
    if do == True:
        print("Un probleme est survenu !")
        exit()   
    else:
        print("Un probleme est survenu !")
    

def main(dir = os.getcwd()):
    
    fichiers = [f for f in lsdir(dir) if isfile(join(dir, f))]
    folder = [f.path for f in os.scandir(dir) if f.is_dir()]
    folders = []

    try:
        for f in os.scandir(dir):
            if f.is_dir():
                folder = "".join(f.path)
                folder = folder.rsplit('\\')
                folder = folder[len(folder)-1]
                folders = folders + folder.rsplit()
    except:
        error(True)

    print(f"Répértoire : {dir} \n\n Fichiers : \n")
    if fichiers != []:
        for i in range(len(fichiers)):
            unite = "o"
            Path(f"{dir}\{fichiers[i]}").stat()
            file_size =Path(f"{dir}\{fichiers[i]}").stat().st_size
            if file_size >= 1000:
                unite = "Ko"
                file_size /= 1000
            if file_size >= 1000:
                unite = "Mo"
                file_size /= 1000
            if file_size >= 1000:
                unite = "Go"
                file_size /= 1000
            print(f"- {fichiers[i]} ({round(file_size, 1)} {unite})")
    else:
        print("Il n'y a aucun fichiers dans le répértoire")

    print("\n Dossiers : \n")

    if folders != []:
        for i in range(len(folders)):
            print("-", folders[i])
    else:
        print("Il n'y a aucun dossiers dans le répértoire\n")

if __name__ == "__main__":
    main()