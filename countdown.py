import pygame
import time
import math

def countdown(screen):
    """オシャレなカウントダウンを表示"""
    font = pygame.font.Font(None, 150)  # 大きめのフォント
    colors = [(255, 69, 0), (255, 165, 0), (255, 255, 0)]  # 赤→オレンジ→黄

    # 効果音
    countdown_sound = pygame.mixer.Sound("sound/effect/countdown.mp3")

    countdown_sound.play()
    for i in range(3, 0, -1):
        start_time = time.time()

        while time.time() - start_time < 1:  # 1秒間アニメーション
            elapsed = time.time() - start_time
            scale = 1 + 0.5 * math.sin(elapsed * math.pi)  # 拡大縮小（sin波）

            screen.fill((0, 0, 0))  # 背景を黒に
            text = font.render(str(i), True, colors[3 - i])  # カウントの色を変化
            text = pygame.transform.scale(text, (int(text.get_width() * scale), int(text.get_height() * scale)))

            # **フェードイン・フェードアウト効果**
            alpha = int(255 * (1 - elapsed))  # 1秒かけてフェードアウト
            text.set_alpha(alpha)

            text_rect = text.get_rect(center=(screen.get_width() // 2, screen.get_height() // 2))
            screen.blit(text, text_rect)
            pygame.display.flip()

            time.sleep(0.02)  # スムーズなアニメーションのための短い待機
