# Generators

# range(100)

# def make_list(num):
#     result = []
#     for i in range(num):
#         result.append(i * 2)
#     return result

# my_list = make_list(100)
# # print(my_list)

# print(list(range(100000)))


# def generator_function(num):
#     for i in range(num):
#         yield i * 2

# g = generator_function(10)
# next(g)
# next(g)
# next(g)
# print(next(g))


# GENERATORS PERFORMANCE EXAMPLE

# from time import time


# def performance(fn):
#     def wrapper(*args, **kawrgs):
#         t1 = time()
#         result = fn(*args, **kawrgs)
#         t2 = time()
#         print(f'took {t2-t1} s')
#         return result
#     return wrapper


# @performance
# def long_time():
#     print('1')
#     for i in range(1000000):
#         i*5


# @performance
# def long_time2():
#     print('2')
#     for i in list(range(1000000)):
#         i*5


# long_time()
# long_time2()


# generator function

def gen_fun(num):
    for i in range(num)
        yield i

for item in gen_fun(100)
