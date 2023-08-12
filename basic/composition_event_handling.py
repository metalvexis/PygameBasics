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
    def register(self, type, fn):
        Event_Handler.targets.setdefault(type, []).append(fn)

    # Notify all functions that are registered to the event type
    def notify(self, event):
        fnl = (
            Event_Handler.targets[event.type]
            if event.type in Event_Handler.targets
            else []
        )
        for fn in fnl:
            fn(event)


def onExit(event):
    pygame.quit()
    sys.exit()


class Controllable:
    e_handler: Event_Handler

    def __init__(self):
        self.e_handler = Event_Handler()
        self.e_handler.register(pygame.KEYDOWN, self.move)

    def notify_event(self, event):
        self.e_handler.notify(event)

    def move(self, event):
        pass


class Car(Controllable):
    def move(self, event):
        print("Car moved")


class Person(Controllable):
    def move(self, event):
        print("Person moved")


handler = Event_Handler()
car1 = Car()
person1 = Person()


def main():
    handler.register(pygame.QUIT, onExit)
    while RUNNING:
        for event in pygame.event.get():
            handler.notify(event)
            car1.notify_event(event)
            person1.notify_event(event)

            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        PAPER.fill(BG_COLOR)
        SCREEN.blit(PAPER, (0, 0))
        CLOCK.tick(MAX_FPS)

        pygame.display.update()


if __name__ == "__main__":
    main()
