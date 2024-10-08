import numpy as np

# Parallel assigment
def parallel_assigment():
    '''
    This method needs a specific
    number of variables to work
    properly, based on of the
    number of items inside the
    iterator
    '''
    coordinates = (33.9425, -118.408056)
    latitude, longitude = coordinates
    print(latitude, longitude)
    
# Swapping values
def swapping_values():
    numbers = [x for x in range(0,50,10)]
    print('Before swapping')
    print(numbers)
    numbers[0], numbers[-1] = numbers[-1], numbers[0]
    print('After swapping')
    print(numbers)
    
# Prefixing an argument
def prefixing_an_argument():
    '''
    This unpacking method use the *
    operator to access to each
    element inside an iterable
    '''
    divmod(20, 8)
    t = (20, 8)
    print(divmod(*t))
    quotient, remainder = divmod(*t)
    print(f'quotient {quotient}, remaider{remainder}')