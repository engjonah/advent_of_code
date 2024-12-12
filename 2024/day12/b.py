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

output = 0
for island in islands: 
    print(island)
    islandBorder = 0
    borderList = set()
    for part in island: 
        currR, currC = part
        count = 0
        for dirR, dirC in dirs: 
            if (currR + dirR, currC + dirC) not in island: 
                count += 1
                if dirR == -1: 
                    addR = -.4
                elif dirR == 1: 
                    addR = .4
                else:
                    addR = 0
                
                if dirC == -1: 
                    addC = -.4
                elif dirC == 1: 
                    addC = .4
                else:
                    addC = 0
                borderList.add((currR + addR, currC + addC))


        islandBorder += count

    borders += islandBorder * len(island)
    print('borderList', borderList)

    sides = 0
    seenBorder = set()
    for border in borderList: 
        #print('border', border)
        if border in seenBorder:
            #print('seen', border)
            continue
        
        toDo = []
        toDo.append(border)

        while toDo: 
            curr = toDo.pop()
            seenBorder.add(curr)
            borderR, borderC = curr
            #top
            if int(borderR + 0.4) == borderR: 
                #print('top')
                #left
                #left
                if (borderR-1, borderC) not in seenBorder and (borderR-1, borderC) in borderList: 
                    toDo.append((borderR-1, borderC))
                #right
                if (borderR+1, borderC) not in seenBorder and (borderR+1, borderC) in borderList: 
                    toDo.append((borderR+1, borderC))

            #bot
            elif int(borderR - 0.4) == borderR:   
                #print('bot')
                #left
                #left
                if (borderR-1, borderC) not in seenBorder and (borderR-1, borderC) in borderList: 
                    toDo.append((borderR-1, borderC))
                #right
                if (borderR+1, borderC) not in seenBorder and (borderR+1, borderC) in borderList: 
                    toDo.append((borderR+1, borderC))
            #left
            elif int(borderC + 0.4) == borderC: 
                if (borderR, borderC-1) not in seenBorder and (borderR, borderC-1) in borderList: 
                    toDo.append((borderR, borderC-1))
                #right
                if (borderR, borderC+1) not in seenBorder and (borderR, borderC+1) in borderList: 
                    toDo.append((borderR, borderC+1))
                #print('left')
                
            
            #right
            elif int(borderC - 0.4) == borderC: 
                #print('right')
                #left
                if (borderR, borderC-1) not in seenBorder and (borderR, borderC-1) in borderList: 
                    toDo.append((borderR, borderC-1))
                #right
                if (borderR, borderC+1) not in seenBorder and (borderR, borderC+1) in borderList: 
                    toDo.append((borderR, borderC+1))
            else: 
                print("ERROR")
        #print('seen', seenBorder)
        sides += 1
        #print('sides', sides)

    print('sides', sides)
    output += sides * len(island)
    

print(output)

#submit(output)