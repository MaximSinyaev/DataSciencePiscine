import resource


def line_gen(src='ratings.csv'):
    with open(src, 'r')as f:
        for line in f:
            yield line

if __name__ == '__main__':
    l = line_gen()
    for _ in l:
        pass
    time = resource.getrusage(0) + resource.getrusage(1)
    memory = resource.getrusage(2)
    print(f'Peak Memory Usage = {memory} GB')
    print(f'User Mode Time + System Mode Time = {time}s')
