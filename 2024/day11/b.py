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

from collections import defaultdict

newnums = defaultdict(int)

for num in nums: 
    newnums[num] += 1

nums = newnums.copy()
for i in range(75): 
    print(i)
    newnums = defaultdict(int)
    for num, copy in nums.items(): 
        numstr = str(num)
        if num == 0: 
            newnums[1] += copy
        elif len(numstr) % 2 == 0: 
            newnums[int(numstr[:len(numstr)//2])] += copy
            newnums[int(numstr[len(numstr)//2:])] += copy
        else:
            newnums[num*2024] += copy

    nums = newnums.copy()

print(nums)
print(len(nums))
output = 0
for num, copy in nums.items(): 
    output += copy

print(output)
#submit(output)