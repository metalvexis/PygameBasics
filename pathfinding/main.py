import pygame
from pygame.locals import *
import sys

from lib.event_handler import Event_Handler
from lib.grid import Grid
from lib.hud import hud_debug

pygame.init()

WINDOW_TITLE = "Pathfinding"
MAX_FPS = 120
BG_COLOR = (255, 255, 255)
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
PAPER = pygame.Surface(size=(SCREEN_WIDTH, SCREEN_HEIGHT), flags=SRCALPHA)
SCREEN = pygame.display.set_mode((1280, 720), flags=SRCALPHA)
SCREEN.blit(PAPER, (0, 0))
CLOCK = pygame.time.Clock()
FONT = pygame.font.SysFont("Arial", 12)
RUNNING = True
DELTA_TIME = 0


def onExit(event):
    print("Exit")
    pygame.quit()
    sys.exit()


sim_grid = Grid(30, 40)
sim_grid_pos = (SCREEN_WIDTH / 2, 50)


def simulate():
    main_handler = Event_Handler()
    secondary_handler = Event_Handler()
    main_handler.register(pygame.QUIT, onExit)
    PAPER.fill(BG_COLOR)
    while RUNNING:
        for event in pygame.event.get():
            for handler in [main_handler, secondary_handler, sim_grid]:
                handler.notify_event(event)

        grid = sim_grid.draw()
        sim_grid_pos = (SCREEN_WIDTH / 2 - grid.get_rect().width / 2, 50)

        sim_grid.update(
            pos=(sim_grid_pos[0], sim_grid_pos[1]),
            size=(grid.get_width(), grid.get_height()),
        )

        PAPER.blit(grid, sim_grid_pos)
        PAPER.blit(hud_debug(CLOCK, FONT), (0, 0))
        SCREEN.blit(PAPER, (0, 0))
        CLOCK.tick(MAX_FPS)

        pygame.display.update()


if __name__ == "__main__":
    simulate()
