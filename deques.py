from collections import deque

def deque_basic_behaviour():
    dq = deque(range(10), maxlen=10)
    print(f'Printing the deque: {dq}')
    dq.rotate(3)
    print(f'Deque rotated: {dq}')
    dq.rotate(-4)
    print(f'Deque rotated (negative shift): {dq}')
    dq.appendleft(-1)
    print(f'Deque printed after append a number by the left: {dq}')
    dq.extend([11, 12, 13])
    print(f'Deque printed after appling extend method with 3 elements: {dq}')
    dq.extendleft([10, 20, 30, 40])
    print(f'Deque printed after appling extend by the left with 4 numbers: {dq}')
    
deque_basic_behaviour()
