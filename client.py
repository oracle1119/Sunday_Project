import socket

HOST='127.0.0.1'
PORT=12345

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))
print(f'{HOST}:{PORT} sever connected')

while True:
    message=input('메세지입력(종료시 exit):')

    if message=='':
        continue
    if message=='exit':
        break

    client_socket.sendall(message.encode())
    data = client_socket.recv(1024)
    print('서버응답:', data.decode())

client_socket.close()