import typing
from collections import namedtuple

class Coordinates():
    def __init__(self, lat, lon) -> None:
        self.lat = lat
        self.lon = lon

def basic_class_case():        
    moscow = Coordinates(55.76, 37.62)
    location = Coordinates(55.76, 37.62)
    print(moscow)
    print(location)
    print(f'Are the classes equals: {location == moscow}')
    print(f'Are their attributes of each class equals: {(moscow.lat, moscow.lon) == (location.lat, location.lon)}')

# basic_class_case()


# Since this point we can create subclasses to
# save data

def collection_use():
    Coordinate = namedtuple('Coordinate', 'lat lon')
    print(f'Is subclass of tuple: {issubclass(Coordinate, tuple)}')
    moscow = Coordinate(55.756, 37.617)
    print(moscow)
    print(f'Is equal the instance moscow with a ne object with the same coordinates: {moscow == Coordinate(lat=55.756, lon=37.617)}')
    
# collection_use()

def using_typing_coordinate():
    # Coordinate = namedtuple('Coordinate', 'lat lon')
    Coordinate = typing.NamedTuple('Coordinate', [('lat', float), ('lon', float)])
    print(f'Is Coordinate a subclass of tuple: {issubclass(Coordinate, tuple)}')
    print(typing.get_type_hints(Coordinate))
    
    
using_typing_coordinate()