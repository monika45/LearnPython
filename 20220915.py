def mutable_object_as_param_test():
    """
    可变对象作为参数传递测试：在函数里改变可变对象，会在外面看到改变，类似传引用/指针
    """
    a = [1, 2, 3]

    # 参数arr是可变对象，改变arr会改变原来的对象
    def increment(arr):
        arr[0] += 1

    print(a)  # 原来的a
    increment(a)
    print(a)  # a 在函数里被改变了，打印新的a


# mutable_object_as_param_test()
spam = 's'


def scope_test():
    """
    作用域测试：

    """

    def do_local():
        """
        局部赋值不会影响对spam的绑定
        """
        spam = "a"  # local的spam，不影响外面的
        obj[0] = 5  # 索引外面的obj

    def do_nonlocal():
        """
        nonlocal赋值会改变对spam的绑定
        """
        nonlocal spam
        spam = 'c'  # 外面的spam

    def do_global():
        """
        global赋值会改变模块层级的绑定
        """
        global spam  # 生命spam是全局的，只读
        print(spam)  # s
        spam = "d"  # 新创建一个本地的，不影响外面的
        print(f'函数内的spam:{spam}')  # 本地的：d

    spam = "b"
    obj = [1, 2, 3]

    print(obj)
    do_local()
    print(obj)

    print(spam)
    do_nonlocal()
    print(spam)  # spam已经改成c了

    do_global()
    print(spam)
    spam = 'e'
    print(spam)


scope_test()
