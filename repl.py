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

    books_div = soup.find('h3')
    for row in books_div:  
        print(books_div.string)

    page_number +=1
    sleep(randint(2,10))

