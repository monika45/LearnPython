"""
上下文管理器,
with expression as viriable:
    with-block
上下文管理协议：
    1.expression计算结果所得对象称为上下文管理器，必须有__enter__和__exit__
    2.__enter__方法被调用，如果as分句存在，其返回值会赋值给as分句中的变量，否则返回值就被直接丢弃
    3.嵌套的with代码块执行
    4.如果with代码块引发异常，__exit__(type,value,traceback)方法就会被调用,它们与sys.exc_info调用返回的三个值相同。如果此方法返回False
        则异常重新引发，如果此方法返回True，异常会终止。一般情况为了把异常传递到with语句外，都是返回False
    5.如果with代码块没有异常，__exit__依然会被调用，type value traceback都传None
"""


class TraceBlock:
    """
    定义上下文管理器
    """
    def __enter__(self):
        print('starting with block')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            print('exited normally')
        else:
            print('raise an exception!' + str(exc_type))
            return False

    def message(self, arg):
        print('running', arg)


if __name__ == '__main__':
    with TraceBlock() as action:
        action.message('test1')
        print('reached')

    with TraceBlock() as action:
        action.message('test2')
        raise TypeError
        print('not reached')
