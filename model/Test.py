def error(do = False):
    if do == True:
        print("Un erreur fatale est survenu!")
        exit()   
    else:
        print("Un probleme est survenu dans l'execution de la commande !\nFaite 'help [cmd]' pour plus d'info\n")

import os
from datetime import datetime
import random
from model.mathplus import *
from model.ls import main as ls
from model.tidy import *
from model.vars import *

def on(test_path = os.getcwd().rsplit("\\"), path = os.getcwd(), echooff=False, is_on = True, dir = os.getcwd()):
    shell = "B.SH"
    """try:
        os.chdir("cache")
    except:
        print("Impossible de trouver le dossier cache, veuillez le creer ou l'ajouter au repertoire !")
        exit()
    else: os.chdir("../")"""
    while is_on:

        if test_path[len(test_path)-1] == os.getlogin():
            path = "~"
        elif test_path[0] == 'C:':
            for i in range(3):
                test_path.pop(0)
            path = "~\\"+"\\".join(test_path)
        if echooff == False:
            userInput = input(f"({path}) {os.environ['COMPUTERNAME']}: $ ")
        else: userInput = input()

        if userInput == "" or userInput == " ":
            first = ""
        else:
            first = userInput.rsplit()[0]
            first = first.lower()

        ### TODO : VARIABLES ###

        vars = {
            "shell" : "bshell", 
            "username" : os.getlogin(),
            "random" : random.randint(0, 100000),
            "homedrive" : "",
            "homepath" : "",
            "os" : "",
            "datetime" : datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 
            "date" : datetime.now().strftime('%Y-%m-%d'),
            "time" : datetime.now().strftime('%H:%M:%S'),
        }


        if first == "":
            pass
        elif first == "mylocation":
            import socket
            import requests
            import urllib
            from functools import partial
            os.system('@echo off\npy -m pip install geopy')
            from geopy.geocoders import Nominatim

            geolocator = Nominatim(user_agent="my-app")
            geocode = partial(geolocator.geocode, language="fr")

            ip = '81.66.81.20'
            response = requests.get(f"https://geolocation-db.com/json/{ip}&position=true").json()

            geolocator = Nominatim(user_agent="my-app")
            location = geolocator.reverse(str(response["latitude"])+","+str(response['longitude']))

            print(geocode(location.raw["address"]['county']))
        elif first == "exit":
            print("\n----------------------------------------------------\n")
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
            try:
                userInput = userInput.rsplit()
                userInput.pop(0)
                if userInput[0] != "off" and userInput[0] != "on":
                    print(" ".join(userInput))
                    if echooff == False:
                        print()
                elif userInput[0] == "off":
                    echooff = True
                else:
                    echooff = False
            except:
                error()
        elif first == "clear" or first == "clr": 
            os.system('cls' if os.name=='nt' else 'clear')
        elif first == "crypt":
            try:
                userInput = userInput.rsplit()
                userInput.pop(0)
                print(crypt(" ".join(userInput)))
            except:
                error()
        elif first == "decrypt":
            try:
                userInput = userInput.rsplit()
                userInput.pop(0)
                print(decrypt(" ".join(userInput)))
            except:
                error()
        elif first == "cd" or first == "chdir":
            userInput = userInput.rsplit()
            userInput.pop(0)
            if list('\\'.join(userInput))[0] != ".":
                try:
                    os.chdir("".join(userInput))
                except:
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

        else:
            if list(userInput)[1] == "*":
                userInput = list(userInput)
                for i in range(2):
                    userInput.pop(0)
                    
            os.system("".join(userInput))