# Task 1
# User enters a list of elements
# items = input("Enter a list of elements (separated by spaces): ").split()
#
# # User enters an element to count
# element = input("Enter an element: ")
#
# # Checks if user entered something
# if len(element.strip()) > 0:
#     # Counts occurrences
#     count = items.count(element)
#
# # Displays the result
# print(f"{element} appears {count} times in the list")
# Task 2
# """User enters a list of numbers"""
# numbers = input("Enter a list of numbers (separated by spaces): ")
# Checks if user entered only numbers
# if numbers.replace(" ", "").replace("-", "").isdigit():
#     numbers_list = numbers.split()
    # Calculates the sum of numbers in the list
    # total = 0
    # for i in numbers_list:
    #     total += int(i)
    # print("The sum of given numbers is:", total)
# else:
#     print("Please enter only numbers")
# Task 3
# User enters list of elements
# elements = input("Enter a list of numbers (separated by spaces): ")
# Checks if elements are only numbers
# if elements.replace(" ", "").replace("-", "").isdigit():
#     Makes list of numbers
#     elements_list = [int(i) for i in elements.split()]
#     Displays the largest number in the list
#     print(max(elements_list))
# else:
#     print("Please enter numbers only")
# Task 4
# User enters list of elements
# elements = input("Enter a list of numbers (separated by spaces): ")
# Checks if elements are only numbers
# if elements.replace(" ", "").replace("-", "").isdigit():
#     Makes list of numbers
#     elements_list = [int(i) for i in elements.split()]
#     Displays the smallest number in the list
#     print(min(elements_list))
# else:
#     print("Please enter numbers only")
# Task 5
# User enters a list of elements
# items = input("Enter a list of elements (separated by spaces): ").split()
# User enters an element
# element = input("Enter an element: ")
# Checks if element is in the list
# if element in items:
#     print(f"{element} is present in the list")
# else:
#     print(f"{element} is not present in the list")
# Task 6
# User enters a list of elements
# items = input("Enter a list of elements (separated by spaces): ").split()
# Checks if the list is empty
# if items:
#     print("The first element of the list:", items[0])
# else:
#     print("The list is empty")
# Task 7
# User enters a list of elements
# items = input("Enter a list of elements (separated by spaces): ").split()
# Checks if the list is empty
# if items:
#     print("The last element of the list:", items[-1])
# else:
#     print("The list is empty")
# Task 8
# User enters a list of elements
# items = input("Enter a list of elements (separated by spaces): ").split()
# Checks if the list is not empty
# if items:
    # new_list = items[:3]
    # Display the result
#     print(new_list)
# else:
#     print("Please enter something")
# Task 9
# User enters a list of elements
# items = input("Enter a list of elements (separated by spaces): ").split()
# Checks if user entered something
# if items:
    # Creates new list in reversed order
    # new_list = items[::-1]
    # Displays the result
#     print(new_list)
# else:
#     print("Please enter something")
# Task 10
# User enters a list of elements
# items = input("Enter a list of elements (separated by spaces): ")
# Checks if items contains only digits
# if items.replace(" ", "").replace("-", "").isdigit():
    # Creates new list in sorted order
    # new_list = sorted([int(i) for i in items.split()])
    # Displays the result
    # print(new_list)
# else:
    # print("Please enter only numbers")
# Task 11
# User enters a list of elements
# items = input("Enter a list of elements (separated by spaces): ").split()
# new_list = []
# Checks if user entered something
# if items:
#     new_list = list(set(items))
#     Displays the result
#     print(new_list)
# else:
#     print("Please enter something")
# Task 12
# User enters a list of elements
# items = input("Enter a list of elements (separated by spaces): ").split()
# User enters an element to insert
# element = input("Enter an element to insert: ")
# User enters index
# number = input("Enter an index: ")
# Checks if user entered something
# if items:
    # Checks if element is not empty
    # if len(element.strip()) > 0:
        # Checks if number is digit
        # if number.isdigit():
            # number = int(number)
            # Inserts the element to the list
            # items.insert(number, element)
            # Display the result
