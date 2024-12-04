from aocd import get_data, submit
import sys

data = get_data()
#print(data)

output = 0

for i, line in enumerate(data):
    #print(line)
    pass

#data = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
#data = 'mul(111,222)'
curr = ''
firstnum = ''
secondnum = ''
firstnumdone = False
for i in range(len(data)): 
    print(curr != '',firstnumdone , (curr != '' and (curr[-1] in '0123456789' or curr[-1] == ',')) , data[i] in '0123456789')
    if data[i] == 'm' and curr == '':
        curr = 'm'
    elif curr != '' and curr[-1] == 'm' and data[i] == 'u':
        curr = 'mu'
    elif curr != '' and curr[-1] == 'u' and data[i] == 'l':
        curr = 'mul'
    elif curr != '' and curr[-1] == 'l' and data[i] == '(':
        curr = 'mul('
        firstnum = ''
        secondnum = ''
        firstnumdone = False
    elif not firstnumdone and curr != '' and (curr[-1] in '0123456789' or curr[-1] == '(') and data[i] in '0123456789':
        curr += data[i]
        firstnum += data[i]
        if len(firstnum) > 3:
            print('first too long')
            curr = ''
    elif curr != '' and curr[-1] in '0123456789' and data[i] == ',':
        curr += ','
        firstnumdone = True
    elif curr != '' and firstnumdone and (curr[-1] in '0123456789' or curr[-1] == ',') and data[i] in '0123456789':
        curr += data[i]
        secondnum += data[i]
        if len(secondnum) > 3:
            print("2nd too long")
            curr = ''
    elif curr != '' and firstnumdone and curr[-1] in '0123456789' and data[i] == ')':
        print('output', firstnum, secondnum)
        output += int(firstnum) * int(secondnum)
        curr = ''
    else:
        print('resetting')
        curr = ''
    print(data[i], curr, firstnum, secondnum)
    

print(output)
