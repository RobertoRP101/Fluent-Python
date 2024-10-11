from array import array
from random import random
# list.sort: change a list in place

# Creating a new list
def sort_list():
    '''
    This method uses the sorted function,
    this means that we are creating
    a new list.
    '''
    l = list(range(0,-20,-1))
    print(f'Id normal list: {id(l)}')
    sorted_l = sorted(l, reverse=True)
    print(f'This function returns a copy: {sorted_l}\nand the reference is: {id(sorted_l)}')