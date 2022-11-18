import random
import pygame as pg

pg.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
window = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pg.display.set_caption("Ant Food Hunting")
background = pg.image.load("pexels-fwstudio-131634.jpg")
window.blit(background, (0, 0))
ant_icon = pg.image.load("icons8-ant-30.png")
pg.display.set_icon(ant_icon)

ant =[]
ant_position_X = []
ant_position_Y = []

number_of_ant = 5git
for i in range (number_of_ant):
    ant.append(pg.image.load("icons8-ant-30.png"))
    ant_position_X.append(random.randint(0,SCREEN_WIDTH/2))
    ant_position_Y.append(random.randint(SCREEN_WIDTH/2,SCREEN_HEIGHT))


def display_ant(x, y,i):
    window.blit(ant[i], (x, y))


food = pg.image.load("icons8-bread-loaf-48.png")
food_position_X = SCREEN_WIDTH/2
food_position_Y = SCREEN_HEIGHT/6


obstacle = pg.image.load("icons8-brick-wall-80.png")
obstacle_position_X = SCREEN_WIDTH/2
obstacle_position_Y = SCREEN_HEIGHT/3


def display_food(x, y):
    window.blit(food, (x, y))


def display_obstacle(x, y):
    window.blit(obstacle, (x, y))


running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        for i in range(number_of_ant):
            display_ant(ant_position_X[i], ant_position_Y[i], i)
    display_food(food_position_X, food_position_Y)
    display_obstacle(obstacle_position_X, obstacle_position_Y)

    pg.display.update()

pg.quit()

