# chapter_select.py
import pygame
from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK, GRAY
from settings import chapter1_clear, chapter2_clear, chapter3_clear, chapter4_clear, chapter5_clear

from ui import draw_text

def chapter_select(screen):
    selected_option = 0

    sub_background = pygame.image.load("assets/Sub.png")
    sub_background = pygame.transform.scale(sub_background, (SCREEN_WIDTH, SCREEN_HEIGHT))  # 画面サイズに調整
    
    # 🔹 背景を描画
    screen.blit(sub_background, (0, 0))

    if chapter1_clear == -1:
        options = ["Chapter 1", "Back"]
    elif chapter1_clear == 1:
        options = ["Chapter 1", "Chapter 2", "Back"]
    elif chapter2_clear == 1:
        options = ["Chapter 1", "Chapter 2", "Chapter 3", "Back"]
    elif chapter3_clear == 1:
        options = ["Chapter 1", "Chapter 2", "Chapter 3", "Chapter 4", "Back"]
    elif chapter4_clear == 1:
        options = ["Chapter 1", "Chapter 2", "Chapter 3", "Chapter 4", "Chapter 5", "Back"]

    running = True

    while running:
        
        draw_text(screen, "Chapter Select", 50, SCREEN_WIDTH // 2, 50, BLACK)

        for i, option in enumerate(options):
            color = BLACK if i == selected_option else GRAY
            draw_text(screen, option, 40, SCREEN_WIDTH // 2, 150 + i * 60, color)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(options)
                elif event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    
                    if chapter1_clear == -1:
                        if selected_option == 0:  # チャプター1を選択
                            return "chapter1"
                        elif selected_option == 1:  # 戻る
                            return "back"
                    elif chapter1_clear == 1:
                        if selected_option == 0:  # チャプター1を選択
                            return "chapter1"
                        elif selected_option == 1:  # チャプター1を選択
                            return "chapter2"
                        elif selected_option == 2:  # 戻る
                            return "back"
                    elif chapter2_clear == 1:
                        if selected_option == 0:  # チャプター1を選択
                            return "chapter1"
                        elif selected_option == 1:  # チャプター1を選択
                            return "chapter2"
                        elif selected_option == 2:  # チャプター1を選択
                            return "chapter3"
                        elif selected_option == 3:  # 戻る
                            return "back"
                    elif chapter3_clear == 1:
                        if selected_option == 0:  # チャプター1を選択
                            return "chapter1"
                        elif selected_option == 1:  # チャプター1を選択
                            return "chapter2"
                        elif selected_option == 2:  # チャプター1を選択
                            return "chapter3"
                        elif selected_option == 3:  # チャプター1を選択
                            return "chapter4"
                        elif selected_option == 4:  # 戻る
                            return "back"
                    elif chapter4_clear == 1:
                        if selected_option == 0:  # チャプター1を選択
                            return "chapter1"
                        elif selected_option == 1:  # チャプター1を選択
                            return "chapter2"
                        elif selected_option == 2:  # チャプター1を選択
                            return "chapter3"
                        elif selected_option == 3:  # チャプター1を選択
                            return "chapter4"
                        elif selected_option == 4:  # チャプター1を選択
                            return "chapter5"
                        elif selected_option == 5:  # 戻る
                            return "back"
