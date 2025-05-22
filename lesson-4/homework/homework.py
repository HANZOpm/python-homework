# Question 2
"""We use continue when we want to skip codes below and get back to the start of the loop and we use break when we
want to skip codes below and also stop the loop"""
# Question 3
"""codes in 'for loop' work in the fixed range or till we break and codes in 'while loop' work while given statement is 
boolean True or till we break"""
# Question 4
"""I would implement a nested for loop system like in the 'Task 6' below. I think 'Task 6' is enough to be an example."""
# Task 1
# list1 = [1, 1, 2, 3, 4, 2]
# list2 = [1, 3, 4, 5]
# new_list = []
# for i in list1:
#     if i not in list2:
#         new_list.append(i)
# for i in list2:
#     if i not in list1:
#         new_list.append(i)
# print(new_list)
# Task 2
# n = 5
# try:
#     int(n)
#     if n > 1:
#         for i in range(1, n):
#             print(i**2)
#     else:
#         print("n must be greater than 1")
# except:
#     print("n must be a digit")
# Task 3
# txt = "abcabcdabcdeabcdefabcdefg"
# vowels_list = ["a", "o", "u", "e", "i"]
# new_txt = ""
# letters_list = []
# count = 1
# for i in txt:
#     new_txt += i
#     if count == 3:
#         if i not in vowels_list:
#             if i not in letters_list:
#                 letters_list.append(i)
#                 new_txt += "_"
#                 count = 0
#             else:
#                 continue
#         else:
#             continue
#     count += 1
# if new_txt[-1] == "_":
#     new_txt = new_txt[:-1]
# print(new_txt)
# Task 4
# import random
# yes_list = ['Y', 'YES', 'y', 'yes', 'ok']
# game = True
# while game:
#     number = random.randint(1, 100)
#     print("Guess the number!")
#     for i in range(10):
#         guess = input(f"Attempt {i+1}: ")
#         if guess.isdigit():
#             guess = int(guess)
#             if guess == number:
#                 print(f"Congratulations you found the number in {i+1} attempts.")
#                 game = False
#                 break
#             elif guess > number:
#                 print("Too high!")
#             elif guess < number:
#                 print("Too low!")
#         else:
#             print("Please enter only numbers")
#     if game:
#         ask = input("You lost. Want to play again? ")
#         if ask not in yes_list:
#             break
# Task 5
# while True:
#     password = input("Please enter password: ")
#     if len(password) < 8:
#         print("Password is too short.")
#     elif password == password.lower():
#         print("Password must contain an uppercase letter.")
#     else:
#         print("Password is strong.")
#         break
# Task 6
# primes_list = []
# for number in range(2, 101):
#     prime = True
#     for i in range(2, number):
#         if number % i == 0:
#             prime = False
#     if prime:
#         primes_list.append(number)
# print(primes_list)
# Bonus challenge
# import random
# game_list = ["rock", "paper", "scissors"]
# computer_score = 0
# player_score = 0
# print("This is the game of rock, paper and scissors.")
# print("First to score 5 points, wins.")
# while computer_score < 5 and player_score < 5:
#     print("Computer points:", computer_score)
#     print("Player points:", player_score)
#     computer_choice = random.choice(game_list)
#     computer_index = game_list.index(computer_choice)
#     player_choice = input("Choose rock, paper or scissors: ")
#     if player_choice in game_list:
#         player_index = game_list.index(player_choice)
#         a = player_index - computer_index
#         if a == 1 or a == -2:
#             player_score += 1
#             print("Computer chose:", computer_choice)
#             print(f"{player_choice} > {computer_choice}")
#             print("Player won! +1 points")
#         elif a == 0:
#             print("Computer chose:", computer_choice)
#             print("Draw. +0 points")
#         else:
#             computer_score += 1
#             print("Computer chose:", computer_choice)
#             print(f"{computer_choice} > {player_choice}")
#             print("Computer won! +0 points")
#     else:
#         print("Please enter one of rock, paper and scissors")
# else:
#     if player_score == 5:
#         print("You won!")
#     else:
#         print("You lost!")