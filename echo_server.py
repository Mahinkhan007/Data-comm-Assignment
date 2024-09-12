import socket;

s= socket.socket();

hostname = "localhost";
port = 28000;


s.bind((hostname, port));

s.listen();

conn, addr = s.accept();

print(f"Got connection from {addr}")

while True:
    try:
        data = conn.recv(1024);
        print("client: "+data.decode());
        
    except:
        break;
    
    conn.send(data);
    
conn.close();