# ui.py
import pygame
import os
from settings import WHITE, BLACK, GRAY, FONT_PATH

def draw_text(screen, text, size, x, y, color=WHITE):
    # フォントをロード（見つからなければデフォルトフォントを使用）
    font = pygame.font.Font(FONT_PATH, size) if FONT_PATH else pygame.font.SysFont("Arial", size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect(center=(x, y))
    screen.blit(text_surface, text_rect)


def draw_timer(screen, time_left):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Time: {int(time_left)}s", True, (0, 0, 0))
    screen.blit(text, (10, 10))

def draw_score(screen, score):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(text, (10, 50))
