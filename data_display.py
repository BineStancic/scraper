import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time
############################
import matplotlib.ticker as ticker
from matplotlib.finance import candlestick_ohlc


style.use('fivethirtyeight')
fig = go.Figure(data)
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    graph_data = open('data_exchange.txt', 'r').read()
    lines = graph_data.split('\n')
    x_axis = []
    y_axis = []
    for line in lines:
        if len(line) > 1:
            x, y = line.split(',')
            x_axis.append(x)
            y_axis.append(y)
    ax1.clear()
    ax1.set_xlabel("time")
    ax1.set_ylabel("price USD")
    ax1.plot(x_axis, y_axis)

#ani = animation.FuncAnimation(fig, animate, interval = 1000)
#plt.show()


ani = animation.FuncAnimation(fig, animate, interval = 1000)
plt.xlabel("Time")
plt.ylabel("Price USD")
plt.show()
