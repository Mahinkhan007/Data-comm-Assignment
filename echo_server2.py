import socket;

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


hostname = "localhost";
port = 28000;



s.bind((hostname, port));

print(f"UDP server started on {hostname}:{port}")



while True:
    try:
        data , addr = s.recvfrom(1024);
        print("client said: "+data.decode());
        s.sendto(data, addr);
    except Exception as e:
        print(f"Error: {e}")
        break
    
   
    
s.close();