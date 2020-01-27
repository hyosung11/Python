class Toy():
    def __init__(self, color, age):
        self.color = color
        self.age = age 
        self.my_dict = {
            'name': 'Yoyo',
            'has_pets': False
        }

    def __str__(self):
        return f'{self.color}'

    def __len__(self):
        return 50

    def __call__(self):
        print('yess??')

    def __getitem__(self, i):
        return self.my_dict[i]

action_figure = Toy('red', 0)
print(action_figure.__str__())
# same as above 
print(str(action_figure))
print(len(action_figure))
print(action_figure())
print(action_figure['name'])