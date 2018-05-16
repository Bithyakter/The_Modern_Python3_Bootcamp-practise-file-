'''For Loop'''
# for x in range(1,10):
# 	print(x)
# 	# print(x*x)                #Try this next
#
# for letter in "coffee":
#     print(letter)
#     # print(letter*10)          #Try this next
#
#
# '''Range'''
# for num in range(12):
#     print(num)
#
#
# for num in range(10,100,2):
#     print(num)
#

'''repeater'''
# times = input("How many times do I have to tell you? ")
# times = int(times)
#
# # Simplest Version
# for time in range(6):
#     print("CLEAN UP YOUR ROOM")             ###inter your input
#
# # Version 2
# for time in range(times):
#     print(f"time {time+1}:CLEAN UP YOUR ROOM")


# Main Solution
# for num in range(1,21):
#     if num == 4 or num == 13:
#         print(f"{num} is unlucky")
#     elif num % 2 == 0:
#         print(f"{num} is even")
#     else:
#         print(f"{num} is odd")
#
#
# # Slight Refactor
# for num in range(1,21):
#     if num == 4 or num == 13:
#         state = "unlucky"
#     elif num % 2 == 0:
#         state = "even"
#     else:
#         state = "odd"
#     print(f"{num} is {state}")


# Continues to ask for user input until the user types 'bananas'
# msg = input("whats the secret password?")
# while msg != "bananas":
#     print("WRONG!")
#     msg = input("whats the secret password?")
# print("CORRECT!")
#
#
# # for num in range(1,11):
# # 	print(num)
#
# # equivalent of above for loop
# num = 1
# while num < 11:
#     print(num)
#     num += 1



'''EXERCISE Emoji Art'''
# With a for loop
# for x in range(1):
#     for num in range(1,11):
#         print("\U0001f600" * num)
#
# # With a while loop
# times = 1
# while times < 11:
#     print("\U0001f600" * times)
#     times += 1
#
# # Without string multiplication - ugly solution
# for num in range(1,11):
# 	count = 1
# 	smileys = ""
# 	while count <= num:
# 		smileys += "\U0001f600"
# 		count += 1
# 	print(smileys)


####Stop copying me
msg = input("Say Something: ")

while msg != "stop copying me":
    print(msg)
    msg = input()
print("UGH FINE YOU WIN, BROTHER!")

while msg != "stop copying me":
    msg = input(f"{msg}\n")
print("UGH FINE YOU WIN, BROTHER!")



''' The Break Keyword'''
# while True:
#     command = input("Type 'exit' to exit: ")
#     if (command == "exit"):
#         break
#
# for x in range(1, 101):
#     print(x)
#     if x == 3:
#         break
#
# times = int(input("How many times do I have to tell you? "))
#
# for time in range(times):
#     print("CLEAN UP YOUR ROOM!")
#     if time >= 3:
#         print("do you even listen anymore?")
#         break
#
