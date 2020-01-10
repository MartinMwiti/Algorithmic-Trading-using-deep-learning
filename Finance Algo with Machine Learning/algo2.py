import os
import requests
import pickle
import bs4 as bs
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


#Getting the s&p 500 list using Beautifulsoup
def save_sp500_tickers():
    resp = requests.get(
        'https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
    # our source page data is in txt
    soup = bs.BeautifulSoup(resp.text, 'lxml')
    table = soup.find('table', {'class': 'wikitable sortable'})
    tickers = []
    for row in table.findAll('tr')[1:]:
        # strip() in-built function of Python is used to remove all the leading and trailing spaces from a string.
        ticker = row.findAll('td')[0].text.strip()
        tickers.append(ticker)

    with open("sp500tickers.pickle", 'wb') as f:
        pickle.dump(tickers, f)

    print(tickers)

    return tickers

#save_sp500_tickers()


def get_data_from_yahoo(reload_sp500=False):
    if reload_sp500:  # if True, i.e if the pickle does not exist
        tickers = save_sp500_tickers()
    else:
        with open("sp500tickers.pickle", "rb") as f:
            tickers = pickle.load(f)

    # if the directory doesn't exist locally, create one
    if not os.path.exists('stocks_dfs'):
        os.makedirs('stocks_dfs')

    start = dt.datetime(2000, 1, 1)
    end = dt.datetime.now()
    # for ticker in tickers[:500]: in case you want 500 tickers
    df = pd.DataFrame
    for ticker in tickers:  # this gets 500 tickers
        print(ticker)

        if not os.path.exists('stocks_dfs/{}.csv'.format(ticker)):  # check for csv file
            try:
                df = web.DataReader(ticker, 'yahoo', start, end)
                df.to_csv('stocks_dfs/{}.csv'.format(ticker))
            except:
                tickers.remove(ticker)

        else:
            print('Already have {}'.format(ticker))

get_data_from_yahoo()

# for ticker in tickers:
#     if not os.path.exists('stocks_dfs/{}.csv'.format(ticker)):
#         print(ticker)
