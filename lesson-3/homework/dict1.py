# Task 1
# dict1 = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e"}
# key1 = 3
# if key1 in dict1:
#     print(dict1[key1])
# else:
#     print("There is no value for such key in the dict")
# Task 2
# dict1 = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e"}
# key1 = 3
# key2 = 213123
# print(key1 in dict1)
# print(key2 in dict1)
# Task 3
# dict1 = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e"}
# print(len(dict1))
# Task 4
# dict1 = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e"}
# keys_list = dict1.keys()
# print(keys_list)
# Task 5
# dict1 = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e"}
# values_list = dict1.values()
# print(values_list)
# Task 6
# dict1 = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e"}
# dict2 = {6: "f", 7: "g", 8: "h", 9: "i", 10: "j"}
# new_dict = dict1 | dict2
# print(new_dict)
# Task 7
# dict1 = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e"}
# key1 = 3
# if key1 in dict1:
#     dict1.pop(key1)
#     print(dict1)
# else:
#     print("There is no such key in the dictionary")
# Task 8
# dict1 = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e"}
# dict1.clear()
# print(dict1)
# Task 9
# dict1 = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e"}
# dict2 = {}
# print(bool(dict1))
# print(bool(dict2))
# Task 10
# dict1 = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e"}
# key1 = 3
# if key1 in dict1:
#     value = dict1[key1]
#     print(key1, value)
# else:
#     print("There is no such key")
# Task 11
# dict1 = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e"}
# key1 = 3
# new_value = "f"
# if key1 in dict1:
#     dict1[key1] = new_value
#     print(dict1)
# else:
#     print("There is no such key")
# Task 12
# dict1 = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e"}
# value = "e"
# new_list = list(dict1.values())
# quantity = new_list.count(value)
# print(quantity)
# Task 13
# dict1 = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e"}
# inverted_dict = {value: key for key, value in dict1.items()}
# print("Inverted dictionary:", inverted_dict)
# Task 14
# dict1 = {1: "c", 2: "b", 3: "c", 4: "d", 5: "c"}
# value = "c"
# keys_list = [k for k, v in dict1.items() if v == value]
# print(keys_list)
# Task 15
# keys_list = [1, 2, 3, 4, 5]
# values_list = ["a", "b", "c", "d", "e"]
# new_dict = dict(zip(keys_list, values_list))
# print(new_dict)
# Task 16
# dict1 = {1: "a", 2: "b", 3: {1: "a", 2: "b"}, 4: "d", 5: "e"}
# check = False
# for i in dict1.values():
#     if type(i) == dict:
#         check = True
# print(check)
# Task 17
# dict1 = {1: "a", 2: "b", 3: {1: "a", 2: "b"}, 4: "d", 5: "e"}
# for i in dict1.values():
#     if type(i) == dict:
#         print(i)
# Task 18
# dict1 = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e"}
# default_value = "Not found"
# key1 = 6
# if not key1 in dict1:
#     dict1[key1] = default_value
# print(dict1[key1])
# Task 19
# dict1 = {1: "c", 2: "b", 3: "c", 4: "d", 5: "c"}
# unique_values_count = len(set(list(dict1.values())))
# print(unique_values_count)
# Task 20
# dict1 = {3: "a", 2: "b", 5: "c", 4: "d", 1: "e"}
# new_dict = dict(sorted(dict1.items()))
# print(new_dict)
# Task 21
# dict1 = {3: "c", 2: "b", 5: "e", 4: "d", 1: "a"}
# dict2 = {v: k for k, v in dict1.items()}
# dict_sorted = dict(sorted(dict2.items()))
# dict3 = {v: k for k, v in dict_sorted.items()}
# print(dict3)
# Task 22
# dict1 = {1: "a", 2: "B", 3: "c", 4: "d", 5: "E"}
# new_dict = {k: v for k, v in dict1.items() if v.isupper()}
# print(new_dict)
# Task 23
# dict1 = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e"}
# dict2 = {3: "f", 7: "g", 8: "h", 5: "i", 10: "j"}
# common_keys = set(dict1.keys()) & set(dict2.keys())
# if common_keys:
#     print(common_keys)
# else:
#     print("No common keys")
# Task 24
# tuple1 = ((1, "a"), (2, "b"), (3, "c"))
# dict1 = dict(tuple1)
# print(dict1)
# Task 25
# dict1 = {1: "a", 2: "b", 3: "c", 4: "d", 5: "e"}
# print(list(dict1.items())[0])