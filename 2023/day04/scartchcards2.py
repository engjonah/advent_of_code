from aocd import get_data, submit
import sys
from collections import defaultdict 

fulldata = get_data(day=4, year=2023).split("\n")

sampledata = []
with open("test.in", 'r') as file:
    for line in file:
        sampledata.append(line)

dataselect = 1

if dataselect == 0:
    data = sampledata
elif dataselect == 1:
    data = fulldata

#print(data)

finalanswer = 0
cards = defaultdict(int)

for i, line in enumerate(data): 
    #finalanswer += 1 #at least 1 card per
    cards[i] += 1
    print(line)

    card, numbers = line.split(":")
    winners, answers = numbers.strip().split("|")

    winners = winners.strip().split()
    answers = answers.strip().split()

    counter = 0
    for answer in answers: 
        if answer in winners:
            counter += 1
            winners.remove(answer)
    for j in range(counter):
        cards[i+j+1] += cards[i]
        print(cards[j+1], cards[i])
    print(cards)

print(cards)
finalanswer = 0
for value in cards.values():
    finalanswer += value

print(finalanswer)
submit(finalanswer)
