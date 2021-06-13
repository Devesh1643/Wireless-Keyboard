#Python_With_D
from pyautogui import sleep, typewrite
import socket
s = socket.socket()
host = socket.gethostname()
host = socket.gethostbyname(host)
port = 9999
s.connect((host,port))
while True:
    global data
    data = str(s.recv(1024),encoding='utf-8')
    #print(data)
    
    typewrite(data)
    