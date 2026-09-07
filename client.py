import socket
import threading
from datetime import datetime

HOST = "127.0.0.1"
PORT = 5000


def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode("utf-8")

            if not message:
                print("\nServer disconnected.")
                break

            print(f"\n{message}")
            print("You: ", end="", flush=True)

        except ConnectionResetError:
            print("\nConnection closed.")
            break

        except OSError:
            break


def start_client():
    print("=" * 45)
    print("          REAL-TIME CHAT CLIENT")
    print("=" * 45)

    username = input("Enter your username: ").strip()

    if not username:
        username = "Guest"

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        client.connect((HOST, PORT))
    except ConnectionRefusedError:
        print("\nCould not connect to the server.")
        print("Make sure server.py is running first.")
        return

    # Send username to server
    client.send(username.encode("utf-8"))

    print("\nConnected to the chat!")
    print("Type your messages below.")
    print("Type /quit to leave the chat.\n")

    # Start receiving thread
    receive_thread = threading.Thread(
        target=receive_messages,
        args=(client,),
        daemon=True
    )

    receive_thread.start()

    try:
        while True:
            message = input("You: ")

            if not message.strip():
                continue

            client.send(message.encode("utf-8"))

            if message.lower() == "/quit":
                break

    except (KeyboardInterrupt, ConnectionResetError):
        pass

    finally:
        client.close()
        print("\nDisconnected from server.")


if __name__ == "__main__":
    start_client()