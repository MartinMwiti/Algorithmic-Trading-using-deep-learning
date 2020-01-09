import datetime as dt
import matplotlib.pyplot as plt
from matplotlib import style
import pandas as pd
import pandas_datareader.data as web


style.use('ggplot')

#start = dt.datetime(2010,1,1)
#end = dt.datetime(2020, 1, 1)

#df = web.DataReader('TSLA', 'yahoo', start, end) #Ticker is a symbol for a company
#print(df.head())
#df.to_csv('tsla.csv') #export data to csv file

df = pd.read_csv('tsla.csv', parse_dates=True, index_col=0)
#print(df.head())

#print(df[['Open', 'High']].head())
#df['Adj Close'].plot()
#plt.show()




