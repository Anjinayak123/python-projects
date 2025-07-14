import pygame
import time
import random
import sys

pygame.init()

# Colors
gray = (119, 118, 110)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 200, 0)
blue = (0, 0, 200)
bright_red = (255, 0, 0)
bright_green = (0, 255, 0)

# Display dimensions
display_width = 800
display_height = 600
car_width = 56

# Initialize game window
gamedisplays = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Car Game by Python Life")
clock = pygame.time.Clock()

# Load images
carimg = pygame.image.load('car.jpg')
backgroundpic = pygame.image.load("download12.jpg")
yellow_strip = pygame.image.load("yellow strip.jpg")
strip = pygame.image.load("strip.jpg")
intro_background = pygame.image.load("0.jpg")
instruction_background = pygame.image.load("3.jpg")

# Text objects function
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

# Button function
def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gamedisplays, ac, (x, y, w, h))
        if click[0] == 1 and action is not None:
            if action == "play":
                countdown()
            elif action == "quit":
                pygame.quit()
                quit()
    else:
        pygame.draw.rect(gamedisplays, ic, (x, y, w, h))

    smalltext = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smalltext)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gamedisplays.blit(textSurf, textRect)

# Car display function
def car(x, y):
    gamedisplays.blit(carimg, (x, y))

# Countdown before game starts
def countdown():
    for i in range(3, 0, -1):
        gamedisplays.fill(gray)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects(str(i), largeText)
        TextRect.center = (display_width / 2, display_height / 2)
        gamedisplays.blit(TextSurf, TextRect)
        pygame.display.update()
        time.sleep(1)
    game_loop()

# Main game loop
def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0

    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gamedisplays.fill(gray)
        gamedisplays.blit(backgroundpic, (0, 0))
        car(x, y)

        if x < 0 or x > display_width - car_width:
            crash()

        pygame.display.update()
        clock.tick(60)

# Crash handler
def crash():
    message_display("You Crashed!")

# Display message function
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 80)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gamedisplays.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(2)
    intro_loop()

# Intro screen
def intro_loop():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
                sys.exit()

        gamedisplays.blit(intro_background, (0, 0))
        largetext = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("Car Game", largetext)
        TextRect.center = (400, 100)
        gamedisplays.blit(TextSurf, TextRect)

        button("START", 150, 520, 100, 50, green, bright_green, "play")
        button("QUIT", 550, 520, 100, 50, red, bright_red, "quit")

        pygame.display.update()
        clock.tick(50)

# Run the game
intro_loop()