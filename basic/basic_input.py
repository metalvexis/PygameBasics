import pygame
from pygame.locals import *
import sys

pygame.init()


class InputProcessor:
    key_event = None

    def new_key_event(self, key_event):
        self.key_event = key_event

    def get_mod_key(self, key_event):
        if key_event.mod == pygame.KMOD_NONE:
            return "none"
        else:
            if key_event.mod & pygame.KMOD_LSHIFT:
                return "LShift"
            if key_event.mod & pygame.KMOD_RSHIFT:
                return "RShift"
            if key_event.mod & pygame.KMOD_LCTRL:
                return "LCtrl"
            if key_event.mod & pygame.KMOD_RCTRL:
                return "RCtrl"
            if key_event.mod & pygame.KMOD_LALT:
                return "LAlt"
            if key_event.mod & pygame.KMOD_RALT:
                return "RAlt"
            if key_event.mod & pygame.KMOD_LMETA:
                return "LMeta"
            if key_event.mod & pygame.KMOD_RMETA:
                return "RMeta"

    def alt_get_mod_key(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            print("K_UP")
        if keys[pygame.K_DOWN]:
            print("K_DOWN")
        if keys[pygame.K_LEFT]:
            print("K_LEFT")
        if keys[pygame.K_RIGHT]:
            print("K_RIGHT")

    def __str__(self) -> str:
        str = f"""
        Mouse:
            
            Pos: {pygame.mouse.get_pos()}
            Move: {pygame.mouse.get_rel()}
            Press: {pygame.mouse.get_pressed()}
            
        Keyboard:
        """
        if self.key_event:
            str += f"""
            Event: {self.key_event}
            KeyName: {pygame.key.name(self.key_event.key)}
            Mods: {self.get_mod_key(self.key_event)}
            
            """

        return str


max_fps = 120

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

screen = pygame.display.set_mode((1280, 720))
screen.fill((255, 255, 255))

clock = pygame.time.Clock()

running = True

clock.tick(max_fps)

pygame.display.set_caption("Main Window")
font = pygame.font.SysFont("Arial", 12)

input_hud = InputProcessor()


def draw_fps(screen):
    text = f"""
    FPS: {round(clock.get_fps(), 2)}
    ---
    Input:
    {input_hud}
    """
    render_text = font.render(text, True, (0, 0, 0), (255, 255, 255))
    screen.blit(source=render_text, dest=(0, 0), special_flags=BLEND_PREMULTIPLIED)


while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            input_hud.new_key_event(event)
            input_hud.alt_get_mod_key()

    draw_fps(screen)

    clock.tick(max_fps)

    pygame.display.update()
