import socket
import time

UDP_IP = "127.0.0.1"
UDP_PORT = 1000

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
endpoint = (UDP_IP, UDP_PORT)

print("Trimit 3 triggeri catre Unicorn Recorder...")

for code in [1, 2, 3]:
    msg = str(code).encode("ascii")
    sock.sendto(msg, endpoint)
    print(f"Trimis trigger: {code}")
    time.sleep(1.0)

sock.close()
print("Gata.")