# def say_hello():
#     print('annyung')
#
# say_hello()


# picture = [
#   [0,0,0,1,0,0,0],
#   [0,0,1,1,1,0,0],
#   [0,1,1,1,1,1,0],
#   [1,1,1,1,1,1,1],
#   [0,0,0,1,0,0,0],
#   [0,0,0,1,0,0,0]
# ]
#
#
# fill = '$'
# empty = ' '
#
# def show_tree():
#     for row in picture:
#         for pixel in row:
#             if pixel:
#                 print(fill, end='')
#             else:
#                 print(empty, end='')
#         print('')
#
# show_tree()
# show_tree()
# show_tree()

# parameters: defined variables to pass into a function
# def say_hello(name, emoji):
#     print(f'annyung {name} {emoji}')
#
# # arguments: called (invoked) values we provide to a function
# say_hello('SungOh', '🤣')
# say_hello('Sohee', '🤣')
# say_hello('Omi', '🤣')

# default parameters
# def say_hello(name='Darth Vader', emoji='👽'):
#     print(f'annyung {name} {emoji}')
#
# # positional arguments: called (invoked) values we provide to a function
# say_hello('SungOh', '🤣')
# say_hello('Sohee', '🤣')
# say_hello('Omi', '🤣')
#
# # keyword arguments
# say_hello(name='MP', emoji='#')
# say_hello()

# Docstrings
# def test(a):
#     '''
#     Info: this function tests and prints param a
#     '''
#     print(a)
#
# print(test.__doc__)

# Clean Code

# 1.
# def is_even(num):
#     if num % 2 == 0:
#         return True
#     elif num % 2 != 0:
#         return False
#
# print(is_even(11))

# 2.
# def is_even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
#
# print(is_even(11))

# 3.
# def is_even(num):
#     if num % 2 == 0:
#         return True
#     return False
#
# print(is_even(11))

# 4.
# def is_even(num):
#     return num % 2 == 0
#
# print(is_even(11))

# *args and **kwargs (keyword args)

# def super_func(*args):
#     print(args)
#     return sum(args)
#
# print(super_func(1,2,3,4,5))

# def super_func(*args, **kwargs):
#     total = 0
#     for items in kwargs.values():
#         total += items
#     return sum(args) + total
#
# print(super_func(1,2,3,4,5, num1=5, num2=10))

# highest even function exercise
# def highest_even(li):
#     evens = []
#     # iterate through li
#     for item in li:
#         # find even numbers
#         if item % 2 == 0:
#             # add to list
#             evens.append(item)
#     # get largest even number
#     return max(evens)
#
# print(highest_even([10,2,3,4,8,11]))

# def highest_even(list):
#     evens = []
#     for num in list:
#         if num % 2 == 0:
#             evens.append(num)
#     return max(evens)
#
# print(highest_even([22,2,4,55,36,5554]))

# total = 0
#
# def count():
#     global total
#     total += 1
#     return total
#
# count()
# count()
# print(count())

# total = 0
#
# # dependency injection
# def count(total):
#     total += 1
#     return total
#
# print(count(count(count(total))))

# Scope - what variables do I have access to?
# def outer():
#     x = "local"
#     def inner():
#         nonlocal x
#         x = "nonlocal"
#         print("inner:", x)
#     inner()
#     print("outer:", x)
# outer()

#1 - start with local
#2 - Parent local?
#3 - global
#4 - built in python functions


# PURE FUNCTIONS
# def multiply_by2(li):
#     new_list = []
#     for item in li:
#         new_list.append(item*2)
#     return new_list

# print(multiply_by2([1,2,3]))

# map, filter, zip, and reduce

# map
# my_list = [1,2,3]
# def multiply_by2(item):
#     return item*2

# print(list(map(multiply_by2, [1, 2, 3])))
# print(my_list)

# filter
# my_list = [1, 2, 3]


# def multiply_by2(item):
#     return item*2

# def check_odd(item):
#     return item % 2 != 0


# print(list(filter(check_odd, my_list)))
# print(my_list)

# zip - join items together in a tuple
my_list = [1, 2, 3]
your_list = [10,20,30]
their_list = [4,5,6]
def multiply_by2(item):
    return item*2


def check_odd(item):
    return item % 2 != 0


print(list(zip(my_list, your_list)))
# => [(1, 10), (2, 20), (3, 30)]

print(list(zip(my_list, your_list, their_list)))
