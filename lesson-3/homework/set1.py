# Task 1
# User enters a list of elements
# set1 = set(input("Enter a list of elements for the first set (separated by spaces): ").split())
# set2 = set(input("Enter a list of elements for the second set (separated by spaces): ").split())
# Checks if user entered something
# if set1 and set2:
#     Creates a new set that contains all unique elements
#     new_set = set1 | set2
#     Displays the result
#     print(new_set)
# else:
#     print("Please enter something")
# Task 2
# User enters a list of elements
# set1 = set(input("Enter a list of elements for the first set (separated by spaces): ").split())
# set2 = set(input("Enter a list of elements for the second set (separated by spaces): ").split())
# Checks if user entered something
# if set1 and set2:
#     Creates a new set that contains all common elements
#     new_set = set1 & set2
#     Displays the result
#     print(new_set)
# else:
#     print("Please enter something")
# Task 3
# User enters a list of elements
# set1 = set(input("Enter a list of elements for the first set (separated by spaces): ").split())
# set2 = set(input("Enter a list of elements for the second set (separated by spaces): ").split())
# if set1 and set2:
#     Creates a new set
#     set3 = set1 - set2
#     Displays the result
#     print(set3)
# else:
#     print("Please enter something")
# Task 4
# User enters a list of elements
# set1 = set(input("Enter a list of elements for the first set (separated by spaces): ").split())
# set2 = set(input("Enter a list of elements for the second set (separated by spaces): ").split())
# Checks if user entered something
# if set1 and set2:
#     Checks if set2 is in set1
#     if set2 <= set1:
#         print("Second set is a subset of the first set")
#     else:
#         print("Second set is not a subset of the first set")
# else:
#     print("Please enter something")
# Task 5
# User enters a list of elements
# set1 = set(input("Enter a list of elements for the set (separated by spaces): ").split())
# User enters an element to check
# element = input("Enter an element: ")
# Checks if user entered something
# if set1:
#     Checks if element is in the set
#     if element in set1:
#         print("The given element is in the set")
#     else:
#         print("The given element is not in the set")
# else:
#     print("Please enter something")
# Task 6
# User enters a list of elements
# set1 = set(input("Enter a list of elements for the set (separated by spaces): ").split())
# print("The number of elements in the list:", len(set1))
# Task 7
# User enters a list of elements
# list1 = input("Enter a list of elements for the set (separated by spaces): ").split()
# Creates a new set from the list
# set1 = set(list1)
# Displays the result
# print(set1)
# Task 8
# User enters a list of elements
# set1 = set(input("Enter a list of elements for the set (separated by spaces): ").split())
# user enters an element to remove
# element = input("Enter an element: ")
# Checks if user entered something
# if set1:
#     Removes the element from the set if it exists
#     set1.discard(element)
#     Displays the result
#     print("Element removed")
#     print(set1)
# else:
#     print("Please enter something")
# Task 9
# User enters a list of elements
# set1 = set(input("Enter a list of elements for the set (separated by spaces): ").split())
# Cleares the set
# set1.clear()
# print("The set is clear")
# print(set1)
# Task 10
# User enters a list of elements
# set1 = set(input("Enter a list of elements for the set (separated by spaces): ").split())
# Checks if set has any elements
# if set1:
#     print("Set has elements")
#     print(set1)
# else:
#     print("Set has no elements")
# Task 11
# User enters a list of elements
# set1 = set(input("Enter a list of elements for the first set (separated by spaces): ").split())
# set2 = set(input("Enter a list of elements for the second set (separated by spaces): ").split())
# Checks if user entered something
# if set1 and set2:
#     new_set = set1 ^ set2
#     print("Here is the new set:", new_set)
# else:
#     print("Please enter something")
# Task 12
# set1 = {1, 2, 3}
# element = input("Enter an element to add: ")
# if element not in set1:
#     set1.add(element)
#     print(f"{element} was added to the set")
# else:
#     print(f"{element} is already in the set")
# Task 13
# set1 = {10, 20, 30, 40}
# element = set1.pop()
# print("element:", element)
# print("set:", set1)
# Task 14
# set1 = {5, 12, 7, 3, 25, 9}
# print("Maximum element:", max(set1))
# Task 15
# set1 = {5, 12, 7, 3, 25, 9}
# print("Minimum element:", min(set1))
# Task 16
# set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# even_set = {i for i in set1 if i % 2 == 0}
# print("Even numbers set:", even_set)
# Task 17
# set1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# odd_set = {i for i in set1 if i % 2 != 0}
# print("Odd numbers set:", odd_set)
# Task 18
# set1 = set(range(1, 11, 2))
# print("Set from 1 to 10 by step 2:", set1)
# Task 19
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
# merged_set = set(list1 + list2)
# print("Merged set with duplicates removed:", merged_set)
# Task 20
# set1 = {1, 2, 3}
# set2 = {4, 5, 6}
# are_disjoint = set1.isdisjoint(set2)
# print("Are the sets disjoint?", are_disjoint)
# Task 21
# list1 = [1, 1, 1, 1, 1, 2, 2, 2, 3]
# set1 = set(list1)
# new_list = list(set1)
# print(new_list)
# Task 22
# list1 = [1, 1, 1, 1, 1, 2, 2, 2, 3]
# set1 = set(list1)
# print(len(set1))
# Task 23
# import random
# set1 = set()
# for i in range(5):
#     set1.add(random.randint(1, 20))
#
# print(set1)