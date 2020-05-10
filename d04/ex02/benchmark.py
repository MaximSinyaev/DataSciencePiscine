import timeit

EXEC_TIME = 9000000


def classical(emails_list, email_end='@gmail.com'):
    res = list()
    for email in emails_list:
        if email.endswith(email_end):
            res.append(email)
    return res


def pythonic(emails_list, email_end='@gmail.com'):
    return [email for email in emails_list if
            email.endswith(email_end)]


def map_func(email_list, email_end='@gmail.com'):
    return list(map(lambda x: x if x.endswith(email_end) else None, email_list))


if __name__ == '__main__':
    email_end = '@gmail.com'
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com',
              'anna@live.com', 'philipp@gmail.com']
    time = dict()
    time['loop'] = timeit.timeit('classical(emails)',
                                 "from __main__ import classical, emails",
                                 number=EXEC_TIME)
    time['list comprehensive'] = timeit.timeit('pythonic(emails)',
                                  "from __main__ import pythonic, emails",
                                  number=EXEC_TIME)
    time['map'] = timeit.timeit('map_func(emails)',
                             "from __main__ import map_func, emails",
                             number=EXEC_TIME)
    print('It is better to use a {}' \
          .format(sorted(time, key=lambda x: time[x]))[0])
    print('{} vs {}'.format(*sorted(time.values())))
