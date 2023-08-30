import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

#Creating a 100x100 grid and a random 10x10 for the big grid
grid = np.zeros((100, 100))
starter = np.random.choice([0, 1], size=(90, 90))
grid[:90, :90] = starter

    
def cellHealth(value_arr):
    neighbor_result = []
    for i in value_arr:
        output = []
        for j in i:
            if j==1:
                output.append(1)
            else:
                output.append(0)
        neighbor_result.append(output)
    return neighbor_result
    
def neighbour_checker(test_grid, i, j, w, h):
    i_down = i+1
    j_right = j+1

    if i == w-1:
        i_down = 0
    if j == h-1:
        j_right = 0
    
    #the current index is  [i][j]
    #Checking left-u neighbor
    lu = test_grid[i-1][j-1]
    #Checking left-c neighbour
    lc =test_grid[i][j-1]
    #Checking left_d neighbour
    ld = test_grid[i_down][j-1]

    #Checking up neighbour
    u = test_grid[i-1][j]
    #Checking down neighbour
    d = test_grid[i_down][j]

    #Checking right-u neighbour
    ru = test_grid[i-1][j_right]
    #Checking right-c neighbour
    rc = test_grid[i][j_right]
    #Checking right-d neighbour
    rd = test_grid[i_down][j_right]
    return cellHealth([[lu, lc , ld], [u, d], [ru, rc, rd]])
    
def neighbour_sum(lists):
    neighbors = 0
    for i in lists:
        neighbors += sum(i)
    return neighbors

def neighbour_calc(grid, i, j, w, h):
    return neighbour_sum(neighbour_checker(grid, i, j, w, h))
    
def cellAliveOrDead(grid, i, j, A, B, C, w, h):
    cellValue = grid[i][j]
    cellState = False
    if cellValue == 1:
        cellState = True
    else:
        cellState = False
    neighbours = neighbour_calc(grid, i, j, w, h)
    
    #For live cells
    if neighbours < A and cellState == True:
        return 0
    if (neighbours == A or neighbours == B) and cellState == True:
        return 1
    if neighbours > B and cellState == True:
        return 0
    
    #For dead cells
    if neighbours == B and cellState == False:
        return 1
    #Condition for dead cells to remain dead
    return 0

def gameOfLife(grid):
    new_grid = []
    for i in range(0, 100):
        new_grid_temp = []
        for j in range(0, 100):
            new_grid_temp.append(cellAliveOrDead(grid, i, j, 2, 3, 3, 100, 100))
        new_grid.append(new_grid_temp)
    return new_grid
  
# print(grid)
# print(" ")
# print(" ")
# print(gameOfLife(grid) == grid)
def update_grid():
    global grid
    grid = gameOfLife(grid)
    
def update(frame):
    update_grid()
    ax.clear()
    ax.imshow(grid, cmap='binary')

fig, ax = plt.subplots()
ani = animation.FuncAnimation(fig, update, frames=100, interval=100)
plt.show()

# print(grid)
