# DAY 22
# SHORTS: STRING SLICING

def main():

    phone = "617-495-1000"
    print(phone[0:3])       # [0:3] => prints the string starting from the 0th index and stopping before the 3rd index.
    # Output: 617

    print(phone[:3])        # [:3] => prints the string starting from the 0th index and stopping before the 3rd index
    # Output: 617

    print(phone[8:12])      # [8:12] => prints the string starting from the 8th index and stopping before the 12rd index
    # Output: 1000

    print(phone[8:])        # [8:] => prints the string starting from the 0th index and stopping before the 3rd index
    # Output: 1000

    print(phone[-4:])       # [-4:] => prints the string starting from the right hand side of 4 indexes.
    # Output: 1000


main()

#################

# SHORT: TUPLE

import sys

def main():
    coordinates = (42.376, -71.115)
    
    latitude,longitude = coordinates

    print(f"Longitude: {coordinates[1]}")
    print(f"Latitude: {coordinates[0]}")

    print(f"Longitude: {longitude}")
    print(f"Latitude: {latitude}")

main()

#######

def main():
    coordinates_tuple = (42.376, -71.115)
    coordinates_list = [42.376, -71.115]
    coordinates_dict = {42.376, -71.115}
    
    print(f"{sys.getsizeof(coordinates_tuple)} bytes")
    print(f"{sys.getsizeof(coordinates_list)} bytes")
    print(f"{sys.getsizeof(coordinates_dict)} bytes")


main()

######################

# SHORT: WHILE LOOPS
"""
def main():
    moisture = sample()
    Days = 0
    print(f"Days: {Days}: Moisture is {moisture}%")

    while moisture > 20:
        moisture = sample()
        days +=1
        print(f"Moisture is {moisture}%")

    print("Time to water")
main()
"""
