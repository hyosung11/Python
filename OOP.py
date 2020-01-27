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


# class PlayerCharacter:
#     # Class Object Attribute
#     membership = True
#     def __init__(self, name, age):
#         self.name = name  # attribute
#         self.age = age

#     def shout(self):
#         print(f'my name is {self.name}')

#     @classmethod
#     def adding_things(cls, num1, num2):
#         return cls('Teddy', num1 + num2)

#     @staticmethod
#     def adding_things2(num1, num2):
#         return (num1 + num2)

# # player1 = PlayerCharacter('Kobe', 41)
# player3 = PlayerCharacter.adding_things(2,3)
# print(player3.age)

# class PlayerCharacter:
#     def __init__(self, name, age):
#         self.name = name  # attribute
#         self.age = age

#     def run(self):
#         return self

#     def speak(self):
#         print(f'my name is {self.name}, and I am {self.age} years old.')

# player1 = PlayerCharacter('Kobe', 41)
# player1.speak()


# Inheritance 
# class User(object):
#     def sign_in(self):
#         print('logged in')

#     def attack(self):
#         print('do nothing')

# class Wizard(User):
#     def __init__(self, name, power):
#         self.name = name
#         self.power = power
    
#     def attack(self):
#         User.attack(self)
#         print(f'attacking with power of {self.power}')

# class Archer(User):
#     def __init__(self, name, num_arrows):
#         self.name = name
#         self.num_arrows = num_arrows

#     def attack(self):
#         print(f'attacking with arrows: arrows left- {self.num_arrows}')

# wizard1 = Wizard('Merlin', 50)
# archer1 = Archer('Robin', 30)
# print(wizard1.attack())

# wizard1.attack()
# archer1.attack()

# print(isinstance(wizard1, object))

# def player_attack(char):
#     char.attack()

# player_attack(wizard1)
# player_attack(archer1)

# for char in [wizard1, archer1]:
#     char.attack()

# User.attack(self)


class User(object):
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power, email):
        super().__init__(email)
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left- {self.num_arrows}')

# introspection
wizard1 = Wizard('Merlin', 60, 'merlin@gmail.com')
print(dir(wizard1))