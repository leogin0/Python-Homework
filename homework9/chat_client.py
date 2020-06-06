import socket


# 创建 socket 对象
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 获取本地主机名
host = socket.gethostname()

# 设置端口号
port = 9999

# 连接服务，指定主机和端口
s.connect((host, port))
while True:
    data = input('客户端:')
    s.send(data.encode('utf-8'))
    # 接收小于 1024 字节的数据

    if data == 'Bey' or data == '拜拜':
        break
    msg = s.recv(1024)
    print (msg.decode('utf-8'))

s.close()



