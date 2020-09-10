"""
面向对象
"""
import math
from abc import ABCMeta, abstractmethod


class Point:
    """
    定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法。
    """

    def __init__(self, x=0, y=0):
        """

        :param x: 横坐标
        :param y: 纵坐标
        """
        self.x = x
        self.y = y
        self._t1 = 1
        self.__t2 = 1

    def __str__(self):
        return '(%s, %s)' % (str(self.x), str(self.y))

    def move_to(self, x, y):
        """
        移动到指定位置
        :param x: 横坐标
        :param y: 纵坐标
        """
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        """
        增量移动
        :param dx:横坐标增量
        :param dy: 纵坐标增量
        """
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        """
        计算到另一个点之间的巨鹿
        :param other: Point对象
        :return: 返回两点间的距离
        """
        dx = math.fabs(self.x - other.x)
        dy = math.fabs(self.y - other.y)
        res = math.sqrt(dx ** 2 + dy ** 2)
        return round(res, 2)


class P(Point):
    pass


class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age

    def play(self):
        print('%s正在愉快的玩耍' % self._name)

    def is_adult(self):
        return True if self._age >= 18 else False


class Student(Person):

    def __init__(self, name, age, grade):
        self._grade = grade
        Person.__init__(self, name, age)

    @property
    def grade(self):
        return self._grade

    @grade.setter
    def grade(self, grade):
        self._grade = grade

    def study(self, course):
        print('%s的%s正在学习%s'% (self._grade, self._name, course))


class Teacher(Person):
    def __init__(self, name, age, title):
        self._title = title
        Person.__init__(self, name, age)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        self._title = title

    def teach(self, course):
        print('%s%s正在讲%s'% (self._name, self._title, course))

    def play(self):
        print('Teacher里重写play')


# 用ABCMeta和abstractmethod来实现抽象类，声明为抽象类后，不可实例化，必须在子类中实现抽象方法（多态）



if __name__ == '__main__':
    # p1 = Point(-10, 10)
    # p2 = Point(2, 12)
    # print(p1.distance_to(p2))
    # print(p2.distance_to(p1))
    # p2.move_by(3, 4)
    # p1.move_to(2, 12)
    # print(p2)
    # print(p2.distance_to(p1))
    # print(dir(p1))
    # p3 = P(2, 6)
    # print(dir(p3))
    stu = Student('张三', 18, '高三')
    stu.study('数学')
    print(stu.is_adult())
    stu.play()

    tea = Teacher('李武', 30, '物理')
    tea.teach('三大定律')
    tea.play()

