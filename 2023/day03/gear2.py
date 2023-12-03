from aocd import get_data, submit
import sys
from collections import defaultdict 

data = get_data(day=3, year=2023).split("\n")

answer = 0

symbols = "!@#$%^&*()+=-/"
numbers = "0123456789"

#linenum = 0

""" data = ["467..114..",
"...*......",
"..35..633.",
"......#...",
"617*......",
".....+.58.",
"..592.....",
"......755.",
"...$.*....",
".664.598.."] """
geardict = defaultdict(list)
for linenum, line in enumerate(data):
#for line in sys.stdin:
    #find each number
    #check top left right bottom for symbol

    inNumber = False
    partialNumber = ""
    for i, number in enumerate(line):
        if number in numbers:
            if not inNumber:
                inNumber = True
                partialNumber += number
                #print('starting num count')
            else:
                partialNumber += number

        
        #ends by . or end of line
        if number not in numbers or i == len(line)-1:
            if inNumber:
                #check top/left/right/bottom
                startIndex = i - len(partialNumber)
                endIndex = i
                symbolPresent = False
                #above
                for p in range(startIndex-1, endIndex+1):
                    try: 
                        if data[linenum-1][p] in symbols:
                            symbolPresent = True
                            if data[linenum-1][p] == "*":
                                print("gear found")
                                geardict[(linenum-1, p)].append(int(partialNumber))
                    except:
                        pass
                #below
                for p in range(startIndex-1, endIndex+1):
                    try: 
                        #print("checking", data[linenum+1][p], linenum, i)
                        if data[linenum+1][p] in symbols:
                            symbolPresent = True
                            if data[linenum+1][p] == "*":
                                print("gear found")
                                geardict[(linenum+1, p)].append(int(partialNumber))
                    except:
                        pass
                #left
                #print("checking left")
                try: 
                    #print("checking", line[startIndex-1], linenum)
                    if line[startIndex-1] in symbols:
                        symbolPresent = True
                        if line[startIndex-1] == "*":
                            print("gear found")
                            geardict[(linenum, startIndex-1)].append(int(partialNumber))
                except:
                    pass
                #right
                #print("checking right")
                #print("endIndex+1", endIndex+1, line[endIndex+1])
                try: 
                    if line[endIndex] in symbols:
                        symbolPresent = True
                        if line[endIndex] == "*":
                            print("gear found")
                            geardict[(linenum, endIndex)].append(int(partialNumber))
                except:
                    pass
                if symbolPresent:
                    try:
                        answer += int(partialNumber)
                        #print("adding", answer, partialNumber)
                    except:
                        pass
                partialNumber = ""
                inNumber = False
    print(line)
    #linenum += 1
print(answer)
print(geardict)
answer = 0
for key, items in geardict.items():

    if len(items)==2:
        answer += items[0] * items[1]
print(answer)
submit(answer, part="b", day=3, year=2023)