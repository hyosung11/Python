#!/usr/bin/env python3

# print('Omi Bidol-Lee')

# name = input('What is your name?')
#
# print('helloo ' + name)

# FUNDAMENTAL DATA TYPES
# int
# float
# bool
# str
# list
# tuple
# set
# dict

# Classes -> custom types

# Specialized Data Types
# from modules

# None

# integers and floats
# print(2 + 4)
# print(2 - 4)
# print(2 * 4)
# print(2 / 4)

# print(type(2 + 4))
# print(type(2 - 4))
# print(type(2 * 4))
# print(type(2.0 / 4))

# print(2 ** 3)
# print(5.0 // 4)
# print(6 % 4)

# Math Functions
# print(round(3.9))
# print(abs(-20))

# Operator Precedence
# print((20 - 3) + 2 ** 2)

# ()
# **
# * /
# + -

# print((5 + 4) * 10 / 2) # 45
#
# print(((5 + 4) * 10) / 2)
#
# print((5 + 4) * (10 / 2))
#
# print(5 + (4 * 10) / 2)

# Floor Division(//)
# divides and returns the integer value of the quotient. It dumps the digits after the decimal.
# print(5 + 4 * 10 // 2)

# complex

# bin()
# print(bin(5)) # 0b101
# print(int('0b101', 2)) # 5

# Variables
# iq = 190
#
# print(iq)
# _user_iq (private variable starts with _underscore)
# user_iq = 190
#
# print(user_iq)

# iq = 190
# user_age = iq/4.0
#
# print(user_age)

# CONSTANTS are CAPITALIZED
# PI = 3.14
#
# __DUNDER

# multiple variables
# a,b,c = 1,2,3
# print(a)
# print(b)
# print(c)

# Expressions vs Statements
# iq = 100
# user_age = iq / 5

# Augmented Assignment Operator
# some_value = 5
# some_value += 2
#
# print(some_value)

# STRINGS
# print('username')
# print(type("hi hello there 24"))
# username = 'supercoder'
# password = 'supersecret'

# triple single quotes for multiline string
# long_string = '''
# WOW
# O O
# ---
# '''
#
# print(long_string)

# first_name = 'Omi'
# last_name = 'Angel'
# full_name = first_name + ' ' + last_name
# print(full_name)

# Type Conversion

# a = str(100)
# b = int(a)
# c = type(b)
# print(c)

# print(type(int(str(100))))

# Escape Sequence

# weather = "It\'s \"kind of\" sunny "
#
# print(weather)

# formatted strings

# name = 'SungOh'
# age = 4

# 1. string concatenation
# print('Hi ' + name + '. You are ' + str(age) + ' years old')

# 2. (f ... )(only works in Python 3)
# print(f'hi {name}. You are {age} years old')

# 3. .format()

## String Indexes
# selfish = '01234567'
#         # 01234567
#
# # [start:stop:stepover]
# print(selfish[1:8:2]) # => 1357
#
# # start from end of string
# print(selfish[-1]) # => 7
#
# #
# print(selfish[::-2]) # => 7531

# Immutability
# string = 'Desirable Difficulties'
#
# string[0] = 'love'
#
# print(string) # => TypeError: 'str' object does not support item assignment

# string = 'Desirable Difficulties'
#
# string = 'I love ' + string
#
# print(string)

# Built-In Functions + Methods
# print(len('antifragile')) # => 11
#
# truth = 'antifragile'
# # print(truth[:]) # antifragile
#
# print(truth[0:len(truth)]) # antifragile

# quote = 'to be or not to be'
# quote2 = quote.replace('be', 'me')
# # print(quote.upper())
# # print(quote.capitalize())
#
# # .find() returns index where string starts
# # print(quote.find('be')) # => 3
#
# # .replace('a', 'b')
# print(quote.replace('be', 'me'))
#
# print(quote2)
# print(quote)

# Booleans
# name = 'Sohee'
# is_cool = False
#
# is_cool = True
#
# print(bool(0)) # False
# print(bool(1)) # True

# Exercise: Type Conversion
# name = 'Omi Bidol-Lee'
# age = 8
# relationship_status = 'single'
#
# relationship_status = 'in love'
#

