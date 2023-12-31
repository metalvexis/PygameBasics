import pygame
from pygame.locals import *
import sys

pygame.init()
WINDOW_TITLE = "Basic Controls"
MAX_FPS = 120
BG_COLOR = (255, 255, 255)
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN = pygame.display.set_mode((1280, 720), flags=SRCALPHA)
PAPER = pygame.Surface(size=(SCREEN_WIDTH, SCREEN_HEIGHT), flags=SRCALPHA)
PAPER.fill(BG_COLOR)
SCREEN.blit(PAPER, (0, 0))
CLOCK = pygame.time.Clock()
FONT = pygame.font.SysFont("Arial", 12)
RUNNING = True
DELTA_TIME = 0

pygame.display.set_caption(WINDOW_TITLE)


def hud_debug(screen: pygame.Surface) -> None:
    text = FONT.render(
        f"FPS: {round(CLOCK.get_fps(), 2)}",
        True,
        (0, 0, 0),
        BG_COLOR,
    )
    screen.blit(text, (0, 0))


def draw_board(
    row=10,
    col=10,
    cell_width=20,
    cell_height=20,
    color: Color = (255, 255, 255, 255),
) -> pygame.Surface:
    board_w = col * cell_width
    board_h = row * cell_height
    board_surface = pygame.Surface(size=(board_w, board_h), flags=SRCALPHA)
    board_surface.fill(BG_COLOR)
    for x in range(col):
        for y in range(row):
            rect = pygame.Rect(x * cell_width, y * cell_height, cell_width, cell_height)
            pygame.draw.rect(board_surface, color, rect, 1)

    return board_surface


def main():
    board_alpha = 255 / 2
    board_row = 40
    board_col = 50

    while RUNNING:
        PAPER.fill(BG_COLOR)

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_KP_MINUS:
                    board_alpha = (board_alpha - 50) if board_alpha - 50 > 0 else 255
                if event.key == pygame.K_KP_PLUS:
                    board_alpha = (board_alpha + 50) if board_alpha + 50 < 255 else 255
                if event.key == pygame.K_PAGEUP:
                    board_row += 1
                    board_col += 1
                if event.key == pygame.K_PAGEDOWN:
                    board_row -= 1 if board_row - 1 > 0 else 0
                    board_col -= 1 if board_col - 1 > 0 else 0

        hud_debug(PAPER)

        board = draw_board(
            board_row,
            board_col,
            cell_width=15,
            cell_height=15,
            color=(0, 0, 0, board_alpha),
        )

        PAPER.blit(board, ((SCREEN_WIDTH / 2) - (board.get_width() / 2), 50))

        SCREEN.blit(PAPER, (0, 0))
        CLOCK.tick(MAX_FPS)

        pygame.display.update()


if __name__ == "__main__":
    main()
