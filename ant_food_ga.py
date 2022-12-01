import math
import random
from math import floor
import pygame as pg
from numpy.random import choice


#import pygame.event

#from ant2 import Ant
from Ant import Ant


SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
ANT_SIZE = 30
should_quit = False
clock = pg.time.Clock()


food_position_x = SCREEN_WIDTH / 2.2
food_position_y = SCREEN_HEIGHT / 6
obstacle_position_x = SCREEN_WIDTH / 4
obstacle_position_y = SCREEN_HEIGHT / 2.5
obstacle_width = 0
obstacle_height = 0

ant_icon = pg.image.load("icons8-ant-30.png")
ant_population_count = 20
ant_list = []
ant_fitness_list = []
ant_lifespan = 15
no_of_generations = 10
new_ant_list = []
fitness_dict = {}


def generate_genes():
    angle = random.random() * 2 * math.pi
    x = random.randrange(0, 100) * math.cos(angle)
    y = random.randrange(0, 200) * math.sin(angle)
    return [x, y]


def generate_ant_population(count):
    for i in range(count):
        x_co_ordinate = random.randrange(ANT_SIZE, SCREEN_WIDTH - ANT_SIZE)
        y_co_ordinate = (random.randrange(SCREEN_HEIGHT - 100, SCREEN_HEIGHT)) - ANT_SIZE
        ant_genes = []
        for l in range(ant_lifespan):
            ant_genes.append(generate_genes())

        generated_ant = Ant(x_co_ordinate, y_co_ordinate, ant_genes)
        ant_list.append(generated_ant)


def calculate_ant_fitness(individual_ant):
    food_location = [food_position_x, food_position_y]
    ant_location = [individual_ant.x_position, individual_ant.y_position]
    ant_fitness = math.dist(ant_location, food_location)
    return 1 / ant_fitness


def evaluate():
    max_fitness = 0
    ant_index = 0

    for individual in ant_list:
        individual_fitness = calculate_ant_fitness(individual)
        if individual_fitness > max_fitness:
            max_fitness = individual_fitness

    for one_ant in ant_list:
        one_ant_fitness = calculate_ant_fitness(one_ant)
        fitness = (one_ant_fitness / max_fitness)*100
        ant_fitness_list.append(fitness)
        fitness_dict.update({ant_index: fitness})
        ant_index += 1


def selection():
    parent_list = list(fitness_dict.keys())
    parent_fitness_list = list(fitness_dict.values())
    no_of_pairs = floor((len(parent_list) / 2))

    for i in range(no_of_pairs):
        parent_indices = choice(parent_list, 2, parent_fitness_list)
        while parent_indices[0] == parent_indices[1]:
            parent_indices[1] = random.choices(parent_list, parent_fitness_list, i=1)[0]

        parent_one = ant_list[parent_indices[0]]
        parent_two = ant_list[parent_indices[1]]
        child_genes = crossover(parent_one, parent_two)
        mutate(child_genes)
        #After gene mutation child_ant creation
        child_x_co_ordinate = random.randrange(ANT_SIZE, SCREEN_WIDTH - ANT_SIZE)
        child_y_co_ordinate = (random.randrange(SCREEN_HEIGHT - 100, SCREEN_HEIGHT)) - ANT_SIZE
        child_ant = Ant(child_x_co_ordinate, child_y_co_ordinate, child_genes)
        new_ant_list.append(child_ant)


def crossover(parent_1, parent_2):
    child_genes = []
    child_ant = []
    midpoint = int(random.choice(len(parent_1.genes)))
    for i in parent_1.genes:
        if i > midpoint:
            child_genes.append(parent_1.genes[i])
        else:
            child_genes.append(parent_2.genes[i])
    return child_genes


def mutate(child):
    for i in child:
        if random.randint(0,1) < 0.01:
            child[i] = random.choice(child)


def load_background():
    # Reloading the background
    window.blit(background, (0, 0))
    # Displaying the food
    food = pg.image.load("icons8-bread-loaf-48.png")
    window.blit(food, (food_position_x, food_position_y))
    # Displaying the obstacle
    obstacle = pg.image.load("brick_wall.png")
    obstacle_rect = obstacle.get_rect()
    obs_width = obstacle_rect.width
    obs_height = obstacle_rect.height
    window.blit(obstacle, (obstacle_position_x, obstacle_position_y))
    pg.display.update()
    return obs_width, obs_height


if __name__ == '__main__':
    pg.init()
    # Setting the background
    window = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pg.display.set_caption("Ant Food Hunting")
    background = pg.image.load("pexels-fwstudio-131634.jpg")

    # Generate the ant population
    generate_ant_population(ant_population_count)
    for g in range(no_of_generations):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                should_quit = True
            else:
                for lifespan_counter in range(ant_lifespan):
                    # Load the background
                    obstacle_width, obstacle_height = load_background()

                    # Display and start movement of the generated ants
                    for eachAnt in ant_list:
                        ant_x_coordinate = eachAnt.x_position
                        ant_y_coordinate = eachAnt.y_position
                        window.blit(ant_icon, (ant_x_coordinate, ant_y_coordinate))

                        # Calculate distance between ant current location and food
                        food_location = [food_position_x, food_position_y]
                        ant_location = [ant_x_coordinate, ant_y_coordinate]
                        ant_food_distance = math.dist(ant_location, food_location)

                        if ant_food_distance < 40:
                            eachAnt.reachedFood = True
                            print("Ant reached food")

                        if ((ant_x_coordinate > obstacle_position_x) and
                                (ant_x_coordinate < (obstacle_position_x + obstacle_width)) and
                                (ant_y_coordinate > obstacle_position_y) and
                                (ant_y_coordinate < (obstacle_position_y + obstacle_height))):
                            eachAnt.clashedObstacle = True
                            print("Ant clashed obstacle")

                        eachAnt.x_position += eachAnt.genes[lifespan_counter][0]
                        eachAnt.y_position -= eachAnt.genes[lifespan_counter][1]
                        pg.display.update()
                    clock.tick(1)
                    # Evaluation -->fitness
        evaluate()
        selection()
                    # Selection --> select best and perform crossover and mutation--add them to new_ant_list
        ant_list = new_ant_list


    if should_quit:
        pg.quit()
