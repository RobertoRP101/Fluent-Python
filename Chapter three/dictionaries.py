import abc
from unicodedata import name 

def dict_comprehensions():
    """
    This method lets us to build a dictionary
    using the concept of 'list comprenhension'
    """
    
    dial_codes = [
    (880, 'Bangladesh'),
    (55, 'Brazil'),
    (86, 'China'),
    (91, 'India'),
    (62, 'Indonesia'),
    (81, 'Japan'),
    (234, 'Nigeria'),
    (92, 'Pakistan'),
    (7, 'Russia'),
    (1, 'United States'),
    ]
    country_dial = {country: code for code, country in dial_codes} 
    country_dial
    {code: country.upper() 
    for country, code in sorted(country_dial.items())
    if code < 70}
    
# Unpacking mapping

def dump(**kwargs):
    return kwargs

# print(dump(**{'x': 1}, y = 2, **{'z':3}))

def merge_mapp():
    d1 = {'a':1, 'b':3}
    d2 = {'a':2, 'b':4, 'c':6}
    d3 = d1 | d2
    return (d3)

def merge_mapp_update():
    d1 = {'a':1, 'b':3}
    d2 = {'a':2, 'b':4, 'c':6}
    d1 |= d2
    return (d1)

# print(merge_mapp())
# print(merge_mapp_update())
    
def get_creators(record: dict) -> list:
 match record:
    case {'type': 'book', 'api': 2, 'authors': [*names]}: 
        return names
    case {'type': 'book', 'api': 1, 'author': name}: 
        return [name]
    case {'type': 'book'}: 
        raise ValueError(f"Invalid 'book' record: {record!r}")
    case {'type': 'movie', 'director': name}: 
        return [name]
    case _: 
        raise ValueError(f'Invalid record: {record!r}')
    
def food():
    food = dict(category='ice cream', flavor='vanilla', cost=199)
    match food:
        case {'category': 'ice cream', **details}:
            print(f'Ice cream details: {details}')

def abc_mapping_check():
    my_dict = {}
    print(isinstance(my_dict, abc.mapping))
    print(isinstance(my_dict, abc.MutableMapping))
    
def remove_duplicates_ordered():
    dict = {}
    l = ['spam', 'spam', 'eggs', 'spam', 'bacon', 'eggs']
    dict.fromkeys(l).keys()
    print(list(dict.fromkeys(l).keys()))
    
# remove_duplicates_ordered()

def set_comprehension():
    x = {chr(i) for i in range(32, 256) if 'SIGN' in name(chr(i),'')}
    print(x)
    
set_comprehension()

def set_operations():
    set1 = {x for x in range(0,10,1)}
    set2 = {x for x in range(10,20,1)}
    set3 = {x for x in range(5,11,1)}
    print(set1)
    print(set2)
    print(f'Making some operations:')
    print(f'Is disjoint: set1 and set2: {set1.isdisjoint(set2)}')
    print(f'Is element 6 in the set3? {set3.__contains__(6)}')
    print(f'Is element 2 in the set3? {set3.__contains__(2)}')
    

set_operations()
