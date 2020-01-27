# OOP
# print(type(None))
# print(type(True))
# print(type(5))
# print(type(5.5))
# print(type('hi'))
# print(type([]))
# print(type(()))
# print(type({}))

# class naming convention
# class BigObject:  # Class
#     # code here
#     pass
#
#
# obj1 = BigObject()  # instantiate the Class
# obj2 = BigObject()
# obj3 = BigObject()
#
# print(type(None))
# print(type(True))
# print(type(5))
# print(type(5.5))
# print(type('hi'))
# print(type([]))
# print(type(()))
# print(type({}))
# print(type(obj1))

# Creating Our Own Objets


# class PlayerCharacter:
#     # Class Object Attribute
#     membership = True
#     def __init__(self, name, age):
#         self.name = name  # attribute
#         self.age = age

#     def run(self):
#         print('run')
#         return 'done'


# player1 = PlayerCharacter('Kobe', 41)
# player2 = PlayerCharacter('Lebron', 35)
# player2.points = 33333

# # help([list])
# print(player2.membership)


class PlayerCharacter:
    # Class Object Attribute
    membership = True
    def __init__(self, name, age):
        self.name = name  # attribute
        self.age = age

    def shout(self):
        print(f'my name is {self.name}')

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('Teddy', num1 + num2)


# player1 = PlayerCharacter('Kobe', 41)
player3 = PlayerCharacter.adding_things(2,3)
print(player3.age)