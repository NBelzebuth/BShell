import time
import json

while 1:

    with open("cache/loop/infos.P.bshobject.json", 'r') as f:
        loop = json.load(f)

    with open("model/_console_/console.bshobject.json", 'r') as f:
        loop_ops = json.load(f)

    current_time = time.time()
    with open("cache/time.bshobject.json", "w") as f:
        f.write('{"epoch": '+str(current_time)+'}')
        
    if loop["loop"] + int(loop_ops["loop"]["during"]) < current_time:
        exit()
