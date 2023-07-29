import random

import pygame

from tetris.consts import COLORS, FPS, IN_PX, REAL_WINDOW_SIZE, WINDOW_SIZE, WHITE, BLACK, YELLOW, GRAY
from tetris.field import Tetris

pygame.init()
surface = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Tetris")

tetris = Tetris()

START_FIGURE_COLOR = random.randint(1, 155)


def draw_xy(x, y, color=WHITE, in_px=IN_PX):
    pygame.draw.rect(surface, color, (x * in_px, y * in_px, in_px, in_px))


def draw_text(text, color=YELLOW, size=30, up=True):
    font = pygame.font.Font("tetris/hd44780.ttf", size)
    text = text.split("|")
    if not up:
        text = text[::-1]
    for index, word in enumerate(text):
        text_surface = font.render(word, True, color)

        text_rect = text_surface.get_rect()
        text_rect.left = 11 * IN_PX
        text_rect.centery = (20 * (index + 1)) if up else (WINDOW_SIZE[1] - (20 * (index + 1)))
        surface.blit(text_surface, text_rect)


def draw_window():
    for y, vy in enumerate(tetris.window[-20:]):
        for x, vx in enumerate(vy):
            draw_xy(x, y, COLORS[(START_FIGURE_COLOR + vx) % len(COLORS)]) if vx else draw_xy(x, y, (0, 0, 0))


pygame.draw.line(surface, GRAY, (REAL_WINDOW_SIZE[0] + 5, 0), (REAL_WINDOW_SIZE[0] + 5, REAL_WINDOW_SIZE[1]))
pygame.display.update()

clock = pygame.time.Clock()

flag = True
tick_counter = 0
temp_FPS = FPS
while flag:
    clock.tick(temp_FPS)
    draw_window()

    pygame.draw.rect(surface, BLACK, (
        REAL_WINDOW_SIZE[0] + 10, 0,
        REAL_WINDOW_SIZE[0] + 10, REAL_WINDOW_SIZE[1])
                     )
    draw_text(f"Your|Score:||{tetris.score: >6}")
    draw_text("AI||", color=tetris.AI_color, size=60, up=False)

    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                pygame.quit()
                flag = False
            case pygame.KEYDOWN:
                match event.key:
                    case pygame.K_LEFT:
                        tetris.event("LEFT")
                    case pygame.K_RIGHT:
                        tetris.event("RIGHT")
                    case pygame.K_UP:
                        tetris.event("ROTATE_CCW")
                    case pygame.K_DOWN:
                        tetris.event("ROTATE_CW")
                    case pygame.K_SPACE:
                        temp_FPS = 30
                        tick_counter = -30
                    case pygame.K_a:
                        tetris.event("SWITCH_AI")
    if tetris.game and flag and tick_counter % 2 == 0:
        next(tetris)
        pygame.display.update()

    if tick_counter > 0:
        temp_FPS = FPS

    tick_counter += 1
