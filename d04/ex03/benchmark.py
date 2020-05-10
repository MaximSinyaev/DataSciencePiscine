import sys
import timeit


def loop_func(emails_list, email_end='@gmail.com'):
    res = list()
    for email in emails_list:
        if email.endswith(email_end):
            res.append(email)
    return res


def list_comprehensive_func(emails_list, email_end='@gmail.com'):
    return [email for email in emails_list if
            email.endswith(email_end)]


def map_func(email_list, email_end='@gmail.com'):
    return list(map(lambda x: x if x.endswith(email_end) else None, email_list))


def filter_func(email_list, email_end='@gmail.com'):
    return list(filter(lambda x: x.endswith(email_end), email_list))


if __name__ == '__main__':
    email_end = '@gmail.com'
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com',
              'anna@live.com', 'philipp@gmail.com']
    func = {
        'loop': 'loop_func',
        'list_comprehensive': 'list_comprehensive_func',
        'map': 'map_func',
        'filter': 'filter_func',
    }
    if len(sys.argv) != 3:
        raise AttributeError('Script inputs 2 params: method itearations_num')
    if sys.argv[1].lower() not in func:
        raise ValueError('Unknown method')
    method = sys.argv[1].lower()
    iter_num = int(sys.argv[2])
    time = timeit.timeit(f'{func[method]}(emails)',
                         f"from __main__ import {func[method]}, emails",
                         number=iter_num)
    print(time)
