from aocd import get_data, submit
import sys
from collections import defaultdict, deque
from functools import cmp_to_key

fulldata = get_data(day=7, year=2023).split("\n")

sampledata = []
with open("test.in", 'r') as file:
    for line in file:
        sampledata.append(line.strip())

dataselect = 1
data = sampledata if dataselect == 0 else fulldata

answer = 0

cardList = "AKQJT98765432"

datatuple = []

for i, line in enumerate(data): 
    print(i, line)

    cards, bid = line.split()
    bit = int(bid)

    datatuple.append((cards, bid))

roughlist = [[], [], [], [], [], [], []]

for cards, bid in datatuple:
    cardDict = defaultdict(int)

    for card in cards:
        cardDict[card] += 1

    freqs = sorted(cardDict.values())

    #five of kind
    if freqs[-1] == 5:
        roughlist[6].append((cards, bid))
    elif freqs[-1] == 4:
        roughlist[5].append((cards, bid))
    elif freqs[-1] == 3 and freqs[-2] == 2:
        roughlist[4].append((cards, bid))
    elif freqs[-1] == 3:
        roughlist[3].append((cards, bid))
    elif freqs[-1] == 2 and freqs[-2] == 2:
        roughlist[2].append((cards, bid))
    elif freqs[-1] == 2:
        roughlist[1].append((cards, bid))
    elif freqs[-1] == 1:
        roughlist[0].append((cards, bid))

print(roughlist)

def customSort(item1, item2):
    card1 = item1[0]
    card2 = item2[0]
    for char1, char2 in zip(card1, card2):
        #print(char1, char2)
        if cardList.find(char1) < cardList.find(char2):
            return 1
        elif cardList.find(char1) > cardList.find(char2):
            return -1
    return 0

#sort through roughlist
for i, lst in enumerate(roughlist): 

    #sorted list
    sortedList = sorted(lst, key=cmp_to_key(customSort))
    #print(lst, sortedList)
    roughlist[i] = sortedList

print(roughlist)
ranks = []
for lst in roughlist:
    ranks += lst
    

#ranking: #inside is bid

finalranks = []

for rank in ranks:
    finalranks.append(rank[1])

print("finalrarnks", finalranks)

for i, rank in enumerate(finalranks):
    answer += int(rank) * (i+1)


print(answer)
submit(answer)
