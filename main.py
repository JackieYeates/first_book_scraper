from dictreader import dict_func


baby_dict = dict_func('dictionary_names.csv')


search_string = str(input("Type in a name to search engine: "))
search_string = search_string.upper()


if search_string in baby_dict:
        print(baby_dict[search_string])

else:
        print( f"{search_string} doesn't exist in this dictionary.")