#             print(f"\"{element}\" was successfully inserted to the list")
#             print(items)
#         else:
#             print("Please enter index in numbers")
#     else:
#         print("Please enter an element")
# else:
#     print("Please enter something")
# Task 13
# User enters a list of elements
# items = input("Enter a list of elements (separated by spaces): ").split()
# User enters an element to insert
# element = input("Enter an element to insert: ")
# Checks if user entered something
# if items:
    # Checks if element is not empty
    # if len(element.strip()) > 0:
        # Checks if element is in the list
        # if element in items:
        #     print(f"{element} first occurence in the list index: {items.index(element)}")
        # else:
        #     print("Element is not in the list")
    # else:
    #     print("Please enter an element")
# else:
#     print("Please enter something")
# Task 14
# User enters a list of elements
# items = input("Enter a list of elements (separated by spaces): ").split()
# Checks if user entered something
# print(bool(items))
# Task 15
# User enters a list of numbers
# items = input("Enter a list of numbers (separated by spaces): ")
# Checks if user entered only numbers
# if items.replace(" ", "").replace("-", "").isdigit():
    # Makes a list of numbers given
    # new_list = items.split()
    # count = 0
    # for i in new_list:
    #     if int(i) % 2 == 0:
    #         count += 1
    # print(f"Number of even numbers in the list: {count}")
# else:
#     print("Please enter only numbers")
# Task 16
# User enters a list of numbers
# items = input("Enter a list of numbers (separated by spaces): ")
# Checks if user entered only numbers
# if items.replace(" ", "").replace("-", "").isdigit():
    # Makes a list of numbers given
    # new_list = items.split()
    # count = 0
    # for i in new_list:
    #     if int(i) % 2 != 0:
    #         count += 1
    # print(f"Number of odd numbers in the list: {count}")
# else:
#     print("Please enter only numbers")
# Task 17
# User enters a list of elements
# list1 = input("Enter a list of elements for the first list (separated by spaces): ").split()
# list2 = input("Enter a list of elements for the first list (separated by spaces): ").split()
# Combine them
# combined_list = list1 + list2
# Display the result
# print("Combined list:", combined_list)
# Task 18
# User enters a list of elements
# list = input("Enter a list of elements for the list (separated by spaces): ").split()
# sublist = input("Enter a list of elements for the sublist (separated by spaces): ").split()
# Checks if user entered something
# if list and sublist:
#     Checks if the list contains the elements of the sublist
#     found = True
#     for i in sublist:
#         if i not in list:
#             found = False
#     if found:
#         print("The list contains the elements of the sublist")
#     else:
#         print("The list does not contain all of the elements of the sublist")
# else:
#     print("Please enter something")
# Task 19
# User enters a list of elements
# list = input("Enter a list of elements (separated by spaces): ").split()
# element = input("Replace: ")
# replacement = input("With: ")
# Checks if user entered something
# if list:
#     Checks if element is in the list
#     if element in list:
#         Checks if user entered something
#         if len(replacement.strip()) > 0:
#             Replaces the given element with another
#             list[list.index(element)] = replacement
#             Display the result
#             print(list)
#         else:
#             print("Please enter something")
#     else:
#         print("Element is not in the list")
# else:
#     print("Please enter something")
# Task 20
# User enters a list of numbers
# items = input("Enter a list of numbers (separated by spaces): ")
# Checks if items contains only digits
# if items.replace(" ", "").replace("-", "").isdigit():
    # Creates new list in sorted order
    # new_list = sorted(list(set([int(i) for i in items.split()])))
    # if len(new_list) >= 2:
        # Displays the result
        # print(f"Second largest number in the list: {new_list[-2]}")
    # else:
    #     print("The list contains only one number")
# else:
#     print("Please enter only numbers")
# Task 21
# User enters a list of numbers
# items = input("Enter a list of numbers (separated by spaces): ")
# Checks if items contains only digits
# if items.replace(" ", "").replace("-", "").isdigit():
    # Creates new list in sorted order
    # new_list = sorted(list(set([int(i) for i in items.split()])))
    # if len(new_list) >= 2:
        # Displays the result
        # print(f"Second smallest number in the list: {new_list[1]}")
    # else:
    #     print("The list contains only one number")
