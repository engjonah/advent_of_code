from aocd import get_data, submit

from queue import PriorityQueue
from collections import Counter

fulldata = get_data(day=17, year=2023).split("\n")

sampledata = []
with open("test.in", 'r') as file:
    for line in file:
        sampledata.append(line.strip())

sampledata2 = []
with open("test2.in", 'r') as file:
    for line in file:
        sampledata2.append(line.strip())

dataselect = 1
data = sampledata if dataselect == 0 else fulldata

answer = 0

grid = []


for i, line in enumerate(data): 
    #print(i, line)

    newline = []
    for j in line:
        newline.append(int(j))
    grid.append(newline)

""" othergrid = []
for i, line in enumerate(sampledata2): 
    #print(i, line)

    newline = []
    for j in line:
        newline.append(j)
    othergrid.append(newline) """

""" for line in grid:
    print("".join(line)) """

toSearch = PriorityQueue() #current loss, x, y

#loss, row, col, (hist1, hist2, hist3), loss
#up-0; right-1; down-2; left-3, none-(-1)
toSearch.put((0, (0, 0, (-1, -1, -1, -1, -1, -1, -1, -1, -1, -1), 0))) 

verticies = [(-1, 0), (0, 1), (+1, 0), (0, -1)]

height = len(grid)
width = len(grid[0])

searched = set()

minLoss = 100000000
while not toSearch.empty():
    _, stuff  = toSearch.get()
    row, col, history, loss = stuff
    if _ > minLoss:
        break
    printing = False
    printing2 = False
    """ if othergrid[row][col] not in "123456789" and row == 12 and col == 12:
        printing = True
        printing = False
        printing2 = False """
        
    
    if printing2:
        print(row, col, history, loss) 

    if row == height-1 and col == width-1:
        #only accept if 4 is correct
        if len(Counter(history[-4:])) == 1:
            if loss < minLoss:
                print("newminloss", loss, history)
            minLoss = min(minLoss, loss)
    if (row, col, history) in searched:
        if printing:
            print("thrown out; searched")
        continue
    searched.add((row, col, history))
    for i, vertex in enumerate(verticies):
        rowadd, coladd = vertex
        if printing:
            print(row, col, rowadd, coladd)
        if row + rowadd in range(height) and col + coladd in range(width):
            
            newLoss = loss + grid[row + rowadd][col + coladd]
            #print(newLoss)

            #min 4, max 10
            if history[0] != -1:
                #maxed out at all filled --> switch direction
                if len(Counter(history)) == 1 and i == history[-1]:
                    if printing:
                        print("thrown out for 10 limit")
                    continue
                if len(Counter(history[-4:])) > 1 and -1 not in history[-4:] and i!=history[-1]:
                    if printing:
                        print("thrown out for min 4 - 1")
                    continue
            #only need to check min 4
            else:
                #...-1,2,3,3 --> only same direction allowed
                # -1,x,x,x
                # -1, -1, -1, x
                if (history[-4] == -1 or history[-3] == -1 or history[-2] == -1) and i != history[-1]:
                    if history[-1] != -1:
                        if printing:
                            print("thrown out for min 4 - 2")
                        continue
                
                # 2, 2, 3, 3 --> not allowed, keep going
                if len(Counter(history[-4:])) > 1 and -1 not in history[-4:] and i!=history[-1]:
                    if printing:
                        print("thrown out for min 4 - 3")
                    continue
            
            #no backwards
            if abs(history[-1] - i) == 2 and history[-1] != -1:
                if printing:
                    print("thrown out for backwards")
                continue

            #no duplicate search
            if (row+rowadd, col+coladd, history[1:] + (i,)) in searched:
                if printing:
                    print("thrown out for duplicate")
                continue 

            #priority calculation
            #cost + min dist of travel (optimistic?)
            priority = newLoss + (width-col) + (height-row)
            if len(Counter(history))==1 and history[-1] == i:
                print("ERRORRRRRRR")
            if printing:
                print("adding to toSearch", row+rowadd, col+coladd)
            toSearch.put((priority, (row+rowadd, col+coladd, history[1:] + (i,), newLoss)))
        else:
            if printing:
                print("thrown out for oor")
            pass
print("minLoss", minLoss)

answer = minLoss

print("answer", answer)
#submit(answer)
