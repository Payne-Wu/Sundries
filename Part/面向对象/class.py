# -*- coding: utf-8 -*-
# @Time     :   2020/3/23 13:04
# @Author   :   Payne
# @File     :   class.py
# @Software :   PyCharm

"""
类(Class): 用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。
类变量：类变量在整个实例化的对象中是公用的。类变量定义在类中且在函数体之外。类变量通常不作为实例变量使用。
数据成员：类变量或者实例变量, 用于处理类及其实例对象的相关的数据。
方法重写：如果从父类继承的方法不能满足子类的需求，可以对其进行改写，这个过程叫方法的覆盖（override），也称为方法的重写。
局部变量：定义在方法中的变量，只作用于当前实例的类。
实例变量：在类的声明中，属性是用变量来表示的。这种变量就称为实例变量，是在类声明的内部但是在类的其他成员方法之外声明的。
继承：即一个派生类（derived class）继承基类（base class）的字段和方法。继承也允许把一个派生类的对象作为一个基类对象对待。例如，有这样一个设计：一个Dog类型的对象派生自Animal类，这是模拟"是一个（is-a）"关系（例图，Dog是一个Animal）。
实例化：创建一个类的实例，类的具体对象。
方法：类中定义的函数。
对象：通过类定义的数据结构实例。对象包括两个数据成员（类变量和实例变量）和方法。
"""

'''创造类'''

'''
使用class语句来创造一个新类
    class ClassName:
        '类的帮助信息'    # 类文档字符串
        class_suite     # 类体 （由类成员，方法，数据属性组成）
'''

'''EG:'''


class Employee:
    # '''所有员工的基类'''
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def EmpCount(self):
        print('Total Employee %d' % Employee.empCount)

    def displayEmployee(self):
        print('Name :', self.name, 'Salary :', self.salary)


emp1 = Employee('Zara', 2000)
emp2 = Employee('Lisa', 3000)
emp3 = Employee('Payne', 4000)
emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()
print("Total Employee %d" % Employee.empCount)

'''
"""self 代表实例 而非类"""
"""
self代表类的实例，而非类
类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。
"""

class Test:
    def prt(self):
        print(self)
        print(self.__class__)


t = Test()
t.prt()
'''
