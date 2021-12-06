with open('input1.txt', 'r') as file: 
    count = 0
    current = file.readline()
    for line in file: 
        if line > current:
            count += 1
        current = line
    print(count)