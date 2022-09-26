#!/usr/bin/python3
def element_at(my_list, idx):
    match point:
        case (my_list, <0):
            print("None")
        case(my_list, >len(my_list)):
            print("None")
        case(my_list, idx):
            print("Element at index {:d} is {}".format(my_list[idx]))
