import random
# def show(array):
#     for i in range(len(array[0])):
#         print array[i]
#     print '------'

# array = [[0,0,0,0,0,0],
#      [0,0,0,1,0,0],
#      [0,1,0,1,0,0],
#      [0,0,1,1,0,0],
#      [0,0,0,0,0,0],
#      [0,0,0,0,0,0]]

# show(array)

def compute_neighbors(array):
    "returns the number of neighbors for each cell and saves it in an array"
    # shape of array
    shape = len(array), len(array[0])
    #makes new array in the same shape
    N  = [[0,]*(shape[0])  for i in range(shape[1])]
    # Leaving a border of 0's...
    for x in range(1,shape[0]-1):
        for y in range(1,shape[1]-1):
            N[x][y] = array[x-1][y-1]+array[x][y-1]+array[x+1][y-1] \
                    + array[x-1][y]            +array[x+1][y]   \
                    + array[x-1][y+1]+array[x][y+1]+array[x+1][y+1]
    return N 

def slow_iterate(array, frame):
    neighbors = compute_neighbors(array)
    # Leaving a border of 0's..
    shape = len(array), len(array[0])
    for x in range(1,shape[0]-1):
        for y in range(1,shape[1]-1):
            rand = random.randint(1, (102 - frame))
            if rand == 1:
                if array[x][y] == 1 and (neighbors[x][y] < 2 or neighbors[x][y] > 3):
                    array[x][y] = 0
                elif array[x][y] == 0 and neighbors[x][y] == 3:
                    array[x][y] = 1
            else:
                array[x][y] = array[x][y]
    
    return array

# for i in range(4):
#     slow_iterate(array) 
#     show(array)
