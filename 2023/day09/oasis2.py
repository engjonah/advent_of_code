from aocd import get_data, submit
import sys
from collections import defaultdict, deque
from functools import cmp_to_key

fulldata = get_data(day=9, year=2023).split("\n")

sampledata = []
with open("test.in", 'r') as file:
    for line in file:
        sampledata.append(line.strip())

dataselect = 1
data = sampledata if dataselect == 0 else fulldata

answer = 0

for i, line in enumerate(data): 
    print(i, line)

    #down
    triangle = [[int(x) for x in line.split()]]
    while True: 

        newlist = []
        for j in range(len(triangle[len(triangle)-1])-1):
            newlist.append(triangle[len(triangle)-1][j+1]-triangle[len(triangle)-1][j])

        #print("newlist", newlist)
        triangle.append(newlist)
        
        flag = True
        for item in triangle[-1]:
            if item != 0:
                flag = False
        if flag:
            break

    print("triangle", triangle)
    
    #back up
    for j in range(len(triangle)-1, -1, -1):
        if j == len(triangle)-1:
            triangle[j].insert(0, 0)
        else:
            triangle[j].insert(0, triangle[j][0] - triangle[j+1][0])
    
    print("triangle", triangle)



    #sum ends
    answer += triangle[0][0]
    

    
print("answer", answer)
submit(answer)
