from aocd import get_data, submit
import sys
from collections import defaultdict, deque
from functools import cmp_to_key

fulldata = get_data(day=10, year=2023).split("\n")

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
    linelist = []
    for letter in line:
        linelist.append(letter)
    grid.append(linelist)

   
""" for line in grid:
    print(line) """

spos = (-1, -1)

for i, row in enumerate(grid):
    for j, col in enumerate(row):
        if col=='S':
            spos = (i, j)
            break
    if spos != (-1, -1):
        break

print(spos)

visited = set()
toVisit = deque()
toVisit.append(spos)
currPipe = "?"
visitHistory = []

started = False

while toVisit: 
    curr = toVisit.pop()
    row, col = curr
    currPipe = grid[row][col]
    #print(curr, currPipe)

    if started and currPipe == 'S':
        print("Found loop")
        break
    
    if curr[0] == spos[0] and curr[1] == spos[1]:
        started = True
        #figure out what s is:
        print("Searching for S")
        S = "?"

        lefts = "-LF"
        rights = "-J7"
        downs = "J|L"
        ups = "|7F"
        
        #left/right ----
        if col > 0 and col < len(grid[0])-1:
            if grid[row][col-1] in lefts and grid[row][col+1] in rights:
                S = "-"
                toVisit.append((row, col+1))
        #up/down
        if col > 0 and col < len(grid)-1:
            if grid[row-1][col] in ups and grid[row+1][col] in 'downs':
                S = "|"
                toVisit.append((row-1, col))
        #F
        if col < len(grid[0])-1 and row < len(grid)-1:
            if grid[row+1][col] in downs and grid[row][col+1] in rights:
                S = "F"
                toVisit.append((row+1, col))

        #J
        if col > 0 and row > 0:
            if grid[row][col-1] in lefts and grid[row-1][col] in ups:
                S = "J"
                toVisit.append((row, col-1))

        #L
        if col < len(grid[0])-1 and row > 0:
            if grid[row-1][col] in ups and grid[row][col+1] in rights:
                S = "L"
                toVisit.append((row-1, col))

        #7
        if col > 0 and row < len(grid)-1:
            if grid[row][col-1] in lefts and grid[row+1][col] in downs:
                S = "7"
                toVisit.append((row, col-1))

        print("S", S)
        currPipe = S
        """ n, m = toVisit.pop()
        toVisit.append((m, n)) """
        #toVisit.append(curr)
        if S == '?':
            print("ERROR - cannot find S type")

    else:
        visitHistory.append(currPipe)

        #print("row, col", row, col)
        if currPipe == "-":
            if (row, col-1) in visited and (row, col+1) not in visited:
                toVisit.append((row, col+1))
            elif (row, col-1) not in visited and (row, col+1) in visited:
                toVisit.append((row, col-1))
            else:
                print("loop?")
                break

        elif currPipe == "|":
            if (row-1, col) in visited and (row+1, col) not in visited:
                toVisit.append((row+1, col))
            elif (row-1, col) not in visited and (row+1, col) in visited:
                toVisit.append((row-1, col))
            else:
                print("loop?")
                break

        elif currPipe == "F":
            if (row, col+1) in visited and (row+1, col) not in visited:
                toVisit.append((row+1, col))
            elif (row, col+1) not in visited and (row+1, col) in visited:
                toVisit.append((row, col+1))
            else:
                print("loop?")
                break

        elif currPipe == "7":
            if (row+1, col) in visited and (row, col-1) not in visited:
                toVisit.append((row, col-1))
            elif (row+1, col) not in visited and (row, col-1) in visited:
                toVisit.append((row+1, col))
            else:
                print("loop?")
                break

        elif currPipe == "J":
            if (row-1, col) in visited and (row, col-1) not in visited:
                toVisit.append((row, col-1))
            elif (row-1, col) not in visited and (row, col-1) in visited:
                toVisit.append((row-1, col))
            else:
                print("loop?")
                break

        elif currPipe == "L":
                
            if (row, col+1) in visited and (row-1, col) not in visited:
                toVisit.append((row-1, col))
            elif (row, col+1) not in visited and (row-1, col) in visited:
                toVisit.append((row, col+1))
            else:
                print("loop?")
                break

    if curr == spos and curr in visited:
        print("Found loop")
        break

    visited.add(curr)

    """ print("visited", visited)
    print("to visit", toVisit)
    print("pipe history", visitHistory)
    print() """

#print("visited", visited)

answer = (len(visited)+1)//2

print("answer", answer)
#submit(answer)
