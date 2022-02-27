# Samruds code


import random
import pygame


# this is a class person
class person:

    # Inits variables randomly
    def __init__(self, x, y, screen):
        self.x = x
        self.y = y
        self.screen = screen
        self.money = random.randint(1, 100)
        self.severity = random.randint(1, 100)
        self.time_to_heal = random.randint(1, 100)
        self.disease = random.choice(('lung', 'heart', 'digestion'))
        self.gender = random.choice(('male', 'female'))
        self.age = random.randint(1, 100)
        self.size = (self.age / 3) + 10

    # changes x,y values of the person
    def move(self, x, y):
        self.x = x
        self.y = y

    # draws the person
    def draw(self):
        # calculates bar size
        bar_size = self.size
        # the person circle.
        pygame.draw.circle(self.screen, (self.severity, self.money, self.time_to_heal), (self.x, self.y), self.size)

        # the severity outer rectangle
        pygame.draw.rect(self.screen, (102, 0, 0),
                         (self.x - (self.size), self.y - (self.size + 5 + bar_size), self.size / 4, bar_size),
                         int(self.size / 20) + 1)
        # calculates hieght of severity
        bar_size_health = ((bar_size / 100) * self.severity)
        # draws the inner rectangle for severity
        pygame.draw.rect(self.screen, (102, 0, 0), (
            self.x - (self.size), self.y - (self.size + 5 + bar_size_health), self.size / 4, bar_size_health))

        # the Money outer rectangle
        pygame.draw.rect(self.screen, (0, 100, 0),
                         (self.x - int(self.size / 8), self.y - (self.size + 5 + bar_size), self.size / 4, bar_size),
                         int(self.size / 20) + 1)
        # calculates hieght of money
        bar_size_health = ((bar_size / 100) * self.money)
        # draws the inner rectangle for money
        pygame.draw.rect(self.screen, (0, 100, 0),
                         (self.x - int(self.size / 8), self.y - (self.size + 5 + bar_size_health), self.size / 4,
                          bar_size_health))
        # the time to heal outer rectangle
        pygame.draw.rect(self.screen, (0, 0, 100), (
            self.x + self.size - int(self.size / 4), self.y - (self.size + 5 + bar_size), self.size / 4, bar_size),
                         int(self.size / 20) + 1)
        # calculates hieght of time to heal
        bar_size_health = ((bar_size / 100) * self.time_to_heal)
        # draws the inner rectangle for time to heal
        pygame.draw.rect(self.screen, (0, 0, 100),
                         (self.x + self.size - int(self.size / 4), self.y - (self.size + 5 + bar_size_health),
                          self.size / 4, bar_size_health))
        # depending on disease gets the path for icons
        if self.disease == 'heart':
            path = 'images/heart.png'
        elif self.disease == 'lung':
            path = 'images/lung.png'
        elif self.disease == 'digestion':
            path = 'images/stomach.png'
        # Loads the image
        prob = pygame.image.load(path)
        # calculates size of image
        prob = pygame.transform.scale(prob, (self.size * 1.5, self.size * 1.5))
        # draws disease icon
        self.screen.blit(prob, (self.x - ((self.size * 1.5) / 2), self.y + (self.size * 1.5) - 5))
