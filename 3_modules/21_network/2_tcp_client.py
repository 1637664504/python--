import socket
address = '127.0.0.1'
port = 9999
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((address,port))
while True:
    cmd = input()
    s.send(cmd.encode('utf-8'))
    if cmd == 'exit':
        break
    
s.close()