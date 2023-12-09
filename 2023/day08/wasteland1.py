from aocd import get_data, submit
import sys
from collections import defaultdict, deque
from functools import cmp_to_key

fulldata = get_data(day=8, year=2023).split("\n")

sampledata = []
with open("test.in", 'r') as file:
    for line in file:
        sampledata.append(line.strip())

dataselect = 1
data = sampledata if dataselect == 0 else fulldata

answer = 0

instructions = []
pathDict = defaultdict(list)

for i, line in enumerate(data): 
    #print(i, line)
    if i == 0:
        instructions = list(line)
    elif i == 1:
        continue
    else:
        #print(line)
        before, after = line.split("=")
        before = before.strip()
        after1, after2 = after.strip().split(",")
        after1 = after1[1:].strip()
        after2 = after2[:-1].strip()

        print(before, after1, after2)
        pathDict[before] = [after1, after2]

print(pathDict)
print(instructions)
curr = "AAA"
counter = 0
flag = False
while True:
    for i in instructions:
        if i == "R":
            curr = pathDict[curr][1]
        elif i == "L":
            curr = pathDict[curr][0]
        
        counter += 1
        if curr == "ZZZ":
            flag = True
            break    
    if flag:
        break

answer = counter
    
print(answer)
#submit(answer)
