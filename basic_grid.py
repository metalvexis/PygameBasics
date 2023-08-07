import pygame
from pygame.locals import *
import sys

pygame.init()

ticker = 0
max_fps = 120

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

running = True

clock.tick(max_fps)

pygame.display.set_caption("Main Window")
font = pygame.font.SysFont("Arial", 12)

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    for x in range(10):
        for y in range(10):
            rect = pygame.Rect(x * 50, y * 50, 50, 50)
            pygame.draw.rect(screen, (255, 255, 255), rect, 1)

    screen.fill((0, 0, 0), (0, 0, 100, 40))
    ticker += 1
    text = font.render(
        f"Ticker: {ticker}\nFPS: {round(clock.get_fps(), 2)}",
        True,
        (255, 255, 255),
        (None),
    )
    screen.blit(text, (0, 0))

    clock.tick(max_fps)
    pygame.display.update()
