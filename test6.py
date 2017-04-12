#!/usr/bin/python

class Animal(object):
    def __init__(self, name):
        self.name = name
    def eat(self, food):
        print "{} is eating {}".format(self.name, food)

class Dog(Animal):
    def fetch(self, thing):
        print "{} goes after the {}".format(self.name, thing)

    def show_affection(self):
        print '{} wags tail'.format(self.name)

class Cat(Animal):
    def swatstring(self):
        print '{} shreds the string'.format(self.name)

    def show_affection(self):
        print '{} purrs'.format(self.name)

r = Dog('Rover')
f = Cat('Murzana')
b = Dog('Zagrya')
c = Cat('Murzana1')
# r.eat("meat")
# f.eat("whiskas")
# r.fetch("bird")
# f.swatstring()

for animal in (r,f,b,c):
    animal.show_affection()
