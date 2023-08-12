import pygame
from pygame.locals import *
import sys

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


class Event_Handler:
    targets = {}

    # Decorator that accepts a type of event
    def register(type):
        def decorator(fn):
            Event_Handler.targets.setdefault(type, []).append(fn)

        return decorator

    # Notify all functions that are registered to the event type
    def notify(event):
        fnl = (
            Event_Handler.targets[event.type]
            if event.type in Event_Handler.targets
            else []
        )
        for fn in fnl:
            fn(event)


@Event_Handler.register(pygame.QUIT)
def onExit(event):
    pygame.quit()
    sys.exit()


@Event_Handler.register(pygame.KEYUP)
def keydownPrint(event):
    print(event.key)


# @Event_Handler.register(pygame.KEYDOWN)
# def keydownAction(event):
#     print("action")


def main():
    while RUNNING:
        for event in pygame.event.get():
            Event_Handler.notify(event)
        PAPER.fill(BG_COLOR)
        SCREEN.blit(PAPER, (0, 0))
        CLOCK.tick(MAX_FPS)

        pygame.display.update()


if __name__ == "__main__":
    main()
