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
