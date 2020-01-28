# Decorator

# def my_decorator(func):
#     def wrap_func():
#         print('********************************')
#         func()
#         print('********************************')
#     return wrap_func

# @my_decorator
# def hello():
#     print('annyunghaseyo')


# @my_decorator
# def bye():
#     print('annyunghigaseyo')

# # hello()
# bye()


# alternatively
# def my_decorator(func):
#     def wrap_func():
#         print('********************************')
#         func()
#         print('********************************')
#     return wrap_func


# def hello():
#     print('annyunghaseyo')


# def bye():
#     print('annyunghigaseyo')


# my_decorator(hello)()


# Decorator 3 Exercise
def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('********************************')
        func(*args, **kwargs)
        print('********************************')
    return wrap_func

@my_decorator
def hello(greeting, emoji=':('):
    print(greeting, emoji)


# same as => hello = my_decorator(hello)
hello('gotcha')
