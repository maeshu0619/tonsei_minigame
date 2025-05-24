# Chapter3/rule.py
import pygame
import time
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK
from ui import draw_text

from countdown import countdown

# 画像の読み込み
STORY_IMAGE = pygame.image.load("assets/story.png")

def show_rules(screen, story_text):
    """
    ルール説明画面を表示し、スペースキーでカウントダウン開始。
    3秒カウント後にゲームを開始する。
    """
    background = pygame.transform.scale(STORY_IMAGE, (SCREEN_WIDTH, SCREEN_HEIGHT))

    page = 0
    running = True

    color = BLACK

    while running:
        screen.blit(background, (0, 0))

        draw_text(screen, "Chapter 3", 47, SCREEN_WIDTH // 2, 100, color)  # タイトル
        #draw_text(screen, "Explanation of the rules", 30, SCREEN_WIDTH // 2, 130, color)
        
        # ストーリーの文章を表示
        y_offset = 200  # 開始Y位置
        for line in story_text[page]:  # 現在のページの文章を表示
            draw_text(screen, line, 25, SCREEN_WIDTH // 2, y_offset, color)
            y_offset += 50  # 次の行へ

        draw_text(screen, "Press any key to continue...", 20, SCREEN_WIDTH // 2, SCREEN_HEIGHT - 20, WHITE)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                page += 1
                if page >= len(story_text):  # 最後のページなら終了
                    running = False

    # カウントダウン
    countdown(screen)


def rule_story(screen):
    story_text = [
        ["You are cooked on a cutting board.",
         "Let's be cut into bite-size pieces",
         "by randomly appearing knives.",
         "Points are awarded if you can get",
         "inside the red dotted circle that appears",
         "near the knife before it disappears."],
        ["Move: W/A/S/D",  
         "Goal: 200 points",
         "",
         "normal knife: +10",
         "golden knife: +30",
         "hammer      : -20"]
    ]
    show_rules(screen, story_text)  # ストーリー終了後にゲーム開始
