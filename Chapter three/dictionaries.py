
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

print(dump(**{'x': 1}, y = 2, **{'z':3}))

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

print(merge_mapp())
print(merge_mapp_update())
    
