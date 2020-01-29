#Given the below class:
class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 1 Instantiate the Cat object with 3 cats
blackie = Cat('Blackie', 4)
chester = Cat('Chester', 5)
snickers = Cat('Snickers', 6)


# 2 Create a function that finds the oldest cat
def find_oldest_cat(*args):
    return max(args)


# 3 Print out: "The oldest cat is x years old.". x will be the oldest cat age by using the function in #2
print(f'The oldest cat is {find_oldest_cat(blackie.age, chester.age, snickers.age)} years old.')