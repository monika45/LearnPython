"""
进程和线程
multiprocessing package:https://docs.python.org/3/library/multiprocessing.html

"""
from random import randint
from time import time, sleep
from multiprocessing import Process, Queue, Pool, Pipe, Lock, Value, Array, Manager, TimeoutError
import os
from os import getpid
import threading
import tkinter
import tkinter.messagebox


def fake_task(task_name):
    print(f'task {task_name} start...')
    sec = randint(4, 10)
    sleep(sec)
    print(f'task {task_name} completed.spend {sec} seconds.')


def do_tasks():
    """
    不使用多进程，
    一个任务执行完后才会继续执行下一个任务
    """
    start = time()
    fake_task('t_1')
    fake_task('t_2')
    end = time()
    print('totally spend %.2f seconds' % (end - start))


# do_tasks()

"""
使用多进程的方式将两个任务放到不同的进程中
:return:
"""


def fake_task2(task_name):
    print('启动一个进程，pid:%d' % getpid())
    print('task %s start' % task_name)
    secs = randint(5, 10)
    sleep(secs)
    print('task %s completed.spend %d' % (task_name, secs))


def do_task2():
    start = time()
    p1 = Process(target=fake_task2, args=('t1',))
    p1.start()
    p2 = Process(target=fake_task2, args=('t2',))
    p2.start()
    p1.join()
    p2.join()
    end = time()
    print('totally spend %.2f seconds' % (end - start))


"""
两个进程间的通信.
启动2个进程，一个输出Ping，一个输出Pong,2个进程加起来一共10个
当程序创建进程时，子进程复制了父进程所有数据结构，每个子进程有自己独立的内存空间
"""


def print_pingpong(p_str, q: Queue):
    while not q.full():
        print(p_str)
        q.put(p_str)


def do_task3():
    q = Queue(10)
    p1 = Process(target=print_pingpong, args=('ping', q))
    p1.start()
    p2 = Process(target=print_pingpong, args=('pong', q))
    p2.start()
    p1.join()
    p2.join()
    print('over.')


def f(x):
    sleep(10)
    print(x * x, f'pid:{os.getpid()},ppid:{os.getppid()}')
    return x * x


def use_pool():
    """
    Pool对象：赋予函数并行处理一系列输入值的能力，
    跨进程分配输入数据（data parallelism）
    """
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))


def info(title):
    print(title)
    print('module name:', __name__)
    print('parent process:', os.getppid())
    print('process id:', os.getpid())


def f2(name):
    info('function f')
    print('hello', name)


def f3(conn):
    """管道"""
    conn.send([42, None, 'Hello'])
    conn.close()


def f4(i, l):
    """进程间同步"""
    l.acquire()
    try:
        sleep(randint(2, 5))
        print('hello world', i)
    finally:
        l.release()


def f5(n, a):
    """进程间共享状态：共享内存"""
    n.value = 3.14
    for i in range(len(a)):
        a[i] = -a[i]


def f6(d, l):
    """进程间共享状态：服务进程"""
    d[1] = '1'
    d['2'] = 2
    d[0.25] = None
    l.reverse()


"""
多个线程共享进程的内存空间，当多个线程竞争一个资源时（临界资源），可能产生不可控结果
"""


class Account:
    def __init__(self):
        self._balance = 0
        self._lock = threading.Lock()

    def deposit(self, money):
        """计算存款后的余额"""
        # 先获取锁才能执行后续的代码
        self._lock.acquire()
        try:
            new_money = self._balance + money
            # 假如存储数据需要0.01秒
            sleep(0.01)
            self._balance = new_money
        finally:
            # 在finally中执行释放锁的操作保证正常异常锁都能被释放
            self._lock.release()

    @property
    def balance(self):
        return self._balance


class AddMoneyThread(threading.Thread):
    def __init__(self, account, money):
        threading.Thread.__init__(self)
        self._account = account
        self._money = money

    def run(self):
        self._account.deposit(self._money)


def simulation_deposit():
    """模拟100个线程向同一个账户中存1元钱"""
    account = Account()
    threads = []
    for _ in range(100):
        t = AddMoneyThread(account, 1)
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    print('账户余额为：%d元' % account.balance)


"""不用多线程的情况"""


def download():
    sleep(10)
    tkinter.messagebox.showinfo('提示', '下载完成')


def show_about():
    tkinter.messagebox.showinfo('关于', 'v1.0')


def single_thread_demo():
    top = tkinter.Tk()
    top.title('单线程')
    top.geometry('200x150')
    top.wm_attributes('-topmost', True)
    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='下载', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='关于', command=show_about)
    button2.pack(side='right')
    panel.pack(side='bottom')

    tkinter.mainloop()


"""使用多线程将耗时间的任务放到一个独立的线程中执行，就不会阻塞主线程"""


