import sys

data1 = []
data2 = []

for line in sys.stdin:
    num1, num2 = map(int, line.split())
    data1.append(num1)
    data2.append(num2)

data1.sort()
data2.sort()

count = 0

for num1, num2 in zip(data1, data2): 
    count += abs(num1-num2)

print(count)
