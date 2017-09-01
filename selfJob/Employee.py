#!/usr/bin/python
# -*- coding: UTF-8 -*-

class Employee:
    '所有员工的基类'\
    '\t飒飒的哈数据库'
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name, ", Salary: ", self.salary


print "Employee.__doc__:", Employee.__doc__
print "Employee.__name__:", Employee.__name__
print "Employee.__module__:", Employee.__module__
print "Employee.__bases__:", Employee.__bases__
print "Employee.__dict__:", Employee.__dict__

# class Action(Employee):
#     '你猜猜'
#     pass
#
#
# print "Employee.__doc__:", Action.__doc__
# print "Employee.__name__:", Action.__name__
# print "Employee.__module__:", Action.__module__
# print "Employee.__bases__:", Action.__bases__
# print "Employee.__dict__:", Action.__dict__