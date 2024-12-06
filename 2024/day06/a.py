from aocd import get_data, submit
import sys

data = get_data().split('\n')

grid = []
output = 0
for line in data: 
    grid.append([i for i in line])

""" for line in sys.stdin:
    grid.append([i for i in line.strip()])
 """
start = -1, -1
print(grid)

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

   
print(seen)
print(len(seen))

#submit(output)