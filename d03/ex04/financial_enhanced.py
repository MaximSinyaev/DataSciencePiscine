import cProfile
import sys
import urllib.request

import requests
from bs4 import BeautifulSoup


def main():
    url = 'https://finance.yahoo.com/quote/{0}/financials?p={0}'
    if len(sys.argv) != 3:
        raise AttributeError('Must be 2 arguments Ticker and param')
    response = urllib.request.urlopen(url.format(sys.argv[1].lower()))
    if not response and not response.url.endswith(sys.argv[1].lower()):
        raise requests.ConnectionError(f'No {sys.argv[0]} company found')
    soup = BeautifulSoup(response.read(), 'html.parser')
    result = list()
    result.append(sys.argv[2])
    row = soup.find(string=sys.argv[2]).parent
    if not row:
        raise Exception(f'No {sys.argv[2]} param found!')
    col = row
    for _ in range(5):
        result.append(col.find_next('span').string)
        col = result[-1]
    return tuple(result)


if __name__ == "__main__":
    cProfile.run('main()', sort='pcalls')
    # print(ans)
