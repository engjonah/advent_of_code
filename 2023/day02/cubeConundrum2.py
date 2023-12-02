import sys

totals = 0

for line in sys.stdin:

    #print(line)

    print(line.split(":"))
    game, draws = line.split(":")
    id = int(game.split()[1])

    draws = draws.split(";")
    print(draws)

    maxred = 0
    maxblue = 0
    maxgreen = 0

    for draw in draws: 
        individuals = draw.strip().split(",")
        print(individuals)
        flag = False
        
        for individual in individuals:
            red = 0
            blue = 0
            green = 0
            colors = individual.strip().split()
            if colors[1] == "green":
                green = int(colors[0])
                maxgreen = max(maxgreen, green)
            elif colors[1] == "red":
                red = int(colors[0])
                maxred = max(maxred, red)
            elif colors[1] == "blue":
                blue = int(colors[0])
                maxblue = max(maxblue, blue)
            
    totals += maxred * maxblue * maxgreen

print(totals)