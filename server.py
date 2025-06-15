import socket

HOST='127.0.0.1'
PORT = 12345

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))

server.listen()
print(f'서버가 {HOST}:{PORT}에서 대기중......')

while True:
    client_socket, client_addr = server.accept()
    print('client connected')

    while True:
        data = client_socket.recv(1024)

        if not data:
            print('client disconnected', client_addr)
            break
        print('received data:', data.decode())
        client_socket.sendall(data)
client_socket.close()