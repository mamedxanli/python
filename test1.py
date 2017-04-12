#!/bin/usr/var python
#
# class Joe(object):
#     def callme(self):
#         print('calling callme method with instance: ')
#         print(self)
#
# thisjoe = Joe()
#
# thisjoe.callme()

# import random
#
# class MyClass(object):
#     def dothis(self):
#         self.rand_val = random.randint(1,10)
#
# myinst = MyClass()
# myinst.dothis()
# print(myinst.rand_val)

# class MyInteger(object):
#     def set_val(self, val):
#         try:
#             val = int(val)
#         except ValueError:
#             return
#         self.value = val
#
#     def get_val(self):
#         return self.value
#
#     def increment_val(self):
#         self.val = self.val + 1
#
# i = MyInteger()
# i.val = 7
# print(i.increment_val())

class MyNum(object):
    def __init__(self, value):
        try:
            value = int(value)
        except:
            ValueError
            value = 0
        self.val = value


    def increment(self):
        self.val = self.val + 1

aa = MyNum('hello')
bb = MyNum(100)
aa.increment()
bb.increment()
print aa.val
print bb.val
