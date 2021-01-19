from persistentclass.persistentclass import Persistent
import datetime


class MyClass(Persistent):
    def init(self):
        value = 'Test'


def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3


myclass = MyClass()
myclass.time = simpleGeneratorFun()
myclass.save()

otherclass = MyClass()
pass
