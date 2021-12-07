with open('input.txt', 'r') as file:
    numbers1 = []
    numbers2 = []

    for line in file: 
        line = line.rstrip()

        numbers1.append(str(line))
        numbers2.append(str(line))

    #oxygen
    place_counter = 0
    common_counter = 0
    while len(numbers1) > 1:
        #count number of 0s per column
        for num in numbers1:
            if int(num[place_counter]) == 0:
                common_counter+=1

        #if 0s > 1s
        #adjust operator sign for >=
        if common_counter > len(numbers1)-common_counter:
            for i in range(len(numbers1)-1,-1,-1): 
                if int(numbers1[i][place_counter])!=0:
                    del numbers1[i]
        else:
            for i in range(len(numbers1)-1,-1,-1): 
                if int(numbers1[i][place_counter])!=1:
                    del numbers1[i]
        place_counter+=1
        common_counter=0
    

    #co2
    place_counter = 0
    common_counter = 0
    while len(numbers2) > 1:
        #count number of 0s per column
        for num in numbers2:
            if int(num[place_counter]) == 0:
                common_counter+=1

        #if 0s > 1s
        #adjust operator sign for >=
        if common_counter <= len(numbers2)-common_counter:
            for i in range(len(numbers2)-1,-1,-1): 
                if int(numbers2[i][place_counter])!=0:
                    del numbers2[i]
        else:
            for i in range(len(numbers2)-1,-1,-1): 
                if int(numbers2[i][place_counter])!=1:
                    del numbers2[i]
        place_counter+=1
        common_counter=0
    


#convert to numerical
o2 = numbers1[0]
co2 = numbers2[0]

print(o2)
print(co2)

o2_sum = 0
co2_sum = 0
counter = 0
for x in range(len(o2)-1,-1,-1):
    o2_sum += int(o2[x]) * (2**counter)
    co2_sum += int(co2[x]) * (2**counter)

    counter+=1



print(o2_sum)
print(co2_sum)
print(o2_sum*co2_sum)

'''
    #most common
    result = ""
    for slot in counter: 
        #if more 1s than 0s
        if line_counter-slot>slot:
            result+="1"
        else:
            result+="0"
        
'''
    
