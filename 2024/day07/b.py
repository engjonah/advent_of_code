from aocd import get_data, submit
import sys

data = get_data().split('\n')
import itertools

output = 0
operations = ['+', '*', '|']

def dfs(curr, nums): 
    #print(curr, nums)
    if len(nums) == 0: 
        if curr == test: 
            #print(curr)
            return curr
        return 0

    for op in operations: 
        if op == '+': 
            output1 = dfs(curr + nums[0], nums[1:])
        elif op == '*': 
            output2 = dfs(curr * nums[0], nums[1:])
        else:
            output3 = dfs(int(str(curr) + str(nums[0])), nums[1:])
    
    return max(output1, output2, output3)
            
for i, line in enumerate(data): 
#for line in sys.stdin: 
    print(i, line)
    test, nums = line.split(':')
    nums = [int(i) for i in nums.strip().split()]
    test = int(test)

    if test == dfs(nums[0], nums[1:]):

        output += test

print(output)

#submit(output)