from aocd import get_data, submit
import sys

data = get_data()
#print(data)

grid = []
for line in sys.stdin:
    grid.append(line)

output = 0
ms, ss = 0, 0
for i in range(len(grid)-2): 
    for j in range(len(grid[0])-2):

        #vert
        if grid[i][j] == 'M' and grid[i+2][j] == 'M' and grid[i][j+2] == 'S'  and grid[i+2][j+2] == 'S' and grid[i+1][j+1] == 'A':
            print(i, j)
            ms += 1
        if grid[i][j] == 'S' and grid[i+2][j] == 'S' and grid[i][j+2] == 'M'  and grid[i+2][j+2] == 'M' and grid[i+1][j+1] == 'A':
            print(i, j)
            ss += 1
        if grid[i][j] == 'M' and grid[i+2][j] == 'S' and grid[i][j+2] == 'M'  and grid[i+2][j+2] == 'S' and grid[i+1][j+1] == 'A':
            print(i, j)
            ms += 1
        if grid[i][j] == 'S' and grid[i+2][j] == 'M' and grid[i][j+2] == 'S'  and grid[i+2][j+2] == 'M' and grid[i+1][j+1] == 'A':
            print(i, j)
            ss += 1

output = ms + ss
print(ms, ss)      
print(output)
