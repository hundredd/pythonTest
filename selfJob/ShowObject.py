#coding:utf-8

class Hun:
    num1 = 10;
    num2 = 15;
    def __init__(self,num1=1,num2=2):
        self.num1 = num1
        self.num2 = num2
        self.show()

    def hunPrint(self):
        print '分别是自己的数字a=%d b=%d'%(self.num1,self.num2)
        return (self.num1,self.num2)

    def show(self):
        print self.hunPrint()

hun = Hun(29)
print getattr(hun,'num1')
print hasattr(hun,'num1')
print getattr(hun,'num1')
delattr(hun,'num1')
print hasattr(hun,'num1')
print getattr(hun,'num1')
# spam = range(10)
# spam[4] = -1
# print spam
#
# spam = 'THIS IS IN LOWERCASE.'
# spam = spam.lower()
# print spam

# class Test:
# #     测试方法
#     def showPrint(self):
#         print "这是我们的类%s"%(self.__class__);
#
#
# t = Test()
# t.showPrint()

# 调整了一段代码!
# class showJob:
#     '自己的类比'
#     showCount = 0
#
#     def __init__(self,num):
#         self.showCount = num;
#
#     def show(self):
#         # self.showCount +=1;
#         return 2
#
#     def showPrint(self,str):
#         print '这是对应的数据%d'%str
#
#
# mm = showJob(5)
#
# while mm.showCount < 10:
#     print mm.showCount
#     mm.showPrint(mm.show())