import random
import pygame

class person:


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

    def move(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        bar_size = self.size
        # circle
        pygame.draw.circle(self.screen, (self.severity, self.money, self.time_to_heal), (self.x, self.y), self.size)

        # severity
        pygame.draw.rect(self.screen, (102, 0, 0),
                         (self.x - (self.size), self.y - (self.size + 5 + bar_size), self.size / 4, bar_size),
                         int(self.size / 20) + 1)
        bar_size_health = ((bar_size / 100) * self.severity)
        pygame.draw.rect(self.screen, (102, 0, 0), (
        self.x - (self.size), self.y - (self.size + 5 + bar_size_health), self.size / 4, bar_size_health))

        # money
        pygame.draw.rect(self.screen, (0, 100, 0),
                         (self.x - int(self.size / 8), self.y - (self.size + 5 + bar_size), self.size / 4, bar_size),
                         int(self.size / 20) + 1)
        bar_size_health = ((bar_size / 100) * self.money)
        pygame.draw.rect(self.screen, (0, 100, 0),
                         (self.x - int(self.size / 8), self.y - (self.size + 5 + bar_size_health), self.size / 4,
                          bar_size_health))
        # time to heal
        pygame.draw.rect(self.screen, (0, 0, 100), (
        self.x + self.size - int(self.size / 4), self.y - (self.size + 5 + bar_size), self.size / 4, bar_size),
                         int(self.size / 20) + 1)
        bar_size_health = ((bar_size / 100) * self.time_to_heal)
        pygame.draw.rect(self.screen, (0, 0, 100),
                         (self.x + self.size - int(self.size / 4), self.y - (self.size + 5 + bar_size_health),
                          self.size / 4, bar_size_health))

        if self.disease == 'heart':
            path = 'images/heart.png'
        elif self.disease == 'lung':
            path = 'images/lung.png'
        elif self.disease == 'digestion':
            path = 'images/stomach.png'
        prob = pygame.image.load(path)
        prob = pygame.transform.scale(prob, (self.size * 1.5, self.size * 1.5))
        self.screen.blit(prob, (self.x - ((self.size * 1.5) / 2), self.y + (self.size * 1.5) - 5))
