import random

import pygame


class Ant:
    def __init__(self):
        self.no_of_ants = 5
        pygame.init()
        # Displaying a 800X600 game window
        self.window_x = 800
        self.window_y = 640
        self.window = pygame.display.set_mode((self.window_x, self.window_y))
        pygame.display.set_caption("Sugar hunt")
        # background image
        self.bg = pygame.image.load("greengrass.jpeg")
        self.window.blit(self.bg, (0, 0))
        self.ants = []
        self.ant_x = []
        self.ant_y = []
        self.wall = pygame.image.load("wall-1475318__480.jpeg")
        self.bread = pygame.image.load("bread.png")

    def load_img(self):
        for i in range(self.no_of_ants):
            self.ants.append(pygame.image.load("ant_final.png"))
            self.ant_x.append(random.randint(0, self.window_x/2))
            self.ant_y.append(random.randint(self.window_y/2, self.window_y - 50))
        # wall_x = self.window_x/4
        # wall_y = self.window_y/3


    def display_ant(self, x, y, i):
        self.load_img()
        self.window.blit(self.ant[i], (x, y))

    def display_wall(self):
        self.window.blit(self.wall, (160, 160))

    def display_bread(self):
        self.window.blit(self.bread, (320, 0))

    def draw_grid(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        block_size = 80
        BLACK = (0, 0, 0)
        WHITE = (200, 200, 200)
        for x in range(SCREEN_WIDTH):
            for y in range(SCREEN_HEIGHT):
                rect = pygame.Rect(x*block_size, y*block_size,
                                   block_size, block_size)
                pygame.draw.rect(self.window, WHITE, rect, 1)


ant = Ant()
# to prevent the window from closing, we use event handler
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    for i in range(ant.no_of_ants):
        ant.display_ant(ant.ant_x[i], ant.ant_y[i], i)
    ant.display_wall()
    ant.display_bread()
    ant.draw_grid(ant.window_x, ant.window_y)
    pygame.display.update()
pygame.quit()
