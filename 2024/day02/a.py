from aocd import get_data, submit
import sys

data = get_data(day=2, year=2024)
print(data)

output = 0

for line in sys.stdin:
#for i, line in enumerate(data):
    report = list(map(int, line.split()))

    if report[1] > report[0]: 
        inc = True
    else:
        inc = False
    
    flag = True
    for i in range(1, len(report)): 
        if inc and report[i] < report[i-1]:
            print('not inc')
            flag = False
            break 
        if not inc and report[i] > report[i-1]:
            print('not dec')
            flag = False
            break
        if not (1 <= abs(report[i] - report[i-1]) <= 3): 
            print('big diff')
            flag = False
            break

    if flag: 
        output += 1


print(output)

#submit(output, part="a", day=2, year=2024)