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

dataselect = 1
data = sampledata if dataselect == 0 else fulldata

answer = 0

all = []

for i, line in enumerate(data): 
    all = line.split(",")    

def hash(myString):
    ascii = 0
    for char in myString:
        ascii += ord(char)
        ascii *= 17
        ascii %= 256
    return ascii

boxdict = defaultdict(list) #labelhash
labeldict = defaultdict(set) #label, [labelhash]
#print(len(all))
for i, item in enumerate(all):
    #print(i)
    #check = or -
    if "-" in item:
        label, focallength = item.split("-")
        labelhash = hash(label)
        removeindicies = []
        #print("removing", label, boxdict)
        for item in labeldict[label]:
            #print(boxdict[labelhash])
            for i, thing in enumerate(boxdict[labelhash]):
                if boxdict[labelhash][i][0] == label:
                    removeindicies.append(i)
            #print("removeindicies", removeindicies, label, labeldict[label])
            for remove in removeindicies[::-1]:
                del boxdict[labelhash][remove]

        del labeldict[label]
        #print("removed", label, boxdict)
            
                
    elif "=" in item:
        label, focallength = item.split("=")
        labelhash = hash(label)

        flag = False
        for i, thing in enumerate(boxdict[labelhash]):
            if label==thing[0]:
                flag = True
                break
        if flag:
            boxdict[labelhash][i] = (label, focallength)
        else:
            boxdict[labelhash].append((label, focallength))
        
        labeldict[label].add(labelhash)

    #print(boxdict)

for key, value in boxdict.items():
    if len(value) == 0:
        continue
    
    for i, item in enumerate(value):
        answer += (1+key) * (1+i) * int(item[1])


print("answer", answer)
#submit(answer)
