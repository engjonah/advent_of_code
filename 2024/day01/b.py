import sys
from collections import defaultdict


data1 = []
data2 = defaultdict(int)

for line in sys.stdin:
    num1, num2 = map(int, line.split())
    data1.append(num1)
    data2[num2] += 1

count = 0

print(data1, data2)

for num1 in data1: 
    count += num1 * data2[num1]

print(count)

