import pygame
import random
from pygame import *
import patient
import person
import file

# Getting a font
newFont = pygame.font.get_default_font()

# Starting resources
capacity_digestion = 5
capacity_lung = 5
capacity_heart = 5
total_money = 1500

# max capacity
total_cap = {'digestion': 5, 'lung': 5, 'heart': 5}

# disharge speed defining
disharge_speed_cardio = 1
disharge_speed_digestion = 1
disharge_speed_lung = 1

# upgrade system
doc_digestion = 2
doc_lung = 2
doc_heart = 2

# heigth and width of a window
WIDTH = 1040
HEIGHT = 585

# initialising pygame
pygame.init()
screen = pygame.display.set_mode((1040, 585))

# Making the name of the game as well as the icon
pygame.display.set_caption("Overworked Hospital")
icon = pygame.image.load('images/clinic (1).png')
pygame.display.set_icon(icon)

# the frame rate limitrer
clock = pygame.time.Clock()

# color
black = (0, 0, 0)
# fonts
font = pygame.font.Font(newFont, 20)
# the main queue
queue = file.queue([], 180 + 44, 300)

# the cardio queue object
cardio = file.queue([], 172, 850)

# the lung queue object
lungs = file.queue([], 324.5, 850)

# the digestion queue object
digestion = file.queue([], 457, 850)

# patients inside operating hospital
cardio_patients = []
lungs_patients = []
digestion_patients = []


#calculates cost for a patient
def cost(severe, ages):
    payement = (severe + ages) * 10
    return payement


#could not implement upgrade system in time
def upgrade_heart(capcity_heart, total_money, upgrade_capacity, total_cap_up, heart_capacity):
    upgrade_capcity = True
    for total_cap_up in range(5, 11):
        if upgrade_capacity == True:
            if total_money - 50 * total_cap_up >= 0:
                total_money -= 60 * total_cap_up
                heart_capacity += 1
            total_money -= 50 * total_cap_up
    return capacity_heart


def upgrade_doc_heart(doc_heart, upgrade_doc, total_money):
    for total_doc_up in range(5, 11):
        if upgrade_doc == True:
            if total_money - 60 * total_doc_up >= 0:
                total_money -= 60 * total_doc_up
                doc_heart += 1
    return doc_heart


def upgrade_lung(capacity_lung, upgrade_capacity, total_money, total_cap_up):
    upgrade_capcity = True
    for total_cap_up in range(5, 11):
        if upgrade_capacity == True:
            if total_money - 50 * total_cap_up >= 0:
                total_money -= 50 * total_cap_up
                capacity_lung += 1

            total_money -= 50 * total_cap_up
    return capacity_lung


def upgrade_doc_lung(doc_lung, upgrade_doc, total_money, total_doc_up):
    for total_doc_up in range(5, 11):
        if upgrade_doc == True:
            if total_money - 60 * total_doc_up >= 0:
                total_money -= 60 * total_doc_up
                doc_lung += 1
            total_money -= 60 * total_doc_up
    return doc_lung


def upgrade_digestion(capacity_digestion, upgrade_capacity, total_money, total_cap_up):
    upgrade_capcity = True
    for total_cap_up in range(5, 11):
        if upgrade_capacity == True:
            if total_money - 50 * total_cap_up >= 0:
                total_money -= 60 * total_cap_up
                capacity_digestion += 1
            total_money -= 50 * total_cap_up
    return capacity_digestion


def upgrade_doc_digestion(doc_digestion, upgrade_doc, total_money, total_doc_up):
    for total_doc_up in range(5, 11):
        upgrade_doc = False
        if WhereIsDaMouse > (947, 150) and WhereIsDaMouse < (969, 186):
            if total_money - 60 * total_doc_up >= 0:
                total_money -= 60 * total_doc_up
                doc_digestion += 1
            total_money -= 60 * total_doc_up
    return doc_digestion


#draws money
def ShowMoney():
    text = font.render("Total money: " + str(total_money), True, black)
    screen.blit(text, (50, 450))


#draws lung capacity
def Show_l_Capacity():
    text = font.render("Lung department capacity: " + str(capacity_lung), True, black)
    screen.blit(text, (50, 500))



#draws digestion capacity
def Show_d_Capacity():
    text = font.render("Digestion department capacity: " + str(capacity_digestion), True, black)
    screen.blit(text, (50, 525))


#draws heart capacity
def Show_h_Capacity():
    text = font.render("Heart department capacity: " + str(capacity_heart), True, black)
    screen.blit(text, (50, 550))


#checkes if anyine needs to be disharged
def disharge(frames, peoples):
    disharge = 0
    try:
        for i in range(0, len(peoples)):
            x = peoples[i].time_up(frames)
            if x:
                peoples.pop(i)
                i = i - 1
                disharge += 1
    finally:
        return [disharge, peoples]


