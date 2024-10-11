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
    
    
# Sorting the original list 
def sort_list_inplace():
    '''
    This method uses the sorted method,
    this means that we are not creating
    a new list, is in place
    '''
    l = [ f'{x}' for x in range(0,-20,-1)]
    print(f'Id normal list: {id(l)}')
    l.sort(key=len, reverse=True)
    print(f'This function don\'t return a copy: {l}\nand the reference is: {id(l)}')