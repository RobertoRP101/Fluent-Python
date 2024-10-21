import abc


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
    
remove_duplicates_ordered()