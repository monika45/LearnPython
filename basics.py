"""
基础知识
"""
import sys


def assignment_operation():
    """
    赋值
    """
    # 基础形式
    spam = 'Spam'
    # 元祖赋值
    spam, ham = 'yum', 'YUM'
    # 列表赋值
    [spam, ham] = ['yum', 'YUM']
    # 推广序列赋值
    a, b, c, d = 'spam'
    # 扩展序列解包
    a, *b = 'spam'
    # 多目标赋值
    spam = ham = 'spam'
    # 增量复制
    a += 10


def usage_of_list():
    """
    使用列表
    :return:
    """
    list1 = [100, 200, 300, 600]
    # print(len(list1))
    # 乘号表示列表元素重复
    # print(list1 * 3)
    # for elem in list1:
    #     print(elem)

    # enumarate生成(k, v)元组
    for index, elem in enumerate(list1):
        print(f'index:{index}, elem:{elem}')

    # 添加元素
    # list1.append(700)
    # list1.insert(2, 333)
    # print(list1)

    # 合并列表
    # list1 += [11, 22]
    # list1.extend([33, 55])
    # print(list1)

    # 判断成员是否在列表中，如果在就删除
    # list1.extend([100, 800])
    # if 100 in list1:
    #     list1.remove(100)

    # 从指定位置删除元素
    # first = list1.pop(0)
    # print(first)
    # print(list1)

    # 清空列表
    # list1.clear()
    # print(list1)

    # 列表切片
    fruits = ['grape', 'apple', 'strawbbery', 'waxbbery']
    fruits += ['pitaya', 'pear']
    print(fruits[1:4])
    print(fruits[:])
    print(fruits[-3:-1])
    # 通过反向切片来获得倒转后的列表
    print(fruits[::-1])

    # sorted函数返回排序后的拷贝，不会修改列表
    print(sorted(fruits))
    print(sorted('asbaedd', reverse=True))
    # key参数提供一个自定义排序函数，如按len排序
    print(sorted(fruits, key=len))

    # 直接在列表上排序（原位置修改）
    print(fruits)
    fruits.sort()
    print(fruits)

    # 列表推导，生成一个新的列表，比for循环快，因为迭代内部用的C
    f = [x for x in range(1, 10)]
    # print(f)
    f = [x + y for x in 'ABCDE' for y in '1234567']
    # print(f)
    f = [x ** 2 for x in range(1, 1000)]
    # 查看对象占用内存的字节数
    print(sys.getsizeof(f))

    # 创建一个生成器对象，通过生成器可以获取数据但它不占用额外的空间存储数据
    # 每次需要数据的时候就通过内部运算得到数据（需要花费额外的时间）
    f2 = (x ** 2 for x in range(1, 1000))
    print(sys.getsizeof(f2))

    # for x in f2:
    #     print(x)

    # 通过yield关键字将一个普通函数改造成生成器函数
    def fib(n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
            yield a

    # for x in fib(20):
    #     print(x)


def usage_of_tuple():
    """
    使用元组（不可变对象）(可迭代)
    :return:
    """
    t = (1, 2, 3)
    for x in t:
        print(x)
    print(list(t))
    print(tuple([1, 2]))


def usage_of_set():
    """
    使用集合
    :return:
    """
    # 不允许重复
    set1 = {1, 2, 3, 3, 3, 2}
    # print(len(set1))
    set2 = set(range(1, 10))
    # print(set2)
    set3 = set((1, 2, 3, 5, 5))
    # print(set3)

    set4 = {x for x in range(1, 10) if x % 2 == 0 or x == 9}
    # print(set4)
    set4.add(10)
    set4.update([11, 12])
    set4.discard(11)
    set4.remove(10)
    set4.add(88)
    set4.pop()
    set4.pop()

    # 交集 并集 差集 对称差运算
    print(set4)
    print(set4.intersection({6, 8, 13}))
    print(set4.union({18, 8, 19}))
    print(set4.difference({6, 8, 19}))
    print(set4.symmetric_difference({6, 8, 77}))
    # 判断子集超集
    print(set4 >= {6, 8})


def usage_of_dict():
    """
    字典
    :return:
    """
    scores = {'a': 78, 'b': 99, 'c': 88}
    items1 = dict(a=1, b=2, c=33)
    # 通过zip将两个序列压成字典
    items2 = dict(zip(('a', 'b', 'c'), [33, 44, 55]))
    # 推导
    items2 = {k: k * 3 for k in 'abc'}
    # print(items2)
    for k in items2:
        print(f'{k}:{items2[k]}')
    items2['a'] = 'sire'
    items2.update({'a': 'dewrew', 'b': 'serwe'})
    print(items2.get('s', 90))
    items2.pop('a')
    items2.popitem()
    print(items2)

if __name__ == '__main__':
    usage_of_dict()
