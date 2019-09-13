import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
import time

time_start = time.time()

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}


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
            time_now = time.time()
            break
    return time_now,y



while True:
    time_now,y = find_exchange()
    x = time_now-time_start
    file1 = open('data_exchange.txt', 'a')
    file1.write(str(x)+ "," +str(y) +"\n")
    file1.close()
    print(x,y)
    time.sleep(6)
