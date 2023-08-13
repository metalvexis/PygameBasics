import pygame
from pygame.locals import *
import sys
import os

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
os.environ["SDL_VIDEO_WINDOW_POS"] = "%i,%i" % (1920 - SCREEN_WIDTH, 75)

from lib.event_handler import Event_Handler
from lib.grid import Grid
from lib.hud import hud_debug

pygame.init()

WINDOW_TITLE = "Pathfinding"
MAX_FPS = 120
BG_COLOR = (255, 255, 255)
PAPER = pygame.Surface(size=(SCREEN_WIDTH, SCREEN_HEIGHT), flags=SRCALPHA)
SCREEN = pygame.display.set_mode((1280, 720), flags=SRCALPHA)
SCREEN.blit(PAPER, (0, 0))
CLOCK = pygame.time.Clock()
FONT = pygame.font.SysFont("Arial", 12)
RUNNING = True
DELTA_TIME = 0

pygame.display.set_caption(WINDOW_TITLE)


def onExit(event):
    is_quit = event.type == pygame.QUIT
    is_esc = event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
    if is_quit or is_esc:
        print("Exit")
        pygame.quit()
        sys.exit()


sim_grid = Grid(30, 40)
sim_grid_pos = (SCREEN_WIDTH / 2, 50)


def simulate():
    main_handler = Event_Handler()
    secondary_handler = Event_Handler()
    main_handler.register(pygame.QUIT, onExit)
    main_handler.register(pygame.KEYDOWN, onExit)
    PAPER.fill(BG_COLOR)
    while RUNNING:
        for event in pygame.event.get():
            for handler in [main_handler, secondary_handler, sim_grid]:
                handler.notify_event(event)

        sim_grid_pos = (SCREEN_WIDTH / 2 - sim_grid.get_rect().width / 2, 50)
        sim_grid.update(
            pos=(sim_grid_pos[0], sim_grid_pos[1]),
        )

        PAPER.blit(sim_grid.grid_surf, sim_grid_pos)
        PAPER.blit(hud_debug(CLOCK, FONT), (0, 0))
        SCREEN.blit(PAPER, (0, 0))
        CLOCK.tick(MAX_FPS)

        pygame.display.update()


if __name__ == "__main__":
    simulate()
