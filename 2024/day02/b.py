from aocd import get_data, submit
import sys

data = get_data(day=2, year=2024)

output = 0

for line in sys.stdin:
#for i, line in enumerate(data):
    report = list(map(int, line.split()))

    test = [report[4] > report[0], report[4] > report[1], report[3] > report[1], report[3] > report[2], report[2] > report[1]]
    count = 0
    for i in test: 
        if i: 
            count += 1
    if count >= 3: 
        inc = True
        print('inc')
    else:
        inc = False
        print('dec')

    def check(report, done):
        #print(report, done)
        if done: 
            print("double checking", report)
        else:
            print("checking", report)
        for i in range(1, len(report)): 
            if inc and report[i] < report[i-1]:
                print('not inc')
                if done: 
                    return False
                #print("checking", report[:i] + report[i+1:])
                return check(report[:i] + report[i+1:], True) or check(report[:i-1] + report[i:], True)
            elif not inc and report[i] > report[i-1]:
                print('not dec')
                if done: 
                    return False
                #print("checking", report[:i] + report[i+1:])
                return check(report[:i] + report[i+1:], True) or check(report[:i-1] + report[i:], True)
            elif not (1 <= abs(report[i] - report[i-1]) <= 3): 
                print('big diff')
                if done: 
                    return False
                #print("checking", report[:i] + report[i+1:])
                return check(report[:i] + report[i+1:], True) or check(report[:i-1] + report[i:], True)
            
        return True

    if check(report, False) or check(report[1:], True): 
        output += 1

print(output)

#submit(output, part="b", day=2, year=2024)