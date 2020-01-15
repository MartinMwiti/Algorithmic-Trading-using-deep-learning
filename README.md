# Algorithmic-Trading-using-deep-learning
### Quantitative modeling with application of Machine Learning, and Deep Learning RNN-LSTM.

## Dependencies
1. ```pip install Keras```
2. ```pip install tensorflow```
3. ```pip install numpy```
4. ```pip install pandas_datareader```
5. ```pip install mpl_finance```
6. ```pip install BeautifulSoup4```
7. ```pip install requests```
8. ```pip install hmmlearn```

## Charts
### 1. Finance Algo with Machine Learning.
* Chart 1 - *Candlestick price movement graph*
![candlestick price movement graph](https://github.com/MartinMwiti/Algorithmic-Trading-using-deep-learning/blob/master/Finance%20Algo%20with%20Machine%20Learning/candlestick_price_movement_graph.png)

* Chart 2 - *100days Moving Average graph*
![100days Moving Average graph](https://github.com/MartinMwiti/Algorithmic-Trading-using-deep-learning/blob/master/Finance%20Algo%20with%20Machine%20Learning/MA100%2CAdj_close_price%26Vol_chart.png)

## Codes
* [stage_1.py](https://github.com/MartinMwiti/Algorithmic-Trading-using-deep-learning/blob/master/Finance%20Algo%20with%20Machine%20Learning/stage_1.py) : Involves data collection from Yahoo Finance.
* [stage_2.py](https://github.com/MartinMwiti/Algorithmic-Trading-using-deep-learning/blob/master/Finance%20Algo%20with%20Machine%20Learning/stage_2.py) : Involves feature engineering.
* [pred_stage_3_ML.py](https://github.com/MartinMwiti/Algorithmic-Trading-using-deep-learning/blob/master/Finance%20Algo%20with%20Machine%20Learning/pred_stage_3_ML.py) : Involves stock prediction using Machine Learning
* [pred_stage_3_HM.py](https://github.com/MartinMwiti/Algorithmic-Trading-using-deep-learning/blob/master/Finance%20Algo%20with%20Machine%20Learning/pred_stage_3_HM.py) : Involve stock prediction using Hidden Markov Model. (**Still a work in progress**)

## Files
* [stocks_dfs](https://github.com/MartinMwiti/Algorithmic-Trading-using-deep-learning/tree/master/Finance%20Algo%20with%20Machine%20Learning/stocks_dfs) : contains stock data for all individual s&p500 companies since 2000.
* [sp500_joined_Adj_closes.csv](https://github.com/MartinMwiti/Algorithmic-Trading-using-deep-learning/blob/master/Finance%20Algo%20with%20Machine%20Learning/sp500_joined_Adj_closes.csv) : containes merged Adjusted Close stock data for all s&p500 companies since 2000.
