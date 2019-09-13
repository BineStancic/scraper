import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time

#time.time() 1970
#time.asctime()

#now = time.gmtime()
#print(now[2])

##############3
#start = time.time()
#stop = time.time()
#print(stop-start)


#URL = 'https://www.coingecko.com/en/coins/bitcoin'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}


#page = requests.get(URL, headers = headers)

#soup = BeautifulSoup(page.content, 'html.parser')

data = []
BTX_DATA = []

def find_exchange():
    URL = 'https://www.coingecko.com/en/coins/bitcoin'

    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')



    i = 0
    for paragraph in soup.find_all('span'):
        i += 1
        if i == 37:
            BTX_price = paragraph.text
            y_1 = BTX_price.translate({ord('$'): None})
            y = y_1.translate({ord(','): None})
            print(y)
            x = time.time()
            break
    return x,y

style.use('fivethirtyeight')
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)

def animate(i):
    #graph_data = open('exchangedata.txt', 'r').read()
    #lines = graph_data.split('\n')
    x_axis = []
    y_axis = []
    #for line in lines:
    #    if len(line) > 1:
    #        x, y = line.split(',')
    x_axis.append(x)
    y_axis.append(y)
    ax1.clear()
    ax1.plot(x_axis, y_axis)

#ani = animation.FuncAnimation(fig, animate, interval = 1000)
#plt.show()

i = 0
while True:
    x,y = find_exchange()
    print(x,y)
    time.sleep(6)
    i+=1
    if i >10:
        ani = animation.FuncAnimation(fig, animate, interval = 1000)
        plt.show()
