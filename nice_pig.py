import pygame
import random
import time
from settings import SCREEN_WIDTH, SCREEN_HEIGHT

class NicePigAnimation:
    def __init__(self):
        """NicePig のアニメーション管理"""
        self.active = False  # 初期状態では非表示
        self.start_time = 0  # アニメーション開始時間
        self.direction = 1  # 1: 右から, -1: 左から
        self.x = 0  # x 座標
        self.y = SCREEN_HEIGHT / 5  # 画面の中央
        self.display_count = 0  # 表示回数（サイズ増加）
        self.size_multiplier = 0.1

        # Pygame の display 初期化後に画像をロード
        try:
            self.image = pygame.image.load("assets/NicePig.png").convert_alpha()
        except pygame.error as e:
            print(f"Error loading NicePig.png: {e}")
            self.image = None

    def start(self):
        """NicePig のアニメーションを開始"""
        if self.image is None:
            return  # 画像が読み込めなかった場合は何もしない

        self.active = True
        self.start_time = time.time()
        self.direction = random.choice([-1, 1])  # 左右ランダム
        self.display_count += 1  # 表示回数カウント

        # 画像の現在の大きさ
        current_width = int(self.image.get_width() * self.size_multiplier)

        # 初期位置設定
        if self.direction == 1:
            self.x = -current_width  # 左の画面外
        else:
            self.x = SCREEN_WIDTH  # 右の画面外

    def update(self):
        """アニメーション更新"""
        if not self.active or self.image is None:
            return

        elapsed = time.time() - self.start_time


        # 画像の現在の大きさ
        current_width = int(self.image.get_width() * self.size_multiplier)

        if elapsed < 0.4:
            # 画面外から 0.4秒かけて移動
            move_distance = (elapsed / 0.4) * current_width

            # **サイズに応じたオフセットを適用**
            if self.direction == 1:  # 右向き（左から出る）
                self.x = -current_width + move_distance
                if self.x > 0:
                    self.x = 0 
            else:  # 左向き（右から出る）
                self.x = SCREEN_WIDTH - move_distance - current_width//2
                if self.x < SCREEN_WIDTH - current_width:
                    self.x = SCREEN_WIDTH - current_width

        elif elapsed < 0.7:
            # 0.3秒間静止
            pass
        else:
            # 1.0秒経過後、アニメーション終了
            self.active = False



    def draw(self, screen):
        if not self.active or self.image is None:
            return

        # `display_count` に応じてサイズを大きくする
        self.size_multiplier = 0.5 + (self.display_count * 0.1)  # 0.5倍からスタートし、表示回数ごとに0.1増加

        # 画像サイズの拡大
        new_size = (
            int(self.image.get_width() * self.size_multiplier),
            int(self.image.get_height() * self.size_multiplier)
        )
        resized_pig = pygame.transform.scale(self.image, new_size)

        # 左から出てくる時は左右反転
        if self.direction == 1:
            resized_pig = pygame.transform.flip(resized_pig, True, False)

        screen.blit(resized_pig, (self.x, self.y))
