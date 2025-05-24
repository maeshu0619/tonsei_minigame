# Chapter3/map.py
import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from settings import TILE_SIZE

# 画像の読み込み
Chapter = "Chapter1"
BACKGROUND_IMAGE = pygame.image.load(f"{Chapter}/assets/BackGround1.png")

map_data = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
]

class Map:
    def __init__(self):
        self.tile_size = TILE_SIZE
        self.background = pygame.transform.scale(BACKGROUND_IMAGE, (SCREEN_WIDTH, SCREEN_HEIGHT))

    def draw(self, screen):
        """背景を描画"""
        screen.blit(self.background, (0, 0))

    def is_wall(self, x, y):
        """指定の座標が壁かどうかを判定"""
        tile_x = int(x // self.tile_size)
        tile_y = int(y // self.tile_size)

        # 範囲外チェック
        if 0 <= tile_y < len(map_data) and 0 <= tile_x < len(map_data[0]):
            return map_data[tile_y][tile_x] == 1
        
        return True  # 範囲外なら壁扱い