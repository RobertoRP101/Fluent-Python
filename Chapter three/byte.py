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

def another_error_decode_encode():
    octets = b'El Ni\xc3\xb1o'  # Byte string representing 'El Niño' in UTF-8
    print("Original byte string:", octets)
    
    # Correct decoding with UTF-8
    print("Decoded with UTF-8:", octets.decode('utf-8'))
    
    # Incorrect decoding with Latin-1
    print("Decoded with Latin-1:", octets.decode('latin1'))
    
    # Incorrect decoding with CP1252
    print("Decoded with CP1252:", octets.decode('cp1252'))
    
    # Attempt to decode with ASCII (will raise an error)
    try:
        print("Decoded with ASCII:", octets.decode('ascii'))
    except UnicodeDecodeError as e:
        print("Error decoding with ASCII:", e)
    
    # Decoding with ASCII using error handling
    print("Decoded with ASCII (ignore errors):", octets.decode('ascii', errors='ignore'))
    print("Decoded with ASCII (replace errors):", octets.decode('ascii', errors='replace'))


    