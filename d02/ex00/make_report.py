from sys import argv

try:
    from numbers import revenue_change, profit_change, average_check
except ImportError:
    raise ValueError("In numbers.py must be 3 variables revenue_change,"
                     " profit_change, average_check")


def main():
    if len(argv) != 2 or not argv[1].endswith('.template'):
        raise ValueError("Script takes 1 parameter with *.template ext")
    with open(argv[1], 'r') as f:
        with open(argv[1].replace('.template', '.txt'), 'w') as output:
            result = f.read()
            # print(result.format(revenue_change))
            output.write(result.format(**{'revenue_change': revenue_change,
                                        'profit_change': profit_change,
                                        'average_check': average_check}))


if __name__ == "__main__":
    main()
