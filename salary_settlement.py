"""
工资结算系统
某公司有三种类型的员工 分别是部门经理、程序员和销售员
需要设计一个工资结算系统 根据提供的员工信息来计算月薪
部门经理的月薪是每月固定15000元
程序员的月薪按本月工作时间计算 每小时150元
销售员的月薪是1200元的底薪加上销售额5%的提成
"""

from abc import ABCMeta, abstractmethod
from decimal import Decimal


class Employee(metaclass=ABCMeta):

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name

    @abstractmethod
    def get_salary(self):
        pass


class Manager(Employee):

    def get_salary(self):
        return '%.2f' % 15000


class Programmer(Employee):

    def __init__(self, name, working_hour=0):
        Employee.__init__(self, name)
        self._working_hour = working_hour

    @property
    def working_hour(self):
        return self._working_hour

    @working_hour.setter
    def working_hour(self, working_hour):
        self._working_hour = working_hour if working_hour > 0 else 0

    def get_salary(self):
        return Decimal(150.0 * self._working_hour).quantize(Decimal('0.00'))


class Salesman(Employee):

    def __init__(self, name, sales=0):
        Employee.__init__(self, name)
        self._sales = sales

    @property
    def sales(self):
        return self._sales

    @sales.setter
    def sales(self, sales):
        self._sales = sales if sales > 0 else 0

    def get_salary(self):
        return round(1200.0 + self._sales * 0.05, 2)


if __name__ == '__main__':
    employees = [Manager('张三'), Programmer('李四'), Salesman('王五')]
    for emp in employees:
        if isinstance(emp, Programmer):
            emp.working_hour = float(input('请输入%s的工作时长:' % emp.name))
        elif isinstance(emp, Salesman):
            emp.sales = float(input('请输入%s的销售额:' % emp.name))
        print('%s的工资是%s' % (emp.name, emp.get_salary()))