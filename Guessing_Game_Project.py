'''This is a Guessing Game Mini Project'''
# handle user guesses
#   if they guess correct, tell them they won
#     otherwise tell them if they are too high or too low

# BONUS - let player play again if they want!

#part1
# import random
#
# random_number = random.randint(1,10)  # numbers 1 - 10
# guess = None
#
# while guess != random_number:
#     guess = input("Pick a number from 1 to 10: ")
#     guess = int(guess)
#     if guess < random_number:
#         print("TOO LOW!")
#     elif guess > random_number:
#         print("TOO HIGH!")
#     else:
#         print("YOU WON!!!!")
#
# print(random_number)

#part2
# import random
#
# random_number = random.randint(1,10)  # numbers 1 - 10
# guess = None
#
# while True:
#     guess = input("Pick a number from 1 to 10: ")
#     guess = int(guess)
#     if guess < random_number:
#         print("TOO LOW!")
#     elif guess > random_number:
#         print("TOO HIGH!")
#     else:
#         print("YOU WON!!!!")
#         play_again = input("Do you want to play again? (y/n) ")
#         if play_again == "y":
#             random_number = random.randint(1,10)  # numbers 1 - 10
#             guess = None
#         else:
#             print("Thank you for playing!")
#             break


# rps-with-loop
from random import randint
player_wins = 0
computer_wins = 0
winning_score = 3

while player_wins < winning_score and computer_wins < winning_score:
    print(f"Player Score: {player_wins} Computer Score: {computer_wins}")
    print("...rock...")
    print("...paper...")
    print("...scissors...")

    player = input("(Enter your choice): ").lower()
    if player == "quit" or player == "q":
        break
    random_num = randint(0, 2)
    if (random_num == 0):
        computer = "rock"
    elif (random_num == 1):
        computer = "paper"
    else:
        computer = "scissors"

    print(f"The computer plays: {computer}")

    if player == computer:
        print("It's a tie!")
    elif player == "rock":
        if computer == "paper":
            print("Computer wins :( ")
            computer_wins += 1
        else:
            print("Player wins!")
            player_wins += 1
    elif player == "paper":
        if computer == "rock":
            print("Player win!")
            player_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1
    elif (player == "scissors"):
        if (computer == "rock"):
            print("Computer wins!")
            computer_wins += 1
        else:
            print("You win!")
            player_wins += 1
    else:
        print("Please enter a valid move!")

if player_wins > computer_wins:
    print("CONGRATS, YOU WON!")
elif player_wins == computer_wins:
    print("IT'S A TIE")
else:
    print("OH NO :( THE COMPUTER WON...")
