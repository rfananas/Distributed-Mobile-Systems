import socket
# https://realpython.com/python-sockets/

HOST = '127.0.0.1'  # The server's hostname or IP address
PORT = 65432        # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    print(f"TCP/IP Client connecting to '{PORT:d}'...", end="", flush=True)
    s.connect((HOST, PORT))
    print("...connected!")

    fctStr   = input("Fct :")
    fctParam = input("Text:")
    sendText = fctStr + ":" + fctParam
    data = bytes(sendText, 'ascii')

    print("--> ", sendText)
    s.sendall(data)

    data = s.recv(1024)  # 1024 is the maximum size of data in bytes
    strReceived = str(data, 'ascii')
    print("<-- ", strReceived)

print(f"TCP/IP Client closed on '{PORT:d}'!")