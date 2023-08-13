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


USEREVENT_LOCK_CAR = pygame.event.custom_type()
USEREVENT_UNLOCK_CAR = pygame.event.custom_type()


class Event_Handler:
    targets = {}

    # Decorator that accepts a type of event
    def register(self, type, fn):
        Event_Handler.targets.setdefault(type, []).append(fn)

    # Notify all functions that are registered to the event type
    def notify_event(self, event):
        fnl = (
            Event_Handler.targets[event.type]
            if event.type in Event_Handler.targets
            else []
        )
        for fn in fnl:
            fn(event)


def onExit(event):
    print("Exit")
    pygame.quit()
    sys.exit()


class Car:
    def __init__(self, e_handler: Event_Handler):
        e_handler.register(USEREVENT_UNLOCK_CAR, self.unlock)
        e_handler.register(USEREVENT_LOCK_CAR, self.lock)

    def move(self, event: pygame.Event):
        print("Car moved")

    def lock(self, event: pygame.Event):
        print(f"Car received: {event.dict['message']}")
        print("Car LOCKED")

    def unlock(self, event: pygame.Event):
        print(f"Car received: {event.dict['message']}")
        print("Car UNLOCKED")


class Person:
    def __init__(self, e_handler: Event_Handler):
        e_handler.register(pygame.MOUSEBUTTONDOWN, self.lock_car)
        e_handler.register(pygame.MOUSEBUTTONDOWN, self.unlock_car)

    def move(self, event: pygame.Event):
        print("Person moved")

    def lock_car(self, event: pygame.Event):
        if pygame.mouse.get_pressed(3)[0]:
            print("Person sent: I want to LOCK my car")
            pygame.event.post(
                pygame.Event(USEREVENT_LOCK_CAR, {"message": "Please LOCK"})
            )

    def unlock_car(self, event: pygame.Event):
        if pygame.mouse.get_pressed(3)[2]:
            print("Person sent: I want to UNLOCK my car")
            pygame.event.post(
                pygame.Event(USEREVENT_UNLOCK_CAR, {"message": "Please UNLOCK"})
            )


main_handler = Event_Handler()
car1 = Car(main_handler)
person1 = Person(main_handler)


def main():
    main_handler.register(pygame.QUIT, onExit)

    while RUNNING:
        for event in pygame.event.get():
            for handler in [main_handler]:
                handler.notify_event(event)

        CLOCK.tick(MAX_FPS)

        pygame.display.update()


if __name__ == "__main__":
    main()
