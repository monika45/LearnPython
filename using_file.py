"""文件"""
from math import sqrt
import json


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




