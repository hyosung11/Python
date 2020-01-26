# def say_hello():
#     print('annyung')
#
# say_hello()


picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]


fill = '$'
empty = ' '

def show_tree():
    for row in picture:
        for pixel in row:
            if pixel:
                print(fill, end='')
            else:
                print(empty, end='')
        print('')

show_tree()
show_tree()
show_tree()
