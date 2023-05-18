import socket

def start_client(host, port):
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))

    received_message = client_socket.recv(1024).decode()
    print(f"Received message: {received_message}")

    client_socket.close()

if __name__ == "__main__":
    host = "localhost"
    port = 1234
    start_client(host, port)
