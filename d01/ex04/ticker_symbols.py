import sys

companies = {
    "Apple": "AAPL",
    "Microsoft": "MSFT",
    "Netflix": "NFLX",
    "Tesla": "TSLA",
    "Nokia": "NOK"
}

stocks = {
    "AAPL": 287.73,
    "MSFT": 173.79,
    "NFLX": 416.90,
    "TSLA": 724.88,
    "NOK": 3.37
}


def main():
    if len(sys.argv) != 2:
        print()
        return
    company_name = sys.argv[1]
    if company_name in stocks:
        print(*(i for i in companies if companies[i] == company_name),
              stocks[company_name])
        return
    print('Unknown ticker')


if __name__ == "__main__":
    main()