# draws stationary objects when called
def stationary(screen):
    # button heart doc-upgrade
    button = pygame.image.load('images/panic-button.png')
    button = pygame.transform.scale(button, (40, 40))
    button_rect = button.get_rect()

    # button heart capacity-upgrade
    button2 = pygame.image.load('images/panic-button.png')
    button2 = pygame.transform.scale(button2, (40, 40))

    # button lung doc-upgrade
    button3 = pygame.image.load('images/panic-button.png')
    button3 = pygame.transform.scale(button3, (40, 40))

    # button lung capacity-upgrade
    button4 = pygame.image.load('images/panic-button.png')
    button4 = pygame.transform.scale(button4, (40, 40))

    # button digestion capacity-upgrade
    button5 = pygame.image.load('images/panic-button.png')
    button5 = pygame.transform.scale(button5, (40, 40))

    # button digestion doc-upgrade
    button6 = pygame.image.load('images/panic-button.png')
    button6 = pygame.transform.scale(button6, (40, 40))

    # Adding Buttons
    screen.blit(button, (940, 150))
    screen.blit(button2, (905, 150))
    screen.blit(button3, (940, 292.5))
    screen.blit(button4, (905, 292.5))
    screen.blit(button5, (940, 425))
    screen.blit(button6, (905, 425))

    # draws doors
    # cardio door
    door = pygame.image.load('images/door.png')
    # lung door
    door2 = pygame.image.load('images/door.png')
    # digestion door
    door3 = pygame.image.load('images/door.png')

    # draws door
    screen.blit(door, (970, 140))
    screen.blit(door2, (970, 282.5))
    screen.blit(door3, (970, 425))

    # draws borders
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, 5, HEIGHT))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, 0, WIDTH, 5))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(WIDTH - 5, 0, 5, HEIGHT))
    pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(0, HEIGHT - 5, WIDTH, 5))

    # draws receptionist
    reception = pygame.image.load('images/receptionist (1).png')
    reception = pygame.transform.scale(reception, (64, 64))
    screen.blit(reception, (260, 10))

    # draws reception desk
    desk = pygame.image.load('images/desk.png')
    desk = pygame.transform.scale(desk, (217, 170))
    desk = pygame.transform.rotate(desk, 180)
    screen.blit(desk, (192, 10))


done = True

# repeats every second
frames = 0
while done:
    # color and deletes previous screen
    screen.fill((255, 255, 255))

    for event in pygame.event.get():
        # gets keyevents for alowing patients
        if event.type == pygame.KEYDOWN:
            # Rejects patients
            if event.key == pygame.K_LEFT:
                queue.remove()
            # accepts patients
            if event.key == pygame.K_RIGHT:
                # makes sure there is a list
                if len(queue.line) == 0:
                    continue
                # checkes and adds patient to their particular line
                if queue.line[0].disease == 'heart':
                    cardio.admit(screen, queue.line[0])
                    cardio_patients.append(patient.patient(frames, queue.line[0].time_to_heal * disharge_speed_cardio))
                if queue.line[0].disease == 'lung':
                    lungs.admit(screen, queue.line[0])
                    lungs_patients.append(patient.patient(frames, queue.line[0].time_to_heal * disharge_speed_lung))
                if queue.line[0].disease == 'digestion':
                    digestion.admit(screen, queue.line[0])
                    digestion_patients.append(
                        patient.patient(frames, queue.line[0].time_to_heal * disharge_speed_digestion))
                queue.remove()
        #quits when the user closes the window
        if event.type == pygame.QUIT:
            done = False

    # checks any patients for discharge
    cardio_patients_heales = disharge(frames, cardio_patients)
    digestion_patients_heales = disharge(frames, digestion_patients)
    lungs_patients_heales = disharge(frames, lungs_patients)

    # discharges patients
    cardio_patients = cardio_patients_heales[1]
    lungs_patients = lungs_patients_heales[1]
    digestion_patients = digestion_patients_heales[1]

    # updates capacity
    capacity_heart = capacity_heart + cardio_patients_heales[0]
    capacity_lung = capacity_lung + lungs_patients_heales[0]
    capacity_digestion = capacity_digestion + digestion_patients_heales[0]

    # Showing Hospital Stats
    ShowMoney()
    Show_l_Capacity()
    Show_d_Capacity()
    Show_h_Capacity()

    # gets mouse pos
    WhereIsDaMouse = pygame.mouse.get_pos()

    # adds a person to main queue of there is capacity as to not lag comp
    if len(queue.line) < capacity_digestion + capacity_lung + capacity_heart + 10:
        queue.line.append(person.person(0, 0, screen))

    queue.draw()

    # draws cardio
    cardio.draw()
    # draws lung queue
    lungs.draw()
    # draws digestion queue
    digestion.draw()
    # draws stationary objects separately
    stationary(screen)

    # admits cardio patients inside portal to opreating table
    if capacity_heart > 0:
        if len(cardio.line) > 0:
            capacity_heart -= 1
            costofheal = cost(cardio.line[0].severity, cardio.line[0].age)
            costofheal += 100 * cardio.line[0].money
            total_money += costofheal
            cardio.remove()

    # admits lung patients inside portal to opreating table
    if capacity_lung > 0:
        if len(lungs.line) > 0:
            capacity_lung -= 1
            costofheal = cost(lungs.line[0].severity, lungs.line[0].age)
            costofheal += 100 * lungs.line[0].money
            total_money += costofheal
            lungs.remove()

    # admits digestion patients inside portal to opreating table
    if capacity_digestion > 0:
        if len(digestion.line) > 0:
            capacity_digestion -= 1
            costofheal = cost(digestion.line[0].severity, digestion.line[0].age)
            costofheal += 100 * digestion.line[0].money
            total_money += costofheal
            digestion.remove()

    frames = frames + 1
    pygame.display.update()
    clock.tick(2)
