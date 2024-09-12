import socket
import sys

def udp_client(server_host='localhost', server_port=28000):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        msg = input("Type your message here: ").strip()  # Read input and remove trailing newline
        if not msg:
            print("Empty message, closing client connection")
            break

        client_socket.sendto(msg.encode(), (server_host, server_port))

        reply, server = client_socket.recvfrom(1024)
        print(f"Server {server} returned: {reply.decode()}")

   
    client_socket.close()

# Example 
if __name__ == "__main__":
    udp_client()
