my_file = open('test.txt')

# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())
# my_file.seek(0)
# print(my_file.read())

# print(my_file.readline())

print(my_file.readlines())
# ["There's nothing on the other side of fear. \n", '\n',
#     'argh\n', '\n', 'Embrace it. Go through it and find love.']

my_file.close()
