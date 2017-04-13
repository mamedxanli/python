#!/usr/bin/python

class YourClass(object):
    classy = 'class value!'

    # def set_val(self):
    #     self.insty = 100

dd = YourClass()
print dd.classy
dd.classy = 'inst.value!'
print(dd.classy)
del dd.classy
print(dd.classy)