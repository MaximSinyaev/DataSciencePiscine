import resource


def file_to_list(src='ratings.csv'):
    res = list()
    with open(src, 'r')as f:
        for line in f:
            res.append(line)
    return res


if __name__ == '__main__':
    l = file_to_list()
    for _ in l:
        pass
    time = resource.getrusage(0) + resource.getrusage(1)
    memory = resource.getrusage(2)
    print(f'Peak Memory Usage = {memory} GB')
    print(f'User Mode Time + System Mode Time = {time}s')
