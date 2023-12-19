from aocd import get_data, submit
from collections import defaultdict, deque

fulldata = get_data(day=19, year=2023).split("\n")

sampledata = []
with open("test.in", 'r') as file:
    for line in file:
        sampledata.append(line.strip())

dataselect = 1
data = sampledata if dataselect == 0 else fulldata

answer = 0

newdata = []
otherdata = []
flag = False

for i, line in enumerate(data): 
    #print(i, line)

    if line == "":
        flag = True
        continue

    if not flag:
        newdata.append(line)
    else:
        otherdata.append(line)


ruledict = defaultdict(list)

for line in newdata:
    label, rules = line.split("{")
    rules = rules.strip("}").split(",")
    newrules = []
    for rule in rules:
        if ":" in rule:
            condition, next = rule.split(":")
        else:
            condition, next = "TRUE", rule
        
        if condition != "TRUE":
            if "<" in condition:
                var, value = condition.split("<")
                comparator = "<"
                newrules.append((var, comparator, value, next))
            else:
                var, value = condition.split(">")
                comparator = ">"
                newrules.append((var, comparator, value, next))
        else:
            newrules.append((var, "=", value, next))
    ruledict[label] = newrules

#print(ruledict)

for line in otherdata:
    vardict = dict()
    values = line.strip("{}").split(",")
    for value in values:
        var, num = value.split("=")
        vardict[var] = int(num)
    
    currlabel = "in"
    while currlabel not in ["A", "R"]:
        for rule in ruledict[currlabel]:
            var, comparator, value, next = rule
            if comparator == '=':
                currlabel = next
                break
            elif comparator == '>':
                if vardict[var] > int(value):
                    currlabel = next
                    break
            elif comparator == '<':
                if vardict[var] < int(value):
                    currlabel = next
                    break
            else:
                print("ERROR")
    if currlabel == "A":
        #print("acecpted")
        answer += sum(vardict.values())
    




    


print("answer", answer)
#submit(answer)
