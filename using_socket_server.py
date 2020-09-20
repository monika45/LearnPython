"""
设计一个使用多线程技术处理多个用户请求的服务器，
该服务器会向连接到服务器的客户端发送一张图片
"""
from socket import socket, SOCK_STREAM, AF_INET
from base64 import b64encode
import json
from threading import Thread


def main():
    # 自定义线程类
    class FileTransferHandler(Thread):
        def __init__(self, cclient):
            Thread.__init__(self)
            self.cclient = cclient

        def run(self):
            my_dict = {'filename': filename, 'filedata': data}
            json_str = json.dumps(my_dict)
            # 发送json字符串
            self.cclient.send(json_str.encode('utf-8'))
            self.cclient.close()

    # 1.创建socket对象并指定使用哪种传输服务
    # family=AF_INET - IPv4
    # family=AF_INET6 - IPv6
    # type=SOCK_STREAM - TCP套接字
    # type=SOCK_DGRAM - UDP套接字
    # type=SOCK_RAW - 原始套接字
    server = socket(family=AF_INET, type=SOCK_STREAM)
    # 2.绑定地址和端口,IP要写本机的IP地址
    server.bind(('192.168.42.10', 5566))
    # 3.开启监听 - 监听客户端连接到服务器
    server.listen(512)
    print('服务器启动开始监听...')
    filename = './res/img/conpon1.png'
    with open(filename, 'rb') as f:
        data = b64encode(f.read()).decode('utf-8')
    while True:
        # 4.通过循环接收客户端的连接并作出相应的处理
        # accept方法是一个阻塞方法如果没有客户端连接到服务器代码不会向下执行
        # accept方法返回一个元组其中的第一个元素是客户端对象
        # 第二个元素是连接到服务器的客户端地址（IP+端口）
        client, addr = server.accept()
        print(str(addr) + '连接到了服务器')
        # 启动一个线程来处理请求：发送数据并关闭连接
        FileTransferHandler(client).start()


if __name__ == '__main__':
    main()
