# player.py
import pygame
from settings import PLAYER_SPEED
from settings import TILE_SIZE, PLAYER_SIZE

from Chapter3.map import Map 

# 画像の読み込み
Chapter = "Chapter3"
PLAYER_IMAGE = pygame.image.load(f"{Chapter}/assets/Pig.png")

class Player:
    def __init__(self, x, y):
        """プレイヤーの初期化"""
        # 内部判定用の当たり判定（PLAYER_SIZE × PLAYER_SIZE）
        self.rect = pygame.Rect(x, y, PLAYER_SIZE, PLAYER_SIZE)

        # 画像は元サイズのまま
        self.image = pygame.transform.scale(PLAYER_IMAGE, (60, 60))  # 画像をリサイズ

        self.velocity = pygame.Vector2(0, 0)
        self.holding = None  # 持っているアイテム
        self.map = Map()  # マップ情報を保持
        self.tile_size = TILE_SIZE
        self.player_size = PLAYER_SIZE

    def handle_input(self, keys):
        self.velocity.x = 0
        self.velocity.y = 0

        if keys[pygame.K_w]:
            self.velocity.y = -PLAYER_SPEED
        if keys[pygame.K_s]:
            self.velocity.y = PLAYER_SPEED
        if keys[pygame.K_a]:
            self.velocity.x = -PLAYER_SPEED
        if keys[pygame.K_d]:
            self.velocity.x = PLAYER_SPEED

    def update(self):
        """壁判定をチェックし、進行可能なら移動"""
        new_x = self.rect.x + self.velocity.x
        new_y = self.rect.y + self.velocity.y

        # 次の位置が壁でないかチェック
        if self.velocity.x > 0:
            if not self.map.is_wall(new_x+self.player_size, self.rect.y):
                if not self.map.is_wall(new_x+self.player_size, self.rect.y+self.player_size):
                    self.rect.x = new_x
        elif self.velocity.x < 0:
            if not self.map.is_wall(new_x, self.rect.y):
                if not self.map.is_wall(new_x, self.rect.y+self.player_size):
                    self.rect.x = new_x
                
        if self.velocity.y > 0:
            if not self.map.is_wall(self.rect.x, new_y+self.player_size):
                if not self.map.is_wall(self.rect.x+self.player_size, new_y+self.player_size):
                    self.rect.y = new_y
        elif self.velocity.y < 0:
            if not self.map.is_wall(self.rect.x, new_y):
                if not self.map.is_wall(self.rect.x+self.player_size, new_y):
                    self.rect.y = new_y

    def draw(self, screen):
        screen.blit(self.image, self.rect.topleft)
