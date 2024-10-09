# Sequence types
# Exclude the last element: range and slice

import numpy as np

l = [10, 20, 30, 40, 50, 60, 70]

# Slicing a list
def getting_specific_element(l):
    '''
    This method prints a sub list of elements,
    specific the first and last ones
    '''
    print(f'Exclude the two first elements: {l[2:]}')
    print(f'Exclude the two last elements: {l[:-2]}')
    
