# Sequence types
# Exclude the last element: range and slice

import numpy as np

l = [10, 20, 30, 40, 50, 60, 70]

# Slicing a list
def getting_specific_element(l):
    '''
    This method prints a sub list of elements,
    specific the first and last ones
    '''
    print(f'Exclude the two first elements: {l[2:]}')
    print(f'Exclude the two last elements: {l[:-2]}')
    
    
# Edit (using slice) and delete information
def edit_and_delete_information():
    '''
    This function let us
    watch how editing and deleting a
    sequence type
    '''
    l = list(range(0,100,10))
    print(l)
    
    # Editing
    l[0:10:2] = (range(1,6))
    print(f'Elements edited: {l}')
    
    # Deleting the las element
    del l[-1]
    print(f'Elememt deleted: {l}')
    

# Duplicate the information from a list
def using_asterisk_duplicate_information():
    l = list(range(0,-20,-2))
    print(f'Normal list: {l}')    
    print(f'Extra list two times: {l*2}')
    
    
# Creating a list to with reference to other lists
def building_list_of_lists():
    '''
    This method allows us to
    create nested list
    '''
    board = [['_']*3 for x in range(3)]
    print(board)
    board_game = np.array(board).reshape((3,3))
    print(board_game)
    x = int(input('Register x value: '))
    y = int(input('Register y value: '))
    board_game[x][y] = 'X'
    print(board_game)
    