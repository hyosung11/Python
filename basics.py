# is_old = False
# is_licensed = False
#
# if is_old:
#     print('You are old enough to drive!')
# elif is_licensed:
#     print('You can drive now')
# else:
#     print('You are not of age')
#
# print('Freedom')


# is_old = True
# is_licensed = False
#
# if is_old and is_licensed:
#     print('You are old enough to drive and you have a license!')
# else:
#     print('You are not of age')

# print('Freedom')

# school = {'Bobby','Tammy','Jammy','Sally','Danny'}
# attendance_list = ['Jammy', 'Bobby', 'Danny', 'Sally']
#
# print(school.difference(attendance_list))

# Truthy and Falsy

# Ternary Operator
# condition_if_true if condition else condition_if_false
# is_friend = False
# can_message = "message allowed" if is_friend else "not allowed to message"
#
# print(can_message)

# Logical Operators
# is_magician = True
# is_expert = False
#
# # check if magician AND expert: 'you are a master magician'
# if is_magician and is_expert:
#     print('you are a master magician')
#
# # check if magician but not expert: 'at least you're getting there'
# elif is_magician and not is_expert:
#     print('at least you\'re getting there')
#
# # if you're not a magician: 'you need magic powers'
# elif not is_magician:
#     print('you need magic powers')

# print(True == 1)
# print('' == 1)
# print([] == 1)
# print(10 == 10.0)
# print([] == [])

# is same as === in JS
# print(True is 1)
# print('' is 1)
# print([] is 1)
# print(10 is 10.0)
# print([] is [])

# For Loops
# for element in {1,2,3,4,5}:
#     print(element)

# Nested Loops
# for item in (1,2,3,4,5):
#     for x in ['a', 'b', 'c']:
#         print(1, 'a')

# Iterables
user = {
    'name': 'Golem',
    'age': 5006,
    'can_swim': False
}
# returns the keys by default
# for item in user:
#     print(item)

# returns the key value pairs in a tuple
# for item in user.items():
#     print(item)

# returns the values
# for item in user.values():
#     print(item)

# returns the keys explicitly
# for item in user.keys():
#     print(item)

# for item in user.items():
#     key, value = item
#     print(key, value)

# for key, value in user.items():
#     print(key, value)


# Tricky Counter Exercise
# my_list = [1,2,3,4,5,6,7,8,9,10]
#
# counter = 0
# for num in my_list:
#     counter = counter + num
#
# print(counter)

# range()
# print(range(100))

# for number in range(0, 100):
#     print(number)

# for number in range(0, 11):
#     print('multiple emails')

# for _ in range(0, 11):
#     print('test')

# 3rd parameter is stepover ascending
# for _ in range(0, 11, 2):
#     print(_)

# stepover descending
# for _ in range(11, 0, -2):
#     print(_)

# list that has integers
# for _ in range(2):
#     print(list(range(10)))

# enumerate() - to get index counter of item that you're looping through
# for i, char in enumerate((1, 2, 3)):
#     print(i, char)

# for i, char in enumerate(list(range(100))):
#     if char == 50:
#         print(f'index of 50 is: {i}')

# While Loop
# i = 0
# while i < 11:
#     print(i)
#     i += 1
#     break
# else:
#     print('All done')

# my_list = [1,2,3]
#
# for item in my_list:
#     print(item)
#
# i = 0
# while i < len(my_list):
#     print(my_list[i])
#     i += 1

# while True:
#     response = input('say something: ')
#     if (response == 'bye'):
#         break

# break, continue, pass

#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

# 1. iterate over picture
    # if 0 => print ' '
    # if 1 => print *

# for row in picture:
#     for pixel in row:
#         if (pixel == 1):
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print('')

# Good Code
# fill = '$'
# empty = ' '
# for row in picture:
#     for pixel in row:
#         if pixel:
#             print(fill, end='')
#         else:
#             print(empty, end='')
#     print('')

# Check for duplicates in list
some_list = ['a', 'b', 'c', 'b', 'd', 'm', 'n', 'n']

duplicates = []
for value in some_list:
    if some_list.count(value) > 1:
        if value not in duplicates:
            duplicates.append(value)

print(duplicates)
