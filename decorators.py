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
# def my_decorator(func):
#     def wrap_func(*args, **kwargs):
#         print('********************************')
#         func(*args, **kwargs)
#         print('********************************')
#     return wrap_func

# @my_decorator
# def hello(greeting, emoji=':('):
#     print(greeting, emoji)


# # same as => hello = my_decorator(hello)
# hello('gotcha')


# time performance decorator.
# from time import time


# def performance(fn):
#   def wrapper(*args, **kwargs):
#     t1 = time()
#     result = fn(*args, **kwargs)
#     t2 = time()
#     print(f'took {t2-t1} seconds')
#     return result
#   return wrapper


# @performance
# def long_time():
#     for i in range(10000):
#         i*5

# long_time()


# AUTHENTICATED
# Create an @authenticated decorator that only allows the function to run if user1 has 'valid' set to True:

user1 = {
    'name': 'Sorna',
    # changing this will either run or not run the message_friends function.
    'valid': True
}


def authenticated(fn):
    def wrapper(*args, **kwargs):
        if args[0]['valid']:
            return fn(*args, **kwargs)
    return wrapper


@authenticated
def message_friends(user):
    print('message has been sent')


message_friends(user1)

