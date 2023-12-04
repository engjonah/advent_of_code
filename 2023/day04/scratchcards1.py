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

for line in data: 
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
    print(counter,  2**(max(0, counter-1)))
    #finalanswer += 2**(max(0, counter-1))
    if counter > 0:
        finalanswer += 2**( counter-1)


    print(card, winners, answers)

print(finalanswer)
submit(finalanswer)
