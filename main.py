import socket

sock = socket.socket(2, 2)
sock.bind(("0.0.0.0", 3478))

while True:
    _, addr = sock.recvfrom(65535)
    sock.sendto(str(addr).encode(), addr)
