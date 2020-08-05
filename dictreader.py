import csv


def dict_func(file_name):
    empty_dict={}
    with open(file_name,'r') as csv_file:
        data = csv.reader(csv_file, delimiter = ',')
        for row in data:
            
            empty_dict[row[0]] = row[1]

    return empty_dict