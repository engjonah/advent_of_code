from aocd import get_data, submit
import sys

import itertools

data = get_data().split('\n')
from collections import defaultdict

output = 0
grid = []

for i, line in enumerate(data): 
#for line in sys.stdin: 
    print(line)
    grid.append([j for j in line.strip()])

antinodes = set()

#freq: locations
freqList = defaultdict(set)

for i, row in enumerate(grid): 
    for j, col in enumerate(row):
        if col != '.': 
            freqList[col].add((i, j))

print(freqList)

toCheck = []
for key, value in freqList.items(): 
    #put every pair in toCheck
    toCheck += list(itertools.combinations(value, 2))

print(toCheck)

def inBounds(i, j): 
    return 0 <= i < len(grid) and 0 <= j < len(grid[0])

for a, b in toCheck: 
    #print(a, b)
    r = abs(a[0] - b[0])
    c = abs(a[1] - b[1])
    if a[1] <= b[1] and a[0] <= b[0]:
        left = a[0], a[1]
        right = b[0], b[1]
        while inBounds(*left): 
            antinodes.add(left)
            left = left[0] - r, left[1] - c
        while inBounds(*right): 
            antinodes.add(right)
            right = right[0] + r, right[1] + c
    elif b[1] <= a[1] and a[0] <= b[0]:
        left = a[0], a[1]
        right = b[0], b[1]
        while inBounds(*left): 
            antinodes.add(left)
            left = left[0] - r, left[1] + c
        while inBounds(*right): 
            antinodes.add(right)
            right = right[0] + r, right[1] - c
    elif a[1] <= b[1] and b[0] <= a[0]:
        left = a[0], a[1]
        right = b[0], b[1]
        while inBounds(*left): 
            antinodes.add(left)
            left = left[0] + r, left[1] - c
        while inBounds(*right): 
            antinodes.add(right)
            right = right[0] - r, right[1] + c
    elif b[1] <= a[1] and b[0] <= a[0]:
        left = a[0], a[1]
        right = b[0], b[1]
        while inBounds(*left): 
            antinodes.add(left)
            left = left[0] + r, left[1] + c
        while inBounds(*right): 
            antinodes.add(right)
            right = right[0] - r, right[1] - c

    for i, antinode in enumerate(antinodes): 
        grid[antinode[0]][antinode[1]] = '#'

    """ for line in grid: 
        print(''.join(line))
    print() """
    
print(antinodes)
print(len(antinodes))

#submit(output)