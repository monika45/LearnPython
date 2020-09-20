"""socket客户端"""
from socket import socket, AF_INET, SOCK_STREAM
import json
from time import time
from base64 import b64decode

def main():
    client = socket(family=AF_INET, type=SOCK_STREAM)
    client.connect(('192.168.42.10', 5566))
    # 定义一个保存二进制数据的对象
    in_data = bytes()
    # 由于不知道服务器发送的数据有多大每次接收1024bytes
    data = client.recv(1024)
    while data:
        in_data += data
        data = client.recv(1024)
    # 解码成字符串,转成字典
    my_dict = json.loads(in_data.decode('utf-8'))
    print('得到文件：', my_dict['filename'])
    with open(f'./res/img/conpon1_copy{time()}.png', 'wb') as f:
        f.write(b64decode(my_dict['filedata'].encode('utf-8')))
    print('图片已保存')


if __name__ == '__main__':
    main()
