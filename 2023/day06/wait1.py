from aocd import get_data, submit
import sys
from collections import defaultdict, deque

fulldata = get_data(day=6, year=2023).split("\n")

sampledata = []
with open("test.in", 'r') as file:
    for line in file:
        sampledata.append(line.strip())

dataselect = 0
data = sampledata if dataselect == 0 else fulldata

answer = 1
beats = []
times = []
dists = []
for i, line in enumerate(data): 
    print(i, line)

    if i == 0:
        times = [int(x) for x in line.split()[1:]]
    elif i ==1:
        dists = [int(x) for x in line.split()[1:]]

print("times", times)
print("dists", dists)


for time, dist in zip(times, dists):
    beatcounter = 0

    #i = time held
    for i in range(time + 1):
        
        if i * (time - i) > dist:
            beatcounter += 1

    beats.append(beatcounter)

for beat in beats:
    answer *= beat

print(answer)
#submit(answer)
