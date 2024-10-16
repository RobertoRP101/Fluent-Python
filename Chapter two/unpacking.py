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
    
    
# Mixing up to strategies to unpack values
def parallel_assignment_and_grab_excess():
    '''
    This method lets us assign as many
    values as we want according to
    the * operator prefixing a
    variable to grab all the excess.
    The context used here is parallel
    assignment 
    '''
    a, b, c, *group, d = range(8)
    print('Position 4:')
    print(f'a: {a}, b: {b}, c: {c}, group: {group}, d: {d}')
    *group, a, b, c, d = range(8)
    print('Position 1:')
    print(f'group: {group}, a: {a}, b: {b}, c: {c}, d: {d}')
    
    
# Using * to yield single values
def operator_asterisk_over_iterables():
    '''
    This method lets us to build an
    iterable with another iterable
    and getting each value by it's
    own
    '''
    print(f'{*range(5), 3}')
    print(f'{(*range(10), 3)}')
    print(f'{set((*range(0,-20,-2), 3, *range(3,13,2)))}')
    
    
def unpacking_nested():
    metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)), 
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
    ]
    
    for x in metro_areas:
        city, abreviation, population, coordinates = x
        print(f'city: {city}, abreviation: {abreviation}, population: {population}, coordinates: {coordinates}')
        
    print(f'{"":15} | {"latitude":>9} | {"longitude":>9}')
    for name, _, _, (lat, lon) in metro_areas: 
        if lon <= 0: 
            print(f'{name:15} | {lat:9.4f} | {lon:9.4f}')
            
# Match case
def handle_match(message):
    match message: # Subject: Subject that Python will try to match
        case ['Option 1', games, category]:
            print(f'Option 1, games: {games}, category: {category}')
        case ['Option 2', books]:
            print(f'Option 2, books: {books}')
        case ['Option 3', hours, exercises, fellas]:
            print(f'Option 3, hours: {hours}, exercises: {exercises}, fellas: {fellas}')
        case [*excess]:
            print('Many variables were detected here')
        case _:
            raise 'Command not found'
        
        
def unpacking_nested_handle_match():
    metro_areas = [
    ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)), 
    ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
    ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ('New York-Newark', 'US', 20.104, (40.808611, -74.020386)),
    ('São Paulo', 'BR', 19.649, (-23.547778, -46.635833)),
    ]
    print()
    for record in metro_areas:
        match record:
            case [name, _, _, (lat, lon)] if lon <= 0:
                print(f'{name:15} | {lat:9.4f}  | {lon:9.4f}')
    
    
def alternative_patterns_lambda(parameters):
    match parameters:
        # case ['lambda', parms, *body] if body:
        #     print(f'Case accepted\n parms: {parms}\n body: {body}')
            
        case ['lambda', [*parms], *body] if body:
            print(f'Rare case: {body}')
        
        case [*execess]:
            print(f'{execess}')
