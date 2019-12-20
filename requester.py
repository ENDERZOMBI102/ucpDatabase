from requests import *
import json

while 1:
    h = input("inserisci la richiesta da fare.\n")
    if h == "res":
        pass
    else:
        e = ""
        try:
            post("https://3000-d88ea5fe-b7a5-492c-98f3-6ed13dd20a0c.ws-eu01.gitpod.io/Database/create", data=json.dumps(h))
            print(h)
        except (Exception):
            print(e)