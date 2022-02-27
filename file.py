import person


# This is a class object for a line of people
class queue:
    # inits programs
    def __init__(self, line, y, start):
        self.line = line
        self.y = y
        self.start = start

    # auto draws the queues
    def draw(self):
        line = self.line
        # Starting x position
        x = self.start
        # loops through the people in the queue
        for i in range(0, len(line)):
            # changes x,y pos for the person
            line[i].move(x, self.y)
            # displays only 8 people.
            if i < 8:
                # draws people
                if x > 0:
                    line[i].draw()
                # calulates the distance from other person
                if (i != len(line) - 1):
                    x = x - (line[i].size + 5 + line[i + 1].size)

    # method to add a random person to the queue
    def add(self, screen):
        self.line.append(person.person(0, 0, screen))

    # method to add a specific person to queue
    def admit(self, screen, person):
        self.line.append(person)

    # Removes first person form the queue
    def remove(self):
        if len(self.line) > 0:
            self.line.pop(0)
