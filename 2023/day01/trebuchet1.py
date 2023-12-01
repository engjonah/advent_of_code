
values = 0
while True:
    inp = input()
    if inp == '-':
        break
    else:
        numbers = "0123456789"
        
        nums = []
        for i in inp:
            if i in numbers:
                nums.append(i)
        values += int(nums[0] + nums[-1])
    
print(values)