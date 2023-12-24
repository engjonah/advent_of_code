from aocd import get_data, submit
from collections import defaultdict, deque

fulldata = get_data(day=24, year=2023).split("\n")

sampledata = []
with open("test.in", 'r') as file:
    for line in file:
        sampledata.append(line.strip())

dataselect = 1
data = sampledata if dataselect == 0 else fulldata

answer = 0

hailstones = []

for i, line in enumerate(data):
    #print(i, line)
    pos, vel = line.split("@")
    pos, vel = pos.split(","), vel.split(",")
    hailstones.append((pos, vel))

for i, hailstone in enumerate(hailstones):
    pos, vel = hailstone
    posx, posy, posz = map(int, pos)
    velx, vely, velz = map(int, vel)

    #changey/changex
    m1 = vely/velx
    b1 = posy - (m1 * posx)

    for j in range(i+1, len(hailstones)):
        hailstone2 = hailstones[j]

        pos2, vel2 = hailstone2
        posx2, posy2, posz2 = map(int, pos2)
        velx2, vely2, velz2 = map(int, vel2)

        m2 = vely2/velx2
        b2 = posy2 - (m2 * posx2)
        
        #parallel - no intersect
        if m1 == m2:
            #print("parallel")
            continue
    
        x = (b2 - b1) / (m1 - m2)
        y = m1 * x + b1
        min, max = (7, 27) if dataselect == 0 else (200000000000000, 400000000000000)
        if not (min <= x <= max and min <= y <= max):
            #print("intersect not in range", x, y)
            pass
        elif (x > posx and velx < 0) or (x < posx and velx > 0) or  (y > posy and vely < 0) or (y < posy and vely > 0):
            #print("out of range hailstone A")
            pass
        elif (x > posx2 and velx2 < 0) or (x < posx2 and velx2 > 0) or  (y > posy2 and vely2 < 0) or (y < posy2 and vely2 > 0):
            #print("out of range hailstone B")
            pass
        else:
            answer += 1
            #print("insersect in range", x, y, hailstone, hailstone2)



print("answer", answer)
#submit(answer)
