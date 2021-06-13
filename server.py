#Python_With_D
import socket
host = ""
port = 9999
s = socket.socket()
try:
    s.bind((host,port))
    print("Listening to The Port "+str(port))
    s.listen(5)
except:
    print("Cant Bind The Port")    

def send_key(conn):
    while True:
        inp = input('Enter: ')
        conn.send(str.encode(inp))

conn ,address = s.accept()
print(f"Connection Established To IP {address[0]} with The Port {address[1]}")
while True:
    send_key(conn)
    conn.close()

