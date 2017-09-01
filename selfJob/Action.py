#!/usr/bin/python
# -*- coding: UTF-8 -*-

# try:
#     fh = open("testfile", "wr")
#     fh.write("这是一个测试文件，用于测试异常!!")
#     str = fh.read(0)
#     print str
# except IOError:
#     print "Error: 没有找到文件或读取文件失败"
# else:
#     print "内容写入文件成功"
#     fh.close()

# try:
#     fh = open("testfile", "w")
#     fh.write("这是一个测试文件，用于测试异常!!")
# finally:
#     print "Error: 没有找到文件或读取文件失败"

#
#
# class Action(Employee):
#     '你猜猜'
#     pass
#
import Employee

print "Employee.__doc__:", Action.__doc__
print "Employee.__name__:", Action.__name__
print "Employee.__module__:", Action.__module__
print "Employee.__bases__:", Action.__bases__
print "Employee.__dict__:", Action.__dict__