"""python singleton design pattern"""
#the singleton pattern is a design pattern that restricts the instantiation of a class to one object.

'''class Singleton:
    # Here will be the instance stored.
    __instance = None

    @staticmethod
    def getInstance():
        """ Static access method. """
        if Singleton.__instance == None:
            Singleton()
        return Singleton.__instance

    def __init__(self):
        """ Virtually private constructor. """
        if Singleton.__instance != None:
            raise Exception("This class is a singleton!")
        else:
            Singleton.__instance = self

# A little testing

s = Singleton() # Ok
#Singleton() # will raise exception
print(s)

s = Singleton.getInstance()
print (s)

s = Singleton.getInstance()
print (s) # will print the same instance as before'''



"""Creating Singletons using Metaclasses"""

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton,cls).__call__(*args, **kwargs)
        return cls._instances[cls]

#singleton implementation
class SingletonClass(metaclass=Singleton):
    pass
class RegularClass():
    pass
x = SingletonClass()
y = SingletonClass()
print(x == y)
x = RegularClass()
y = RegularClass()
print(x == y)



"""create Singleton classes by inheriting from a Singleton class"""

class Singleton(object):
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
        return cls._instance

class SingletonClass(Singleton):
    pass
class RegularClass():
    pass
x = SingletonClass()
y = SingletonClass()
print(x == y)
x = RegularClass()
y = RegularClass()
print(x == y)

