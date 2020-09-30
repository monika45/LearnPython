"""文件"""
from math import sqrt
import json
import struct


def read_file():
    f = None
    try:
        f = open('./res/1.txt', 'r', encoding='utf-8')
        print(f.read())
        # for line in f:
        #     print(line)
        # print(f.readlines())
    except Exception:
        print('文件读取错误')
        # 重新引发当前异常
        raise
    finally:
        if f:
            f.close()


def write_file():
    def is_prime(n):
        # 表达式为False时触发AssertionError
        assert n > 0
        for factor in range(2, int(sqrt(n)) + 1):
            if n % factor == 0:
                return False
        return True if n != 1 else False

    filenames = ('./res/a.txt', './res/b.txt', './res/c.txt')
    fs_list = []
    try:
        for filename in filenames:
            fs_list.append(open(filename, 'w', encoding='utf-8'))
        for number in range(1, 10000):
            if is_prime(number):
                if number < 100:
                    fs_list[0].write(str(number) + '\n')
                elif number < 1000:
                    fs_list[1].write(str(number) + '\n')
                else:
                    fs_list[2].write(str(number) + '\n')
    except IOError as ex:
        print(ex)
        print('写文件时发生错误')
    finally:
        for fs in fs_list:
            fs.close()
    print('操作完成')


# write_file()

# 读写二进制文件，下面代码实现了复制图片文件的功能
def binary_file():
    try:
        with open('./res/img/conpon1.png', 'rb') as fs1:
            data = fs1.read()
            print(type(data))
        with open('./res/img/conpon2.png', 'wb') as fs2:
            fs2.write(data)
    except FileNotFoundError as e:
        print('文件不存在')

    except Exception as ea:
        print(ea)
    print('程序执行结束')


# binary_file()


# 读写json文件
def json_file():
    mydict = {
        'name': '骆昊',
        'age': 38,
        'qq': 957658,
        'friends': ['王大锤', '白元芳'],
        'cars': [
            {'brand': 'BYD', 'max_speed': 180},
            {'brand': 'Audi', 'max_speed': 280},
            {'brand': 'Benz', 'max_speed': 320}
        ],
        'is_male': True
    }
    try:
        with open('./res/data.json', 'w', encoding='utf-8') as fs:
            # 将对象序列化到文件中
            json.dump(mydict, fs)
            # 将对象序列化到字符串中
            str1 = json.dumps(mydict)
            print(str1)
            print(mydict)

        fp1 = open('./res/data.json')
        # load 将文件中的json反序列化成对象
        o1 = json.load(fp1)
        print(o1)
        print(type(o1))

        # loads将字符串中的内容反序列化成对象
        o2 = json.loads(str1)
        print(o2)

    except Exception as e:
        print(e)
    print('保存数据完成')


# json_file()


# 二进制字节文件
def binary_bytes_files():
    # create packed binary data, 10 bytes, not objects or text
    packed = struct.pack('>i4sh', 7, b'spam', 8)
    print(packed)
    # 二进制模式写入文件
    file = open('./res/data.bin', 'wb')
    file.write(packed)
    file.close()

    # 读二进制数据
    data = open('./res/data.bin', 'rb').read()
    print(data)
    print(data[4:8])
    print(list(data))
    # unpack into objects
    unpack_data = struct.unpack('>i4sh', data)
    print(unpack_data)


# unicode文本文件: automatically encode on writes and decode on reads
def unicode_text_files():
    # 非ASCII编码的Unicode文本
    s = 'sp\xc4m'
    print(s)
    print(s[2])
    # write/encode UTF-8 text
    file = open('./res/unidata.txt', 'w', encoding='utf-8')
    file.write(s)
    file.close()

    # read/decode UTF-8 text
    text = open('./res/unidata.txt', 'r', encoding='utf-8').read()
    print(text)
    # 4 chars
    print(len(text))
    # 通过二进制模式查看文件中真正存储的内容
    raw = open('./res/unidata.txt', 'rb').read()
    print(raw)
    # really 5 bytes in utf-8
    print(len(raw))

    # 手动编码和解码
    # encode to bytes
    print(text.encode('utf-8'))
    # decode to string
    print(raw.decode('utf-8'))


if __name__ == '__main__':
    unicode_text_files()
