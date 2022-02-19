import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
server_address = ('localhost', 65432)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(1024)
            print('received {!r}'.format(data))
            if data:
                temp_string = data.decode("utf-8")
                key, data_string = data.split("|", 1)

                alphabet = "abcdefghijklmnopqrstuvwxyz1234567890"
                new_key = int(key) % len(alphabet)

                for char in data_string:
                    new_list = [alphabet[alphabet.find(char) + new_key] for char in data_string]
                    last_data = "".join(new_list)
                    print(last_data)

                    print("sending data back to the client")

                    connection.sendall(data.upper())
            else:
                print('no data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()