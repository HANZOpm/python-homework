# Task 1
# ism = input("Ismingizni kiriting: ")
# yil = int(input("Tug'ilgan yilingizni kiriting: "))
#
# yosh = 2025 - yil
#
# print(f"{ism}, sizning yoshingiz: {yosh} da")
# Task 2
# I couldn't do it
# Task 3
# word = input("So'z kiriting: ")
#
# word_uppercase = word.upper()
# word_lowercase = word.lower()
#
# print(f"uppercase: {word_uppercase}")
# print(f"lowercase: {word_lowercase}")
# Task 4
# my_str = input("Input: ")
#
# my_str_lower = my_str.lower()
#
# text = f"{my_str} palindrom"
#
# if not my_str_lower == my_str_lower[::-1]:
#     text += " emas"
#
# print(text)
# Task 5
# vowels = "aeiou"
#
# text = input("Input: ")
#
# vowels_count = 0
# consonants_count = 0
#
# for i in text:
#     if i in vowels:
#         vowels_count += 1
#     else:
#         consonants_count += 1
#
# print(f"Vowels: {vowels_count}")
# print(f"Consonants: {consonants_count}")
# Task 6
# text1 = input("Enter first text: ")
# text2 = input("Enter second text: ")
#
# if text2 in text1 or text1 in text2:
#     print("True")
# else:
#     print("False")
# Task 7
# text = input("Input sentence: ")
# word1 = input("Replace: ")
# if word1 in text:
#     word2 = input("With: ")
#     new_text = text.replace(word1, word2)
#     print("Output:", new_text)
# else:
#     print(f"Error: \"{text}\" does not contain \"{word1}\"")
# Task 8
# text = input("Enter a string: ")
#
# if len(text) > 0:
#     print("First character:", text[0])
#     print("Last character:", text[-1])
# else:
#     print("String can't be empty.")
# Task 9
# text = input("Enter a string: ")
# print(text[::-1])
# Task 10
# text = input("Enter text: ")
#
# new_text = text.split(" ")
#
# print(f"Text has {len(new_text)} words in it.")
# Task 11
# text = input("Input: ")
# check = False
# for i in text:
#     if i.isdigit():
#         check = True
#
# print(check)
# Task 12
# text = input("Enter a sentence: ")
# list = text.split(" ")
# new_text = ""
# for i in list:
#     new_text += f"{i}-"
#
# print(new_text[:-1])
# Task 13
# text = input("Input: ")
# new_text = text.replace(" ", "")
# print(new_text)
# Task 14
# string1 = input("Enter first string: ")
# string2 = input("Enter second string: ")
#
# if string1 == string2:
#     print(True)
# else:
#     print(False)
# Task 15
# text = input("Enter a sentence: ")
# words = text.split(" ")
# acronym = ""
# for i in words:
#     acronym += i[0].upper()
#
# print("Acronym for this sentence:", acronym)
# Task 16
# text = input("Enter a string: ")
# character = input("Enter a character to remove from the string: ")
#
# new_text = text.replace(character, "")
#
# print(new_text)
# Task 17
# vowels = "euioa"
# text = input("Enter a string: ")
# new_text = ""
# for i in text:
#     if i.lower() in vowels:
#         new_text += "*"
#     else:
#         new_text += i
#
# print(new_text)
# Task 18
# text = input("Enter a text: ")
# list = text.split(" ")
#
# print("The text starts with:", list[0])
# print("The text ends with:", list[-1])