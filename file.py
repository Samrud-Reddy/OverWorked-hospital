import person

class queue:
    def __init__(self, line, y, start):
        self.line = line
        self.y = y
        self.start = start

    def draw(self):
        line = self.line
        x = self.start
        for i in range(0, len(line)):
            line[i].move(x, self.y)
            if i<8:

                if x>0:
                    line[i].draw()

                if (i != len(line)-1):
                    x = x - (line[i].size + 5 + line[i + 1].size)



    def add(self, screen):
        self.line.append(person.person(0, 0, screen))

    def admit(self, screen, person):
        self.line.append(person)

    def remove(self):
        if len(self.line)>0:
            self.line.pop(0)



    def average(self, x, y):
        return (x+y)/2
