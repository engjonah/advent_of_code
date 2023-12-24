from aocd import get_data, submit
from collections import defaultdict, deque
import sys

sys.setrecursionlimit(10000)
fulldata = get_data(day=23, year=2023).split("\n")

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

for line in grid:
    print("".join(line))

maxsteps = 0
longestPath = set()

directions = [(0, 1, 1), (0, -1, 3), (-1, 0, 0), (1, 0, 2)]
height, width = len(grid), len(grid[0])

def dfs(row, col, visited, steps):
    global maxsteps
    global longestPath

    visited = set(visited)
    
    if (row, col) in visited:
        #print("visited", row, col)
        return
    
    downhill = False
    slope = -1
    match grid[row][col]:
        case '.':
            pass
        case '#':
            return
        case '^':
            slope = 0
            downhill = True
        case '>':
            slope = 1
            downhill = True
        case 'v':
            slope = 2
            downhill = True
        case '<':
            slope = 3
            downhill = True

    visited.add((row, col))
    """ print(row, col, visited)

    for i, row1 in enumerate(grid):
        printline = ""
        for j, col2 in enumerate(row1):
            if (i, j) in longestPath:
                printline += "O"
            else:
                printline += col2
        print(printline) """
    
    #input()

    if steps > maxsteps:
        maxsteps = steps
        longestPath = visited

    for direction in directions:
        rowadd, coladd, hill = direction
        if downhill and hill != slope:
            continue
        if row+rowadd in range(height) and col+coladd in range(width) and grid[row+rowadd][col+coladd] != '#':
            #print("next check", row+rowadd, col+coladd)
            dfs(row+rowadd, col+coladd, tuple(visited), steps+1)

dfs(0, 1, (), 0)

print(len(longestPath))
counter = 0
for i, row in enumerate(grid):
    line = ""
    for j, col in enumerate(row):
        if (i, j) in longestPath:
            line += "O"
        else:
            line += col
        if col != '#':
            counter += 1
    print(line)

answer = maxsteps

print("answer", answer)
#submit(answer)
