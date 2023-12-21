from aocd import get_data, submit
from collections import defaultdict, deque

fulldata = get_data(day=21, year=2023).split("\n")

sampledata = []
with open("test.in", 'r') as file:
    for line in file:
        sampledata.append(line.strip())

dataselect = 1
data = sampledata if dataselect == 0 else fulldata

answer = 0

grid = []

for i, line in enumerate(data):
    #print(i, line)

    grid.append([x for x in line])

""" for line in grid:
    print("".join(line)) """

start = (-1,-1)

for i, row in enumerate(grid):
    for j, col in enumerate(row):
        if col == 'S':
            start = (i, j)
            break
    if start != (-1, -1):
        break

currThings = set()
directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

height = len(grid)
width = len(grid[0])

currThings.add(start)
grid[start[0]][start[1]] = '.'

for i in range(64):
    nextThings = set()
    for item in currThings:
        row, col = item

        #skip rocks
        if grid[row][col] == '#':
            continue
        for direction in directions:
            rowadd, coladd = direction
            newrow, newcol = row+rowadd, col+coladd
            if newrow in range(height) and newcol in range(width) and grid[newrow][newcol] != '#':
                nextThings.add((newrow, newcol))

    currThings = nextThings

newgrid = []
for i, row in enumerate(grid):
    newrow = []
    for j, col in enumerate(row):
        if (i, j) in currThings:
            newrow.append('O')
        else:
            newrow.append(grid[i][j])
    newgrid.append(newrow)

for line in newgrid:
    print("".join(line))
print()


#print(currThings)

newgrid = []
for i, row in enumerate(grid):
    newrow = []
    for j, col in enumerate(row):
        if (i, j) in currThings:
            newrow.append('O')
        else:
            newrow.append(grid[i][j])
    newgrid.append(newrow)

for line in newgrid:
    print("".join(line))

answer = len(currThings)

print("answer", answer)
submit(answer)
