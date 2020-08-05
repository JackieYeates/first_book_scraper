import pandas as pd
import requests 
import csv
import numpy as np
from bs4 import BeautifulSoup
from time import sleep
from random import randint


URL = 'http://books.toscrape.com/catalogue/category/books_1/page-6.html'
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")

book_name = []
book_price = []
book_avail = []


"""pages = np.arange(1,1001,50)"""


books_div = soup.find_all('div', class_ = 'col-xs-6 col-sm-4 col-md-3 col-lg-3')
    
"""sleep(randint(2,10))"""

for container in books_div:

    name = container.h3.a.text
    book_name.append(name)
    
    price = container.find('p', class_='price_color').text 
    book_price.append(price)

    avail = container.find('p', class_='instock availability').text
    book_avail.append(avail)

    books = pd.DataFrame({
    'Book name' : book_name,
    'Book price': book_price,
    'Number of books available' : book_avail
    })

print(book_name)    
print(book_price)
print(book_avail)


