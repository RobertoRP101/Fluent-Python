def byte_and_arraybyte():
    cafe = bytes('café', encoding='utf_8') 
    print(f'Cafe: {cafe}')
    print(f'Cafe[0]: {cafe[0]}') 
    print(f'Cafe[:1]: {cafe[:1]}')
    cafe_arr = bytearray(cafe)
    print(f'cafe_arr: {cafe_arr}')
    print(f'cafe_arr[-1:]: {cafe_arr[-1:]}')
    

byte_and_arraybyte()