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
    user_companies = [_.strip() for _ in sys.argv[1].split(',')]
    if not all(user_companies):
        print()
        return
    for name in user_companies:
        if name.upper() in stocks:
            print(name.upper(), 'is a ticker symbol for',
                  *(i for i in companies if companies[i] == name.upper()))
        elif name.capitalize() in companies:
            print(name.capitalize(), 'stock price is',
                  stocks[companies[name.capitalize()]])
        else:
            print(name,
                  'is an unknown company or an unknown ticker symbol')


if __name__ == "__main__":
    main()
