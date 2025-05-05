import socket
import ssl

SERVER_IP = "10.30.200.123"
SERVER_PORT = 5000
CERT_FILE = 'server.crt'  # Path to the server's SSL certificate

def connect_to_server():
    """Connects to the server and interacts with it."""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        # Create SSL context for the client and verify server's certificate
        context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)
        context.load_verify_locations(CERT_FILE)
        print("SSL Certificate Verified successfully.")

        # Wrap the client socket with SSL encryption
        client_socket = context.wrap_socket(client_socket, server_hostname=SERVER_IP)

        client_socket.connect((SERVER_IP, SERVER_PORT))

        while True:
            # Receive song list or final message
            data = client_socket.recv(4096).decode()
            print(data)

            if "No songs available" in data or "Goodbye" in data:
                break

            # User selects song or exits
            choice = input("Your choice: ").strip()
            client_socket.sendall(choice.encode())

            if choice.lower() == "exit":
                goodbye = client_socket.recv(1024).decode()
                print(goodbye)
                break

            # Receive confirmation or error
            response = client_socket.recv(1024).decode()
            print(response)

            if "Invalid" in response or "Error" in response:
                continue

            # Receive command instructions
            response = client_socket.recv(1024).decode()
            print(response)

            # Music control loop
            while True:
                command = input("Command (pause/resume/stop): ").strip().lower()
                client_socket.sendall(command.encode())
                response = client_socket.recv(1024).decode()
                print(response)

                if "Stopped" in response or "Song finished" in response or "Error" in response:
                    break

if __name__ == "__main__":
    connect_to_server()
