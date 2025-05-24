# main.py
import pygame

from settings import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE, BLACK, GRAY, FPS

from ui import draw_text

from chapter_select import chapter_select
from Chapter1.game import chapter1_run_game  # ゲーム開始用の関数
#from Chapter2.game import chapter2_run_game  # ゲーム開始用の関数
from Chapter3.game import chapter3_run_game  # ゲーム開始用の関数

'''
TITLE_IMAGE = pygame.image.load(f"assets/Title.png")
SUB_IMAGE = pygame.image.load(f"assets/Sub.png")
'''
def title_screen(screen):
    selected_option = 0
    options = ["Start Game", "Chapter Select", "Settings"]

    # 🔹 BGM 再生（ループ）
    pygame.mixer.music.load("sound/background/title.mp3")
    pygame.mixer.music.set_volume(0.5)  # 音量調整 (0.0 ～ 1.0)
    pygame.mixer.music.play(-1)  # 無限ループ再生

    # 効果音
    decision_sound = pygame.mixer.Sound("sound/effect/decision.mp3")
    selection_sound = pygame.mixer.Sound("sound/effect/selection.mp3")
    
    # 背景画像をロード
    background = pygame.image.load("assets/Title.png")
    background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))  # 画面サイズに調整
    
    running = True
    while running:
        # 🔹 背景を描画
        screen.blit(background, (0, 0))
        
        for i, option in enumerate(options):
            color = BLACK if i == selected_option else GRAY
            draw_text(screen, option, 40, SCREEN_WIDTH // 6, SCREEN_HEIGHT - 200 + i * 60, color)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    selection_sound.play() 
                    selected_option = (selected_option + 1) % len(options)
                elif event.key == pygame.K_UP:
                    selection_sound.play() 
                    selected_option = (selected_option - 1) % len(options)
                elif event.key == pygame.K_RETURN:
                    decision_sound.play() 
                    pygame.mixer.music.stop()
                    if selected_option == 0:  # はじめから
                        return "start"
                    elif selected_option == 1:  # チャプター選択
                        return "chapter"
                    elif selected_option == 2:  # 設定（何もしない）
                        pass

def main():
    pygame.init()    
    pygame.mixer.init()  # 🎵 オーディオ初期化

    # アイコンの設定
    icon = pygame.image.load("assets/Icon.png")
    pygame.display.set_icon(icon)  # アイコンを設定

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Pig Life ~The Cycle of Pig Life~")
    clock = pygame.time.Clock()
    

    while True:
        action = title_screen(screen)

        if action == "start":
            chapter1_run_game(screen)  # ゲームを開始
        elif action == "chapter":
            chapter_action = chapter_select(screen)
            if chapter_action == "chapter1":
                chapter1_run_game(screen)  # チャプター1開始
            elif chapter_action == "chapter2":
                chapter2_run_game(screen) # チャプター2開始
            elif chapter_action == "chapter3":
                chapter3_run_game(screen) # チャプター3開始
            elif chapter_action == "chapter4":
                chapter4_run_game(screen) # チャプター4開始
            elif chapter_action == "chapter5":
                chapter5_run_game(screen) # チャプター5開始

        clock.tick(FPS)

if __name__ == "__main__":
    main()