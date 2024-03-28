import time

def decor(func):
    def inner(*args, **kwargs):
        start = time.time()
        print(start)
        res = func(*args, **kwargs)
        end = time.time()
        print(end)
        print(end - start)
        return res
    return inner

@decor
def summ(a:int, b:int):
    return a + b

print(summ(1, 2))


def show_menu(func):
    def inner(*args):
        res = func(*args)
        for i, v in enumerate(res, 1):
            print(f'{i}. {v}')
        return res
    return inner


@show_menu
def get_menu(s):
    return s.split()

print(get_menu('sdsd dddd ddd'))

def get_add(a, b):
    if type(a) is str and type(b) is str:
        return a + b
    elif type(a) in (int, float) and type(b) in (int, float):
        return a + b

print(get_add('dd', 'ss'))

print(hash(get_add))

ss = [1, 3, 6] * 3

print(ss)

import math
fun = lambda x : 1 if x == 1 else math.ceil(math.sinh(fun (x-1)))
print(fun(5))
