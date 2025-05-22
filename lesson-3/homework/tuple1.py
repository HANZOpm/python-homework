# Task 1
# User enters a list of elements
# items = tuple(input("Enter a list of elements (separated by spaces): ").split())
# User enters an element to count
# element = input("Enter an element to count: ")
# Checks if user entered something
# if items:
#     if element in items:
#         print(f"The element appears {items.count(element)} times in the tuple")
#     else:
#         print("The element doesn't appear in the tuple")
# else:
#     print("Please enter something")
# Task 2
# User enters a list of numbers
# items = input("Enter a list of numbers (separated by spaces): ")
# Checks if user entered something
# if items:
    # Checks if user entered only numbers
    # if items.replace(" ", "").replace("-", "").isdigit():
    #     items_list = tuple((int(i) for i in items.split()))
        # Displays the result
        # print("Largest element of the given tuple:", max(items_list))
    # else:
    #     print("Please enter only numbers")
# else:
#     print("Please enter something")
# Task 3
# User enters a list of numbers
# items = input("Enter a list of numbers (separated by spaces): ")
# Checks if user entered something
# if items:
    # Checks if user entered only numbers
    # if items.replace(" ", "").replace("-", "").isdigit():
    #     items_list = tuple((int(i) for i in items.split()))
        # Displays the result
        # print("Smallest element of the given tuple:", min(items_list))
    # else:
    #     print("Please enter only numbers")
# else:
#     print("Please enter something")
# Task 4
# User enters a list of elements
# items = tuple(input("Enter a list of elements (separated by spaces): ").split())
# User enters an element to check
# element = input("Enter an element to check presense: ")
# Checks if user entered something
# if items:
    # Checks if the element is in the tuple
    # if element in items:
    #     print("The given element is present in the tuple")
    # else:
    #     print("The given element is not present in the tuple")
# else:
#     print("Please enter something")
# Task 5
# User enters a list of elements
# items = tuple(input("Enter a list of elements (separated by spaces): ").split())
# Checks if user entered something
# if items:
    # Displays the first element of the tuple
    # print("The first element of the tuple:", items[0])
# else:
#     print("Please enter something")
# Task 6
# User enters a list of elements
# items = tuple(input("Enter a list of elements (separated by spaces): ").split())
# Checks if user entered something
# if items:
    # Displays the last element of the tuple
    # print("The last element of the tuple:", items[-1])
# else:
    # print("Please enter something")
# Task 7
# User enters a list of elements
# items = tuple(input("Enter a list of elements (separated by spaces): ").split())
# Checks if user entered something
# if items:
    # Displays the number of elements in the tuple
    # print("The number of elements in the tuple:", len(items))
# else:
#     print("Please enter something")
# Task 8
# User enters a list of elements
# items = tuple(input("Enter a list of elements (separated by spaces): ").split())
# Checks if user entered something
# if items:
    # Creates a new tuple that contains only first three elements
    # new_tuple = items[:3]
    # Displays the result
    # print("Here is the new tuple that contains only first three elements:", new_tuple)
# else:
#     print("Please enter something")
# Task 9
# User enters a list of elements
# items1 = tuple(input("Enter the first list (separated by spaces): ").split())
# items2 = tuple(input("Enter the second list (separated by spaces): ").split())
# Checks if user entered something
# if items1 and items2:
    # Creates a new tuple that combines both
    # new_tuple = items1 + items2
    # Displays the result
    # print("Here is the new tuple that combines both tuples:", new_tuple)
# else:
#     print("Please enter something")
# Task 10
# User enters a list of elements
# items = tuple(input("Enter a list of elements (separated by spaces): ").split())
# Checks if user entered something
# if items:
#     print("Tuple has elements")
# else:
#     print("Tuple is empty")
# Task 11
# User enters a list of elements
# items = tuple(input("Enter a list of elements (separated by spaces): ").split())
# User enters an element
# element = input("Enter an element: ")
# Checks if user entered something
# if items:
    # Checks if element is in the tuple
    # if element in items:
    #     count = 0
    #     indices = []
        # Appends indices of the element to the new list
        # for i in items:
        #     if i == element:
        #         indices.append(count)
        #     count += 1
        # Displays the result
        # print("Here is the indices of the given element:", indices)
    # else:
    #     print("Element doesn't appear in the tuple")
# else:
#     print("Please enter something")
# Task 12
# User enters a list of numbers
# items = input("Enter a list of numbers (separated by spaces): ")
# Checks if user entered something
# if items.replace(" -", "").replace(" ", "").isdigit():
#     items_tuple = tuple(items.split())
    # Sorts the given tuple
    # new_list = sorted(tuple(set(items_tuple)))
    # Checks if the tuple has more than 2 elements
    # if len(new_list) >= 2:
    #     print("Here is the second largest number in the list:", new_list[-2])
    # else:
    #     print("The tuple has only one element:", new_list[0])
# else:
#     print("Please enter only numbers")
# Task 13
# User enters a list of numbers
# items = input("Enter a list of numbers (separated by spaces): ")
# Checks if user entered something
# if items.replace(" -", "").replace(" ", "").isdigit():
#     items_tuple = tuple(items.split())
    # Sorts the given tuple
    # new_list = sorted(tuple(set(items_tuple)))
    # Checks if the tuple has more than 2 elements
    # if len(new_list) >= 2:
    #     print("Here is the second smallest number in the list:", new_list[1])
    # else:
    #     print("The tuple has only one element:", new_list[0])
