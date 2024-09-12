import socket, sys

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM);


hostname ="localhost";
port =28000;



while True:
    print("Type your message here: ")
    msg = sys.stdin.readline().strip();
    
    if not msg:
        print("Empty message, closing client connection");
        break;
    
    s.sendto(msg.encode(), (hostname, port));
    
    reply, server = s.recvfrom(1024);
    print(f"server {server} returned: "+reply.decode());
    
    
s.close();