import csv


def book_func(file_name):
    empty_book={}
    with open(file_name,'r') as csv_file:
        data = csv.reader(csv_file, delimiter = ',')
      

    return empty_book