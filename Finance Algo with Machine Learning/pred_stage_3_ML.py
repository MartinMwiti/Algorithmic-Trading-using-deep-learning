from collections import Counter
import numpy as np
import pandas as pd
import pickle

hm_days = 7

#Objective: if price moves up by say 2% in the last 'hm_days', BUY, if price fell by 2% in those days, SELL, otherwise hold
def process_data_for_labels(ticker):
    hm_days = 7 #past days to check price movement
    df = pd.read_csv('sp500_joined_Adj_closes.csv', index_col=0)
    tickers = df.columns.values.tolist()
    df.fillna(0, inplace=True)

    for i in range(1, hm_days+1):
        df['{}_{}d'.format(ticker, i)] = ((df[ticker].shift(-i) - df[ticker])/df[ticker])

    df.fillna(0 , inplace=True)

    return tickers,  df


def buy_sell_hold(*args):
    cols = [c for c in args]
    requirement = 0.02
    for col in cols:
        if col > requirement:
            return 1 #BUY
        if col < requirement:
            return -1 #SELL
    return 0 #HOLD


def extract_featuresets(ticker):
    tickers, df = process_data_for_labels(ticker)

    df['{}_target'.format(ticker)] = list(map(buy_sell_hold, *[df['{}_{}d'.format(ticker, i)] for i in range(1, hm_days+1)]))
    vals = df['{}_target'.format(ticker)].values
    str_vals = [str(i) for i in vals]
    print('Data spread: ', Counter(str_vals))
    df.fillna(0, inplace=True)

    df = df.replace([np.inf, -np.inf], np.nan) #replace infinite number with NA
    df.dropna(inplace=True)
    
    df_vals = df[[ticker for ticker in tickers]].pct_change()
    df_vals = df_vals.replace([np.inf, -np.inf], 0)
    df_vals.fillna(0, inplace=True)

    X = df_vals
    y = df['{}_target'.format(ticker)].values

    return X, y, df

extract_featuresets('NVDA')