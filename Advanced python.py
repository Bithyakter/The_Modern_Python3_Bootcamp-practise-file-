# num = int (input("Enter the number of rows:"))
#
# num = [5]
# for n in num:
#     for i in range(0,n):
#         for j in range(0,n-i-1):
#              print(end=" ")
#         for j in range(0,i+1):
#              print("*",end=" ")
#         print()


# num = int(input("Enter the number of rows:"))
# for i in range(0, num):
#     for j in range(0, num - i - 1):
#         print(end=" ")
#     for j in range(0, i + 1):
#         print("*", end=" ")
#     print()


# for row in range(6):
#     for col in range(7):
#         if (row==0 and col%3!=0) or (row==1 and col%3==0) or (row-col==2) or (row + col==8):
#          print("*", end=" ")
#         else:
#             print(end=" ")
#     print()


# def pyramid(rows):
#
#     for i in range(rows):
#         print(''*(rows-i-1)+'*'*(i+1))
#     for j in range(rows-1,0,-1):
#
#         print(''*(rows-j)+'*'*(j))
#
# pyramid(5)

#
# d={'X':"Red", 'Y':"Red", 'Z':"Blue"}
# Search=input("Enter your word\n")
# Count=0
#
# for i in d.values():
#     if i==Search:
#
#         Count+=1
#
# print(str(Count))


# d={}
# lst = ['Shammi', 'Nitu', 'Monisha', 'Nitu', 'Bithy', 'Shammi']
# search = input("Enter your Word: ")
# count = 0
# for value in lst:
#     if value == search:
#         count = count + 1
#
# d[search] = count
#
# print(d)


# dict1={'a': 1, 'b': 2, 'e': {'c': 3, 'd': 4}, 'f': {'g': 3, 'h': 4} }
# print(dict1['e'])
#
# print(dict1 ['e'] ['c'])


## Example 2:Print Fabonacci Number Using recursion

# def fibR(n):
#     if n==1 or n==2:
#         return 1
#     return fibR(n-1)+fibR(n-2)
#
# print (fibR(5))
#
# def fibonacci(n):
#     if(n <= 1):
#         return n
#     else:
#         return(fibonacci(n-1) + fibonacci(n-2))
# n = int(input("Enter number of terms:"))
# print("Fibonacci sequence:")
# for i in range(n):
#     print (fibonacci(i))


# def fact(n):
#     if(n<=1):
#         return 1
#     else:
#         return(n*fact(n-1))
# n=int(input("Enter the number:"))
# print("Factorial:")
# print(fact(n))


'''DateTime'''

# from datetime import date
# x= date(1993, 12, 14)
# print(x)
#
#
# from datetime import date
# print(date.min)
# print(date.max)


#
# from datetime import date
# x= date(1993, 12, 14)
# print(x)
# print(x.day)
# print(x.month)
# print(x.year)


# from datetime import time
# t = time(18, 5, 25)
# print(t)
# print(t.hour, t.minute, t.second)
#
#
# print(time.min)
# print(time.max)
#
#
# t = t.replace(hour=12, minute=59)


# from datetime import datetime,  timedelta as delta
# ndays = 10
# start = datetime(1991, 4, 30)
# dates = [start - delta(days=x) for x in range(0,ndays)]
# print(dates)

#
# from datetime import datetime
# t = datetime(2017, 4, 19,  16, 31, 0)
# print(t)


# import datetime
# now = datetime.datetime.now()

import datetime

# today = datetime.date.today()
# print (today)
# print ('ctime:', today.ctime())
# # print ('tuple:', today.timetuple())
# # print ('ordinal:', today.toordinal())
# print ('Year:', today.year)
# print ('Mon :', today.month)
# print ('Day :', today.day)

#
# import datetime
#
# today = datetime.datetime.today()
# print(today)
#
# print('ctime:', today.ctime())
#
# print('Year:', today.year)
# print('Mon:', today.month)
# print('Day:', today.day)


# String

'''print ("My name is %s and weight is %d kg!" % ('Bithy', 40))

count = 0
for letter in 'Hello World':
    if(letter == 'l'):
        count += 1
print(count,'letters found')


from datetime import datetime
t = datetime(18, 5, 25, 12, 5, 59)
print(t)
print(t.day, t.month, t.year, t.hour, t.minute, t.second)'''

