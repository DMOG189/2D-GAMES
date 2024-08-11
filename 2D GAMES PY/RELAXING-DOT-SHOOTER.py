# MLRS SHOOTIN GAME THAT AN AI DEVELOPED DURING CLASS

# !!!!!INSTRUCTIONS!!!!
# IN ORDER TO PLAY
# MAKE SURE YOUR PYTHON INTERPERTER AND OR CMD HAVE PYGAME
# pip install pygame   <--- WRITE THIS TO INSTALL PYGAME IN YOUR CONSOLE


# START

import pygame
import math
import random

# Initialize Pygame
pygame.init()

# Define colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Define display dimensions
display_width = 800
display_height = 600

# Set up display
dis = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('MLRS Truck Shooting Missiles')

# Define clock
clock = pygame.time.Clock()

# Missile class
class Missile:
    def __init__(self, x, y, angle):
        self.x = x
        self.y = y
        self.angle = angle
        self.speed = 10

    def move(self):
        self.x += self.speed * math.cos(self.angle)
        self.y -= self.speed * math.sin(self.angle)

    def draw(self, dis):
        pygame.draw.circle(dis, red, (int(self.x), int(self.y)), 5)

# MLRS Truck class
class MLRSTruck:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.missiles = []

    def launch_missile(self):
        angle = random.uniform(math.pi / 6, math.pi / 3)  # Random angle between 30 and 60 degrees
        self.missiles.append(Missile(self.x + 50, self.y, angle))

    def draw(self, dis):
        pygame.draw.rect(dis, black, [self.x, self.y, 100, 50])
        for missile in self.missiles:
            missile.draw(dis)

    def update_missiles(self):
        for missile in self.missiles:
            missile.move()

def game_loop():
    truck = MLRSTruck(100, display_height - 100)
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    truck.launch_missile()

        truck.update_missiles()

        dis.fill(blue)
        truck.draw(dis)
        pygame.display.update()
        clock.tick(30)

    pygame.quit()

if __name__ == '__main__':
    game_loop()


# END