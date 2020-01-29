# lambda expressions
from functools import reduce

# lambda syntax:
# lambda param: action(param)

# my_list = [1, 2, 3]

# def multiply_by2(item):
#     return item*2

# def only_odd(item):
#     return item % 2 != 0

# def accumulator(acc, item):
#     print(acc, item)
#     return acc + item


# print(list(map(lambda item: item*2, my_list)))
# print(list(filter(lambda item: item % 2 != 0, my_list)))
# print(reduce(lambda acc, item: acc + item, my_list))
# print(my_list)


# Square a List 
# my_list = [5,4,3]

# # Andrei's code
# new_list = list((map(lambda num: num**2, my_list)))
# print(new_list)

# # my code
# print(list(map(lambda item: item*item, my_list)))


# List Sorting
a = [(0,2), (4,3), (9,9), (10, -1)]
# a.sort() sorts by first item
# a.sort(key=lambda x: x[1]) sorts by the second item
# print(a)