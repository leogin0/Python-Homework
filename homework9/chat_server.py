import socket

# 创建 socket 对象
serversocket = socket.socket(
    socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

port = 9999

# 绑定端口号
serversocket.bind((host, port))

# 设置最大连接数，超过后排队
serversocket.listen(5)

while True:
    # 建立客户端连接
    clientsocket, addr = serversocket.accept()

    print("成功连接服务器: %s" % str(addr))
    while True:
        # 对接收到的消息进行解码
        print(clientsocket.recv(1024).decode('utf-8'))

        data = input('服务器:')
        if data == 'bey' or data == '拜拜':
            break
        clientsocket.send(data.encode('utf-8'))
    clientsocket.close()