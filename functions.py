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
def is_even(num):
    return num % 2 == 0

print(is_even(11))
