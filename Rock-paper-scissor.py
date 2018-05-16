''' Rock Paper Scissor Mini Project BASIC Version'''
# print("...rock...")
# print("...paper...")
# print("...scissors...")
#
# player1 = input("(enter Player 1's choice): ")
# player2 = input("(enter Player 2's choice): ")
#
# print("SHOOT!")
#
#
#
# #Main solution
# print("Rock...")
# print("Paper...")
# print("Scissors...")
#
# # player1 = input("Player 1, make your move: ")
# # player2 = input("Player 2, make your move: ")
#
# if player1 == "rock" and player2 == "scissors":
#     print("player1 wins!")
# elif player1 == "rock" and player2 == "paper":
#     print("player2 wins!")
# elif player1 == "paper" and player2 == "rock":
#     print("player1 wins!")
# elif player1 == "paper" and player2 == "scissors":
#     print("player2 wins!")
# elif player1 == "scissors" and player2 == "rock":
#     print("player2 wins!")
# elif player1 == "scissors" and player2 == "paper":
#     print("player1 wins!")
# elif player1 == player2:
#     print("It's a tie!")
# else:
#     print("something went wrong")



'''RPS Mini Project Refactoring Time'''
# print("Rock...")
# print("Paper...")
# print("Scissors...")
#
# player1 = input("Player 1, make your move: ")
# print("***NO CHEATING!\n\n" * 20)
# player2 = input("Player 2, make your move: ")
#
# if player1 == player2:
#     print("It's a tie!")
# elif player1 == "rock":
#     if player2 == "scissors":
#         print("player1 wins!")
#     elif player2 == "paper":
#         print("player2 wins!")
# elif player1 == "paper":
#     if player2 == "rock":
#         print("player1 wins!")
#     elif player2 == "scissors":
#         print("player2 wins!")
# elif player1 == "scissors":
#     if player2 == "paper":
#         print("player1 wins!")
#     elif player2 == "rock":
#         print("player2 wins!")
# else:
#     print("something went wrong")


'''RPS Mini Project Computer AI Solution'''
from random import randint

player = input("Player, make your move: ").lower()
rand_num = randint(0,2)

if rand_num == 0:
    computer = "rock"
elif rand_num == 1:
    computer = "paper"
else:
    computer = "scissors"

print(f"Computer plays {computer}" )

if player == computer:
    print("It's a tie!")
elif player == "rock":
    if computer == "scissors":
        print("player wins!")
    else:
        print("computer wins!")
elif player == "paper":
    if computer == "rock":
        print("player wins!")
    else:
        print("computer wins!")
elif player == "scissors":
    if computer == "paper":
        print("player wins!")
    else:
        print("computer wins!")
else:
    print("Please enter a valid move!")
