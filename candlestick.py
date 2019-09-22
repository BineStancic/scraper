import matplotlib.pyplot as plt
import plotly.graph_objects as go

from matplotlib.finance import candlestick_ohlc

data = open("candle_data.txt","r").read()

lines = graph_data.split('\n')
date, open, high, low, close = line.split(',')


fig = go.Figure(data=[go.Candlestick(x=df['date'],
                open=df['AAPL.Open'],
                high=df['AAPL.High'],
                low=df['AAPL.Low'],
                close=df['AAPL.Close'])])

fig.show()
