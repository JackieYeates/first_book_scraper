import pandas as pd
import requests 
import csv
from bs4 import BeautifulSoup
from time import sleep
from random import randint
import numpy as np


book_name = []
book_price = []
book_avail = []
book_rating = []
book_reviews = []

pages = np.arange(1,1001,20)

for page in pages:
    page = requests.get("http://books.toscrape.com/catalogue/category/books_1/page-"+ str(page)+ ".html")
    soup = BeautifulSoup(page.content, "html.parser")
    books_div = soup.find_all('li', class_ = 'col-xs-6 col-sm-4 col-md-3 col-lg-3')
    sleep(randint(2,10))

    try:

        for name in soup.find_all('h3'):
            name = name.text
            print(name)

        for price in soup.select('p', class_='price_color'):
            price = price.text

        for avail in soup.find_all('p', class_='instock availability'):
            avail = avail.text

    


    except:
        print("unavailable data")





