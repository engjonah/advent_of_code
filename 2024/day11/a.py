from aocd import get_data, submit
import sys

import itertools

data = get_data().split('\n')
from collections import defaultdict

output = 0
nums = []

for i, line in enumerate(data): 
#for line in sys.stdin: 
    print(line)
    nums = [int(j) for j in line.strip().split()]

for i in range(25): 
    newnums = []
    for num in nums: 
        numstr = str(num)
        if num == 0: 
            newnums.append(1)
        elif len(numstr) % 2 == 0: 
            newnums.append(int(numstr[:len(numstr)//2]))
            newnums.append(int(numstr[len(numstr)//2:]))
        else:
            newnums.append(num*2024)

    nums = newnums[:]

print(nums)
print(len(nums))

#submit(output)