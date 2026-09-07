import socket
import threading
from datetime import datetime

HOST = "127.0.0.1"
PORT = 5000

clients = {}
lock = threading.Lock()


def timestamp():
    return datetime.now().strftime("%H:%M")


def broadcast(message, sender=None):
    with lock:
        for client in list(clients):
            if client != sender:
                try:
                    client.send(message.encode("utf-8"))
                except:
                    client.close()
                    clients.pop(client, None)


def handle_client(client_socket, address):
    print(f"[CONNECTED] {address}")

    try:
        # Receive username
        username = client_socket.recv(1024).decode("utf-8").strip()

        if not username:
            username = f"User-{address[1]}"

        with lock:
            clients[client_socket] = username

        join_message = f"[{timestamp()}] SYSTEM: {username} joined the chat."
        print(join_message)
        broadcast(join_message, client_socket)

        while True:
            data = client_socket.recv(1024)

            if not data:
                break

            message = data.decode("utf-8").strip()

            if message.lower() == "/quit":
                break

            formatted_message = f"[{timestamp()}] {username}: {message}"

            print(formatted_message)
            broadcast(formatted_message, client_socket)

    except ConnectionResetError:
        pass

    finally:
        with lock:
            username = clients.pop(client_socket, "Unknown")

        client_socket.close()

        leave_message = f"[{timestamp()}] SYSTEM: {username} left the chat."

        print(leave_message)
        broadcast(leave_message)


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server.bind((HOST, PORT))
    server.listen(2)

    print("=" * 45)
    print("      REAL-TIME CHAT SERVER")
    print("=" * 45)
    print(f"Server running on {HOST}:{PORT}")
    print("Waiting for clients...")
    print("Press CTRL+C to stop the server.")
    print()

    try:
        while True:
            client_socket, address = server.accept()

            thread = threading.Thread(
                target=handle_client,
                args=(client_socket, address),
                daemon=True
            )

            thread.start()

    except KeyboardInterrupt:
        print("\nServer stopped.")

    finally:
        server.close()


if __name__ == "__main__":
    start_server()