"""进程和线程"""
from random import randint
from time import time, sleep


def fake_task(task_name):
    print(f'task {task_name} start...')
    sec = randint(4, 10)
    sleep(sec)
    print(f'task {task_name} completed.spend {sec} seconds.')


def do_tasks():
    start = time()
    fake_task('t_1')
    fake_task('t_2')
    end = time()
    print('totally spend %.2f seconds' % (end - start))


do_tasks()