# else:
#     print("Please enter only numbers")
# Task 14
# User enters an element
# item = input("Enter an element: ")
# Checks if user entered something
# if item:
    # Checks if user entered only one element
    # if len(item.split()) == 1:
    #     new_tuple = (item.strip(),)
    #     print("Here is the tuple:", new_tuple)
    # else:
    #     print("Please enter only one element")
# else:
#     print("Please enter something")
# Task 15
# User enters a list of elements
# items = input("Enter a list of elements (separated by spaces): ").split()
# Checks if user entered something
# if items:
    # Creates a new tuple from the list
    # new_tuple = tuple(items)
    # Displays the result
    # print("Here is the tuple:", new_tuple)
# else:
#     print("Please enter something")
# Task 16
# User enters a list of elements
# items = tuple(input("Enter a list of elements (separated by spaces): ").split())
# Checks if user entered something
# if items:
    # Checks if the tuple is sorted and returns a boolean
    # print(items == tuple(sorted(items)))
# else:
#     print("Please enter something")
# Task 17
# User enters a list of numbers
# numbers = input("Enter a list of numbers (separated by spaces): ")
# User enters starting and ending  index of a specified subtuple
# start = input("Enter starting index of a specified sublist: ")
# end = input("Enter ending index of a specified sublist: ")
# Checks if user entered only numbers
# if numbers.replace(" -", "").replace(" ", "").isdigit() and start.isdigit() and end.isdigit():
#     numbers_tuple = tuple(numbers.split())
    # Gets a subtuple from a tuple
    # numbers_list = tuple(int(i) for i in numbers_tuple[int(start):int(end)])
    # Checks if subtuple has elements
    # if numbers_list:
    #     print("Maximum of a given subtuple:", max(numbers_list))
    # else:
    #     print("There is no element in the given subtuple")
# else:
#     print("Please enter only numbers")
# Task 18
# User enters a list of numbers
# numbers = input("Enter a list of numbers (separated by spaces): ")
# User enters starting and ending  index of a specified subtuple
# start = input("Enter starting index of a specified sublist: ")
# end = input("Enter ending index of a specified sublist: ")
# Checks if user entered only numbers
# if numbers.replace(" -", "").replace(" ", "").isdigit() and start.isdigit() and end.isdigit():
#     numbers_tuple = tuple(numbers.split())
    # Gets a subtuple from a tuple
    # numbers_list = tuple(int(i) for i in numbers_tuple[int(start):int(end)])
    # Checks if subtuple has elements
    # if numbers_list:
    #     print("Minimum of a given subtuple:", min(numbers_list))
    # else:
    #     print("There is no element in the given subtuple")
# else:
#     print("Please enter only numbers")
# Task 19
# User enters a list of elements
# items = tuple(input("Enter a list of elements (separated by spaces): ").split())
# User enters an element to remove
# element = input("Enter an element to remove: ")
# Checks if user entered something
# if items:
    # Checks if element is in the tuple
    # if element in items:
    #     list1 = list(items)
    #     list1.remove(element)
    #     new_tuple = tuple(list1)
    #     print("Here is the new tuple:", new_tuple)
    # else:
    #     print("The tuple doesn't contain given element")
# else:
#     print("Please enter something")
# Task 20
# User enters a list of elements
# items = tuple(input("Enter a list of elements (separated by spaces): ").split())
# User enters the length of subtuples
# subtuple_size = input("Enter the length of subtuples: ")
# Checks if user entered something
# if items:
    # Checks if user entered only numbers
    # if subtuple_size.isdigit():
    #     subtuple_size = int(subtuple_size)
    #     new_tuple = tuple(items[i:i+subtuple_size] for i in range(0, len(items), subtuple_size))
    #     print("Here is the new tuple:", new_tuple)
    # else:
    #     print("Please enter the length of subtuples only in numbers")
# else:
#     print("Please enter something")
# Task 21
# User enters a list of elements
# items = tuple(input("Enter a list of elements (separated by spaces): ").split())
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
    #     new_tuple = tuple(new_list)
    #     print(new_tuple)
    # else:
    #     print("Please enter numbers only")
# else:
#     print("Please enter something")
# Task 22
# User enters starting number, ending number and step
# start = input("Enter starting number: ")
# end = input("Enter ending number: ")
# step = input("Enter step: ")
# Checks if user entered only numbers
# if start.isdigit() and end.isdigit() and step.isdigit():
#     if int(step) > 0:
#         new_tuple = tuple(i for i in range(int(start), int(end), int(step)))
        # Displays the result
        # print("Here is the tuple:", new_tuple)
    # else:
    #     print("Step must be greater than zero")
# else:
#     print("Please enter only numbers")
# Task 23
# User enters a list of elements
# items = tuple(input("Enter a list of elements (separated by spaces): ").split())
# Checks if user entered something
# if items:
    # Creates new tuple in reversed order
    # new_tuple = items[::-1]
    # Displays the result
    # print(new_tuple)
# else:
#     print("Please enter something")
# Task 24
# User enters a list of elements
# items = tuple(input("Enter a list of elements (separated by spaces): ").split())
# Checks if user entered something
# if items:
    # Checks if the tuple is palindrome
    # if items == items[::-1]:
    #     print("The given tuple is palindrome")
    # else:
    #     print("The given tuple is not palindrome")
# else:
#     print("Please enter something")
# Task 25
# User enters a list of elements
# items = tuple(input("Enter a list of elements (separated by spaces): ").split())
# Checks if user entered something
# if items:
#     new_list = []
#     for i in items:
#         if i not in new_list:
#             new_list.append(i)
#     new_tuple = tuple(new_list)
    # Displays the result
    # print("Here is the tuple that contains unique elements:", new_tuple)
# else:
#     print("Please enter something")