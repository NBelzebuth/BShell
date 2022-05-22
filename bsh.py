import os

root = "C:\\"

imports = ["geopy", "requests"]

try:
    with open(f"{root}\cache\install.data", "r") as fichier:
        file = fichier.read()
    if file.split("\n")[1] == "geopy" and file.split("\n")[2] == "requests":
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

print("""B.SH is a shell developped by belz.
Type 'help' for more informations
""")

os.system("title BShell")
on(root)