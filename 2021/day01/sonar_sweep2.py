with open('input.txt', 'r') as file: 
    count = 0
    frame = []
    current = 0
    sum = 0
    for line in file: 
        line = line.rstrip()
        frame.append(line)
        
        if (len(frame)==3):
            sum =  int(frame[0]) + int(frame[1]) + int(frame[2])
            current = sum
            print(sum)

        elif (len(frame)>3):
            del frame[0]
            sum =  int(frame[0]) + int(frame[1]) + int(frame[2])
            print(sum)
            if sum > current:
                count += 1
            current = sum

        
    print(count)