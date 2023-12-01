
values = 0
while True:
    inp = input()
    if inp == '-':
        break
    else:
        numbers = "0123456789"
        othernums = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
        nums = []
        for i, num in enumerate(inp):
            if num in numbers:
                nums.append(num)
            elif inp[i:i+3] == "one":
                nums.append("1")
            elif inp[i:i+3] == "two":
                nums.append("2")
            elif inp[i:i+5] == "three":
                nums.append("3")
            elif inp[i:i+4] == "four":
                nums.append("4")
            elif inp[i:i+4] == "five":
                nums.append("5")
            elif inp[i:i+3] == "six":
                nums.append("6")
            elif inp[i:i+5] == "seven":
                nums.append("7")
            elif inp[i:i+5] == "eight":
                nums.append("8")
            elif inp[i:i+4] == "nine":
                nums.append("9")
        print(nums, int(nums[0] + nums[-1]))
        values += int(nums[0] + nums[-1])
    
print(values)