from aocd import get_data, submit
import sys

data = get_data().split('\n')

rules = []
updates = []
for line in data: 
    if '|' in line: 
        rules.append(line.split('|'))
    elif ',' in line: 
        updates.append(line.split(','))

""" for line in sys.stdin:
    if '|' in line: 
        rules.append(line.strip().split('|'))
    elif ',' in line: 
        updates.append(line.strip().split(',')) """

output = 0
#print(rules, updates)

from collections import defaultdict
rulemap = defaultdict(set)
for before, after in rules: 
    rulemap[after].add(before)
correct = 0
for update in updates:
    #input()
    #cannot be ahead
    banned = set()

    flag = True
    #print(update)
    for i, num in enumerate(update): 
        if num in banned:
            #print('mistake:', update, num)
            flag = False
            break
        elif num not in rulemap.keys():
            #print('no rule for', num)
            continue
        elif num in rulemap:
            #print('adding', rulemap[num], 'to ban list')
            for item in rulemap[num]:
                banned.add(item)
            #print(banned)
        
    if flag: 
        output += int(update[len(update)//2])
        correct += 1
        #print('adding', update[len(update)//2])

print(output)

#submit(output)