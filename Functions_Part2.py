''''This is Functions Part2'''
# def feed_me(*stuff):
#     for thing in stuff:
#         print(f"YUMMY I EAT {thing}")
# feed_me("apple", "tire", "shoe", "salmon")
#
#
# def ensure_correct_info(*args):
#     if "Pinky" in args and "Steele" in args:
#         return "Welcome back Pinky!"
#     return "Note sure who you are?"
#
# print(ensure_correct_info("hello", False, 78))     # Not sure who you are...
#
# print(ensure_correct_info(1, True, "Steele", "Pinky"))
#
# #sum
# def sum_all_nums(*nums):
#     total = 0
#     for num in nums:
#         total += num
#     return total
#
# print(sum_all_nums(4,6,9,4,10))
# print(sum_all_nums(4,6))

#fun_colors
# def fav_colors(**kwargs):
#     for person, color in kwargs.items():
#         print(f"{person}'s favorite color is {color}")
#
# fav_colors(Pinky="purple", Ruby="red", Rani="teal")
# fav_colors(Pinky="purple", Ruby="red", Rani="teal", Ted="blue")
# fav_colors(Pinky="royal deep amazing purple")
#
#
# def display_info(a, b, *args, instructor="Colt", **kwargs):
#     # return [a, b, args, instructor, kwargs]
#     print(type(args))
#
# print(display_info(1, 2, 3, last_name="Steele", job="Instructor"))
#
# # a - 1
# # b - 2
# # args (3)
# # instructor - "Colt"
# # kwargs - {'last_name': "Steele", "job": "Instructor"}
#
# [1, 2, (3,), 'Colt', {'last_name': 'Steele', 'job': 'Instructor'}]


# #Unpacking
def display_names(first, second):
    print(f"{first} says hello to {second}")

names = {"first": "Colt", "second": "Rusty"}

# display_names(names) # nope..
display_names(**names)  # yup!

def add_and_multiply_numbers(a,b,c,**kwargs):
    print(a + b * c)
    print("OTHER STUFF....")
    print(kwargs)

data = dict(a=1,b=2,c=3,d=55,name="Tony")

add_and_multiply_numbers(**data) # 7


#Dict-unpacking
def display_names(first, second):
    print(f"{first} says hello to {second}")

names = {"first": "Colt", "second": "Rusty"}

# display_names(names) # nope..
display_names(**names)  # yup!

def add_and_multiply_numbers(a,b,c,**kwargs):
    print(a + b * c)
    print("OTHER STUFF....")
    print(kwargs)

data = dict(a=1,b=2,c=3,d=55,name="Tony")

add_and_multiply_numbers(**data) # 7

