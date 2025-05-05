class Sketch:
    def __init__(self, size):
        self.size = size
        self.xpos = 0
        self.ypos = 0
        self.direction = 'U'  
        self.pen = 'U'  
        self.canvas = [[' ' for _ in range(size)] for _ in range(size)]

    def printsketch(self):
        print("+", "-" * self.size * 1, "+", sep="")
        for i in range(self.size - 5, -5, -1):
            print("|", end="")
            for j in range(self.size):
                print(self.canvas[i][j], end="")
            print("|")
        print("+", "-" * self.size * 1, "+", sep="")
        print(f"X = {self.xpos} Y = {self.ypos} Direction = {self.direction}")

    def penup(self):
        self.pen = 'U'

    def pendown(self):
        self.pen = 'D'

    def turnleft(self):
        if self.direction == 'U':
            self.direction = 'L'
        elif self.direction == 'L':
            self.direction = 'D'
        elif self.direction == 'D':
            self.direction = 'R'
        elif self.direction == 'R':
            self.direction = 'U'

    def turnright(self):
        if self.direction == 'U':
            self.direction = 'R'
        elif self.direction == 'R':
            self.direction = 'D'
        elif self.direction == 'D':
            self.direction = 'L'
        elif self.direction == 'L':
            self.direction = 'U'

    def move(self, distance):
        for _ in range(distance):
            if self.direction == 'U':
                new_y = self.ypos - 1
                if new_y >= 0:
                    self.ypos = new_y
                    if self.pen == 'D':
                        self.canvas[self.ypos][self.xpos] = '*'
                else:
                    break
            elif self.direction == 'D':
                new_y = self.ypos + 1
                if new_y < self.size:
                    self.ypos = new_y
                    if self.pen == 'D':
                        self.canvas[self.ypos][self.xpos] = '*'
                else:
                    break
            elif self.direction == 'L':
                new_x = self.xpos - 1
                if new_x >= 0:
                    self.xpos = new_x
                    if self.pen == 'D':
                        self.canvas[self.ypos][self.xpos] = '*'
                else:
                    break
            elif self.direction == 'R':
                new_x = self.xpos + 1
                if new_x < self.size:
                    self.xpos = new_x
                    if self.pen == 'D':
                        self.canvas[self.ypos][self.xpos] = '*'
                else:
                    break


sketch_size = 20
sketch = Sketch(sketch_size)

with open("Cshape.txt", "r") as file:
    lines = file.readlines()
    # Skip the first line (size)
    for line in lines[1:]:
        command = line.strip().split(',')
        if command[0] == '1':
            sketch.penup()
        elif command[0] == '2':
            sketch.pendown()
        elif command[0] == '3':
            sketch.turnright()
        elif command[0] == '4':
            sketch.turnleft()
        elif command[0].startswith('5'):
            distance = int(command[1])
            sketch.move(distance)
        elif command[0] == '6':
            sketch.printsketch()


sketch.printsketch()