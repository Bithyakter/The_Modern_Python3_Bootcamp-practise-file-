'''def my_decorator(func):
    def decorate():
        print("--------------")
        func()

        print("--------------")
    return decorate

def print_raw():

    print("Clear Text")

# decorated_function = my_decorator(print_raw)
# decorated_function()

print_raw = my_decorator(print_raw)
print_raw()


# We can pass funcs as args to other funcs

def sum(n, func):
    total = 0
    for num in range(1,n+1):
        total += func(num)
    return total

def square(x):
    return x*x

def cube(x):
    return x*x*x


print(sum(3,cube))
print(sum(3,square))


###exmple-2

# We can nest functions inside one another
from random import choice

def greet(person):
    def get_mood():
        msg = choice(('Hello there ', 'Go away ', 'I love you '))
        return msg

    result = get_mood() + person
    return result

print(greet("Alu"))


# We can return funcs from other funcs
def make_laugh_func():
    def get_laugh():
        l = choice(('HAHAHAH', 'lol', 'tehehe'))
        return l

    return get_laugh

laugh = make_laugh_func()
print(laugh())'''


###exmple-3

'''def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day!")
    return wrapper
def greet():
    print("My name is Colt.")

def rage():
    print("I Hate You")

# we are decorating our function
# with politeness!
greet = be_polite(greet)

greet()

polite_rage = be_polite(rage)
polite_rage()



###exmple-4
def be_polite(fn):
    def wrapper():
        print("What a pleasure to meet you!")
        fn()
        print("Have a great day!")
    return wrapper

@be_polite
def greet():
    print("My name is Colt.")


@be_polite
def rage():
    print("I HATE YOU!")


greet()
rage()'''



# This version only accepts one argument
# def shout(fn):
#     def wrapper(name):
#         return fn(name).upper()
#     return wrapper

# This version works with any number of args

def shout(fn):
    def wrapper(*args, **kwargs):
        return fn(*args, **kwargs).upper()
    return wrapper

@shout
def greet(name):
    return f"Hi, I'm {name}."

@shout
def order(main, side):
    return f"Hi, I'd like the {main}, with a side of {side}, please."

@shout
def lol():
     return "lol"

print(greet("Rani"))
print(order(side="pizza", main="fries"))
print(lol())






