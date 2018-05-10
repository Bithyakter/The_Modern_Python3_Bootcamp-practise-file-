# greeting = "hello"
# name = input("Please enter your name\n")
# print(greeting + ' ' + name)

# splitString = "This string has been\nsplit over\nseveral\nlines"
# print(splitString)
#
# tabbedStirng = "1\t2\t3\t4\t5\t6"
# print(tabbedStirng)
#
# #print("The pet shop owner said "No, no, \'e\'s uh,,,,he\s resting"')
# anotherSplitString = """This string has been
# split over
# several lines"""
# print(anotherSplitString)

# age = 21
# age1 = 33
# age2 = 35
# age3 = 32
#
# print("My age is " + str(age) + " years old.")
# print("My age is {0} years old".format(age))
# print("My age {0} rima's age {1} sima's age {2} raihan's age {3} years old".format(age, age1, age2, age3))
# print("My age is %d %s, %d %s" % (age,"years", 7, "months."))

print("The First one")
for i in range(1, 12):
    print("No. %2d squared is %4d and cubed is %6d" %(i, i**2, i**3))
print("The second one")

for i in range(1, 12):
    print("No. {0:2} squared is {1:4} and cubed is {2:6}".format(i, i**2, i**3))
print("The Third one")
for i in range(1, 12):
    print("No. {0:<2} squared is {1:<4} and cubed is {2:<6}".format(i, i**2, i**3))