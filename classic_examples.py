"""
经典例子
"""
import math
import os
import time
from random import randint, randrange, sample


# 寻找水仙花数
# 将数字转成字符串，遍历
def f1(start=100, stop=1000):
    for i in range(start, stop):
        s = str(i)
        n = 0
        for c in s:
            n += int(c) ** 3
        if n == i:
            print(i)


def f2(start=100, stop=1000):
    for i in range(start, stop):
        n = (i % 10) ** 3
        x = i // 10
        while x >= 1:
            n += (x % 10) ** 3
            x = x // 10
        if n == i:
            print(i)


# 正整数反转如，12345 反转成 54321
def f3(n):
    reversed_num = n % 10
    x = n // 10
    while x >= 1:
        reversed_num = reversed_num * 10 + x % 10
        x //= 10
    print(reversed_num)


# 百钱白鸡问题
# 穷举法
def f4():
    for x in range(0, 20):
        for y in range(0, 33):
            z = 100 - x - y
            if 5 * x + 3 * y + 1 / 3 * z == 100:
                print('公鸡 %d 只，母鸡%d只，小鸡%d只' % (x, y, z))


"""
craps游戏，假设玩家有1000元，输光结束游戏
说明：CRAPS又称花旗骰，是美国拉斯维加斯非常受欢迎的一种的桌上赌博游戏。
该游戏使用两粒骰子，玩家通过摇两粒骰子获得点数进行游戏。简单的规则是：
玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
玩家第一次如果摇出2点、3点或12点，庄家胜；
其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
如果玩家摇出了第一次摇的点数，玩家胜；
其他点数，玩家继续要骰子，直到分出胜负。
"""


def f5(money=1000):
    while money > 0:
        while True:
            debt = int(input('请下注(%d < xxx <= %d):' % (0, money)))
            if 0 < debt <= money:
                break
        n = randint(1, 6) + randint(1, 6)
        if n == 7 or n == 11:
            money += debt
            print('第1次摇出点数%d，玩家胜,余额：%d' % (n, money))
        elif n == 2 or n == 3 or n == 12:
            money -= debt
            print('第1次摇出%d,庄家胜,余额：%d' % (n, money))
        else:
            t = 1
            while True:
                t += 1
                m = randint(1, 6) + randint(1, 6)
                if n == m:
                    money += debt
                    print('第%d次摇出点数%d，与第一次相同，玩家胜,余额：%d' % (t, m, money))
                    break
                elif m == 7:
                    money -= debt
                    print('第%d次摇出点数%d,庄家胜,余额：%d' % (t, m, money))
                    break
    print('玩家钱输完，游戏结束！')


def f6():
    """
    生成斐波那契数列的前20个数。
    说明：斐波那契数列（Fibonacci sequence），又称黄金分割数列，
    是意大利数学家莱昂纳多·斐波那契（Leonardoda Fibonacci）在《计算之书》中
    提出一个在理想假设条件下兔子成长率的问题而引入的数列，
    所以这个数列也被戏称为"兔子数列"。
    斐波那契数列的特点是数列的前两个数都是1
    ，从第三个数开始，每个数都是它前面两个数的和，形如：
    1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...。
    斐波那契数列在现代物理、准晶体结构、化学等领域都有直接的应用。
    """
    l = [1, 1]
    for i in range(2, 20):
        l.append(l[i - 1] + l[i - 2])
    print(l)


def f7(n=10000):
    """
    找出10000以内的完美数。
    完美数又称为完全数或完备数，
    它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身。例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美数。完美数有很多神奇的特性，有兴趣的可以自行了解。
    """
    for i in range(1, n + 1):
        m = 0
        for j in range(1, i):
            if i % j == 0:
                m += j
        if i == m:
            print(i)


def f8(n=100):
    """
    输出100以内所有的素数。
    素数指的是只能被1和自身整除的正整数（不包括1）。
    """
    l = []
    for x in range(2, n + 1):
        if is_prime(x):
            l.append(x)
    print(l)


def f9(n):
    """
    算n的阶乘
    :param n:
    """
    fm = n
    for i in range(1, n):
        fm *= i
    return fm


def f10(m, n):
    """
    算C(m, n)
    :param m:
    :param n:
    :return:
    """
    return f9(m) // (f9(n) * f9(m - n))


def gcd(x, y):
    """
    算最大公约数
    :param x:
    :param y:
    :return:
    """
    if x % y == 0:
        return y
    if y % x == 0:
        return x
    s1, s2 = (x, y) if x > y else (y, x)
    if x % 2 == 0 and y % 2 == 0:
        s1 //= 2
        s2 //= 2
    m = s1 - s2
    while m != s2:
        if m > s2:
            s1 = m
        else:
            s1 = s2
            s2 = m
        m = s1 - s2
    return m


def lcm(x, y):
    """
    算最小公倍数
    :param x:
    :param y:
    :return:
    """
    if x % y == 0:
        return x
    if y % x == 0:
        return y
    return (x * y) // gcd(x, y)


