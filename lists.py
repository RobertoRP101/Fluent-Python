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
    

# Array tip: Array can save memory if we need to retain million of floating-point
# Deque tip: If we need to add and remove information from opposite ends of a list, it's better use the 'deque'
# Set tip: Use a set its an excellent option for checking if an element is in the set
# Set are optimazed for fast membership checking
# Array recommendation: It's better to use an array if the values saved are numbers
# fast loading and saving {.frombytes and .tofile as example}


# When a LIST IS NOT THE ANSWER

def array_for_millions_of_numbers():
    print(f'\narray_for_millions_of_numbers FUNCTION')
    floats = array('d', (random() for x in range(10**7))) # Creating an array of double precision floats
    print(f'First variable: {floats[-1]}') # Reading the last element
    fp = open('floats.bin', 'wb') # Open a pipeline to a binary file with write permissions
    floats.tofile(fp) # Loading the array into the file
    fp.close() # Close the pipeline
    floats2 = array('d')
    fp = open('floats.bin', 'rb') # Open a pipeline to a binary file with read permissions
    floats2.fromfile(fp, 10**7)
    fp.close() # Close the pipeline
    print(f'Second variable: {floats2[-1]}')
    print(f'Are the same the two variables above? {floats == floats2}')


    