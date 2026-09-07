# 💬 Real-Time Chat Application

## 🚀 Project Overview

This project is a **Real-Time Chat Application** developed using Python.

The application uses **TCP socket programming** to establish communication between a server and multiple clients.

The server manages connected clients and broadcasts messages between them. Multithreading is used to allow multiple clients to communicate simultaneously.

The project consists of two main Python files:

* `server.py`
* `client.py`

The client establishes a TCP connection with the server and sends messages, while the server receives, processes, and broadcasts messages to connected clients.

---

## 🎯 Project Objectives

The main objectives of this project are:

* Establish client-server communication.
* Implement TCP socket programming.
* Allow multiple clients to connect.
* Send messages between clients.
* Broadcast messages to connected users.
* Display usernames.
* Add timestamps to messages.
* Handle client connections and disconnections.
* Use multithreading for simultaneous communication.
* Provide a simple real-time chat system.

---

## 🛠️ Technologies & Tools

### Programming Language

* Python

### Python Modules

* `socket`
* `threading`
* `datetime`

The application uses Python's built-in modules, so no external packages are required.

### Communication Protocol

* TCP/IP

### Platform

* VS Code
* Windows
* Command Prompt / PowerShell

---

## 🏗️ System Architecture

```text
                ┌─────────────────┐
                │     SERVER      │
                │    server.py    │
                │   Port: 5000    │
                └────────┬────────┘
                         │
              ┌──────────┼──────────┐
              │          │          │
              ↓          ↓          ↓
        ┌──────────┐ ┌──────────┐ ┌──────────┐
        │ Client 1 │ │ Client 2 │ │ Client 3 │
        │ client.py│ │ client.py│ │ client.py│
        └──────────┘ └──────────┘ └──────────┘
```

---

## 🔄 Application Workflow

```text
Start Server
     ↓
Listen for Connections
     ↓
Client Connects
     ↓
Enter Username
     ↓
Register Client
     ↓
Send / Receive Messages
     ↓
Broadcast Messages
     ↓
Client Sends /quit
     ↓
Disconnect Client
     ↓
Continue Server
```

---

## 🖥️ Server

The server creates a TCP socket and listens for incoming client connections.

The server uses:

```python
HOST = "127.0.0.1"
PORT = 5000
```

The server maintains connected clients and uses separate threads to handle client communication.

---

## 💻 Client

The client connects to the server using the configured host and port.

The client asks the user for a username and then allows the user to send messages.

A separate receiving thread allows incoming messages to be displayed while the user continues typing.

---

## 🕐 Message Handling

Messages are displayed with timestamps and usernames.

Example:

```text
[20:30] Saaketh: Hello
[20:31] User2: Hi!
```

The server also displays system messages when users join or leave the chat.

---

## 📁 Project Structure

```text
Real-Time-Chat/
│
├── 📄 server.py
├── 📄 client.py
├── 📄 requirements.txt
└── 📖 README.md
```

---

## 📦 Requirements

No external Python packages are required.

```txt
# No external packages required
```

The application uses Python's built-in `socket`, `threading`, and `datetime` modules.

---

## ▶️ How to Run the Project

### Step 1: Install Python

Check Python installation:

```bash
python --version
```

### Step 2: Open the Project

Open the project folder in VS Code.

### Step 3: Start the Server

Open a terminal and run:

```bash
python server.py
```

The server will start listening on:

```text
127.0.0.1:5000
```

### Step 4: Start the Client

Open another terminal:

```bash
python client.py
```

Enter a username when prompted.

### Step 5: Connect Multiple Clients

Open additional terminals and run:

```bash
python client.py
```

Each client can enter a different username and communicate through the server.

### Step 6: Exit the Chat

Type:

```text
/quit
```

to leave the chat.

---

## 💡 Skills Demonstrated

This project demonstrates practical knowledge of:

* Python Programming
* Socket Programming
* TCP/IP Communication
* Client-Server Architecture
* Multithreading
* Network Communication
* Message Broadcasting
* Exception Handling
* Connection Management
* Real-Time Communication

---

## 🚀 Future Improvements

The project can be extended with:

* Graphical User Interface.
* User authentication.
* Private messaging.
* Group chat rooms.
* File sharing.
* Message history.
* Database integration.
* Online/offline user status.
* End-to-end encryption.
* Web-based chat interface.

---

👩‍💻 GitHub Profile
Annreddy Saaketh Reddy 
B.Tech Student |Python pragramming & Data Analytics Enthusiast

📬 Connect With Me

GitHub 
https://github.com/asreddy2209-arch

LinkedIn
https://www.linkedin.com/in/saaketh-reddy-annreddy-22434937b/

---

## 📜 License

This project is intended for **educational and portfolio purposes**.

---

## 🙏 Thank You

Thank you for visiting this project!

**Made with ❤️ using Python, Socket Programming & Multithreading.**
