import os
import requests
import pickle
import bs4 as bs
import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import numpy as np
import pandas as pd
import pandas_datareader.data as web
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


# Scraping the s&p 500 ticker name using Beautifulsoup
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

# save_sp500_tickers()


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

# get_data_from_yahoo()


'''Check for any ticker data not downloaded'''
# for ticker in tickers:
#     if not os.path.exists('stocks_dfs/{}.csv'.format(ticker)):
#         print(ticker)

# COMPILE ALL INDIVIDUAL STOCKS INTO ONE DATAFRAME


def compile_data():
    with open('sp500tickers.pickle', 'rb') as f:
        tickers = pickle.load(f)

        main_df = pd.DataFrame()
        
        for count, ticker in enumerate(tickers):
            if not os.path.exists('stocks_dfs/{}.csv'.format(ticker)): #skip any tickers not found in our stored directory
                continue

            df = pd.read_csv('stocks_dfs/{}.csv'.format(ticker.replace('.', '-')))
            df.set_index('Date', inplace=True)

            df.rename(columns={'Adj Close': ticker}, inplace=True)
            df.drop(['Open', 'High', 'Low', 'Close', 'Volume'], 1, inplace=True)

            if __name__==df.empty:
                main_df = df
            else:
                main_df = main_df.join(df, how='outer')

            if count % 10 == 0:
                print(count)
        print(main_df.head())
        main_df.to_csv('sp500_joined_Adj_closes.csv')

# compile_data()


#CORRELATION TABLE
def visualize_data():
    df = pd.read_csv('sp500_joined_Adj_closes.csv')
    # df['AAPL'].plot()
    # plt.show()
    df_corr = df.corr()  # correlation table
    print(df_corr.head())

    data = df_corr.values #numpy array of columns and rows
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1) #last number=plot number 1

    heatmap = ax.pcolor(data, cmap=plt.cm.RdYlGn) #Red, Yellow, Green(RGB)
    fig.colorbar(heatmap)
    ax.set_xticks(np.arange(data.shape[0]) + 0.5, minor=False)
    ax.set_yticks(np.arange(data.shape[1]) + 0.5, minor=False)
    ax.invert_yaxis()
    ax.xaxis.tick_top() #places the ticks(tickers) labels at the bottom compared to the dafault bottom

    column_labels = df_corr.columns
    row_labels = df_corr.index

    ax.set_xticklabels(column_labels)
    ax.set_yticklabels(row_labels)
    plt.xticks(rotation=90)
    heatmap.set_clim(-1,1) #color limit-max(-1)=negative corr to min(1)=positive corr
    plt.tight_layout()
    plt.show()


visualize_data()
