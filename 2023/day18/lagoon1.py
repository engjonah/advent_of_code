from aocd import get_data, submit
from collections import defaultdict, deque

fulldata = get_data(day=18, year=2023).split("\n")

sampledata = []
with open("test.in", 'r') as file:
    for line in file:
        sampledata.append(line.strip())

dataselect = 1
data = sampledata if dataselect == 0 else fulldata

answer = 0

newdata = []

for i, line in enumerate(data): 
    #print(i, line)

    dir, num, tag = line.split()
    tag = tag.strip("()")
    newdata.append((dir, int(num), tag))

row = 0
col = 0

edge = set()
edge.add((0, 0))

for line in newdata:
    dir, num, tag = line

    match dir:
        case "U":
            for i in range(1, num+1):
                edge.add((row-i, col))
            row -= num

        case "D":
            for i in range(1, num+1):
                edge.add((row+i, col))
            row += num
        
        case "L":
            for i in range(1, num+1):
                edge.add((row, col-i))
            col -= num

        case "R":
            for i in range(1, num+1):
                edge.add((row, col+i))
            col += num

#print(edge)

minrow = 10e6
mincol = 10e6
maxrow = -10e6
maxcol = -10e6
#reshift coords
for item in edge:
    row, col = item
    minrow = min(minrow, row)
    mincol = min(mincol, col)
    maxrow = max(maxrow, row)
    maxcol = max(maxcol, col)

#print(minrow, mincol, maxrow, maxcol)

height = maxrow - minrow + 1
width = maxcol - mincol + 1

grid = [['.' for _ in range(width)] for _ in range(height)]

for item in edge:
    row, col = item
    row, col = row - minrow, col - mincol
    grid[row][col] = "#"

""" for line in grid:
    print("".join(line)) """

#iterate through all edge points
#bfs/dfs to mark all 'outside' points
#remaining stuff is inside loop

todo = deque()

for i in range(height):
    todo.append((i, 0))
    todo.append((i, width-1))

for i in range(width):
    todo.append((0, i))
    todo.append((height-1, i))


moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
seen = set()

#print(grid)

while todo:
    curr = todo.pop()
    #print(curr)

    row, col = curr
    if (row, col) in seen or grid[row][col] == "#":
        continue
    seen.add((row, col))
    if grid[row][col] == '.':
        grid[row][col] = 'O'
    for move in moves:
        rowadd, coladd = move
        newrow = row + rowadd
        newcol = col + coladd

        if newrow in range(height) and newcol in range(width):
            if grid[newrow][newcol] == '.':
                todo.append((newrow, newcol))
    #print(todo)

""" for line in grid:
    print("".join(line))
 """
for i, row in enumerate(grid):
    counter = 0
    for j, col in enumerate(row):
        if col == "#" or col == '.':
            counter += 1

    answer += counter
    #print("line", i, counter)


print("answer", answer)
#submit(answer)
