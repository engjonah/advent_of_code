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
##print(data)

finalanswer = 0

seeds = []
seedSoil = dict()
soilFertilizer = dict()
fertilizerWater = dict()
waterLight = dict()
lightTemp = dict()
tempHumid = dict()
humidLocation = dict()

seedSoil2 = []
soilFertilizer2 = []
fertilizerWater2 = []
waterLight2 = []
lightTemp2 = []
tempHumid2 = []
humidLocation2 = []

state = 0
fullseeds = set()
for i, line in enumerate(data): 
    ##print(line)
    print(i)

    if i == 0:
        seeds = line.split(":")[1].strip().split()
        seeds = [int(seed) for seed in seeds]
        
        
        #fullseeds = set(fullseeds)
    
    if line == "":
        state += 1
        continue

    if line[-1] == ":":
        continue
    
    #add to maps
    if state == 1:
        dest, source, ranges = map(int, line.split())
        seedSoil2.append([dest, source, ranges])
        """  for j in range(ranges):
            seedSoil[source+j] = dest + j """
    elif state == 2:
        dest, source, ranges = map(int, line.split())
        soilFertilizer2.append([dest, source, ranges])
        """ for j in range(ranges):
            soilFertilizer[source+j] = dest + j """
    elif state == 3:
        dest, source, ranges = map(int, line.split())
        fertilizerWater2.append([dest, source, ranges])
        """ for j in range(ranges):
            fertilizerWater[source+j] = dest + j """
    elif state == 4:
        dest, source, ranges = map(int, line.split())
        waterLight2.append([dest, source, ranges])
        """ for j in range(ranges):
            waterLight[source+j] = dest + j """
    elif state == 5:
        dest, source, ranges = map(int, line.split())
        lightTemp2.append([dest, source, ranges])
        """ for j in range(ranges):
            lightTemp[source+j] = dest + j """
    elif state == 6:
        dest, source, ranges = map(int, line.split())
        tempHumid2.append([dest, source, ranges])
        """ for j in range(ranges):
            tempHumid[source+j] = dest + j """
    elif state == 7:
        dest, source, ranges = map(int, line.split())
        humidLocation2.append([dest, source, ranges])
        """ for j in range(ranges):
            humidLocation[source+j] = dest + j """

    ##print()
print("seedsoil", seedSoil2)
print(soilFertilizer2)
print(fertilizerWater2)
print(waterLight2)
print(lightTemp2)
print(tempHumid2)
print(humidLocation2)


""" 
minloc = 999999999999
for seed in fullseeds: 
    #print("seed", seed)
    soil = -1
    for item in seedSoil2: 
        end = item[1] + item[2]
        if seed-end <= 0 and seed-item[1] >= 0:
            soil = item[0] + seed-item[1]
            break
    if soil == -1:
        soil = seed
    ##print("soil", soil)

    fertilizer = -1
    for item in soilFertilizer2: 
        end = item[1] + item[2]
        if soil-end <= 0 and soil-item[1] >= 0:
            fertilizer = item[0] + soil-item[1]
            break
    if fertilizer == -1:
        fertilizer = soil

    ##print("fert", fertilizer)

    water = -1
    for item in fertilizerWater2: 
        end = item[1] + item[2]
        if fertilizer-end <= 0 and fertilizer-item[1] >= 0:
            water = item[0] + fertilizer-item[1]
            break
    if water == -1:
        water = fertilizer

    ##print("water", water)

    light = -1
    for item in waterLight2: 
        end = item[1] + item[2]
        if water-end <= 0 and water-item[1] >= 0:
            light = item[0] + water-item[1]
            break
    if light == -1:
        light = water

    ##print("light", light)

    temp = -1
    for item in lightTemp2: 
        end = item[1] + item[2]
        if light-end <= 0 and light-item[1] >= 0:
            temp = item[0] + light-item[1]
            break
    if temp == -1:
        temp = light

    ##print("temp", temp)

    humid = -1
    for item in tempHumid2: 
        end = item[1] + item[2]
        if temp-end <= 0 and temp-item[1] >= 0:
            humid = item[0] + temp-item[1]
            break
    if humid == -1:
        humid = temp

    ##print("humid", humid)

    location = -1
    for item in humidLocation2: 
        end = item[1] + item[2]
        if humid-end <= 0 and humid-item[1] >= 0:
            location = item[0] + humid-item[1]
            break
    if location == -1:
        location = humid

    ##print("location", location)
    
    if location <= minloc:
        minloc = location
    #print(location)

    ##print() """
print("done making map")
fullseeds = []
seedranges = []
for j in range(len(seeds)):
    print("j", j)
    if j%2==1:
        continue
    #fullseeds.update(range(seeds[j], seeds[j] + seeds[j+1]))
    #fullseeds += range(seeds[i], seeds[i] + seeds[i+1])
    seedranges.append((seeds[j], seeds[j] + seeds[j+1]))
    print(j)
print(seedranges)

#assert 1==2
print("done making seed set")
i = 0
flag = False
while True:
    print(i)

    location = i
    
    humid = -1
    for item in humidLocation2: 
        end = item[0] + item[2]
        if location-end <= 0 and location-item[0] >= 0:
            humid = item[1] + location-item[0]
            break
    if humid == -1:
        humid = location
    #print("humid", humid)

    temp = -1
    for item in tempHumid2: 
        end = item[0] + item[2]
        if humid-end <= 0 and humid-item[0] >= 0:
            temp = item[1] + humid-item[0]
            break
    if temp == -1:
        temp = humid
    #print("temp", temp)

    light = -1
    for item in lightTemp2: 
        end = item[0] + item[2]
        if temp-end <= 0 and temp-item[0] >= 0:
            light = item[1] + temp-item[0]
            break
    if light == -1:
        light = temp
    #print("light", light)

    water = -1
    for item in waterLight2: 
        end = item[0] + item[2]
        if light-end <= 0 and light-item[0] >= 0:
            water = item[1] + light-item[0]
            break
    if water == -1:
        water = light
    #print("water", water)

    fertilizer = -1
    for item in fertilizerWater2: 
        end = item[0] + item[2]
        if water-end <= 0 and water-item[0] >= 0:
            fertilizer = item[1] + water-item[0]
            break
    if fertilizer == -1:
        fertilizer = water
    #print("fertilizer", fertilizer)

    soil = -1
    for item in soilFertilizer2: 
        end = item[0] + item[2]
        if fertilizer-end <= 0 and fertilizer-item[0] >= 0:
            soil = item[1] + fertilizer-item[0]
            break
    if soil == -1:
        soil = fertilizer
    #print("soil", soil)

    seed = -1
    for item in seedSoil2: 
        end = item[0] + item[2]
        if soil-end <= 0 and soil-item[0] >= 0:
            seed = item[1] + soil-item[0]
            break
    if seed == -1:
        seed = soil
    #print("seed", seed)

    for seedrange in seedranges:
        #print("seedgrange", seedrange)
        #print("seed", seed)
        if seed >= seedrange[0] and seed <= seedrange[1]:
            print(i)
            flag = True
            submit(i)
            break

    if flag:
        break
    i+=1



##print(minloc)
#submit(minloc)
