from array import array
from random import random
import numpy as np
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

# --------------------------------
# Array section
from array import array



# Memory view
def memory_distribution():
    '''
    This function lets us to interact
    with an array with three
    reference. Each reference has a
    different distribution, but
    the content they point out is the
    same. We constructed 3 different
    memoryview variables
    '''
    
    octets = array('B', range(6))
    m1 = memoryview(octets)
    print(m1.tolist())
    m2 = m1.cast('B', [2,3])
    print(m2.tolist())
    m3 = m1.cast('B', [3,2])
    print(m3.tolist())
    m2[1,1] = 22
    m3[1,1] = 33
    print(octets)
  

# -
def basic_numpy():
    '''
    This function lets us see
    the beahaviour of numpy
    for basic operations
    '''
    a = np.arange(12)
    print(a)
    print(a.shape)
    a.shape = (3,4)
    print(a)
    # Acess to one element
    print(a[2,1])
    # Getting a specific column with all its rows
    print(a[:, 1])
    # Transpose method
    print(a.transpose())

    
       
    
    
memory_distribution()
basic_numpy()
    