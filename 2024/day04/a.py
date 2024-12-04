from aocd import get_data, submit
import sys

data = get_data()

grid = []
for line in sys.stdin:
    grid.append(line)

horz = 0
vert = 0
diag = 0
for line in grid:
    for i in range(len(line)-3):
        if line[i:i+4] == 'XMAS':
            print(i)
            horz += 1
        if line[i:i+4] == 'SAMX':
            print(i)
            horz += 1

for i in range(len(grid)-3): 
    for j in range(len(grid[0])):
        #vert
        if grid[i][j] == 'X' and grid[i+1][j] == 'M' and grid[i+2][j] == 'A'  and grid[i+3][j] == 'S':
            print(i, j)
            vert += 1
        if grid[i][j] == 'S' and grid[i+1][j] == 'A' and grid[i+2][j] == 'M'  and grid[i+3][j] == 'X':
            print(i, j)
            vert += 1
        if j < len(grid[0]) - 4: 
            if grid[i][j] == 'X' and grid[i+1][j+1] == 'M' and grid[i+2][j+2] == 'A'  and grid[i+3][j+3] == 'S':
                print(i, j)
                diag += 1
            if grid[i][j] == 'S' and grid[i+1][j+1] == 'A' and grid[i+2][j+2] == 'M'  and grid[i+3][j+3] == 'X':
                print(i, j)
                diag += 1
        if j > 2: 
            if grid[i][j] == 'X' and grid[i+1][j-1] == 'M' and grid[i+2][j-2] == 'A'  and grid[i+3][j-3] == 'S':
                print(i, j)
                diag += 1
            if grid[i][j] == 'S' and grid[i+1][j-1] == 'A' and grid[i+2][j-2] == 'M'  and grid[i+3][j-3] == 'X':
                print(i, j)
                diag += 1
print(horz, vert, diag)
output = horz + vert + diag
print(output)
