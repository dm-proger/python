import socket

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    input_key = input("Give me a key: \n")
    input_data = input("Give me data to encrypt: \n")
    string_to_send = input_key + "|" + input_data
    print(string_to_send)
    # s.sendall(b"%s" % string_to_send)
    s.sendall(string_to_send.encode("utf-8"))
    data = s.recv(1024)

print('Received', repr(data))