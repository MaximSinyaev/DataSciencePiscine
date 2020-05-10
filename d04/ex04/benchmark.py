import random
import timeit
from collections import Counter

EXEC_NUM = 20


def loop_func(random_list):
    res = dict(zip(range(100), [0] * 100))
    for i in random_list:
        res[i] += 1
    return res


def my_top_func(res_dict):
    return dict(sorted(res_dict.items(), key=lambda x: x[1], reverse=True)[:10])


def counter_func(random_list):
    return Counter(random_list)


def counter_top_func(res_counter):
    return res_counter.most_common(10)


if __name__ == '__main__':
    func = {
        'loop': 'loop_func',
        'counter': 'counter_func',
        'my_top': 'my_top_func',
        'counter_top': 'counter_top_func',
    }
    random_list = [random.randrange(0, 100) for i in range(10 ** 6)]
    time = dict()
    method = 'loop'
    time['my function'] = timeit.timeit(f'{func[method]}(random_list)',
                                        f"from __main__ import {func[method]}, random_list",
                                        number=EXEC_NUM)
    method = 'counter'
    time['counter'] = timeit.timeit(f'{func[method]}(random_list)',
                                    f"from __main__ import {func[method]}, random_list",
                                    number=EXEC_NUM)
    my_counter = loop_func(random_list)
    std_counter = counter_func(random_list)
    method = 'my_top'
    time['my top'] = timeit.timeit(f'{func[method]}(my_counter)',
                                   f"from __main__ import {func[method]}, my_counter",
                                   number=EXEC_NUM)
    method = 'counter_top'
    time['counter_top'] = timeit.timeit(f'{func[method]}(std_counter)',
                                        f"from __main__ import {func[method]}, std_counter",
                                        number=EXEC_NUM)
    print(f"my function: {time['my function']}")
    print(f"Counter: {time['counter']}\n")
    print(f"my top: {time['my top']}")
    print(f"Counter's top: {time['counter_top']}")
