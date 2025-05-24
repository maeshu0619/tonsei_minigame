# Chapter3/task.py
import pygame
import random
import time
import math
import random

from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, RED, GREEN, PLAYER_SIZE


# 画像の読み込み
Chapter = "Chapter1"
MILK_NORMAL = pygame.image.load(f"{Chapter}/assets/milk_normal.png")
MILK_GOLDEN = pygame.image.load(f"{Chapter}/assets/goldenknife.png")
MILK_SPOILED = pygame.image.load(f"{Chapter}/assets/milk_spoiled.png")

Radian = 25

class TaskManager:
    def __init__(self):
        """ミルクの生成"""
        self.milk_x = random.randint(100, SCREEN_WIDTH - 100)  # ミルクの X 座標
        self.milk_y = SCREEN_HEIGHT * (3/5)  # 固定の Y 座標

        # ミルクの種類を決定
        rand_value = random.random()
        if rand_value < 0.10:
            self.kind = "golden"  # 10% の確率でゴールデンミルク
            self.time_limit = 3.0  # 3秒間吸える
            self.required_hits = 15  # 15回の連打で成功
        elif rand_value < 0.35:
            self.kind = "spoiled"  # 25% の確率で腐ったミルク
            self.time_limit = 1.5  # 1.5秒で腐る
            self.required_hits = 10  # 10回の連打で成功
        else:
            self.kind = "normal"  # 65% の確率で普通のミルク
            self.time_limit = 2.0  # 2秒間吸える
            self.required_hits = 12  # 12回の連打で成功

        self.start_time = None
        self.player_nearby = False
        self.current_hits = 0  # 連打回数
        
        self.normal_put = pygame.mixer.Sound("sound/effect/cutting-1.mp3")
        self.glass_put = pygame.mixer.Sound("sound/effect/cutting-1.mp3")
        self.tank_put = pygame.mixer.Sound("sound/effect/cutting-1.mp3")

    def update(self, player):
        """プレイヤーが近くに来たら吸えるようにする"""
        px, py = player.rect.center
        if abs(px - self.milk_x) <= 25:  # プレイヤーが範囲内にいるか？
            if self.start_time is None:  # 初めて近づいたとき
                self.start_time = time.time()
            self.player_nearby = True
        else:
            self.player_nearby = False

    def handle_input(self, events):
        """プレイヤーがEnterキーを押したらカウント"""
        if self.player_nearby and self.start_time:
            elapsed = time.time() - self.start_time
            if elapsed < self.time_limit:
                for event in events:
                    if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                        self.current_hits += 1  # 1回押すごとに+1


    def check_completion(self):
        """ミルクを吸う成功判定"""
        if self.start_time and (time.time() - self.start_time >= self.time_limit):
            if self.current_hits >= self.required_hits:
                if self.kind == "golden":
                    return 50  # ゴールデンは50点
                elif self.kind == "spoiled":
                    return -20  # 腐ったミルクは減点
                else:
                    return 20  # 普通のミルクは20点
            else:
                return 0  # 失敗なら無得点
        return None  # まだ終了していない

    def draw(self, screen):
        """ミルクを描画"""
        if self.kind == "golden":
            image = MILK_GOLDEN
        elif self.kind == "spoiled":
            image = MILK_SPOILED
        else:
            image = MILK_NORMAL
        
        screen.blit(image, (self.milk_x - image.get_width() // 2, self.milk_y - image.get_height() // 2))
        