import os
from os.path import *
import json

root = os.getcwd()

imports = ["geopy", "requests", "pytube"]

try:
    with open(f"{root}\cache\install.data", "r") as fichier:
        file = fichier.read()
    if file.split("\n")[1] == "geopy" and file.split("\n")[2] == "requests" and file.split("\n")[3] == "pytube":
        pass
    else:
        os.system(f"echo .>{root}\cache\install.data")
        for i in imports:
            os.system(f'python -m pip install {i}')
            os.system(f"echo {i}>>{root}\cache\install.data")
        os.system('cls' if os.name=='nt' else 'clear')
except:
    os.system(f"echo .>{root}\cache\install.data")
    for i in imports:
        os.system(f'python -m pip install {i}')
        os.system(f"echo {i}>>{root}\cache\install.data")
    os.system('cls' if os.name=='nt' else 'clear')

from model.Tests import on

print("""B.SH is a shell developped by belz. Powered by python 3.8
Type 'help' for more informations
""")

with open("model\_console_\console.bshobject.json", 'r') as f:
    dat = json.load(f)

os.system("title " + dat["bsh"]["title"])
on(root)