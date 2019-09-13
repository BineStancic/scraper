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

#style.use('fivethirtyeight')
#fig = plt.figure()
#ax1 = fig.add_subplot(1,1,1)

#def animate(i):
#    graph_data = open('samplefile.txt').read()

URL = 'https://www.coingecko.com/en/coins/bitcoin'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}


page = requests.get(URL, headers = headers)

soup = BeautifulSoup(page.content, 'html.parser')

#<span class="no-wrap" data-price-btc="1" data-coin-id="1" data-coin-symbol="btc" data-target="price.price" data-price-previous="10297.252">$10,297.25</span>










data = []
BTX_DATA = []

def find_exchange():
    i = 0
    for paragraph in soup.find_all('span'):
        i += 1
        if i == 37:
            print(paragraph.text)
            break




while True:
    find_exchange()
    time.sleep(60)
#title = soup.find('h4' class_="Header__StyledHeader-sc-1q6y56a-0 gEArVu TextElement__Spacer-sc-18l8wi5-0 hpeTzd")
#print(title)
#price = title.get_text()
