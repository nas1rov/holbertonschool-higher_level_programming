#!/usr/bin/python3

def search_replace(my_list, search, replace):
    # Siyahıdakı hər element üçün: əgər element search-ə bərabərdirsə replace qoy,
    # deyilsə elementin özünü saxla.
    return [replace if x == search else x for x in my_list]
