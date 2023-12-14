from aocd import get_data, submit
import sys
from collections import defaultdict, deque
from functools import cmp_to_key
from itertools import combinations

fulldata = get_data(day=14, year=2023).split("\n")

sampledata = []
with open("test.in", 'r') as file:
    for line in file:
        sampledata.append(line.strip())

dataselect = 1
data = sampledata if dataselect == 0 else fulldata

answer = 0

grid = []

for i, line in enumerate(data): 
    print("i", i, line)
    linearr = []
    for item in line:
        linearr.append(item)
    grid.append(linearr)

#iterate by column then row

allsquares = []
for j in range(len(grid[0])):
    #count how many rounds between squares
    squares = [-1]
    counter = 0
    for i in range(len(grid)):
        if grid[i][j] == '#':
            squares.append(counter)
            counter = 0
            squares.append(i)
        elif grid[i][j] == '.':
            continue
        elif grid[i][j] == 'O':
            counter += 1

    squares.append(counter)

    allsquares.append(squares)

#squares: 
#even - square row #
#odd - number of circles
print(allsquares)
for allsquare in allsquares:
    for i in range(0, len(allsquare), 2):
        for j in range(allsquare[i]+1, allsquare[i]+1 + allsquare[i+1]):
            answer += len(grid) - j
            print(answer, len(grid) - j, j, allsquare)


print("answer", answer)
#submit(answer)
