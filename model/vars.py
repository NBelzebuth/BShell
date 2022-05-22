import os
from datetime import datetime
import random
import os
import platform

from model._uses_.ip import *
from model._uses_.mathplus import *

def vars(userInput, root):
    vars = {
        "shell" : "B.SHell", 
        "username" : os.getlogin(),
        "random" : "randomnumbertodo",
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
        "locate" : "chosenlocation",
        "datetime" : datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 
        "date" : datetime.now().strftime('%Y-%m-%d'),
        "time" : datetime.now().strftime('%H:%M:%S'),
    }

    lowUserInupt = userInput.lower().rsplit()
    userInput = userInput.rsplit()

    for i in range(len(userInput)):
        if list(userInput[i])[0] == "$":
            try:
                word = list(lowUserInupt[i])
                word.pop(0)
                userInput[i] = vars["".join(word)]
            except:
                pass

        if userInput[i] == "chosenlocation":
            userInput[i] = ""
            userInput[i+1] = str(ip.locate(userInput[i+1]))
        elif userInput[i] == "randomnumbertodo":
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
                except:
                    if is_number(userInput[i+1]):
                        userInput[i+1] = str(random.randint(0, int(userInput[i+1])))
                        userInput.pop(1)
                        return " ".join(userInput)
                    else:
                        userInput[i] = str(random.randint(0, 1000000))
            except:
                userInput[i] = str(random.randint(0, 1000000))
 
    return " ".join(userInput)
