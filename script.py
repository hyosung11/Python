# my_file = open('test.txt')

# # print(my_file.read())
# # my_file.seek(0)
# # print(my_file.read())
# # my_file.seek(0)
# # print(my_file.read())

# # print(my_file.readline())

# print(my_file.readlines())
# # ["There's nothing on the other side of fear. \n", '\n',
# #     'argh\n', '\n', 'Embrace it. Go through it and find love.']

# my_file.close()


# better way so don't have to open and close the file
# standard way to read a file
# with open('test.txt') as my_file:
#     print(my_file.readlines())

# mode='r' defaults to reading the file
# mode='r+' lets you write but starts with cursor at position 0
# with open('test.txt', mode='r+') as my_file:
#     text = my_file.write('Phil Collins')
#     print(text)

# mode='a' appends to end of file
# with open('test.txt', mode='a') as my_file:
#     text = my_file.write('1980s')
#     print(text)

# mode='w' writes and will create a new file
with open('breathe.txt', mode='w') as my_file:
    text = my_file.write('breathe you are alive')
    print(text)
