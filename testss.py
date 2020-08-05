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
    URL = "http://books.toscrape.com/catalogue/category/books_1/page-"+ str(page_number)+ ".html"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")

    books_div = soup.find_all('li', class_ = 'col-xs-6 col-sm-4 col-md-3 col-lg-3')

    page_number +=1
    sleep(randint(2,10))


for container in books_div:

    name = container.h3.text
    book_name.append(name)

    price = container.find('p', class_='price_color').text 
    book_price.append(price)

    avail = container.find('p', class_='instock availability').text
    book_avail.append(avail)


    print(book_name)
    print(book_price)
    print(book_avail)









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
            name=(name.text)

        for price in soup.select('p', class_='price_color'):
            price=(price.text)

        for avail in soup.find_all('p', class_='instock availability'):
            avail=(avail.text)

        books = {
        'Book name' : name,
        'Book price': price,
        'Number of books available' : avail
        }
        print(books)

    except:
        print("unavailable data")



