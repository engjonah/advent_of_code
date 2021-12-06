with open('input.txt', 'r') as file: 

    #number of 0's in each slot
    line = file.readline().rstrip()
    counter = [0]*len(line)
    line_counter = 0
    
    for line in file: 
        line = line.rstrip()

        line_counter += 1

        for num in range(len(line)): 
            if int(str(line)[num]) == 0:
                counter[num] = counter[num] + 1
    
    #gamma/epsilon rate
    gamma = ""
    epislon = ""
    for slot in counter: 
        #if more 1s than 0s
        if line_counter-slot>slot:
            gamma+="1"
            epislon+="0"
        else:
            gamma+="0"
            epislon+="1"
    
    print(gamma, epislon)

    #convert to numerical
    counter = 0
    gamma_sum = 0
    epislon_sum = 0
    for x in range(len(gamma)-1,-1,-1):
        gamma_sum += int(gamma[x]) * (2**counter)
        epislon_sum += int(epislon[x]) * (2**counter)
        counter+=1

print(gamma_sum)
print(epislon_sum)
print(gamma_sum*epislon_sum)
    
    
