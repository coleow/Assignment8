import socket

def start_server(host, port):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")

    while True:
        client_socket, client_address = server_socket.accept()
        print(f"Connected to client: {client_address[0]}:{client_address[1]}")

        message = "A message from CS361"

        client_socket.sendall(message.encode())
        client_socket.close()

if __name__ == "__main__":
    host = "localhost"
    port = 1234
    start_server(host, port)