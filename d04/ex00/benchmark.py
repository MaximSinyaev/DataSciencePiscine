import timeit

EXEC_TIME = 90000000


def classical(emails_list, email_end='@gmail.com'):
    res = list()
    for email in emails_list:
        if email.endswith(email_end):
            res.append(email)
    return res


def pythonic(emails_list, email_end='@gmail.com'):
    return [email for email in emails_list if
            email.endswith(email_end)]


if __name__ == '__main__':
    email_end = '@gmail.com'
    emails = ['john@gmail.com', 'james@gmail.com', 'alice@yahoo.com',
              'anna@live.com', 'philipp@gmail.com']
    classic_time = timeit.timeit('classical(emails)',
                                 "from __main__ import classical, emails",
                                 number=EXEC_TIME)
    pythonic_time = timeit.timeit('pythonic(emails)',
                                  "from __main__ import pythonic, emails",
                                  number=EXEC_TIME)
    print('It is better to use a {}' \
          .format('list comprehensive' if pythonic_time < classic_time
                  else 'loop'))
    print('{} vs {}'.format(*sorted((classic_time, pythonic_time))))
