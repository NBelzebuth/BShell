import os
from datetime import datetime
import random
import os
import platform
import contextlib
import json

from model._uses_.ip import *
from model._uses_.mathplus import *

def vars(userInput, root):
    vars = {
        "shell" : "B.SHell",
        "version" : "3.0.0",
        "username" : os.getlogin(),
        "random" : "]]randomnumber",
        "homedrive" : "",
        "homepath" : "",
        'root' : root,
        "os" : f"{platform.system()}_{os.name} {platform.release()}",
        "os.platform" : platform.system(),
        "os.name" : os.name,
        "os.release" : platform.release(),
        "ip" : ip.local(),
        "publicip" : ip.public(),
        "mylocation" : str(ip.locate(ip.public())),
        "addresslocate" : str(ip.adresslocate(ip.public())),
        "locate" : "]]chosenlocation",
        "datetime" : datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 
        "date" : datetime.now().strftime('%Y-%m-%d'),
        "time" : datetime.now().strftime('%H:%M:%S'),
        "file.read" : "::FROMLIB::file]]read",
    }

    lowUserInupt = userInput.lower().rsplit()
    userInput = userInput.rsplit()

    with open("model\_console_\console.bshobject.json", 'r') as f:
        dat = json.load(f)

    for i in range(len(userInput)):
        if list(userInput[i])[0] == "$":
            with contextlib.suppress(Exception):
                word = list(lowUserInupt[i])
                word.pop(0)
                if dat["vars"]["".join(word)]:
                    userInput[i] = vars["".join(word)]

        if userInput[i] == "]]chosenlocation":
            userInput[i] = ""
            userInput[i+1] = str(ip.locate(userInput[i+1]))
        elif userInput[i] == "]]randomnumber":
            try:
                userInput[i] = ""
                try:
                    if is_number(userInput[i+1]) and is_number(userInput[i+2]):
                        userInput[i+2] = str(random.randint(int(userInput[i+1]), int(userInput[i+2])))
                        userInput[i+1] = ""

                        for _ in range(2):
                            userInput.pop(1)
                        return " ".join(userInput)
                    elif is_number(userInput[i+1]):
                        userInput[i+1] = str(random.randint(0, int(userInput[i+1])))
                        userInput.pop(1)
                        return " ".join(userInput)
                    else:
                        userInput[i] = str(random.randint(0, 1000000))
                except Exception:
                    if is_number(userInput[i+1]):
                        userInput[i+1] = str(random.randint(0, int(userInput[i+1])))
                        userInput.pop(1)
                        return " ".join(userInput)
                    else:
                        userInput[i] = str(random.randint(0, 1000000))
            except Exception:
                userInput[i] = str(random.randint(0, 1000000))
 
    return " ".join(userInput)
