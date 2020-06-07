import socket
import get
import threading
import os


class ChatSever:

    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr = (get.get_ip(), 10000)
        self.users = {}
        self.names = {}

    def start_sever(self):
        try:
            self.sock.bind(self.addr)
        except Exception as e:
            print(e)
        self.sock.listen(5)
        print("服务器已开启，等待连接...")
        print("在空白处输入stop sever并回车，来关闭服务器")

        self.accept_cont()

    def accept_cont(self):
        while True:
            s, addr = self.sock.accept()
            self.users[addr] = s
            self.names[addr] = s.recv(4096).decode("gbk")
            number = len(self.users)
            print("用户{}连接成功！现在共有{}位用户".format(self.names[addr], number))

            threading.Thread(target=self.recv_send, args=(s, addr)).start()

    def recv_send(self, sock, addr):
        while True:
            try:  # 测试后发现，当用户率先选择退出时，这边就会报ConnectionResetError
                response = sock.recv(4096).decode("gbk")
                msg = "{}  {}：{}".format(get.get_time(), self.names[addr], response)

                for client in self.users.values():
                    client.send(msg.encode("gbk"))
            except ConnectionResetError:
                print("用户{}已经退出聊天！".format(self.names[addr]))
                self.users.pop(addr)
                break

    def close_sever(self):
        for client in self.users.values():
            client.close()
        self.sock.close()
        os._exit(0)


if __name__ == "__main__":
    sever = ChatSever()
    sever.start_sever()
    while True:
        cmd = input()
        if cmd == "stop sever":
            sever.close_sever()
        else:
            print("输入命令无效，请重新输入！")