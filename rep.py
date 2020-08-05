import pandas as pd
import numpy as np
import requests 
import csv
from bs4 import BeautifulSoup
from time import sleep
from random import randint



book_name = []
book_price = []
book_avail = []
book_rating = []
book_reviews = []

pages = np.arange(1,1001,20)


for page in pages:
    page_number = 1
    URL = "http://books.toscrape.com/catalogue/category/books_1/page-3.html"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    
    books_div = soup.find_all('h3', class_ = 'col-xs-6 col-sm-4 col-md-3 col-lg-3')

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
    
    page_number +=1
    sleep(randint(2,10))

    print(book_name)    
    print(book_price)
    print(book_avail)

