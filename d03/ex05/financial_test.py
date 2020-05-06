import sys
import time
import pytest

import requests
from bs4 import BeautifulSoup


def main(company, par):
    url = 'https://finance.yahoo.com/quote/{0}/financials?p={0}'
    response = requests.get(url.format(company.lower()))
    if not response or not response.url.endswith(company.lower()):
        raise requests.ConnectionError(f'No {company} company found')
    soup = BeautifulSoup(response.text, 'html.parser')
    result = list()
    result.append(par)
    if not soup.find(string=par):
        raise Exception(f'No {par} param found!')
    row = soup.find(string=par).parent
    col = row
    for _ in range(5):
        result.append(col.find_next('span').string)
        col = result[-1]
    time.sleep(5)
    return tuple(result)

def test_main():
    with pytest.raises(Exception):
        assert main('Some shit', 'Cost of Revenue')
        assert main('AAPL', 'Some shit')
    assert main('AAPL', 'Total Revenue') == \
           ('Total Revenue', '267,981,000', '260,174,000', '265,595,000',
            '229,234,000', '215,639,000')
    assert isinstance(main('AAPL', 'Cost of Revenue'), tuple)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        raise AttributeError('Must be 2 arguments Ticker and param')
    # print(main('AAPL', 'Total Revenue'))
    ans = main(sys.argv[1], sys.argv[2])
    print(ans)