'''import datetime
now = datetime.datetime.now()
delay = float (raw_input ("enter delay (s): "))
dt = datetime.timedelta (seconds=delay)         
then = now + dt
print (now)
print (then)


import datetime
x = datetime.date.today()
print(x)

print("Today is:", x)

n=datetime.timedelta(days=1)
print("Tomorrow is", x+n)

print("Yesterday is", x-n)


import datetime
print( 'Now:', datetime.datetime.now())
print( 'UTC Now:', datetime.datetime.utcnow())     #Error

d = datetime.datetime.now()
for attr in ['Year:', 'Month:', 'Day:', 'Hour:', 'Minute:', 'Second:','Microsecond:']:
    print(attr, getattr(d, attr)



import datetime

format = "%a %b %d %H:%M:%S %Y"

today = datetime.datetime.today()
print ('ISO     :', today)

s = today.strftime(format)
print ('strftime:', s)

d = datetime.datetime.strptime(s, format)
print ('strptime:', d.strftime(format))'''

# repr

'''class Person:
    name = 'Anmul'

    def __repr__(self):
        return repr(self.name)
repr(Person())'''

# Details with Class

'''class Res:
    name  =" "
    owner =" "

    def details(self):
        print(self.name , self.owner)

    def address(self, address):
        print(self.name , self.owner)

        print(address)

Res1=Res()
Res1.name = "Book"
Res1.owner= "Bithy"
Res1.address("Bogra")




class Math:                             #parent clss
    def __init__(self, x, y):
        self.x = x
        self.y = y
        def sum(self):
            return self.x + self.y

class Math2 (Math):                      #child clss
    def __init__(self, x, y):
        super().__init__(x, y)

    def subtract(self):
        return self.x -self.y

Math2_obj = Math2 (10, 2)               #problem

print (Math2_obj.sum())'''

# from random import choice
#
# list=[1,2,3,4,5]
#
# for x in range(1,3):
#
#     print(choice(list))


# List

'''cars = ['honda', 'toyota', 'audi']
for car in cars:                          #List_iteration
    print(car)
    if car == 'toyota':
        print("I love toyota")


Relative = ['Me', 'You', 'I', 'We']
                                                      #list_slicing
print(Relative[0:2])

for We_are in Relative:
    print(We_are)
    if We_are == 'I':

        print("I Love Myself")


Relative.append('They')          #Add
print(Relative)

Relative += ['They_are']

print(Relative)


Relative = ['Me', 'You', 'I', 'We']
print(Relative)                         #deleting

del Relative [1]
print(Relative)

Relative.remove('I')                   #Remove_value
print(Relative)

item = Relative.pop()                       #Using_pop
print(Relative, "\n", item)


Me = ['"I', 'Love', 'Myself"']
print(Me)                               #string concatnation
Me_str =' '.join(Me)
print(Me_str)


import re
                                       #string to convert List
Me= "I, Love, Myself"
List = re.split(',' , Me)
print(List)


Relative = ['Me', 'You', 'I', 'We']
print(sorted(Relative))                       #sort List

print(Relative)

Relative.sort(reverse = True)

print(Relative)



Relative = ['Me', 'You', 'I', 'We']
Relative.reverse()                       #len checking & reverse
print(Relative)

print(len(Relative))'''

# Tuple & Dictionary


'''tp = (2, 3, 4, 5, 6, 7, True, 'Me', ['I', 'You'], ('Me'))

print(tp)
print(type(tp))                                            #Tuple
print(tp.count(4))
print(tp.index(7))

tp = (2, 3, 4, 5, 6, 7)
a, b, c, d, e, f = tp
print(a, b, c, d, e, f, sep=' ')


tp = ('Hello',)

print(type(tp))

print( ((1,2,3) + (4,5,6))* 3 )

print(("Bithy", )* 3)

for name in ('Bithy', 'RaFin', 'AriF', 'Shammi', 'Nitu'):

    print("Hello", name)



dict = {'Me' : 'Bithy'}

print(dict)                                                       #dictionary

List = {'Me':'good', 'You':'Faul', 'Result':'False'}
print("What:", (List))
print(List ['Result'])

for key, value in List.items():
    print(key,value, sep='>')


dict = {}
for x in range(5):
    dict[x] = x*x

print(dict)


people = {1 : {'name':'Radi', 'age':'4'},            #Nested dict
          2 : {'name':'Rafin', 'age':'5'} }
print(people)


people2 = {1: {'name': 'John', 'age': '27', 'sex': 'Male'},
          2: {'name': 'Marie', 'age': '22', 'sex': 'Female'}}
print(people2)'''

