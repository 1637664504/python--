import socket
import threading

listenAddress = '127.0.0.1'
listenPort = 9999
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((listenAddress,listenPort))
s.listen(5)
print('waitting for connection')

def tcplink(sock,addr):
    print("recv new connect from %s:%s.."%addr)
    sock.send(b'welcomm .')
    while True:
        data=sock.recv(2048)
        if (not data) or (data.decode('utf-8') == 'exit'):
            break
        print("recv: "+data.decode('utf-8'))
    
    sock.close()
    print('disconnect %s:%s' % addr)

while True:
    sock,addr = s.accept()
    t = threading.Thread(target=tcplink,args=(sock,addr))
    t.start()
