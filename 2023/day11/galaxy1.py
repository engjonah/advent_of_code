from aocd import get_data, submit
import sys
from collections import defaultdict, deque
from functools import cmp_to_key

fulldata = get_data(day=11, year=2023).split("\n")

sampledata = []
with open("test.in", 'r') as file:
    for line in file:
        sampledata.append(line.strip())

dataselect = 0
data = sampledata if dataselect == 0 else fulldata

answer = 0

grid = []
for i, line in enumerate(data): 
    #print("i", i, line)
    
    row = []
    for char in line:
        row.append(char)

    grid.append(row)

emptyRows = []

print(grid)

for line in grid:
    print("".join(line))

for i, row in enumerate(grid):
    if row == ["."] * len(row):
        emptyRows.append(i)

print("emptyRows", emptyRows)

emptyCols = []
for j in range(len(grid[0])):
    empty = True
    for i in range(len(grid)):
        if grid[i][j]!='.':
            empty = False
    if empty:
        emptyCols.append(j)
    

print("emptyCols", emptyCols)

emptyRows.reverse()
emptyCols.reverse()

print(emptyRows)

for row in emptyRows:
    for _ in range(9):
        grid.insert(row, ["."] * len(grid[0]))

for col in emptyCols:
    for i, row in enumerate(grid):
        for _ in range(9):
            grid[i].insert(col, '.')

for line in grid:
    print("".join(line))

galaxies = []

for i, row in enumerate(grid):
    for j, col in enumerate(row):
        if col == '#':
            galaxies.append((i, j))

print(galaxies)

galaxyPairs = []

for i, galaxy1 in enumerate(galaxies):
    for galaxy2 in galaxies[i+1:]:
        galaxyPairs.append((galaxy1, galaxy2))

print(galaxyPairs, len(galaxyPairs))

for galaxyPair in galaxyPairs:
    galaxy1, galaxy2 = galaxyPair
    answer += abs(galaxy2[0]-galaxy1[0]) + abs(galaxy2[1]-galaxy1[1])

print("answer", answer)
#submit(answer)
