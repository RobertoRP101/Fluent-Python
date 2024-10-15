def parallel_assignment():
    coordinates = (33.9425, -118.408056)
    latitude, longitude = coordinates  # Directly assigns values
    print("Latitude:", latitude, "Longitude:", longitude)

def swapping_values():
    numbers = [0, 10, 20, 30, 40]
    print("Before swapping:", numbers)
    numbers[0], numbers[-1] = numbers[-1], numbers[0]  # Swaps first and last items
    print("After swapping:", numbers)

def prefixing_an_argument():
    t = (20, 8)
    result = divmod(*t)  # Unpacks the tuple into divmod
    print("Quotient and Remainder:", result)
    
def grab_excess_items():
    a, b, *excess = range(10)  # First two items to a and b, the rest to excess
    print(f"a: {a}, b: {b}, excess: {excess}")

def parallel_assignment_and_grab_excess():
    a, b, *middle, d = range(8)  # First, last, and middle items separated
    print(f"a: {a}, b: {b}, middle: {middle}, d: {d}")

def operator_asterisk_over_iterables():
    result = {*range(5), 3}  # Set with unpacked range and an additional value
    print("Set with unpacked range:", result)

def unpacking_nested():
    metro_areas = [
        ('Tokyo', 'JP', 36.933, (35.689722, 139.691667)), 
        ('Delhi NCR', 'IN', 21.935, (28.613889, 77.208889)),
        ('Mexico City', 'MX', 20.142, (19.433333, -99.133333)),
    ]
    
    for name, _, _, (lat, lon) in metro_areas:
        print(f"City: {name}, Latitude: {lat}, Longitude: {lon}")

def handle_match(message):
    match message:
        case ['Option 1', games, category]:
            print(f"Option 1 with games: {games}, category: {category}")
        case ['Option 2', books]:
            print(f"Option 2 with books: {books}")
        case [*others]:
            print("Other options detected")
