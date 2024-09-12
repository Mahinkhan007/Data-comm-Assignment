import socket, sys

s = socket.socket();


hostname ="localhost";
port =28000;

s.connect((hostname, port))

while True:
    print("Type your message here: ")
    msg = sys.stdin.readline();
    
    s.send(msg.encode());
    
    reply = s.recv(1024);
    print("server: "+reply.decode());
    
    
s.close();