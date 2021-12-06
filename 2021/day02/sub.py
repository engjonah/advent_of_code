class Sub: 
    def __init__(self):
        self.x = 0
        self.y = 0
        self.aim = 0
    
    def forward(self,x):
        self.x +=x
        self.y += self.aim*x
    
    def down(self,x):
        #self.y += x
        self.aim += x
    
    def up(self,x):
        #self.y -= x
        self.aim -= x
    
    def position(self):
        return self.x, self.y, self.x * self.y


my_sub = Sub()
with open('input.txt', 'r') as file: 
    for line in file: 
        line = line.rstrip()
        line = line.split()
        if (line[0]=="forward"):
            my_sub.forward(int(line[1]))
        elif (line[0]=="down"):
            my_sub.down(int(line[1]))
        elif (line[0]=="up"):
            my_sub.up(int(line[1]))

print(my_sub.position()[2])
