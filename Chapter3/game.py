# game.py
import pygame
import time

from settings import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, TASK_TIME_LIMIT, CLEAR_SCORE
from settings import chapter3_clear

from failure import failure_screen

from nice_pig import NicePigAnimation

from Chapter3.player import Player
from Chapter3.task import TaskManager
from ui import draw_timer, draw_score
from Chapter3.rule import rule_story
from Chapter3.story import st_story, en_story
from Chapter3.map import Map

# 画像の読み込み
SUCCESS_IMAGE = pygame.image.load("assets/QuestSuccess.png")
FAILED_IMAGE = pygame.image.load("assets/QuestFailed.png")

def chapter3_run_game(screen):
    """
    Chapter 3 のゲームを開始する。
    まずルール画面を表示し、3秒カウント後にゲーム開始。
    """
    clock = pygame.time.Clock()

    # ゲーム前のストーリー
    st_story(screen)

    # ルール説明を表示
    rule_story(screen)

    # ゲーム初期化
    player = Player(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100)
    game_map = Map()
    task_manager = TaskManager()
    score = 0
    start_time = time.time()

    quest_success = pygame.transform.scale(SUCCESS_IMAGE, (SCREEN_WIDTH, SCREEN_HEIGHT))
    quest_failed = pygame.transform.scale(FAILED_IMAGE, (SCREEN_WIDTH, SCREEN_HEIGHT))
        
    # 🔹 BGM 再生（ループ）
    pygame.mixer.music.load("sound/background/minigame.mp3")
    pygame.mixer.music.set_volume(0.5)  # 音量調整 (0.0 ～ 1.0)
    pygame.mixer.music.play(-1)  # 無限ループ再生

    # 効果音
    nicepig_sound = pygame.mixer.Sound("sound/effect/nicepig.mp3")
    hammer_sound = pygame.mixer.Sound("sound/effect/hammer.mp3")
    congratulation_sound = pygame.mixer.Sound("sound/effect/congratulation.mp3")
    disappointing_sound = pygame.mixer.Sound("sound/effect/disappointing.mp3")

    nice_pig_animation = NicePigAnimation()

    running = True
    while running:
        screen.fill((0, 0, 0))
        keys = pygame.key.get_pressed()
        player.handle_input(keys)
        player.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        # 経過時間
        game_time = time.time() - start_time

        # タスクの更新（時間経過で難易度増加）
        task_manager.update(game_time)

        # タスククリア判定
        score_change = task_manager.check_completion(player)
        score += score_change
    
        # 描画
        game_map.draw(screen)
        player.draw(screen)
        task_manager.draw(screen)
        draw_timer(screen, TASK_TIME_LIMIT - game_time)
        draw_score(screen, score)

        if score_change == 10 or score_change == 30:
            nice_pig_animation.start()
            nicepig_sound.play()
        elif score_change == -20:
            hammer_sound.play()
            pass

        # NicePig のアニメーション更新と描画
        nice_pig_animation.update()
        nice_pig_animation.draw(screen)
        
        pygame.display.flip()
        clock.tick(FPS)

        # 時間切れで終了
        if time.time() - start_time >= TASK_TIME_LIMIT:
            running = False
            pygame.mixer.music.stop()


            if score >= CLEAR_SCORE:
                screen.blit(quest_success, (0, 0))
                pygame.display.flip()  # 🎥 画面を更新
                congratulation_sound.play()
            else:
                screen.blit(quest_failed, (0, 0))
                pygame.display.flip()  # 🎥 画面を更新
                disappointing_sound.play()

            time.sleep(4)

            # ⏳ 何かキーを押すまで待機
            waiting = True
            while waiting:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        exit()
                    elif event.type == pygame.KEYDOWN:
                        waiting = False  # 🔓 キーを押したら進む

            # クリア or 失敗後の処理
            if score >= CLEAR_SCORE:
                chapter3_clear = 1
                en_story(screen)  # クリアストーリーを表示
            else:
                failure_screen(screen)  # 失敗画面を表示


    #return "title"