from aocd import get_data, submit
import sys
from collections import defaultdict, deque
from functools import cmp_to_key

fulldata = get_data(day=11, year=2023).split("\n")

sampledata = []
with open("test.in", 'r') as file:
    for line in file:
        sampledata.append(line.strip())

dataselect = 1
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


""" for line in grid:
    print("".join(line)) """

galaxies = []

for i, row in enumerate(grid):
    for j, col in enumerate(row):
        if col == '#':
            galaxies.append((i, j))

#print(galaxies)

galaxyPairs = []

for i, galaxy1 in enumerate(galaxies):
    for galaxy2 in galaxies[i+1:]:
        galaxyPairs.append((galaxy1, galaxy2))

#print(galaxyPairs, len(galaxyPairs))

for galaxyPair in galaxyPairs:

    galaxy1, galaxy2 = galaxyPair
    #print(galaxy1, galaxy2)

    #check cols
    #find which ones get crossed?
    if galaxy2[1] > galaxy1[1]:
        col1 = galaxy1[1]
        col2 = galaxy2[1]
    else:
        col1 = galaxy2[1]
        col2 = galaxy1[1]


    if galaxy2[0] > galaxy1[0]:
        row1 = galaxy1[0]
        row2 = galaxy2[0]
    else:
        row1 = galaxy2[0]
        row2 = galaxy1[0]

    #print(row1, row2, col1, col2)
    for emptyCol in emptyCols:
        if  emptyCol > col1:
            break
    
    counter = 0
    for j in range(emptyCols.index(emptyCol), len(emptyCols)):
        if  emptyCols[j] > col2:
            break
        counter += 1

    if col1 > emptyCols[-1] or col2 < emptyCols[0]:
        counter = 0
        
    answer += col2-col1 + (counter * (1000000-1))
    

    #print("col dist", col2-col1 + counter * (10-1), counter)

    for emptyRow in emptyRows:
        if emptyRow > row1:
            break

    counter = 0
    for j in range(emptyRows.index(emptyRow), len(emptyRows)):
        if emptyRows[j] > row2:
            break
        counter += 1
    
    if row1 > emptyRows[-1] or row2 < emptyRows[0]:
        counter = 0

    #print("row dist", row2-row1 + (counter * (10-1)), counter)
        
    answer += row2-row1 + (counter * (1000000-1))


print("answer", answer)
#submit(answer)
