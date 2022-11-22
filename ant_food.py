import math
import random
import pygame as pg
import pygame.event

from Ant import Ant

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
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
ant_lifespan = 50
no_of_generations = 20


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


def calculate_ant_fitness():
    food_location = [food_position_x, food_position_y]
    for individual_ant in ant_list:
        ant_location = [individual_ant.x_position, individual_ant.y_position]
        ant_fitness = math.dist(ant_location, food_location)
        ant_fitness_list.append(1 / ant_fitness)


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

    for g in range(no_of_generations):
        # Generate the ant population
        generate_ant_population(ant_population_count)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
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

    if should_quit:
        pygame.quit()
