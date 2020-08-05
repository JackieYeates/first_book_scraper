import pandas as pd
import requests 
import csv
from bs4 import BeautifulSoup

URL = 'http://books.toscrape.com/catalogue/its-only-the-himalayas_981/index.html'
page = requests.get(URL)

soup = BeautifulSoup(page.content, "html.parser")


book_name = []
book_price = []
book_avail = []
book_rating = []

books.to_csv(r'C:\Users\Jackie Yeates\Documents\codebase\Scraper\scraper.csv')
books_div = soup.find_all('div', class_ = 'col-sm-6 product_main')



for container in books_div:

        name = container.h1.text
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



