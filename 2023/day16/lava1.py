from aocd import get_data, submit
import sys
from collections import defaultdict, deque
from functools import cmp_to_key
from itertools import combinations

fulldata = get_data(day=16, year=2023).split("\n")

sampledata = []
with open("test.in", 'r') as file:
    for line in file:
        sampledata.append(line.strip())

dataselect = 0
data = sampledata if dataselect == 0 else fulldata

answer = 0

grid = []

for i, line in enumerate(data): 
    #print(i, line)

    newline = []
    for j in line:
        newline.append(j)
    grid.append(newline)

todo = set()
checked = set()
#row, col, direction
#NESW
"""   0
3   1
  2 """
todo.add((0,0,1))

#energy = [["." for x in range(len(grid[0]))] for x in range(len(grid))]
energy = []

for i in range(len(grid)):
    newline = []
    for j in range(len(grid[0])):
        newline.append(".")
    energy.append(newline)

#
while todo:
    flag = True
    curr = todo.pop()
    if curr in checked:
        continue
    else:
        checked.add(curr)
    row, col, direction = curr
    print("working on ", curr)
    while flag:
        if not (row >=0 and row < len(grid)):
            break
        if not (col >= 0 and col < len(grid[0])):
            break
            
        print('adjusting energy for', row, col, direction)
        energy[row][col] = '#'
        print("curr", row, col, grid[row][col], direction)
        match grid[row][col]:
            case ".":
                pass
            case "/":
                match direction:
                    case 0:
                        direction = 1
                    case 1:
                        direction = 0
                    case 2:
                        direction = 3
                    case 3:
                        direction = 2
            case "\\":
                match direction:
                    case 0:
                        direction = 3
                    case 1:
                        direction = 2
                    case 2:
                        direction = 1
                    case 3:
                        direction = 0
        
            case "|":
                #pass through
                if direction in [0, 2]:
                    pass
                #split
                else:
                    print("vert split")
                    todo.add((row, col, 0))
                    todo.add((row, col, 2))
                    break

            case "-":
                #pass through
                if direction in [1, 3]:
                    pass
                else:
                    print("horz split")
                    todo.add((row, col, 1))
                    todo.add((row, col, 3))
                    break
        print("new direction", direction)
        match direction:
            case 0:
                if row - 1 >=0:
                    row = row - 1
                else:
                    flag = False
            case 1:
                if col + 1 < len(grid[0]):
                    col = col + 1
                else:
                    flag = False
            case 2:
                print(row + 1 < len(grid), row + 1, len(grid))
                if row + 1 < len(grid):
                    row = row + 1
                else:
                    flag = False
            case 3:
                if col - 1 >= 0:
                    col = col - 1
                else:
                    flag = False

        print("flag", flag, row, col)
        if not flag:
            continue

        print("moved to ", row, col, grid[row][col], direction)
        
    print(todo)
    for line in energy:
        print("".join(line))
    
                
""" for line in energy:
    print("".join(line)) """

for row in energy:
    for col in row:
        if col == '#':
            answer += 1

print("answer", answer)
#submit(answer)