# else:
#     print("Please enter only numbers")
# Task 22
# User enters a list of numbers
# items = input("Enter a list of numbers (separated by spaces): ")
# Checks if user entered only numbers
# if items.replace(" ", "").replace("-", "").isdigit():
    # Makes a list of numbers given
    # new_list = items.split()
    # even_numbers = []
    # for i in new_list:
    #     if int(i) % 2 == 0:
    #         even_numbers.append(int(i))
    # print(f"New list that contains only even numbers:", even_numbers)
# else:
#     print("Please enter only numbers")
# Task 23
# User enters a list of numbers
# items = input("Enter a list of numbers (separated by spaces): ")
# Checks if user entered only numbers
# if items.replace(" ", "").replace("-", "").isdigit():
    # Makes a list of numbers given
    # new_list = items.split()
    # even_numbers = []
    # for i in new_list:
    #     if int(i) % 2 != 0:
    #         even_numbers.append(int(i))
    # print(f"New list that contains only odd numbers:", even_numbers)
# else:
    # print("Please enter only numbers")
# Task 24
# User enters a list of elements
# items = input("Enter a list of elements (separated by spaces): ").split()
# Checks if user entered something
# if items:
#     print("Number of elements in the list:", len(items))
# else:
#     print("Please enter something")
# Task 25
# User enters a list of elements
# items = input("Enter a list of elements (separated by spaces): ").split()
# Checks if user entered something
# if items:
    # Copies elements to a new list
    # new_list = items.copy()
    # Displays the result
    # print(f"Here is a copy of the list:", new_list)
# else:
#     print("Please enter something")
# Task 26
# User enters a list of elements
# items = input("Enter a list of elements (separated by spaces): ").split()
# Checks if user entered something
# if items:
    # Gets length of the list
    # length = len(items)
    # Checks if the list has even number of elements
    # if length % 2 == 0:
    #     print("Middle elements of the list:", items[length//2-1], items[length//2])
    # else:
    #     print("Middle element of the list:", items[length//2])
# else:
#     print("Please enter something")
# Task 27
# User enters a list of numbers
# numbers = input("Enter a list of numbers (separated by spaces): ")
# User enters starting and ending  index of a specified sublist
# start = input("Enter starting index of a specified sublist: ")
# end = input("Enter ending index of a specified sublist: ")
# Checks if user entered only numbers
# if numbers.replace(" ", "").replace("-", "").isdigit() and start.isdigit() and end.isdigit():
#     numbers_list = [int(i) for i in numbers.split()[int(start):int(end)]]
#     if numbers_list:
#         print("Maximum of a given sublist:", max(numbers_list))
#     else:
#         print("There is no element in the given sublist")
# else:
#     print("Please enter only numbers")
# Task 28
# User enters a list of numbers
# numbers = input("Enter a list of numbers (separated by spaces): ")
# User enters starting and ending  index of a specified sublist
# start = input("Enter starting index of a specified sublist: ")
# end = input("Enter ending index of a specified sublist: ")
# Checks if user entered only numbers
# if numbers.replace(" ", "").replace("-", "").isdigit() and start.isdigit() and end.isdigit():
#     numbers_list = [int(i) for i in numbers.split()]
#     if numbers_list:
#         print("Minimum of a given sublist:", min(numbers_list))
#     else:
#         print("There is no element in the given sublist")
# else:
#     print("Please enter only numbers")
# Task 29
# User enters a list of elements
# items = input("Enter a list of elements (separated by spaces): ").split()
# User enters index
# number = input("Enter an index: ")
# Checks if user entered something
# if items:
    # Checks if number is digit
    # if number.isdigit():
    #     number = int(number)
    #     Checks if the element at that index exists
        # if len(items) > number:
        #     items.pop(number)
        #     Display the result
            # print(f"The element at the index {number} was successfully removed")
            # print(items)
        # else:
        #     print("There is no element in such index")
    # else:
    #     print("Please enter index in numbers")
# else:
#     print("Please enter something")
# Task 30
# User enters a list of numbers
# items = input("Enter a list of numbers (separated by spaces): ")
# Checks if items contains only numbers
# if items.replace(" ", "").replace("-", "").isdigit():
#     Splits to the list
    # items_list = [int(i) for i in items.split()]
    # Creates new list in sorted order
    # new_list = sorted(items_list)
    # Displays the result
    # print(items_list == new_list)
