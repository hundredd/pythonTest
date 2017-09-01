#!/usr/bin/python
# -*- coding: UTF-8 -*-

import thread
import time

def showTime(ThreadName,delay):
    count = 0
    while count<5:
        time.sleep(delay)
        count+=1
        print "%s :%s"%(ThreadName,time.ctime(time.time()))


def anotherTime(ThreadName,delay):
    num = 0
    while num<5:
        time.sleep(delay)
        num += 1
        print "%s :%s"%(ThreadName,time.ctime(time.time()))


try:
    thread.start_new(anotherTime, ('hund', 3,))
    # thread.start_new(showTime('hunShow',2,))
except:
    print "Error"
else:
    print '没用到'

while True:
    pass
# import thread
# import time
#
#
# # 为线程定义一个函数
# def print_time(threadName, delay):
#     count = 0
#     while count < 5:
#         time.sleep(delay)
#         count += 1
#         print "%s: %s" % (threadName, time.ctime(time.time()))
#
#
# # 创建两个线程
# try:
#     thread.start_new_thread(print_time, ("Thread-1", 2,))
#     thread.start_new_thread(print_time, ("Thread-2", 4,))
# except:
#     print "Error: unable to start thread"
#
# while 1:
#     pass