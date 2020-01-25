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

birth_year = input('What year were you born?')
print(type(birth_year))

age = 2020 - int(birth_year)

print(f'Your age is: {age}')