# script arguments

'''import sys
print(sys.argv)


set_country = {'Bangladesh', 'USA', 'India', 'Malaysia'}
country = 'Bangladesh'

if country in set_country:
     print(country.title(), 'exits')'''

# conditional expression
# syntax: expression if condition1 if condition else experssion2
'''sum = 100
num = 10

sum += num if num % 2 == 0 else 0
print(sum)

###normal way
if num%2 == 0:
    sum += num
else:
    sum += 0
print(sum)'''

# Comprehension

# syntax: expression for value in iterable if condition

'''square = [v * v for v in range(1, 12) if v%2 != 0]

print(square)


###normal way
square = []

for v in range(1, 12):
    square += [v * v]
print(square)

Square_set = {v * v for v in range(1, 12) if v%2 != 0}
print("This is set:", Square_set)

Square_dict ={ v: v * v for v in range(1, 12) if v%2 != 0}
print("This is dict:", Square_dict)

Square_list = [v * v for v in range(1, 12) if v%2 != 0]
print("This is list:", Square_list)'''

# list

'''movies = ["Gabbar", "Jabbar", "Chandu", "Nandu", "Ghiblu", "Jhiblu", "Jhablu", "Jaba", "Faltu", "Taklu"]

Jmovies = []

for title in movies:                       #normal ways
    if title.startswith("J"):
        Jmovies.append(title)
print(Jmovies)


Jmovies = [ title for title in movies if title.startswith("J")]
print(Jmovies)


movies = [("Gabbar",2003),("Jabbar",1991),("Chandu",2006),("Nandu",1971),("Ghiblu",2012),("Jhiblu",2008),("Jhablu",1870),("Jaba",2000),("Faltu",2001),("Taklu",1991)]


Details = [title for (title,year) in movies if year<=2000]
print(Details)


n = [4, -2, 5]

result = [4 * x for x in n]
print(result)


A = [1, 3, 5, 7]
B = [2, 4, 6, 8]

cartesian_product = [(x, y) for x in A for y in B]
print(cartesian_product )'''

###Quadratic Reciprocity
# findout the logic
'''p_logic = [ x ** 2 % p for x in range(0,p)]
len(p_logic) = p+1/2'''

###Exception Handling

'''try:
    print (5/0)

except ZeroDivisionError:
    print ("You can't divide by zero, you're silly.")


try:
    num = 5 / 0
except:

    print("Custom message about an error!")
    raise


print(1)                     #Assertions
assert 2 + 2 == 4
print(2)
assert 1 + 1 == 3
print(3)'''

###try_except_finally

'''import math
num = int(input("Please Inter your number:"))
try:
    result = math.factorial(num)
    print(result)
except ValueError:
    print("Factorial not defined negative values")

finally:
    print('"Good Bye"')


import math
num = int(input("Please Inter your number:"))
try:
    result = math.factorial(num)
    print(result)
except Exception as e:

    print("Unknown Error occurs:",e)

finally:
    print('"Good Bye"')



import math
num = int(input("Please Inter your number:"))
try:
    result = math.factorial(num)
    print(result)
except ValueError:
    print("Factorial not defined negative values")
else:
    print("Result is:", result)
finally:
    print('"Good Bye"')'''

###map

'''a = [1, 2, 3, 4]

def square(x):
    return x*x
print(map(square, a))

###if use to lambda

map(lambda x:x*x, a)'''

###Logging

import logging

logging.basicConfig(filename="Logging_File",)

logger = logging.getLogger()

logger.info("Fst Mesg")

print(logger.level)


