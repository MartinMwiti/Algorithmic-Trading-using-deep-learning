import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
from mpl_finance import candlestick_ohlc
import matplotlib.dates as mdates
import pandas as pd
import pandas_datareader.data as web
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()


style.use('ggplot')

#start = dt.datetime(2010,1,1)
#end = dt.datetime(2020, 1, 1)

# I'll be working with TESLA stock data
# df = web.DataReader('TSLA', 'yahoo', start, end) #Ticker is a symbol for a company
# print(df.head())
# df.to_csv('tsla.csv') #export data to csv file

df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)
# print(df.head())

#print(df[['Open', 'High']].head())
#df['Adj Close'].plot()
# plt.show()

# takes todays price, takes 99 prior day prices then creates the average
#df['100ma'] = df['Adj Close'].rolling(window=100, min_periods=0).mean()
# print(df.head())

# ohlc-open, high, low, close. Based on 10 days of data
df_ohlc = df['Adj Close'].resample('10D').ohlc()
# .resample('10D') is another form of selecting timeframe for your price, eg, daily, weekly, monthly, weekly.
df_volume = df['Volume'].resample('10D').sum()

df_ohlc.reset_index(inplace=True)

df_ohlc['Date'] = df_ohlc['Date'].map(mdates.date2num)

# Visualizaion
# (6,1)-rows, columns. (0,0)-top corner
ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5, colspan=1)
ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=5, colspan=1, sharex=ax1)
ax1.xaxis_date()

# PLOT 1 - MA100,Adj_close_price&Vol_chart
# ax1.plot(df.index, df['Adj Close'])#df.index-plot date
# ax1.plot(df.index, df['100ma'])
# ax2.bar(df.index, df['Volume'])

# PLOT 2 - candlestick_price_movement_graph
# candlestick_ohlc(ax1, df_ohlc.values, width=2, colorup='g')
# ax2.fill_between(df_volume.index.map(mdates.date2num),
#                  df_volume.values, 0)  # fill y-values(df_volume.values) from 0 to that y-value. fill_between fills entire color within the bad plot
# plt.show()
