from aocd import get_data, submit
import sys

data = get_data().split('\n')
from collections import defaultdict

output = 0

grid = []
for i, line in enumerate(data): 
#for line in sys.stdin: 
    grid.append([i for i in line.strip()])

""" for line in grid: 
    print(''.join(line)) """

#find islands then find border? 

islands = []

seen = set()

dirs = [(0, 1), (-1, 0), (0, -1), (1, 0)]

def inBound(i, j): 
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

for i, row in enumerate(grid): 
    for j, col in enumerate(row): 
        if (i, j) in seen: 
            continue

        toDo = set()
        
        toDo.add((i, j))

        islandLetter = col

        currIsland = set()

        while toDo:
            currR, currC = toDo.pop()
            seen.add((currR, currC))
            currIsland.add((currR, currC))

            for dir in dirs: 
                dirR, dirC = dir
                if (currR + dirR, currC + dirC) not in seen and inBound(currR + dirR, currC + dirC) and grid[currR + dirR][currC + dirC] == islandLetter: 
                    toDo.add((currR + dirR, currC + dirC))
        
        islands.append(currIsland)

borders = 0
for island in islands: 
    
    islandBorder = 0
    for part in island: 
        currR, currC = part
        count = 4
        for dirR, dirC in dirs: 
            if (currR + dirR, currC + dirC) in island: 
                count -= 1

        islandBorder += count
    borders += islandBorder * len(island)


print(borders)


#submit(output)