#! /home/aswin/anaconda3/bin/python

import sys
import os
import socket
from datetime import datetime
os.system("toilet -f ivrit 'Port Scanner' | boxes -d cat -a hc -p h8 | lolcat")

#Defining target
if len(sys.argv)==2:
  target=socket.gethostbyname(sys.argv[1]) #Translate hostname to IPv4
else:
  print("Invalid amount of arguments")
  print("Syntax : python3 scanner.py <ip>")

#Banner Section
print("-" * 50)
print("Starting PortScanner")
print("Scanning target "+target)
print("Time started: "+str(datetime.now()))
print("-" * 50)
flag=0
start=int(input("Start range:"))
end=int(input("End range:"))
try:
  for port in range(start,end):
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(3)
    result=s.connect_ex((target,port)) #returns an error indicator
    if result == 0:
      print("Port {} is open".format(port))
      flag=1
    s.close()
  if flag==0:
    print("No open ports found")
  print("PortScanner done")

except KeyboardInterrupt:
  print("\nExiting program.")
  sys.exit()

except socket.gaierror:
  print("Hostname could not be resolved.")
  sys.exit()

except socket.error:
  print("Couldn't connect to server.")
  sys.exit()
