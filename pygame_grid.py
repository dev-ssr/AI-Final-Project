import pygame as pg

pg.init()
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
window = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
window.fill(BLACK)
pg.display.set_caption("Ant Food Hunting")


def draw_grid():
    block_size = 80
    for x in range(SCREEN_WIDTH):
        for y in range(SCREEN_HEIGHT):
            rect = pg.Rect(x*block_size, y*block_size,
                               block_size, block_size)
            pg.draw.rect(window, WHITE, rect, 1)


running = True
while running:
    draw_grid()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    pg.display.update()

pg.quit()
