from model._uses_.progress_bar import *

def read_file(userInput):
    pass

def file_using(userInput):
    if userInput[2].lower() in ["crypt", "decrypt"]:
        for _ in range(3):
            userInput.pop(0)
        fcrypt(userInput[0], userInput[1], userInput[2])

def fcrypt(enter, out, key):
    from hashlib import sha256

    keys = sha256(key.encode('utf-8')).digest()

    with open(enter, 'rb') as f_enter:
        with open(out, 'wb') as f_out:

            i = 0
            while f_enter.peek():
                c = ord(f_enter.read(1))
                j = i % len(keys)
                b = bytes([c^keys[j]])
                f_out.write(b)
                i += 1
    print(f"(De)Crypted {enter} to {out} with the key : {key}")

