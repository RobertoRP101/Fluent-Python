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
    
    
# Grab arbitrary excess arguments
def grab_excess_items():
    '''
    This method lets us show how
    to take a group of items
    without defining additional
    variables
    '''
    print('Range 5')
    a, b, *excess = range(2)
    print(f'a: {a}, b: {b}, excess: {excess}')
    print('Range 10')
    a, b, *excess = range(10)
    print(f'a: {a}, b: {b}, excess: {excess}')
    print('Random range')
    a, b, *excess = np.random.normal(0,1,100)
    print(f'a: {a}, b: {b}, excess: {excess}')