def multithreading_demo():
    class DownloadTaskHandler(threading.Thread):
        def run(self):
            sleep(10)
            tkinter.messagebox.showinfo('提示', '下载完成')
            button1.config(state=tkinter.NORMAL)

    def download():
        button1.config(state=tkinter.DISABLED)
        # 设置为守护进程，主程序退出就不再保留执行
        DownloadTaskHandler(daemon=True).start()

    def show_aboout():
        tkinter.messagebox.showinfo('关于', 'v1.0')

    top = tkinter.Tk()
    top.title('多线程')
    top.geometry('200x150')
    top.wm_attributes('-topmost', 1)
    panel = tkinter.Frame(top)
    button1 = tkinter.Button(panel, text='下载', command=download)
    button1.pack(side='left')
    button2 = tkinter.Button(panel, text='关于', command=show_aboout)
    button2.pack(side='right')
    panel.pack(side='bottom')
    tkinter.mainloop()


def task_handler(curr_list, result_queue):
    total = 0
    for number in curr_list:
        total += number
    result_queue.put(total)


def multiprocess_sum():
    """利用多进程分而治之"""
    processes = []
    number_list = [x for x in range(0, 100000001)]
    request_queue = Queue()
    index = 0
    # 启动8个进程将数据切片后运算
    for _ in range(8):
        p = Process(target=task_handler, args=(number_list[index:index + 12500000], request_queue))
        index += 12500000
        processes.append(p)
        p.start()

    start = time()
    for p in processes:
        p.join()
    total = 0
    while not request_queue.empty():
        total += request_queue.get()
    print(total)
    end = time()
    print('Execution time: ', (end - start), 's')



if __name__ == '__main__':
    # do_task2()
    # do_task3()
    # use_pool()

    # info('main line')
    # p = Process(target=f2, args=('bob',))
    # p.start()
    # p.join()

    """
    返回的两个连接对象Pipe()表示管道的两端。
    每个连接对象都有send()和recv()方法。
    如果两个进程（或线程）同时尝试读取或写入管道的同一端，则管道中的数据可能会损坏
    """
    # parent_conn, child_conn = Pipe()
    # p = Process(target=f3, args=(child_conn,))
    # p.start()
    # print(parent_conn.recv())
    # p.join()

    """
    进程间同步
    可以使用锁来确保一次只有一个进程打印到标准输出。
    不使用锁的情况下，来自于多进程的输出很容易产生混淆
    """
    # for num in range(10):
    #     lock = Lock()
    #     Process(target=f4, args=(num, lock)).start()

    """
    进程间共享状态：共享内存
    使用Value或Array将数据存储在共享内存映射中
    """
    # typecode:'d'表示双精度浮点数，'i'表示有符号整数
    # num = Value('d', 0.0)
    # arr = Array('i', range(10))
    # p = Process(target=f5, args=(num, arr))
    # p.start()
    # p.join()
    # print(num.value)
    # print(arr[:])

    """
    进程间共享状态：服务进程
    使用Manager()返回的管理器对象控制一个服务进程，
    该进程保存Python对象并允许其他进程使用代理操作它们
    """
    # with Manager() as manager:
    #     d = manager.dict()
    #     l = manager.list(range(10))
    #     p = Process(target=f6, args=(d, l))
    #     p.start()
    #     p.join()
    #     print(d)
    #     print(l)

    """
    使用工作进程
    Pool类表示一个工作进程池。
    它具有允许以几种不同方式将任务分配到工作进程的方法
    """
    # start 4 worker processes
    # with Pool(processes=4) as pool:
    #     print(pool.map(f, range(10)))
    #
    #     # 无序的
    #     print(list(pool.imap_unordered(f, range(10))))
    #
    #     # 异步调用，仅一个进程中运行
    #     res = pool.apply_async(f, (20,))
    #     print(res.get())
    #
    #     res = pool.apply_async(os.getpid, ())
    #     print(res.get())
    #
    #     # 让单个进程睡10秒
    #     pool.apply_async(sleep, (10,))
    #
    #     multi_res = [pool.apply_async(os.getpid, ()) for i in range(4)]
    #     print([r.get() for r in multi_res])

    # p = Process(target=f, args=(2,))
    # print(f'process name:p.name')
    # p.start()
    # print(f'process is alive? {p.is_alive()}')
    # print(p.exitcode)
    # p.join()
    # print(p.exitcode)
    # print('ssss', os.getpid())

    """
    多线程开发使用threading模块
    
    """
    # start = time()
    # t1 = Thread(target=fake_task, args=('t1',))
    # t1.start()
    # t2 = Thread(target=fake_task, args=('t2',))
    # t2.start()
    # t1.join()
    # t2.join()
    # end = time()
    # print('totally spend %.3f seconds' % (end - start))

    # simulation_deposit()

    # single_thread_demo()
    # multithreading_demo()
    multiprocess_sum()