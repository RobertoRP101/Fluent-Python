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

basic_class_case()