# Local Chat Application

## Description

This is a local network chat application that allows real-time communication between multiple clients connected to a single server. The server hosts the connections, receiving messages from each client and broadcasting them to all other connected clients, creating a group chat environment.

## Project Structure

- **Server (`Servidor.py`)**: Manages connections for multiple clients, receiving messages from each client and broadcasting them to others. It also manages the addition and removal of clients.
- **Client (`Cliente.py`)**: Connects to the server, enabling the user to send and receive messages in the chat. Each message is sent with a timestamp and the client’s username, identifying the sender and time of each message.

## Features

- **IP Validation**: Both server and client files validate the server IP address before establishing a connection.
- **Message Broadcasting**: Messages sent by one client are broadcast by the server to all other connected clients.
- **Timestamp and User Identification**: Client messages include a timestamp and username, helping identify the sender and when the message was sent.
- **Connection Management**: The server maintains a list of connected clients and removes any clients that disconnect.

## Setup and Execution

1. **Server**:
   - Run the `Servidor.py` file, providing the server IP and port.
   - The server will start listening for client connections and broadcast messages.

2. **Client**:
   - Run the `Cliente.py` file.
   - Enter the server IP and port to connect.
   - Once connected, the client is ready to send and receive messages in the chat.

## Requirements

- **Python 3.x**
- Libraries: `socket`, `threading`, `ipaddress`, `datetime`, `customtkinter` (all are standard Python libraries, except `customtkinter`)
- There's no need to install any library if you are using the executable file (`*.exe`)

## Usage

1. Start the server on one machine:
```
   python Servidor.py
```
2. In a separate terminal, run a client:
```
    python Cliente.py
```
3. Enter the server IP and port when prompted.

4. Send messages from one client, and they will appear on all other connected clients.