from os import listdir as lsdir
from os.path import isfile, join
import os

def tidy(dir = os.getcwd()):
    
    sure = input(f"Etes-vous sure de vouloir faire cette action dans {dir} ? [Y/N] : ")
    if sure.lower() == "y":
        fichiers = [f for f in lsdir(dir) if isfile(join(dir, f))]
        ext = []

        if fichiers != []:
            for i in range(len(fichiers)):
                ext = fichiers[i].rsplit(".")
                f = ext[0]
                ext = ext[len(ext)-1]
                if f != "tidy":
                    try:
                        os.mkdir(ext)
                        os.replace(f"{dir}\{fichiers[i]}", f"{dir}\{ext.lower()}\{fichiers[i]}")
                    except:
                        os.replace(f"{dir}\{fichiers[i]}", f"{dir}\{ext.lower()}\{fichiers[i]}")
            print(f"Tout a été rangé dans {dir}")
        else:
            print(f"Il n'y a aucun fichiers dans {dir} !")
    elif sure.lower() == "n":
        print("Action annulée !")
    else:
        print("Un problème est survenu : impossible de lire l'entrée !")