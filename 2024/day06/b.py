from aocd import get_data, submit
import sys

data = get_data().split('\n')

grid = []
output = 0
for line in data: 
    grid.append([i for i in line])

""" for line in sys.stdin:
    grid.append([i for i in line.strip()]) """

start = -1, -1

possibleBarriers = set()

for i, row in enumerate(grid): 
    for j, col in enumerate(row): 
        if col == '^': 
            print('found start')
            start = (i, j)
            
def inBounds(row, col): 
    return 0 <= row < len(grid) and 0 <= col < len(grid[0])

curri, currj = start
seen = set()
#NESW : 0123
direction = 0
directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

seen.add((curri, currj))
while True:
    if not inBounds(curri, currj): 
        break
    
    curri, currj = curri + directions[direction][0], currj + directions[direction][1]

    if not inBounds(curri, currj): 
        break
    #if next hit # 
    if grid[curri][currj] == '#': 
        curri, currj = curri - directions[direction][0], currj - directions[direction][1]
        direction = (direction + 1) % 4

    seen.add((curri, currj))
    print(curri, currj)

from collections import defaultdict


goodBarriers = []

print(seen)
print(len(seen))

newgrid = [line[:] for line in grid]
posb = list(seen)
for i, possibleBarrier in enumerate(posb):
    print(i)
    newseen = defaultdict(set)
    #print('testing', possibleBarrier)
    pbi, pbj = possibleBarrier
    if i != 0: 
        newgrid[posb[i-1][0]][posb[i-1][1]] = '.'
    
    newgrid[pbi][pbj] = '#'
    #print(newgrid)

    flag = False

    curri, currj = start
    direction = 0

    while True:
        if not inBounds(curri, currj): 
            flag = True
            break
        
        curri, currj = curri + directions[direction][0], currj + directions[direction][1]

        #stuck in loop 
        if direction in newseen[(curri, currj)]:
            #print(newseen)
            break

        if not inBounds(curri, currj):
            flag = True 
            break
        #if next hit # 
        if newgrid[curri][currj] == '#': 
            curri, currj = curri - directions[direction][0], currj - directions[direction][1]
            direction = (direction + 1) % 4

        seen.add((curri, currj))

        newseen[(curri, currj)].add(direction)
        #print(curri, currj)
    
    if not flag: 
        goodBarriers.append(possibleBarrier)

print(goodBarriers)
print(len(goodBarriers))

#submit(output)