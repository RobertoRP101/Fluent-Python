def parallel_assignment():
    coordinates = (33.9425, -118.408056)
    latitude, longitude = coordinates  # Directly assigns values
    print("Latitude:", latitude, "Longitude:", longitude)

def swapping_values():
    numbers = [0, 10, 20, 30, 40]
    print("Before swapping:", numbers)
    numbers[0], numbers[-1] = numbers[-1], numbers[0]  # Swaps first and last items
    print("After swapping:", numbers)