def is_palindrome(n):
    """
    判断一个数是不是回文数
    :return:
    """
    m = 0
    x = n
    while x > 0:
        m = m * 10 + x % 10
        x //= 10
    if m == n:
        return True
    return False


def is_prime(n):
    """
    判断是否是素数
    :param n:
    :return:
    """
    if n <= 3:
        return n - 1
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


def marquee():
    """
    跑马灯
    :return:
    """
    content = '北京欢迎你。。。'
    while True:
        # os.system('clear')
        print(content)
        time.sleep(0.2)
        content = content[1:] + content[0]


def generate_code(code_len=6):
    """
    产生指定长度的验证码，验证码由大小写字母和数字构成。
    :return:
    """
    all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    last_idx = len(all_chars) - 1
    code = ''
    for _ in range(6):
        code += all_chars[randint(0, last_idx)]
    return code


def get_suffix(filename: str):
    """
    返回给定文件名的后缀名。
    :param filename: 完整文件名
    :return:
    """
    return filename[filename.rfind('.'):]


def max2(l):
    """
    返回传入的列表中最大和第二大的元素的值
    :return:
    """
    if len(l) < 2:
        return l[0], l[0]
    nl = sorted(l, reverse=True)
    return nl[0], nl[1]


def max3(l):
    """
    返回传入的列表中最大和第二大的元素的值
    :param l:
    :return:
    """
    a, b = (l[0], l[1]) if l[0] > l[1] else (l[1], l[0])
    for x in range(2, len(l)):
        if l[x] > a:
            a, b = l[x], a
        elif l[x] > b:
            b = l[x]
    return a, b


def is_leap_year(year):
    """
    判断是否是闰年
    :param year:
    :return:
    """
    return year % 4 == 0 and year % 100 != 100 or year % 400 == 0


def which_day(datestr: str):
    """
    计算指定的年月日是这一年的第几天
    :param datestr 格式：yyyy-mm-dd
    :return:
    """
    dayarr = datestr.split('-')
    year = int(dayarr[0])
    month = int(dayarr[1])
    day = int(dayarr[2])
    days = [
        [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
        [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ][is_leap_year(year)]
    total = 0
    for m in range(month - 1):
        total += days[m]
    total += day
    return total


def yanghui_triangle():
    """
    打印杨辉三角
    :return:
    """
    n = int(input('行数：'))
    yh = [[]] * n
    for row in range(n):
        yh[row] = [None] * (row + 1)
        for col in range(row + 1):
            if row == 0 or row == col:
                yh[row][col] = 1
            else:
                yh[row][col] = yh[row - 1][col - 1] + yh[row - 1][col]
            print(yh[row][col], end='\t')
        print()


def bichromatic_sphere():
    """
    双色球选号
    :return:
    """
    # 随机选择一组号码
    red_balls = [x for x in range(1, 34)]
    selected_balls = sample(red_balls, 6)
    selected_balls.sort()
    selected_balls.append(randint(1, 16))

    # 输出列表中的双色球号码
    for index, elem in enumerate(selected_balls):
        if index == len(selected_balls) - 1:
            print('|', end=' ')
        print('%02d' % elem, end=' ')
    print()


def joseph_circle():
    """
    约瑟夫环问题
    《幸运的基督徒》
有15个基督徒和15个非基督徒在海上遇险，为了能让一部分人活下来不得不将其中15个人扔到海里面去，有个人想了个办法就是大家围成一个圈，由某个人开始从1报数，报到9的人就扔到海里面，他后面的人接着从1开始报数，报到9的人继续扔到海里面，直到扔掉15个人。由于上帝的保佑，15个基督徒都幸免于难，问这些人最开始是怎么站的，哪些位置是基督徒哪些位置是非基督徒。
    :return:
    """
    persons = [True] * 30
    index, number, counter = 0, 0, 0
    while counter < 15:
        if persons[index]:
            number += 1
            if number == 9:
                number = 0
                persons[index] = False
                counter += 1
        index += 1
        index %= 30
    for i, p in enumerate(persons):
        print(f'{i}:{"基督徒" if p else "非基督徒"}')

def tic_tac_toe():
    """
    井字棋游戏
    :return:
    """
    def print_board(board):
        print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
        print('-+-+-')
        print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
        print('-+-+-')
        print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])

    init_board = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' ',
    }
    begin = True
    while begin:
        curr_board = init_board.copy()
        begin = False
        turn = 'x'
        counter = 0
        os.system('cls')
        print_board(curr_board)
        while counter < 9:
            move = input(f'轮到{turn}走棋，请输入走棋位置：')
            if move not in curr_board:
                print('输入走棋位置不正确,应在以下位置中选择：')
                print(list(curr_board.keys()))
                continue
            if curr_board[move] == ' ':
                curr_board[move] = turn
                if turn == 'x':
                    turn = 'o'
                else:
                    turn = 'x'
                counter += 1
                os.system('cls')
                print_board(curr_board)
        again = input('游戏结束，再玩一局？（yes|no）')
        begin = again == 'yes'


if __name__ == '__main__':
    tic_tac_toe()