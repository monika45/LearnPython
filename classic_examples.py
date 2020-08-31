"""
经典例子
"""
from random import randint

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
def f5(money = 1000):
    while money > 0:
        while True:
            debt = int(input('请下注:'))
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


if __name__ == '__main__':
    # f1()
    # f2()
    # f3(12345)
    # f4()
    f5()

