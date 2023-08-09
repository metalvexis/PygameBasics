import pygame
from pygame.locals import *
import sys

pygame.init()

ticker = 0
max_fps = 120

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

running = True

clock.tick(max_fps)

boardOffset = {"x": SCREEN_WIDTH / 4, "y": SCREEN_HEIGHT / 6}

pygame.display.set_caption("Main Window")
font = pygame.font.SysFont("Arial", 12)


def draw_fps(screen):
    text = font.render(
        f"Ticker: {ticker}\nFPS: {round(clock.get_fps(), 2)}",
        True,
        (255, 255, 255),
        pygame.SRCALPHA,
    )
    screen.blit(text, (0, 0))


def draw_board(screen, w=10, h=10):
    for x in range(w):
        for y in range(h):
            rect = pygame.Rect(
                x * 50 + boardOffset["x"], y * 50 + boardOffset["y"], 50, 50
            )
            pygame.draw.rect(screen, (255, 255, 255), rect, 1)


while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    ticker += 1

    draw_fps(screen)

    draw_board(screen, 10, 10)

    clock.tick(max_fps)

    pygame.display.update()
