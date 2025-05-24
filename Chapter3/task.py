# Chapter3/task.py
import pygame
import random
import time
import math
import random

from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, RED, GREEN, PLAYER_SIZE


# 画像の読み込み
Chapter = "Chapter3"
KNIFE_IMAGE = pygame.image.load(f"{Chapter}/assets/knife.png")
GOLDENKNIFE_IMAGE = pygame.image.load(f"{Chapter}/assets/goldenknife.png")
HAMMER_IMAGE = pygame.image.load(f"{Chapter}/assets/hammer.png")

Radian = 30

class Task:
    def __init__(self):
        self.state = "brandish"
        self.start_time = time.time()  # タスクの開始時刻
        self.player_size = PLAYER_SIZE

        # 包丁のランダムな座標と角度
        self.knife_x = random.randint(50, SCREEN_WIDTH - 50)  
        self.knife_y = random.randint(50, SCREEN_HEIGHT - 50)  
        self.angle = random.uniform(-90, 90)  # -90度〜90度の範囲でランダムに設定

        # 初期状態の角度（brandish時は +60度）
        self.current_angle = self.angle - 60

        # `transition` の回転管理
        self.transition_step = 0  # 0 〜 2 で 2回回転（30°ずつ）

        # 乱数を生成 (0.0 ～ 1.0 の範囲)
        rand_value = random.random()

        # 確率に応じて選択
        if rand_value < 0.10:
            self.color = "golden knife"  # 10% の確率
        elif rand_value < 0.35:
            self.color = "hammer"  # 25% の確率
        else:
            self.color = "knife"  # 65% の確率


        # ナイフ画像関連の変数
        self.knife_index = 0  # knife 画像のインデックス
        self.last_knife_update = time.time()  # knife 更新時間
        
        self.cutting_sound = pygame.mixer.Sound("sound/effect/cutting-1.mp3")
        self.hammer_sound = pygame.mixer.Sound("sound/effect/hammer.mp3")

    def update(self):
        """状態を更新"""
        elapsed_time = time.time() - self.start_time

        if elapsed_time >= 1.1:  # 2.2秒経過（完了）
            if self.color == "knife" or self.color == "golden knife":
                self.cutting_sound.play()
            elif self.color == "hammer":
                self.hammer_sound.play()

            return True  # タスク完了
        elif elapsed_time >= 1.0:  # 2.0秒で `cutting` に変更
            self.state = "cutting"
        elif elapsed_time >= 0.9:  
            self.state = "transition"
            # 0.05秒ごとに 30° ずつ回転
            if (elapsed_time - 0.9) // 0.05 > self.transition_step:
                self.transition_step += 1
                self.current_angle += 30
        else:
            self.state = "brandish"

        return False  # まだタスク継続中

    def check_completion(self, player):
        """プレイヤーが包丁付近にいるか判断"""
        add_score = 0

        if self.state != "cutting":
            return False
        
        px, py = player.rect.center

        distance = math.sqrt((self.knife_x - px) ** 2 + (self.knife_y - py) ** 2)

        if distance < Radian:
            if self.color == "knife":
                add_score = 10
            elif self.color == "golden knife":
                add_score = 30
            elif self.color == "hammer":
                add_score = -20
        
        return add_score


    def draw(self, screen):
        """包丁を描画し、その周りに半径Radian pxの点線の円を描画"""
        radius = Radian
        for angle in range(0, 360, 20):  # 20°ごとに点を描く
            dot_x = self.knife_x + radius * math.cos(math.radians(angle))
            dot_y = self.knife_y + radius * math.sin(math.radians(angle))
            pygame.draw.circle(screen, RED, (int(dot_x), int(dot_y)), 2)  # 小さな円を描画

        # ナイフ画像を回転して描画
        if self.color == "knife":
            rotated_knife = pygame.transform.rotate(KNIFE_IMAGE, -self.current_angle)
            knife_rect = rotated_knife.get_rect(center=(self.knife_x, self.knife_y))
            screen.blit(rotated_knife, knife_rect.topleft)
        elif self.color == "golden knife":
            rotated_knife = pygame.transform.rotate(GOLDENKNIFE_IMAGE, -self.current_angle)
            knife_rect = rotated_knife.get_rect(center=(self.knife_x, self.knife_y))
            screen.blit(rotated_knife, knife_rect.topleft)
        elif self.color == "hammer":
            rotated_knife = pygame.transform.rotate(HAMMER_IMAGE, -self.current_angle)
            knife_rect = rotated_knife.get_rect(center=(self.knife_x, self.knife_y))
            screen.blit(rotated_knife, knife_rect.topleft)
        
class TaskManager:
    """タスクを管理するクラス"""
    def __init__(self):
        self.tasks = []
        self.last_spawn_time = time.time()
        self.spawn_interval = 2  # 最初のタスク出現間隔（秒）
        self.max_tasks = 2  # 最初の同時タスク数

    def update(self, game_time):
        """タスクを更新し、時間経過で難易度を上げる"""
        self.tasks = [task for task in self.tasks if not task.update()]

        # 時間経過で出現速度とタスク量を増加
        if game_time > 10:  # 15秒経過したら
            self.spawn_interval = max(1, 3 - game_time // 20)  # 最大1秒まで短縮
            self.max_tasks = min(8, 2 + game_time // 20)  # 最大5個まで同時出現

        # 新しいタスクの出現
        if time.time() - self.last_spawn_time > self.spawn_interval:
            self.spawn_tasks()
            self.last_spawn_time = time.time()

    def spawn_tasks(self):
        """ランダムな数のタスクを追加"""
        num_new_tasks = random.randint(1, self.max_tasks)
        for _ in range(num_new_tasks):
            self.tasks.append(Task())

    def check_completion(self, player):
        """プレイヤーがタスクをクリアしたかチェック"""
        score_change = 0
        for task in self.tasks[:]:  # `[:]` を使ってコピーを作りながらループ
            result = task.check_completion(player)
            if result:  # False でなければ
                score_change += result  # `10`, `30`, `-20` のいずれか
                self.tasks.remove(task)

        return score_change

    def draw(self, screen):
        """タスクを描画"""
        for task in self.tasks:
            task.draw(screen)