# else:
#     print("Please enter only numbers")
# Task 31
# User enters a list of elements
# items = input("Enter a list of elements (separated by spaces): ").split()
# User enters a number
# number = input("Enter how many times should elements be repeated: ")
# Checks if the list contains something
# if items:
    # Checks if number is digit
    # if number.isdigit():
        # Creates a new list
        # new_list = []
        # Repeats elements in the new list
        # for i in items:
        #     if i not in new_list:
        #         for x in range(int(number)):
        #             new_list.append(i)
    #     Displays the result
    #     print(new_list)
    # else:
    #     print("Please enter numbers only")
# else:
#     print("Please enter something")
# Task 32
# User enters a list of elements
# items1 = input("Enter the first list (separated by spaces): ").split()
# items2 = input("Enter the second list (separated by spaces): ").split()
# Checks if the list contains something
# if items1 and items2:
#     # Creates new list that merges both lists
#     new_list = list(set(items1 + items2))
#     DIsplays the result
#     print(new_list)
# else:
#     print("Please enter something")
# Task 33
# User enters a list of elements
# items = input("Enter a list of elements (separated by spaces): ").split()
# User enters which element's indexes must be displayed
# target = input("Enter the element to see indices: ")
# Checks if user entered something
# if items:
#     if target in items:
#         indices_list = []
#         count = 0
#         for i in items:
#             if i == target:
#                 indices_list.append(count)
#             count += 1
#         Displays the result
#         print("Here are indices of the given element:", indices_list)
#     else:
#         print("Given element is not in the list")
# else:
#     print("Please enter something")
# Task 34
# User enters a list of elements
# items = input("Enter a list of elements (separated by spaces): ").split()
# Checks if user entered something
# if items:
    # new_list = items[::-1]
    # Displays the result
#     print("Here is the rotated version of the list:", new_list)
# else:
#     print("Please enter something")
# Task 35
# User enters starting number, ending number and step
# start = input("Enter starting number: ")
# end = input("Enter ending number: ")
# step = input("Enter step: ")
# Checks if user entered only numbers
# if start.isdigit() and end.isdigit() and step.isdigit():
#     new_list = [i for i in range(int(start), int(end), int(step))]
    # Displays the result
    # print("Here is the list:", new_list)
# else:
#     print("Please enter only numbers")
# Task 36
# User enters a list of numbers
# numbers = input("Enter a list of numbers (separated by spaces): ")
# Checks if user entered only numbers
# if numbers.replace(" ", "").replace("-", "").isdigit():
    # numbers_list = [int(i) for i in numbers.split() if int(i) > 0]
    # Displays the result
    # print("The sum of positive numbers of the given list:", sum(numbers_list))
# else:
#     print("Please enter only numbers")
# Task 37
# User enters a list of numbers
# numbers = input("Enter a list of numbers (separated by spaces): ")
# Checks if user entered only numbers
# if numbers.replace(" ", "").replace("-", "").isdigit():
#     numbers_list = [int(i) for i in numbers.split() if int(i) < 0]
    # Displays the result
    # print("The sum of negative numbers of the given list:", sum(numbers_list))
# else:
#     print("Please enter only numbers")
# Task 38
# User enters a list of elements
# items = input("Enter a list of elements (separated by spaces): ").split()
# Checks if user entered something
# if items:
#     if items == items[::-1]:
#         print("The given list is palindrome")
#     else:
#         print("The given list is not palindrome")
# else:
#     print("Please enter something")
# Task 39
# User enters a list of elements
# items = input("Enter a list of elements (separated by spaces): ").split()
# User enters the length of sublists
# sublist_size = input("Enter the length of sublists: ")
# Checks if user entered something
# if items:
    # Checks if user enterd only numbers
    # if sublist_size.isdigit():
    #     sublist_size = int(sublist_size)
    #     new_list = [items[i:i+sublist_size] for i in range(0, len(items), sublist_size)]
    #     print("Here is the new list:", new_list)
    # else:
    #     print("Please enter the length of sublists only in numbers")
# else:
#     print("Please enter something")
# Task 40
# User enters a list of elements
# items = input("Enter a list of elements (separated by spaces): ").split()
# Checks if user entered something
# if items:
#     new_list = []
#     for i in items:
#         if i not in new_list:
#             new_list.append(i)
    # Displays the result
    # print("Here is the list that contains unique elements:", new_list)
# else:
#     print("Please enter something")