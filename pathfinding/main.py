import pygame
from pygame.locals import *
import sys

from lib.event_handler import Event_Handler
from lib.grid import Grid

pygame.init()
WINDOW_TITLE = "Event Handling"
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


sim_grid = Grid(10, 10)


def simulate():
    main_handler = Event_Handler()
    main_handler.register(pygame.QUIT, onExit)
    while RUNNING:
        for event in pygame.event.get():
            for handler in [main_handler, sim_grid]:
                handler.notify_event(event)

        PAPER.fill(BG_COLOR)

        PAPER.blit(sim_grid.draw(), (0, 0))

        SCREEN.blit(PAPER, (0, 0))
        CLOCK.tick(MAX_FPS)

        pygame.display.update()


if __name__ == "__main__":
    simulate()
