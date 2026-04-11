#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    # Requirement: Return a copy of the original list if idx is invalid
    if idx < 0 or idx >= len(my_list):
        return my_list.copy()
    # Create a shallow copy of the list
    new_list = my_list.copy()
    new_list[idx] = element
    return new_list
