import sys
import timeit
from functools import reduce


def loop_func(n):
    res = 0
    for i in range(1, n + 1):
        res += i ** 2
    return res


def reduce_func(n):
    reduce(lambda x, y: x + y ** 2, range(1, n + 1))


if __name__ == '__main__':
    func = {
        'loop': 'loop_func',
        'reduce': 'reduce_func',
    }
    if len(sys.argv) != 4:
        raise AttributeError('Script inputs 3 params: method itearations_num n')
    if sys.argv[1].lower() not in func:
        raise ValueError('Unknown method')
    method = sys.argv[1].lower()
    iter_num = int(sys.argv[2])
    n = int(sys.argv[2])
    time = timeit.timeit(f'{func[method]}({n})',
                         f"from __main__ import {func[method]}",
                         number=iter_num)
    print(time)
