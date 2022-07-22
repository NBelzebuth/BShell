def error(do = False):
    if do == True:
        print("Un erreur fatale est survenu!")
        exit()   
    else:
        print("Un probleme est survenu dans l'execution de la commande !\nFaite 'help [cmd]' pour plus d'info\n")

import os
import urllib, json
import time
from rich.console import Console

console = Console()

from model._uses_.mathplus import *
from model._uses_.ls import main as ls
from model._uses_.tidy import *
from model.vars import *
from model._uses_.ip import *
from model._uses_.weather import *
from model._uses_.download import *
from model._using_.discord import *
from model._using_.file import *


test_path = os.getcwd().rsplit("\\")
path = os.getcwd()

def on(root, test_path = test_path, path = path, echooff=False, is_on = True, dir = path):

    os.system("start timer.pyw")

    t = time.perf_counter()
    try:
        for i in ["cache", "model"]:
            os.chdir(f"{root}\{i}")
            os.chdir(dir)
    except:
        print("An error has occurred")
        exit()
    t2 = time.perf_counter()
    print(f"Launched in {t2-t}")
    while is_on:

        current_time = time.time()
        with open("cache/loop/infos.P.bshobject.json", "w") as f:
            f.write('{"loop": '+str(current_time)+'}')

        if test_path[len(test_path)-1] == os.getlogin():
            path = "~"
        elif test_path[0] == 'C:':
            for _ in range(3):
                test_path.pop(0)
            path = "~\\"+"\\".join(test_path)
        if echooff == False:
            userInput = input(f"({path}) {os.environ['COMPUTERNAME']}: $ ")
        else: userInput = input()
        t = time.perf_counter()
        try:
            if userInput in ["", " "]:
                first = ""
            else:
                first = userInput.rsplit()[0]
                first = first.lower()
        except: first = ""
        if not first:
            pass
        elif first == "mylocation":
            data = json.loads(urllib.request.urlopen("http://ip.jsontest.com/").read())
            print(ip.locate(data["ip"]))

        elif first == "params":
            os.system("start model\menu.py")

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

        elif first == "myweather":
            my_weather(userInput)

        elif first == "weather":
            weather(userInput)

        elif first == "download":
            userInput = userInput.split()
            download(userInput[1])
        elif first == "using":
            userInput = userInput.split()
            libs = {
                    "discord" : discord_using,
                    "file" : file_using,
                    }
            if userInput[1].lower() in libs:
                libs[userInput[1].lower()](userInput)

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
        t2 = time.perf_counter()
        tt = t2-t
        if tt > 5:
            console.print(f"Responce in [black][bold]{round(tt, 5)}[/][/]")
        elif tt > 0.01:
            console.print(f"Responce in [red][bold]{round(tt, 5)}[/][/]")
        elif tt < 0.001:
            console.print(f"Responce in [green][bold]{round(tt, 5)}[/][/]")
        else:
            console.print(f"Responce in [yellow][bold]{round(tt, 5)}[/][/]")