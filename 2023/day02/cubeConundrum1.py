import sys

totals = 0

for line in sys.stdin:

    #print(line)

    print(line.split(":"))
    game, draws = line.split(":")
    id = int(game.split()[1])

    draws = draws.split(";")
    print(draws)

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
            elif colors[1] == "red":
                red = int(colors[0])
            elif colors[1] == "blue":
                blue = int(colors[0])
            
            if red > 12 or green > 13 or blue > 14:
                flag = True
                break
        if flag:
            break
    if not flag:
        totals += id

print(totals)