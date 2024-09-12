import socket, sys

s = socket.socket();


hostname ="tcpbin.net";
port =58631;

s.connect((hostname, port))

while True:
    msg = sys.stdin.readline();
    
    s.send(msg.encode());
    
    
s.close();