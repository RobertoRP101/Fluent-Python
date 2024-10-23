import array

def byte_and_arraybyte():
    cafe = bytes('café', encoding='utf_8') 
    print(f'Cafe: {cafe}')
    print(f'Cafe[0]: {cafe[0]}') 
    print(f'Cafe[:1]: {cafe[:1]}')
    cafe_arr = bytearray(cafe)
    print(f'cafe_arr: {cafe_arr}')
    print(f'cafe_arr[-1:]: {cafe_arr[-1:]}')
    

def creating_array_numbers():
    numbers = array.array('h', [-2, -1, 0, 1, 2]) 
    octets = bytes(numbers) 
    octets


def encode_by_codecs():
    city = 'São Paulo'
    print(city.encode('utf_8') )
    print(city.encode('utf_16'))
    print(city.encode('iso8859_1') )
    print(f'This line of code will give an error. city.encode("cp437") ')
    print(city.encode('cp437', errors='ignore') )
    print(city.encode('cp437', errors='replace') )
    print(city.encode('cp437', errors='xmlcharrefreplace') )


# byte_and_arraybyte()
encode_by_codecs()


def error_decode_encode():
    octets = b'Montr\xe9al' 
    print(octets.decode('cp1252') )
    print(octets.decode('iso8859_7') )
    print(octets.decode('koi8_r') )
    print(octets.decode('utf_8') )
    print(octets.decode('utf_8', errors='replace') )
    
error_decode_encode()

    