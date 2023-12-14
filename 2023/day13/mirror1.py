from aocd import get_data, submit
import sys
from collections import defaultdict, deque
from functools import cmp_to_key
from itertools import combinations

fulldata = get_data(day=13, year=2023).split("\n")

sampledata = []
with open("test.in", 'r') as file:
    for line in file:
        sampledata.append(line.strip())

dataselect = 1
data = sampledata if dataselect == 0 else fulldata

answer = 0

grids = []

grid = []
for i, line in enumerate(data): 
    #print("i", i, line)
    
    if line == "":
        grids.append(grid)
        grid = []
    else:
        grid.append(line)

grids.append(grid)


for grid in grids:
    for line in grid:
        print(line)
    print()


for grid in grids:
    potentialmirrors = []
    for i in range(len(grid)-1):
        if grid[i] == grid[i+1]:
            potentialmirrors.append(i)

    print(potentialmirrors)

    for potentialmirror in potentialmirrors:
        counter = 1
        flag = False
        while potentialmirror+counter+1 < len(grid) and potentialmirror-counter >= 0:
            print(grid[potentialmirror+counter+1], grid[potentialmirror-counter])
            if grid[potentialmirror+counter+1] != grid[potentialmirror-counter]:
                flag = True
                break
            counter += 1
        if flag:
            continue
        else:
            print("mirror found", potentialmirror)
            answer += 100 * (potentialmirror+1)
    
    #find vertical mirror
    potentialmirrors = []
    newgrid = []
    for j in range(len(grid[0])):
        newline = []
        for i in range(len(grid)):
            newline.append(grid[i][j])

        newgrid.append(newline)

    grid = newgrid
    for i in range(len(grid)-1):
        if grid[i] == grid[i+1]:
            potentialmirrors.append(i)

    print(potentialmirrors)

    for potentialmirror in potentialmirrors:
        counter = 1
        flag = False
        while potentialmirror+counter+1 < len(grid) and potentialmirror-counter >= 0:
            if grid[potentialmirror+counter+1] != grid[potentialmirror-counter]:
                flag = True
                break
            counter += 1
        if flag:
            continue
        else:
            print("mirror found", potentialmirror)
            answer += (potentialmirror+1)
    
print("answer", answer)
#submit(answer)
