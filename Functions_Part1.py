'''This is Functions Part1'''
# #Example-1
# def sing_happy_birthday():
#     print("Happy Birthday To You")
#     print("Happy Birthday To You")
#     print("Happy Birthday Dear You")
#     print("Happy Birthday To You")
#
#
# sing_happy_birthday()
#
# #Exmple-2
# def print_square_of_7():            #This function does not return anything
#     print(7**2)
#
# print_square_of_7()
#
# def square_of_7():
#     print("I AM BEFORE THE RETURN!")
#     return 7**2
#     print("I AM AFTER THE RETURN!")
#
# result = square_of_7()
# print(result)
#
#
# #Exmple-3
# from random import random
#
# def flip_coin():
#     if random() > 0.5:
#         return "HEADS"
#     else:
#         return "TAILS"
#
# print(flip_coin())
#
#
# #Exmple-4
# ###Divide
# def divide(num1, num2):
#     return num1/num2
#
# print(divide(2,5))
# print(divide(5,2))
#
# ###Square
# def square(num):
#     return num * num
#
# print(square(4))
# print(square(8))


#Exmple-5
#OLD=VERSION===OLD=VERSION===OLD=VERSION
# def is_odd_number(num):
#     if num % 2 != 0:
#         return True
#     else:                          #This else is unnecessary
#         return False
# #OLD=VERSION===OLD=VERSION===OLD=VERSION
#
#
# def is_odd_number(num):
#     if num % 2 != 0:
#         return True
#     return False                   # We can just return without the else
#
# print(is_odd_number(4))
# print(is_odd_number(9))
#
# #Part-2
# #OLD-VERSION----OLD-VERSION----OLD-VERSION-----
# def sum_odd_numbers(numbers):
#     total = 0
#     for num in numbers:
#         if num % 2 != 0:
#             total += num
#         return total               #Returning too early :(
# #OLD-VERSION----OLD-VERSION----OLD-VERSION-----
#
#
# # NEW AND IMPROVED VERSION :)
# def sum_odd_numbers(numbers):
#     total = 0
#     for num in numbers:
#         if num % 2 != 0:
#             total += num
#     return total
#
# print(sum_odd_numbers([1,2,3,4,5,6,7]))
#
#
#
# #Math
# def add(a,b):
#     return a+b
#
# def math(a,b,fn=add):
#     return fn(a,b)
#
# def subtract(a,b):
#     return a-b
#
# print(math(4,5))       #results in add(4,5) which is 9
#
# print(math(4,5,subtract))    #results in subtract(4,5) which is -1
#
#
# def exponent(num, power=2):
#     return num ** power
#
#
# # Order doesn't matter anymore, if we use key word arguments:
# print(exponent(num=2,power=3))     #8
# print(exponent(power=3, num=2))    #8
#
# # Without keywords args, order still matters:
# print(exponent(3,4))     #81
# print(exponent(4,3))     #64
#
#
#
# # EXAMPLE OF A SCOPING PROBLEM:
# total = 0
#
# def increment():
#     total += 1
#     return total
#
# # print(increment())     # Error!
# # "I can't find a variable named total in this function"
#
#
# def increment():
#     global total     #use the global variable total
#     total += 1
#     return total
#
# print(increment()) # 1
# print(increment()) # 2
# print(increment()) # 3


#doc
def exponent(num, power=2):
    """exponent(num, power)raises num to specified power. Power defaults to 2."""
    return num ** power

print(exponent(2,3))     #8
print(exponent(3))       #9
print(exponent(7))      #49

print(exponent.__doc__)












