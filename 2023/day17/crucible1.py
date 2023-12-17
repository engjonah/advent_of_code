from aocd import get_data, submit

from queue import PriorityQueue

fulldata = get_data(day=17, year=2023).split("\n")

sampledata = []
with open("test.in", 'r') as file:
    for line in file:
        sampledata.append(line.strip())

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

""" for line in grid:
    print("".join(line)) """

toSearch = PriorityQueue() #current loss, x, y

#loss, row, col, (hist1, hist2, hist3), loss
#up-0; right-1; down-2; left-3, none-(-1)
toSearch.put((0, (0, 0, (-1, -1, -1), 0))) 

verticies = [(-1, 0), (0, 1), (+1, 0), (0, -1)]

height = len(grid)
width = len(grid[0])

searched = set()

minLoss = 100000000
while not toSearch.empty():
    _, stuff  = toSearch.get()
    row, col, history, loss = stuff
    print(row, col, history, loss)
    if row == height-1 and col == width-1:
        if loss < minLoss:
            print(minLoss)
        minLoss = min(minLoss, loss)
    if (row, col, history) in searched:
        continue
    searched.add((row, col, history))
    for i, vertex in enumerate(verticies):
        rowadd, coladd = vertex
        
        if row + rowadd in range(height) and col + coladd in range(width):
            
            newLoss = loss + grid[row + rowadd][col + coladd]
            #print(newLoss)

            #no 3 consecutive values - have to move
            if history[1] != -1:
                if history[0] == history[1] and history[1] == history[2] and history[2] == i:
                    continue
            
            #no backwards
            if abs(history[2] - i) == 2:
                continue

            #no duplicate search
            if (row+rowadd, col+coladd, (history[1], history[2], i)) in searched:
                continue 

            #priority calculation
            #cost + min dist of travel (optimistic?)
            priority = newLoss + (width-col) + (height-row)

            toSearch.put((priority, (row+rowadd, col+coladd, (history[1], history[2], i), newLoss)))

print("minLoss", minLoss)


answer = minLoss

print("answer", answer)
submit(answer)
