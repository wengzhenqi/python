import socket

server = '192.168.4.254'
port = 12345
addr = (server, port)
c = socket.socket()
c.connect(addr)

while True:
    data = input('(quit to end)> ') + '\r\n'
    c.send(data.encode())
    if data.strip() == 'quit':
        break

    rdata = c.recv(1024)
    print(rdata.decode(), end='')
c.close()