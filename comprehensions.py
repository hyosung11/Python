# Comprehensions: List, Set, Dictionary

# without list comprehension
# my_list = []

# for char in 'hello':
#     my_list.append(char)

# print(my_list)

# with LIST comprehension
# my_list = [char for char in 'hello']

# print(my_list)

# numbers_list = [num for num in range(0,100)]
# numbers_list2 = [num*2 for num in range(0,100)]
# numbers_list3 = [num**2 for num in range(0, 100)]
# numbers_list4 = [num**2 for num in range(0, 100) if num % 2 == 0]

# print(numbers_list4)


# Set {} Comprehensions => only unique items unordered
# my_list = {char for char in 'hello'}
# numbers_list = {num for num in range(0, 100)}
# numbers_list2 = {num*2 for num in range(0, 100)}
# numbers_list3 = {num**2 for num in range(0, 100)}
# numbers_list4 = {num**2 for num in range(0, 100) if num % 2 == 0}

# # print(my_list)
# print(numbers_list4)


# Dictionary Comprehensions
# simple_dict = {
#     'a': 1,
#     'b': 2
# }

# my_dict = {key:value**2 for key,value in simple_dict.items() if value % 2 == 0}

# my_dict = {num:num*2 for num in [1,2,3]}

# print(my_dict)


# Comprehensions Exercise

some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

# duplicates = []
# for value in some_list:
#     if some_list.count(value) > 1:
#         if value not in duplicates:
#             duplicates.append(value)

# returns multiple values e.g., => ['b', 'b', 'n', 'n']
# duplicates = [char for char in some_list if some_list.count(char) > 1]

duplicates = list(set([char for char in some_list if some_list.count(char) > 1]))
print(duplicates)