# birth_year = input('What year were you born?')
# print(type(birth_year))
#
# age = 2020 - int(birth_year)
#
# print(f'Your age is: {age}')

# Password Checker
# username = input('What is your username?')
# password = input('What is your password?')
#
# password_length = len(password)
# hidden_password = '*' * password_length
#
# print(f'{username}, your password {hidden_password}, is {password_length} letters long')

# Lists
# list = [1,2,3,4,5]
# list2 = ['a', 'b', 'c']
# list3 = [1,2,'a', True]

# amazon_cart = ['notebooks', 'pens']
# print(amazon_cart[2])

# List Slicing (creates a new list)
# amazon_cart = [
#     'notebooks',
#     'pens',
#     'monkeys',
#     'bunnies'
# ]
#
# # print(amazon_cart[0::2])
# amazon_cart[0] = 'books'
# new_cart = amazon_cart[:]
# print(new_cart)
# print(amazon_cart)

# Matrix
# matrix = [
#     [1,5,1],
#     [0,1,0],
#     [1,0,1]
# ]
#
# print(matrix[0][1])

# List Methods
# basket = [1,2,3,4,5]

# ADDING
# new_list = basket.append(100)
# print(basket.append(100))
# print(basket)
# print(new_list)

# basket.append(100)
# new_list = basket
# print(basket)
# print(new_list)

# insert
# basket.insert(1, 100)
# new_list = basket
# print(basket)
# print(new_list)

# extend
# basket.extend([100, 101])
# new_list = basket
# # print(basket)
# print(new_list)

# REMOVING

# pop - pops last item by default or by index
# basket.pop()
# basket.pop(2)
# print(basket)

# remove the value
# basket.remove(5)
# print(basket)

# clear completely clears the list
# basket.clear()
# print(basket)

# index to return the index of the value
# basket = ['a', 'b', 'c', 'd', 'e', 'd']

# print(basket.index('d'))
# print(basket.index('d', 0, 2))

# keyword `in`
# print('c' in basket)
# print('x' in basket)
# print('q' in 'The Queen arises'.lower())

# keyword `count` returns how many times a value occurs
# print(basket.count('b'))

# keyword `sort`
# basket.sort()
# print(basket)

# `sorted()` function produces a new list (array)
# print(sorted(basket))

# keyword `copy`

# keyword `reverse`
# basket.reverse()
# print(basket)

# basket.sort()
# basket.reverse()
# print(basket)

# COMMON LIST PATTERNS
# basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']
# basket.sort()
# basket.reverse()
# print(basket[::-1])
# print(basket)

# range
# print(list(range(100)))

# join
# sentence = ' '.join(['hi', 'my', 'name', 'is', 'Gael'])
# print(sentence)

# LIST UNPACKING
# a,b,c = [1,2,3]
#
# print(a)
# print(b)
# print(c)

# a,b,c, *other, d = [1,2,3,4,5,6,7,8,9]
#
# print(a)
# print(b)
# print(c)
# print(other)
# print(d)

# None (null in JavaScript)
# cookies = None
# print(cookies)

# DICTIONARY
# dictionary = {
#     'a': 1,
#     'b': 2,
#     'c': 3
# }
#
# print(dictionary)

# .get
user = {
    'basket': [1,2,3],
    'greet': 'hello',
    'age': 46
}

# # print(user.get('age'))
# print(user.get('age', 55))
#
# # another less common way
# user2 = dict(name='Sungster')
# print(user2)

# keys
# print('age' in user.keys())

# values
# print('hello' in user.values())

# items
# print(user.items())

# clear
# print(user.clear())
#
# user.clear()
# print(user)

# copy
# print(user.copy())

# pop
# print(user.pop('age'))
# print(user)

# popitem

# update
# print(user.update({'age': 55}))
# print(user)

# TUPLE ()
# my_tuple = (1,2,3,4,5)
# my_tuple[1] = 'z'
#
# print(my_tuple)

# SETS
# my_set = {1,2,3,4,5,5}
# print(my_set)

# my_list = [1,2,3,4,5,5]
#
# print(set(my_list)) # => {1, 2, 3, 4, 5}

my_set = {1,2,3,4,5,5}

print(1 in my_set) # => True

print(len(my_set)) # => 5 (duplicate not recorded)
