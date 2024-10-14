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
    
    
    
# Creating list of lists but the reference is the same for the inner listskc
def building_list_of_lists_weird():
    '''
    This method allows us to
    create nested list, however
    the inner list has the same
    reference, so its changes
    are going to be reflected
    in all of them
    '''
    weird_board = [['_'] * 3] * 3 # The inner lists have the same reference
    # The only change was the listcomp and the replication using * operator
    print(weird_board)
    weird_board[1][2] = 'O'
    print(weird_board)
    
# Reminder to not include mutable objects inside immutable objects e.g lists into tuples 
def mutable_objects_inside_immutable_objects():
    '''
    This exercise represents how an error could
    raise if we use mutable objects inside an immutable
    object
    '''
    t = (1,2,[4,5,6,7])
    t[2] += [8,9]
    print(t)

# Use multidimensional slice
def multimensional_slicing():
    arr = np.array([[np.random.normal(0.1,1,3)]*2]*3)
    print(arr)
    sub_array = arr[0, :, :2]
    
    
multimensional_slicing()
print(np.random.normal(0.1,1,5))