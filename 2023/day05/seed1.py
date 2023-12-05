from aocd import get_data, submit
import sys
from collections import defaultdict, deque

fulldata = get_data(day=5, year=2023).split("\n")

sampledata = []
with open("test.in", 'r') as file:
    for line in file:
        sampledata.append(line.strip())

dataselect = 1
data = sampledata if dataselect == 0 else fulldata

seeds = []

seedSoil = []
soilFertilizer = []
fertilizerWater = []
waterLight = []
lightTemp = []
tempHumid = []
humidLocation = []

state = 0
fullseeds = set()
for i, line in enumerate(data): 

    if i == 0:
        seeds = line.split(":")[1].strip().split()
        seeds = [int(seed) for seed in seeds]
    
    if line == "":
        state += 1
        continue

    if line[-1] == ":":
        continue
    
    #add to maps
    if state == 1:
        dest, source, ranges = map(int, line.split())
        seedSoil.append([dest, source, ranges])

    elif state == 2:
        dest, source, ranges = map(int, line.split())
        soilFertilizer.append([dest, source, ranges])

    elif state == 3:
        dest, source, ranges = map(int, line.split())
        fertilizerWater.append([dest, source, ranges])

    elif state == 4:
        dest, source, ranges = map(int, line.split())
        waterLight.append([dest, source, ranges])

    elif state == 5:
        dest, source, ranges = map(int, line.split())
        lightTemp.append([dest, source, ranges])

    elif state == 6:
        dest, source, ranges = map(int, line.split())
        tempHumid.append([dest, source, ranges])

    elif state == 7:
        dest, source, ranges = map(int, line.split())
        humidLocation.append([dest, source, ranges])

minloc = 999999999999
for seed in seeds: 
    #print("seed", seed)
    soil = -1
    for item in seedSoil: 
        end = item[1] + item[2]
        if seed-end < 0 and seed-item[1] > 0:
            soil = item[0] + seed-item[1]
            break
    if soil == -1:
        soil = seed
    #print("soil", soil)

    fertilizer = -1
    for item in soilFertilizer: 
        end = item[1] + item[2]
        if soil-end < 0 and soil-item[1] > 0:
            fertilizer = item[0] + soil-item[1]
            break
    if fertilizer == -1:
        fertilizer = soil

    #print("fert", fertilizer)

    water = -1
    for item in fertilizerWater: 
        end = item[1] + item[2]
        if fertilizer-end < 0 and fertilizer-item[1] > 0:
            water = item[0] + fertilizer-item[1]
            break
    if water == -1:
        water = fertilizer

    #print("water", water)

    light = -1
    for item in waterLight: 
        end = item[1] + item[2]
        if water-end < 0 and water-item[1] > 0:
            light = item[0] + water-item[1]
            break
    if light == -1:
        light = water

    #print("light", light)

    temp = -1
    for item in lightTemp: 
        end = item[1] + item[2]
        if light-end < 0 and light-item[1] > 0:
            temp = item[0] + light-item[1]
            break
    if temp == -1:
        temp = light

    #print("temp", temp)

    humid = -1
    for item in tempHumid: 
        end = item[1] + item[2]
        if temp-end < 0 and temp-item[1] > 0:
            humid = item[0] + temp-item[1]
            break
    if humid == -1:
        humid = temp

    #print("humid", humid)

    location = -1
    for item in humidLocation: 
        end = item[1] + item[2]
        if humid-end < 0 and humid-item[1] > 0:
            location = item[0] + humid-item[1]
            break
    if location == -1:
        location = humid

    #print("location", location)
    
    if location < minloc:
        minloc = location
    #print(location)


print(minloc)
submit(minloc)
