def error(do = False):
    if do == True:
        print("Un erreur fatale est survenu!")
        exit()   
    else:
        print("Un probleme est survenu dans l'execution de la commande !\nFaite 'help [cmd]' pour plus d'info\n")

import os
import urllib
import urllib, json
from datetime import datetime
import random
import os

from model._uses_.mathplus import *
from model._uses_.ls import main as ls
from model._uses_.tidy import *
from model.vars import *
from model._uses_.ip import *

test_path = os.getcwd().rsplit("\\")
path = os.getcwd()

def on(root, test_path = test_path, path = path, echooff=False, is_on = True, dir = path):
    # sourcery skip: avoid-builtin-shadow
    try:
        for i in ["cache", "model"]:
            os.chdir(f"{root}\{i}")
            os.chdir(dir)
    except:
        print("Impossible de trouver le dossier cache, veuillez le creer ou l'ajouter au repertoire !")
        exit()
    while is_on:

        if test_path[len(test_path)-1] == os.getlogin():
            path = "~"
        elif test_path[0] == 'C:':
            for _ in range(3):
                test_path.pop(0)
            path = "~\\"+"\\".join(test_path)
        if echooff == False:
            userInput = input(f"({path}) {os.environ['COMPUTERNAME']}: $ ")
        else: userInput = input()
        try:
            if userInput in ["", " "]:
                first = ""
            else:
                first = userInput.rsplit()[0]
                first = first.lower()
            if list(first)[0] == "$":
                userInput = f"echo {userInput}"
            userInput = vars(userInput, root)
        except: first = ""

        if not first:
            pass
        elif first == "mylocation":
            data = json.loads(urllib.request.urlopen("http://ip.jsontest.com/").read())
            print(ip.locate(data["ip"]))

        elif first == "myip":
            print("public IP:", ip.public())
            print("local IP:", ip.local())
        elif first == "exit":
            print("\n-----------------------logout-----------------------\n")
            exit()
        elif first == "tidy":
            tidy(dir)
        elif first == "cmd":
            print("\n----------------------------------------------------\n")
            os.system('cmd')
        elif first == "ps":
            print("\n----------------------------------------------------\n")
            os.system('powershell')
        elif first == "ls":
            ls(dir)
        elif first == "echo":
            ## TODO echo off / on
            userInput = userInput.rsplit()
            userInput.pop(0)
            print(' '.join(userInput))
        elif first in {"clear", "clr"}: 
            os.system('cls' if os.name=='nt' else 'clear')
        elif first == "crypt":
            try:
                userInput = userInput.rsplit()
                userInput.pop(0)
                print(crypt(" ".join(userInput)))
            except Exception:
                error()
        elif first == "decrypt":
            try:
                userInput = userInput.rsplit()
                userInput.pop(0)
                print(decrypt(" ".join(userInput)))
            except Exception:
                error()
        elif first in {"chdir", "cd"}:
            userInput = userInput.rsplit()
            userInput.pop(0)
            if list('\\'.join(userInput))[0] != ".":
                try:
                    os.chdir("".join(userInput))
                except Exception:
                    print(f"Aucun répértoire nommé {''.join(userInput)}")
                else:                    
                    path += "\\"+" ".join(userInput)
                    dir += "\\"+" ".join(userInput)

            elif ''.join(userInput) == "../":
                os.chdir("../")  
                path = dir.rsplit("\\")
                dir = dir.rsplit("\\")
                path.pop()
                dir.pop()
                path = "\\".join(path)
                dir = "\\".join(dir)

        elif first == "kali-linux":
            os.system("C:\WINDOWS\system32\wsl.exe -d kali-linux")
        elif first == "ubuntu":
            os.system("ubuntu.exe")
        elif first == "debian":
            os.system("C:\WINDOWS\system32\wsl.exe -d Debian")

        else:
            ps = 0
            if list(userInput)[1] in ["*", "!", ":", "§"]:
                userInput = list(userInput)
                for _ in range(2):
                    userInput.pop(0)

            elif list(userInput)[1] == "!":
                os.system("powershell "+"".join(userInput))
                ps = 1

            elif list(userInput)[1] == ":":
                exec("".join(userInput))
                ps = 1

            elif list(userInput)[1] == "§":
                os.system(f"ubuntu.exe run {userInput}")

            elif list(userInput)[1] == "/":
                os.system(f"C:\WINDOWS\system32\wsl.exe -d kali-linux {userInput}")

            if ps==0:
                os.system("".join(userInput))