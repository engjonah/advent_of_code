from aocd import get_data, submit
import sys
from collections import defaultdict, deque
from functools import cmp_to_key
from itertools import combinations

fulldata = get_data(day=15, year=2023).split("\n")

sampledata = []
with open("test.in", 'r') as file:
    for line in file:
        sampledata.append(line.strip())

dataselect = 0
data = sampledata if dataselect == 0 else fulldata

answer = 0

all = []

for i, line in enumerate(data): 
    all = line.split(",")    

for thing in all:
    ascii = 0
    for char in thing:
        ascii += ord(char)
        ascii *= 17
        ascii %= 256

    answer += ascii

print("answer", answer)
#submit(answer)
